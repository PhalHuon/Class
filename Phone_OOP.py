#this program utilizes "class" to make attributes for a normal smart phone containing 
#phone plan and network

from re import S
from typing import Optional

class Network:
    
    def __init__(self) -> None:
        self._database = {} # phone number -> phone object

    def register(self, phone_number:str, phone: "Smartphone"):
        self._database[phone_number] = phone

    def get(self, phone_number:str) -> Optional["Smartphone"]:

        return self._database.get(phone_number)

class Plan:

    def __init__(self, provider, data, minutes, text) -> None:
        self.__provider = provider

        self.__max_data = data
        self.__used_data = 0

        self.__max_min = minutes
        self.__used_min = 0

        self.__max_text = text
        self.__used_text = 0 

    @property
    def provider(self):
        return self.__provider

    @property
    def max_minutes(self):   
        return self.__max_min
    
    @property
    def used_minutes(self):
        return self.__used_min

    def call(self, duration:int) -> bool:

        if duration > (self.max_minutes - self.used_minutes):
            return False

        self.__used_min += duration

        return True

    def reset(self):
        self.__used_data = 0
        self.__used_min = 0
        self.__used_text = 0

    def __str__(self):
        return f"Data: {self.__used_data} of {self.__max_data}\nMinutes: {self.__used_min} of {self.__max_min}\nText: {self.__used_text} of {self.__max_text}"


class Smartphone:

    def __init__(self, phone_number:str, make:str, model:str, network:Network, plan:Plan) -> None:
        
        self.__phone_number = phone_number
        self.__make = make 
        self.__model = model
        self.__network = network
        self.__plan = plan

    @property
    def plan(self):
        return self.__plan


    def register(self):
        self.__network.register(self.__phone_number, self)

    def call(self, phone_number:str, duration:int):
        # other_phone = self.__network.get(phone_number)
        # if other_phone:
        #     ...

        if other_phone := self.__network.get(phone_number): # get the other phone and check if its not None  
            if self.plan.call(duration):
                other_phone.plan.call(duration)
                return True

        return False



    def __str__(self) -> str:
        return f"{self.__plan.provider} {self.__make} {self.__model} [{self.__phone_number}]"


north_america = Network()

verizon = Plan("Verizon", 100, 100, 100)
t_mobile = Plan("T-Mobile", 100, 100, 100)

iphone = Smartphone("+1-123-456-7890", "Apple", "iPhone 15", north_america, verizon)
pixel = Smartphone("+1-012-345-6789", "Google", "Pixel", north_america, t_mobile)

iphone.register()
pixel.register()

print(iphone)
print(pixel)

iphone.call("+1-012-345-6789", 10)
pixel.call("+1-123-456-7890", 20)

print("Iphone Plan")
print(iphone.plan)

print("Pixel Plan")
print(pixel.plan)
