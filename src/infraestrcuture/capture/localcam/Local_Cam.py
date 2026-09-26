import cv2
from typing import Any, Tuple
from src.domain.interface.I_Camera import ICamera

class LocalCam(ICamera):
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None

    def connect_cam(self) -> None:
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError(f"No se pudo abrir la cámara en el índice {self.camera_index}")

    def read_frame(self) -> Tuple[bool, Any]:
        if self.cap is None or not self.cap.isOpened():
            raise RuntimeError("Intento de leer fotograma en una cámara local desconectada.")
        return self.cap.read()

    def disconnect_cam(self) -> None:
        if self.cap is not None:
            self.cap.release()
            self.cap = None