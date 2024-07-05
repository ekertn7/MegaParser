from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

__all__ = [
    'DynamicParserTypeChrome',
    'DynamicParserTypeFirefox',
    'DynamicParserType'
]


class DynamicParserTypeChrome:
    """Initialization dynamic parser for Chrome webdriver."""
    def __init__(self, headless, window_width, window_height, driver_path,
                 user_agent, proxy):
        self.driver_path = '/chromedriver' if not driver_path else driver_path

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
        if user_agent:
            self.options.add_argument(f'user-agent={user_agent}')
        if proxy:
            proxy_url = f'http://{proxy.username}:{proxy.password}@' \
                        f'{proxy.host}:{proxy.port}'
            self.options.add_argument(proxy_url)

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
    """Initialization dynamic parser for Firefox webdriver."""
    def __init__(self, headless, window_width, window_height, driver_path,
                 user_agent, proxy):
        self.driver_path = '/geckodriver' if not driver_path else driver_path

        self.options = webdriver.FirefoxOptions()
        self.options.profile = FirefoxProfile()

        if window_width:
            self.options.add_argument(f'--width={window_width}')
        if window_height:
            self.options.add_argument(f'--height={window_height}')
        if headless:
            self.options.add_argument('--headless')
        if user_agent:
            self.options.profile.set_preference("general.useragent.override", user_agent)
            self.options.profile.update_preferences()
        if proxy:
            self.options.profile.set_preference("network.proxy.type", 1)
            self.options.profile.set_preference("network.proxy.http", proxy.host)
            self.options.profile.set_preference("network.proxy.http_port", proxy.port)
            self.options.profile.update_preferences()


class DynamicParserType:
    """Enum class to choise dynamic pasrser type."""
    chrome = DynamicParserTypeChrome
    firefox = DynamicParserTypeFirefox
