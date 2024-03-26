import Serviceable
from abc import abstractmethod

class Tire(Serviceable):
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass
