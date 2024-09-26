#This R project combines 3 years worth of raw data of COVID 19 in the US from github that was then used to analyse 
#the mortality rate pers state and whole nation.

install.packages("tidyverse")
library(tidyverse)
library(readr)
library(lubridate)


############################################################
#Part 1

URL <- "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"
start_date <- as.Date("12-04-2020", format = "%m-%d-%Y")
end_date <- as.Date("09-03-2023", format = "%m-%d-%Y")
dates_range <- seq(start_date, end_date, by = "days")

result <- character(length(dates_range))

for (i in seq_along(dates_range)) {
  result[i] <- paste0(URL, format(dates_range[i], format = "%m-%d-%Y"), ".csv")
  print(result[i])
}

#merge all the tables together into 1 dataframe
merged_df <- data.frame()

for (i in seq_along(dates_range)) {
  url <- paste0(URL, format(dates_range[i], format = "%m-%d-%Y"), ".csv")
  temp_df <- read.csv(url, header = TRUE)
  
  if (nrow(merged_df) == 0) {
    merged_df <- temp_df
  } else {
    merged_df <- rbind(merged_df, temp_df)
  }
}

str(merged_df)

############################################################
#Part 2 - create 3 functions

# State cases per day
cases_per_day <- function(data) {
  data %>%
    filter(Province_State == "Alabama") %>%
    arrange(Date) %>%
    mutate(Confirmed_cases_daily = Confirmed - lag(Confirmed)) %>%
    select(Province_State, Country_Region, Confirmed_cases_daily, Date)
}
state_cases_per_day <- cases_per_day(merged_df)

library(ggplot2)
ggplot(state_cases_per_day, aes(x = Date, y = Confirmed_cases_daily)) +
  geom_point(color = "Black") 

#-----------------------------------------------------------

#State deaths per day
deaths_per_day <- function(data) {
  data %>%
    filter(Province_State == "Alabama") %>%
    arrange(Date) %>%
    mutate(Death_cases_daily = Deaths - lag(Deaths)) %>%
    select(Province_State, Country_Region, Death_cases_daily, Date)
}
state_deaths_per_day <- deaths_per_day(merged_df)

library(ggplot2)
ggplot(state_deaths_per_day, aes(x = Date, y = Death_cases_daily)) +
  geom_point(color = "Black")

library(stats)
data1 <- state_deaths_per_day$Date
data2 <- state_deaths_per_day$Death_cases_daily
bind_1_and_2 <- c(data1,data2)

linear_model_deaths <- lm (state_deaths_per_day ~ Death_cases_daily)


#----------------------------------------------------------

#extract data and then put them in another table called
# "national_death_per_day_table"

library(tidyverse)  
calculate_national_death_per_day <- function(merged_df, dates_range) {
  national_death_per_day_table <- data.frame()
  
  for (i in seq_along(dates_range)) {
    current_date <- dates_range[i]
    previous_date <- current_date - 1
    
    current_date_data <- merged_df[merged_df$Date == as.character(current_date), ]
    previous_date_data <- merged_df[merged_df$Date == as.character(previous_date), ]
    
    national_death_per_day <- data.frame(
      Date = as.character(current_date),
      National_death_per_day = sum(current_date_data$Deaths - previous_date_data$Deaths)
    )
    national_death_per_day_table <- rbind(national_death_per_day_table, national_death_per_day)
  }
  return(national_death_per_day_table)
}

national_death_per_day_table <- calculate_national_death_per_day(merged_df, dates_range)
print(national_death_per_day_table)

ggplot(national_death_per_day_table, aes(x = Date, y = National_death_per_day)) +
  geom_point() +
  labs(title = "National Deaths Per Day Over Time", x = "Date", y = "National Deaths Per Day") 




