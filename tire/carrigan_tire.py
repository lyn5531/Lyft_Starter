from tire_service import Tire

class CarriganTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array
    
    def needs_service(self) -> bool:
        return any(tire_wear >= 0.9 for tire_wear in self.wear_array)