class EV:
    def __init__(self, brand, model, year, battery_capacity, owner=None):
        super().__init__(brand, model, year, owner) # type: ignore
        self.battery_capacity = battery_capacity  # in kWh
    
    def start_engine(self):
        print(f"The electric engine of the {self.brand} {self.model} is starting silently.") # type: ignore
    
    def charge_battery(self):
        print(f"The battery of the {self.brand} {self.model} is charging. Capacity: {self.battery_capacity} kWh.") # type: ignore
        