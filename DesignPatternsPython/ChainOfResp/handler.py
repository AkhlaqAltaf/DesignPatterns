
from abc import ABC , abstractmethod
from typing import Any , Optional
class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Any) -> Optional[str]:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass
