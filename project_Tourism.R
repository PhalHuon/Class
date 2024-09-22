#This project uses function to pass the years as parameters and will create a chart describing the trend as for GDP of the country

#used excel to clean data

install.packages("tidyverse")
install.packages("read_xl")

library(tidyverse)
library(ggplot2)
library(readxl)

#already imported dataset using "Environment"
#tourism_data <- read_excel("tourism_data.xlsx")

View(tourism_data)
#---------------------------------------------------------------------------------

names(tourism_data)[1] <- "Country"

#years range can be changed from up here
plot_custom_countries <- function(data, ..., starting_year = 1995, ending_year = 2017) {
  # convert the year columns to numeric
  year_columns <- as.character(starting_year:ending_year)
  
  tour_plot <- data %>%
    select(Country, year_columns) %>%
    pivot_longer(!Country, names_to = "Years", values_to = "Price_value") %>%
    filter(Country %in% c(...)) %>%
    ggplot(aes(x = as.numeric(Years), y = Price_value, group = Country, color = Country)) +
    geom_line() + geom_point() +scale_y_log10() +
    labs(title = "Tourism Data",
         x = "Years",
         y = "Price Value ($)")
  
  print(tour_plot)
}

#can change values of country1,2,3 into any countries in the dataset
plot_custom_countries(tourism_data, country1 = "China", country2 = "Ghana", country3 = "United States")
