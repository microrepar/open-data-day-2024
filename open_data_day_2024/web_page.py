"""Modulo para criar instancias do driver da pagina a ser controlada 
e verificar a existencia de elementos com wait explicito
"""
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def get_page_driver(url: str) -> WebDriver:
    """Retorna o driver com a pagina carregada a partir da url

    Args:
        url (str): endereco da pagina a ser controlada

    Returns:
        WebDriver: controladora da pagina carregada
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    

    # Cria a instancia do ChromeWebDriver
    driver = webdriver.Chrome( 
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    # Acessa a pagina da url
    driver.get(url)

    return driver


def get_element_by_xpath(driver: WebDriver, xpath: str, max_wait: int = 10) -> WebDriver:
    """Verifica se o elemento na pagina foi encontrado em um máximo de tempo
    se nenhum valor for informado para o parametro max_wait o valor default 
    de espera eh de 10 segundos

    Args:
        driver (WebDriver): controladora da pagina carregada
        xpath (str): tipo de seletor para identificar um elemento DOM
        max_wait (int, optional): tempo maximo de espera para um elemento ser encontrado na DOM. Defaults to 10.

    Returns:
        WebElement : retorna um objeto WebElement somente com o elemento encontrado
    """
    try:
        element = WebDriverWait(driver, max_wait).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    except:
        return None
    
    return element
    
