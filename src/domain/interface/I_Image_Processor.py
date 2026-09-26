import numpy as np
from typing import List
from abc import ABC, abstractmethod
from src.domain.entity.Deteccion import Deteccion

class IImageProcessor(ABC):
    
    @abstractmethod
    def load_model(self) -> None:
        pass

    @abstractmethod
    def predict(self, frame: np.ndarray, stream: bool = True) -> List[Deteccion]:
        pass