from enum import Enum
from selenium import webdriver

__all__ = [
    'DynamicParserTypeChrome',
    'DynamicParserTypeFirefox',
    'DynamicParserType'
]


class DynamicParserTypeChrome:
    """Chrome."""
    def __init__(
        self, headless, window_width, window_height, driver_path
    ):
        self.driver_path = '/geckodriver' if not driver_path else driver_path

        self.options = webdriver.ChromeOptions()

        self.options.add_argument('start-maximized')
        self.options.add_argument('--window-size=minimaze_window')

        self.options.add_argument('--disable-browser-side-navigation')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--ignore-certificates-errors')
        self.options.add_argument('--disable-prefetch-disable')

        self.options.add_argument('enable-automation')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-setuid-sandbox')
        self.options.add_argument('--disable-software-rasterizer')

        if window_width:
            self.options.add_argument(f'--width={window_width}')
        if window_height:
            self.options.add_argument(f'--height={window_height}')
        if headless:
            self.options.add_argument('--headless')

        self.options.add_experimental_option(
            'prefs',
            {
                'download.default_directory': '.',
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing_for_trusted_sources_enabled': False,
                'safebrowsing.enabled': False
            }
        )


class DynamicParserTypeFirefox:
    """Firefox."""
    def __init__(
        self, headless, window_width, window_height, driver_path
    ):
        self.driver_path = '/geckodriver' if not driver_path else driver_path

        self.options = webdriver.FirefoxOptions()

        if window_width:
            self.options.add_argument(f'--width={window_width}')
        if window_height:
            self.options.add_argument(f'--height={window_height}')
        if headless:
            self.options.add_argument('--headless')


class DynamicParserType(Enum):
    chrome = DynamicParserTypeChrome
    firefox = DynamicParserTypeFirefox
