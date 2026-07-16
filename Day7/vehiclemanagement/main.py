from car import Car
from ev import EV
from polymorphism import Overloading_demo

car1 = Car("Toyota", "Camry", 2020) # type: ignore
ev1 = EV("Tesla", "Model 3", 2021, 75)  # 75 kWh battery capacity 
print(car1.brand) # type: ignore

car1.set_owner("Alice") # type: ignore
print(car1.get_owner()) # type: ignore

car1.set_owner("Bob")  # type: ignore # Attempt to change owner
print(car1.get_owner())  # type: ignore # Should still be Alice

car1.start_engine() # type: ignore
car1.show_info() # type: ignore
