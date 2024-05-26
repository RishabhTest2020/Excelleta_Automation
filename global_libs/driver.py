import logging
import os
import platform
import selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
# from seleniumwire import webdriver as wire_webdriver
import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_browser_value():
    try:
        browser_type = os.environ['browser']
    except KeyError:
        browser_type = 'chrome'
    return browser_type



@pytest.fixture()
def browser():
    """
    Configures driver parameters - local device or remote
    Use when calling pytest
    Example: browser=chrome url=https:your_url pytest
    """
    Browser = get_browser_value()
    if Browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_extension(os.getcwd() + '/files/modheader.crx')
        prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument('--disable-notifications')
        # ext_path = os.getcwd() + "/files/APE.crx"
        # options.add_extension(ext_path)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        print("Selenium version:", selenium.__version__)
    elif Browser == 'headless_chrome':
        options = webdriver.ChromeOptions()
        # caps = DesiredCapabilities.CHROME
        # caps['loggingPrefs'] = {'performance': 'ALL'}
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument('--disable-notifications')
        options.add_argument('ignore-certificate-errors')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
            # else:
            #     driver = wire_webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        def interceptor(request):
            request.headers['CF-Access-Client-Id'] = '352a2f064e280d15bf045a6c9740638c.access'
            request.headers[
                'CF-Access-Client-Secret'] = '6cd0992b7b60282508def9d038f51f2371c4cf2b1a2ed6d6392868b5e4bfbd4c'
        driver.request_interceptor = interceptor
    else:
        driver = None
    logging.basicConfig(level=logging.INFO)
    driver.implicitly_wait(40)
    driver.maximize_window()
    driver.set_script_timeout(1000)
    driver.set_page_load_timeout(3000)
    yield driver
    driver.quit()

