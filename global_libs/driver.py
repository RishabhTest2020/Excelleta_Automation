import logging
import os
import shutil
import selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from helpers.common_helpers import take_screenshot


def get_browser_value():
    try:
        browser_type = os.environ['browser']
    except KeyError:
        browser_type = 'chrome'
    return browser_type


def clear_screenshots():
    folder_path = os.getcwd() + '/screenshots/'
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Check if it is a file and not a directory
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # Optionally, delete directories as well
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


@pytest.fixture()
def browser(request):
    """
    Configures driver parameters - local device or remote
    Use when calling pytest
    Example: browser=chrome url=https:your_url pytest
    """
    Browser = get_browser_value()
    clear_screenshots()
    if Browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_extension(os.getcwd() + '/files/modheader.crx')
        prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False,
                 "profile.password_manager_enabled": False, "profile.default_content_setting_values.geolocation": 2,
                 "profile.default_content_setting_values.autofill": 2, "autofill.profile_enabled": False,
                 "autofill.address_enabled": False,
                 "autofill.credit_card_enabled": False}
        options.add_experimental_option("prefs", prefs)
        options.page_load_strategy = 'normal'
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-notifications')
        # ext_path = os.getcwd() + "/files/APE.crx"
        # options.add_extension(ext_path)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-autofill-keyboard-accessory-view")
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
    else:
        driver = None
    logging.basicConfig(level=logging.INFO)
    driver.implicitly_wait(40)
    driver.maximize_window()
    driver.set_script_timeout(1000)
    driver.set_page_load_timeout(3000)
    print(request.node.name)
    yield driver
    try:
        failed = request.node.session.testsfailed
        if failed > 0:
            take_screenshot(driver)
    except:
        pass
    driver.quit()
