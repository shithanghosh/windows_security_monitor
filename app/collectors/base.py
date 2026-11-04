from abc import ABC, abstractmethod

class BaseCollector(ABC):
    """
    Abstract base class for all Windows Security collectors.
    Enforces the structured evidence format.
    """
    @abstractmethod
    def collect(self) -> dict:
        pass
