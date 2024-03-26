from engine import engine
import battery
from tire import tire_service
import Serviceable

class Car(Serviceable):
    def __init__(self, engine: engine, battery: battery, tire: tire_service):
        self.engine = engine
        self.battery = battery
        self.tire = tire
    
    def need_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
