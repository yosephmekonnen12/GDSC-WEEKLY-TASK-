#car class
class car:
    def __init__ (self,make:str,model:str,year:int):
        self.make=make
        self.model=model
        self.year=year
    def info(self):
        print(f"this car is made by {self.make}  and its model is {self.model} and it made in {self.year}")
car=car("tesla","cybertruck",2023)
car.info()

#inheritance

class car:
    def __init__ (self,make:str,model:str,year:int):
        self.make=make
        self.model=model
        self.year=year
    def info(self):
        print(f"this car is made by {self.make}  and its model is {self.model} and it made in {self.year}")
class electricar(car):
    def __init__(self,make,model,year,battery):
        super().__init__(make,model,year)
        self.battery= battery
    def einfo(self):
        print(f"electric cars are revolutionary cars and their battery measured in {self.battery}")
    
#car=car("tesla","cybertruck",2023)
#car.info()
electricar=electricar("tesla","model 3",2023,57.1)
electricar.einfo()







