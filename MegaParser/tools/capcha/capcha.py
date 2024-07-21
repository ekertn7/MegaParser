from PIL import Image
import easyocr
import cv2

__all__ = ['recognize_capcha']


def recognize_capcha(image_url: str) -> str:
    # python -m pytest tests/tools/capcha/test_capcha.py::TestRecognizeCapcha -v
    pass


def _extract_image_from_url(image_url: str) -> Image:
    pass


def _recognizer(image: Image) -> str:
    # python -m pytest tests/tools/capcha/test_capcha.py::TestRecognizer -v
    reader = easyocr.Reader(['en'])
    results = reader.recognize(image)
    for result in results:
        return result[1]
