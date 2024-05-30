from PIL import Image

__all__ = ['recognize_capcha']


def recognize_capcha(image_url: str) -> str:
    # python -m pytest tests/tools/capcha/test_capcha.py::TestRecognizeCapcha -v
    pass


def _extract_image_from_url(image_url: str) -> Image:
    pass


def _recognizer(image: Image) -> str:
    # python -m pytest tests/tools/capcha/test_capcha.py::TestRecognizer -v
    pass
