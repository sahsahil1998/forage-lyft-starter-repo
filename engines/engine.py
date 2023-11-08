from abc import abstractmethod
from serviceable import Serviceable

class Engine(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
