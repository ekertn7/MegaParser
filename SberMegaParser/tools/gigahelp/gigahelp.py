from langchain.chat_models.gigachat import GigaChat
import requests
from bs4 import BeautifulSoup
import re
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__all__ = ['gigahelp']


#TOKEN_GIGACHAT = ''


def gigahelp(url: str, query: str, tag=None, type_parser='bs', driver_path = None, type_query = 'code', auth_token=None) -> str:
    """url - ссылка на сайт,
       query - запрос для GigaChat,
       tag - тэг для указания, если html-код страницы большой,
       type_parser - 'bs' (html-код) или 'selenium' (JavaScipt)
       driver_path - путь к веб-драйверу для selenium
       type_query - вид запроса для GigaChat:
                    'code' - чтобы GigaChat написал парсер по html-коду 
                    'question' - режим работы вопрос-ответ
       auth_token - токен для подключения к GigaChat, по умолчанию None, но без указания не подключится
                    """
    
    """Основная функция для выдачи результата по запросу пользователя.

    Если нужен обычный запрос, в виде вопроса-подсказки то type_query == 'question',
    если нужен парсер по коду html-страницы, то type_query == 'code'"""

    """Пример query для type_query = 'code': 
    
       'Напиши парсер на python используя selenium чтобы получить список отзывов
      [{'name':'Благодарность сотрудникам за профессионализмб вежливость и скорость решения вопросов',
       'full_descr':/services/responses/bank/response/11557227/,
       'date':['07.06.2024 20:37', '25.06.2024 10:09']}].
        Для поиска элементов используй By.XPATH.'
        
        Обязательно нужно дать пример того, что хотите получить, какие поля и пример их содержания.
        """
    if type_query == 'question':
        return _ask_gigachat(query, auth_token)
    if type_query == 'code':
        clear_html = _crop_html(url, tag, type_parser, driver_path)
        return _ask_gigachat("Вот кода сайта: " + clear_html + query, auth_token)




def _crop_html(url: str, tag=None, type_parser='bs', driver_path = None) -> str:
    """Приватная функция для обрезки html.
    Функция для очистки html-кода. Работает по 2-м сценариям, если сайт маленький, то берется весь body от всего html-кода,
    очищается от лишних символов и результат затем можно подать на вход GigaChat.
    Если код большой, то подается тэг, в котором есть необходимая информация (придется посмотреть в код), далее этот текст
    сокращается до 20000 символов (токенов) для экономии кол-ва токенов, которые подаются на вход модели."""
    if type_parser == 'bs':
        if tag==None:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text_with_tags = soup.body.prettify()
            lines = text_with_tags.split('\n')
            cleaned_lines = [line for line in lines if 'script' not in line and '$' not in line and 'noindex' not in line and
                            '</a>' not in line and '</p>' not in line and '</i>' not in line and
                            '<br/>' not in line and '</span>' not in line and '</header>' not in line and '</li>' not in line and
                            '</ul>']
            cleaned_txt = '\n'.join(cleaned_lines)
            cleaned_txt = cleaned_txt[0:20000]

            
        else:
            cleaned_txt = """"""
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            need_html = soup.body.find_all('div', class_=tag)
            for i in need_html:
                cleaned_txt += "".join(i.prettify())
            
            cleaned_txt = cleaned_txt[0:20000]
            
            
            
        cleaned_txt = re.sub(r"\s+", ' ', cleaned_txt)
    
    if type_parser == 'selenium':
        options=ChromeOptions()
        DRIVER = webdriver.Chrome(executable_path=driver_path, options=options)
        DRIVER.get(url)
        DRIVER.implicitly_wait(1)
        
        if tag==None:
                    
            html = DRIVER.find_element_by_tag_name('body').get_attribute('innerHTML')
            
            DRIVER.quit()
            
            lines = html.split('\n')
            cleaned_lines = [line for line in lines if 'script' not in line and '$' not in line and 'noindex' not in line and
                            '</a>' not in line and '</p>' not in line and '</i>' not in line and
                            '<br/>' not in line and '</span>' not in line and '</header>' not in line and '</li>' not in line and
                            '</ul>']
            cleaned_txt = '\n'.join(cleaned_lines)
            cleaned_txt = cleaned_txt[0:20000]

        else:
            cleaned_txt = """"""
            html = DRIVER.find_elements_by_class_name(tag)
            
            for i in html:
                cleaned_txt += "".join(i.get_attribute('innerHTML'))
                
            DRIVER.quit()
            
            cleaned_txt = cleaned_txt[0:20000]
        
        cleaned_txt = re.sub(r'\s+', ' ', cleaned_txt)
    
    return cleaned_txt


def _ask_gigachat(query: str, auth_token) -> str:
    """Запрос к API гигачата."""
    # Авторизация в сервисе GigaChat
    chat = GigaChat(credentials=auth_token,
                verify_ssl_certs=False)
    messages = [SystemMessage(content="""Вы отличный помощник, 
                который помогает писать парсеры по предоставленному коду html-страницы.
                Вы отвечаете только по сути.
                Отвечай только на поставленный вопрос, ответ должен быть краткий и подходящий вопросу.""")]
    messages.append(HumanMessage(content=query))
    res = chat(messages)
    messages.append(res)
    # Ответ модели
    return res.content