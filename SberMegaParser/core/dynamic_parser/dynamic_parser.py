from typing import List, Iterable, Tuple, Dict
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException as SeleniumWebDriverException,
    TimeoutException as SeleniumTimeoutException,
    JavascriptException as SeleniumJavascriptException,
    StaleElementReferenceException as SeleniumStaleElementReferenceException,
    ElementNotInteractableException as SeleniumElementNotInteractableException,
    NoSuchDriverException as SeleniumNoSuchDriverException
    # NoSuchElementException as SeleniumNoSuchElementException
)
from SberMegaParser.core.parser import (
    Parser
)
from SberMegaParser.core.dynamic_parser.dynamic_parser_type import (
    DynamicParserType, DynamicParserTypeChrome, DynamicParserTypeFirefox
)
from SberMegaParser.core.dynamic_parser.dynamic_parser_keys import (
    DynamicParserKeys
)
from SberMegaParser.tools.other.sleep import (
    sleep_random, TimeRange
)
from SberMegaParser.exceptions import (
    ElementDoesNotExistException, UnsupporetdDynamicParserTypeException,
    DriverIsNotInitializedException, DriverDoesNotExistException,
    DriverAlreadyInitializedException
)
from SberMegaParser.tools.proxy.dynamic_parser_proxy import DynamicParserProxy

__all__ = ['DynamicParser']


