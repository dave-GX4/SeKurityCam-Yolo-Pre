from abc import ABC, abstractmethod
from typing import Any, Tuple

class ICamera(ABC):
    @abstractmethod
    def connect_cam(self) -> None:
        pass

    @abstractmethod
    def read_frame(self) -> Tuple[bool, Any]:
        pass

    @abstractmethod
    def disconnect_cam(self) -> None:
        pass