from abc import ABC, abstractmethod

class Serviceable(ABC):

    @abstractmethod
    def need_service() -> bool:
        pass