class DynamicParser(Parser):
    """Dynamic parser realisation."""
    def __init__(
        self,
        dynamic_parser_type: DynamicParserTypeChrome | DynamicParserTypeFirefox,
        headless: bool = False,
        window_width: int = None,
        window_height: int = None,
        user_agent: str = None,
        cookies: Dict | List[Dict] = None,
        proxy: DynamicParserProxy = None,
        driver_path: str = None
    ):
        if not dynamic_parser_type in (DynamicParserType.chrome,
                                       DynamicParserType.firefox):
            raise UnsupporetdDynamicParserTypeException()
        self.parser_type = dynamic_parser_type(
            headless=headless,
            window_width=window_width,
            window_height=window_height,
            driver_path=driver_path,
            user_agent=user_agent,
            proxy=proxy
        )
        self.__driver = None
        self.__cookies = None
        if cookies is not None:
            if isinstance(cookies, dict):
                self.__cookies = [cookies]
            elif isinstance(cookies, list):
                self.__cookies = cookies
            else:
                raise TypeError('Unvailable cookies format!')

    def open_connection(self) -> None:
        """Create web driver object."""
        if self.__driver is not None:
            raise DriverAlreadyInitializedException()
        match type(self.parser_type):
            case DynamicParserType.chrome:
                try:
                    self.__driver = webdriver.Chrome(
                        options=self.parser_type.options
                    )
                except (SeleniumWebDriverException,
                        SeleniumNoSuchDriverException) as se:
                    raise DriverDoesNotExistException(self.parser_type) from se
            case DynamicParserType.firefox:
                try:
                    self.__driver = webdriver.Firefox(
                        options=self.parser_type.options
                    )
                except (SeleniumWebDriverException,
                        SeleniumNoSuchDriverException) as se:
                    raise DriverDoesNotExistException(self.parser_type) from se
            case _:
                raise UnsupporetdDynamicParserTypeException()

    def windows(self) -> list[str]:
        """Returns list with windows ids."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        return self.__driver.window_handles

    def switch_to_window(self, window_id: str) -> None:
        """Swith to window by id."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        self.__driver.switch_to.window(window_id)

    def close_current_window(self) -> None:
        """Close current window."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        self.__driver.close()

    def get(self, url: str) -> None:
        """Get web page by URI/URL."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        self.__driver.get(url)

    def set_cookies(self):
        """Set cookies for current website."""
        if self.__cookies is not None:
            self.__driver.add_cookie(self.__cookies)
        else:
            raise NotImplementedError('Set cookies when init parser!')

    def del_cookies(self):
        """Delete cookies from opened connection."""
        self.__driver.delete_all_cookies()

    def find(
        self,
        element_xpath: str,
        sleep_range: Tuple[int, int] | TimeRange = TimeRange(100, 200)
    ) -> WebElement:
        """Find one element on web page by xpath."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        sleep_random(sleep_range)
        return self.__driver.find_element(By.XPATH, element_xpath)

    def find_all(
        self,
        element_xpath: str,
        sleep_range: Tuple[int, int] | TimeRange = TimeRange(100, 200)
    ) -> List[WebElement]:
        """Find multiple elements on web page by xpath."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        sleep_random(sleep_range)
        return self.__driver.find_elements(By.XPATH, element_xpath)

    def wait_until_element_located(
        self,
        element_xpath: str,
        waiting_time: int = 10
    ) -> None:
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        wait = WebDriverWait(self.__driver, waiting_time)
        try:
            wait.until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, element_xpath)
                )
            )
        except SeleniumTimeoutException as ste:
            raise ElementDoesNotExistException() from ste

    def wait_until_element_visible(
        self,
        element_xpath: str,
        waiting_time: int = 10
    ) -> None:
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        wait = WebDriverWait(self.__driver, waiting_time)
        try:
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, element_xpath)
                )
            )
        except SeleniumTimeoutException as ste:
            raise ElementDoesNotExistException() from ste

    def write(
        self,
        field: WebElement,
        content: str | DynamicParserKeys | Iterable[str | DynamicParserKeys],
        clear: bool = False,
        sleep_range: Tuple[int, int] | TimeRange = TimeRange(700, 900)
    ) -> None:
        """Write text in the field.

        Parameters
        ----------
        field
            Web element in which you can write some text. You can get this
            element using find or find_all methods.
        content
            Text or keys that you want to write in selected field.
        clear, optional
            Clear the field from previous text before write your text,
            by default False.
        sleep_range, optional
            Sleep range before action, by default TimeRange(700, 900).
        """
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        sleep_random(sleep_range)
        if clear:
            while field.get_attribute('value') != '':
                field.send_keys(DynamicParserKeys.BACKSPACE)
        field.send_keys(*content)

    def get_html(self) -> BeautifulSoup:
        """Returns BS4 object from current web page."""
        return BeautifulSoup(self.__driver.page_source, 'html.parser')

    def click(
        self,
        element: WebElement,
        attempts_number: int = 42,
        sleep_range: Tuple[int, int] | TimeRange = TimeRange(100, 200)
    ) -> bool:
        """Click on the element.

        Parameters
        ----------
        element
            Web element that you want to click.
        attempts_number, optional
            The the number of attempts to press a button, necessary to track
            dynamically changing elements, by default 42.
        sleep_range, optional
            Sleep range before action, by default TimeRange(100, 200).

        Returns
        -------
            A bool value indicating success of the function execution.
        """
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        sleep_random(sleep_range)
        result = False
        while True:
            if attempts_number == 0:
                break
            try:
                self.__driver.execute_script(
                    'arguments[0].scrollIntoView();', element
                )
                # x = element.location['x']
                # y = element.location['y']
                # self.__driver.execute_script(f'window.scrollTo({x}, {y});')
                # self.__driver.execute_script('window.scrollBy(0, -120);')
                ActionChains(self.__driver).move_to_element(element).\
                    click(element).perform()
            except (SeleniumStaleElementReferenceException,
                    SeleniumElementNotInteractableException,
                    SeleniumJavascriptException):
                attempts_number -= 1
                continue
            else:
                result = True
                break
        return result

    def close_connection(self, reason: str = None) -> str | None:
        """Delete web driver object."""
        if self.__driver is None:
            raise DriverIsNotInitializedException()
        self.__driver.close()
        self.__driver.quit()
        self.__driver = None
        if reason:
            return reason

    def get_cookies(self):
        return self.__driver.get_cookies()
