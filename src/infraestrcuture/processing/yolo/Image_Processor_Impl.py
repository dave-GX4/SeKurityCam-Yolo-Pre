from ultralytics import YOLO
from src.domain.interface.I_Image_Processor import IImageProcessor

class ImageProcessorImpl(IImageProcessor):
    def __init__(self, model: str):
        self.model = model

    def load_model(self) -> None:
        try:
            self.model = YOLO(self.model)

        except Exception as e:
            raise RuntimeError(f"Error al cargar el modelo: {e}")
        