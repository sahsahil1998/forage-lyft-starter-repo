from abc import ABC, abstractmethod
from serviceable import Serviceable

class Battery(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
