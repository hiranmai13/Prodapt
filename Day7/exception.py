class VehicleError(Exception):
    """Base class for exceptions in this module."""
    pass
class OwnerAlreadyExistsError(VehicleError):
    """Exception raised when trying to set an owner for a vehicle that already has one."""
    def __init__(self, owner_name):
        message = f"Owner '{owner_name}' already exists."
        super().__init__(message)
class InvalidBatteryCapacityError(VehicleError):
    """Exception raised for invalid battery capacity values."""
    def __init__(self, battery_capacity):
        message = f"Invalid battery capacity: {battery_capacity}. Must be a positive number."
        super().__init__(message)