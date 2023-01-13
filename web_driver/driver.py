import os
import platform
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from seleniumwire import webdriver as wire_webdriver
import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from urllib3.exceptions import LocationValueError
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from web_driver.config import *


@pytest.fixture()
def browser():
    """
    Configures driver parameters - local device or remote
    Use when calling pytest
    Example: browser=chrome url=https://promo.com/ pytest
    """
    Browser = os.environ['browser']
    if Browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_extension(os.getcwd() + '/files/modheader.crx')
        prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument('--disable-notifications')
        ext_path = os.getcwd() + "/files/APE.crx"
        options.add_extension(ext_path)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver.implicitly_wait(40)
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
        # options.set_capability('caps', caps)
        if platform.system() == 'Windows':
            if os.environ['url'] == 'https://promo.com':
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            else:
                driver = wire_webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        else:
            if os.environ['url'] == 'https://promo.com':
                driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
            else:
                driver = wire_webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

        def interceptor(request):
            request.headers['CF-Access-Client-Id'] = '352a2f064e280d15bf045a6c9740638c.access'
            request.headers[
                'CF-Access-Client-Secret'] = '6cd0992b7b60282508def9d038f51f2371c4cf2b1a2ed6d6392868b5e4bfbd4c'
        driver.request_interceptor = interceptor
        driver.implicitly_wait(40)
    elif Browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.implicitly_wait(40)
    elif Browser == "browserstack":
        options = webdriver.ChromeOptions()
        options.add_extension(os.getcwd() + '/files/modheader.crx')
        prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument('--disable-notifications')
        ext_path = os.getcwd() + "/files/APE.crx"
        options.add_extension(ext_path)
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--dns-prefetch-disable')
        options.page_load_strategy = 'eager'
        options.set_capability('bstack:options', desired_cap['bstack:options'])
        try:
            try:
                driver = webdriver.Remote(command_executor=browserstack_url,
                                          options=options)
            except BrokenPipeError:
                driver = webdriver.Remote(command_executor=browserstack_url,
                                          options=options)
        except LocationValueError:
            try:
                driver = webdriver.Remote(command_executor=default_browserstack_url,
                                          options=options)
            except BrokenPipeError:
                driver = webdriver.Remote(command_executor=default_browserstack_url,
                                          options=options)
    else:
        raise ValueError("browser must be of value 'chrome' or 'firefox' or 'browserstack or headless_chrome")
    driver.maximize_window()
    driver.set_script_timeout(1000)
    driver.set_page_load_timeout(3000)
    yield driver
    driver.quit()


@pytest.fixture()
def mob_browser():
    """
    Configures driver parameters - local or remote for mobile tests
    Use when calling pytest
    Example: browser=chrome url=https://promo.com/ pytest
    """
    mobile_emulation = {
        "deviceName": "Nexus 7"
    }
    Browser = os.environ['browser']
    if Browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_extension(os.getcwd() + '/files/modheader.crx')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options, keep_alive=True)
    elif Browser == "browserstack":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_experimental_option('w3c', False)
        options.add_extension(os.getcwd() + '/files/modheader.crx')
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        options.set_capability('bstack:options', mob_desired_cap['bstack:options'])
        try:
            driver = webdriver.Remote(command_executor=browserstack_url,
                                      options=options, keep_alive=True)
        except LocationValueError:
            driver = webdriver.Remote(command_executor=default_browserstack_url,
                                      options=options, keep_alive=True)
    else:
        raise ValueError("browser must be of value 'chrome' or 'browserstack")
    driver.implicitly_wait(30)
    driver.set_script_timeout(40)
    yield driver
    driver.quit()
