from enum import Enum
from SberMegaParser.core.parser import Parser
from selenium import webdriver
from SberMegaParser.exceptions import UnsupporetdDynamicParserTypeException
from selenium.common.exceptions import WebDriverException

__all__ = ['DynamicParser', 'DynamicParserType']


class DynamicParserTypeChrome:
    """Chrome."""
    def __init__(self, headless, window_width, window_height):
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
                'download.default_directory': '. SberMegaParser',
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing_for_trusted_sources_enabled': False,
                'safebrowsing.enabled': False
            }
        )


class DynamicParserTypeFirefox:
    """Firefox."""
    def __init__(self, headless, window_width, window_height):
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


class DynamicParser(Parser):
    def __init__(
        self,
        dynamic_parser_type: DynamicParserType,
        headless: bool = False,
        window_width: int = None,
        window_height: int = None
    ):
        if not isinstance(dynamic_parser_type, DynamicParserType):
            raise UnsupporetdDynamicParserTypeException()
        self.parser_type = dynamic_parser_type.value(
            headless=headless,
            window_width=window_width,
            window_height=window_height
        )

    def open_connection(self) -> None:
        if isinstance(self.parser_type, DynamicParserTypeChrome):
            try:
                self.driver = webdriver.Chrome(
                    options=self.parser_type.options
                )
            except WebDriverException:
                raise Exception(
                    'Install webdriver for Chrome from https://developer.'
                    'chrome.com/docs/chromedriver/downloads and put this file '
                    'into the project\'s root directory please!'
                )
        elif isinstance(self.parser_type, DynamicParserTypeFirefox):
            try:
                self.driver = webdriver.Firefox(
                    options=self.parser_type.options
                )
            except WebDriverException:
                raise Exception(
                    'Install webdriver for FireFox from https://github.com/'
                    'mozilla/geckodriver/releases and put this file '
                    'into the project\'s root directory please!'
                )
        else:
            raise UnsupporetdDynamicParserTypeException()

    def get(self, url: str) -> None:
        self.driver.get(url)

    def save_cookies():
        pass

    def close_connection(self, reason: str = None) -> str | None:
        self.driver.close()
        self.driver.quit()
        if reason:
            return reason
