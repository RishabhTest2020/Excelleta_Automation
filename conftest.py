import base64
import pdb
import pytest
import pytest_html
from pytest_metadata.plugin import metadata_key
from _pytest.fixtures import FixtureRequest
import logging
import os
import shutil
import selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from helpers.common_helpers import delete_all_class_vars_in_project

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_browser_value():
    try:
        browser_type = os.environ['browser']
    except KeyError:
        browser_type = 'chrome'
    return browser_type


@pytest.fixture(scope="class", autouse=True)
def browser(request):
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
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-autofill-keyboard-accessory-view")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
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
    driver.implicitly_wait(40)
    driver.maximize_window()
    driver.set_script_timeout(1000)
    driver.set_page_load_timeout(3000)
    print(request.node.name)
    yield driver
    delete_all_class_vars_in_project(os.getcwd())
    driver.quit()


def pytest_html_report_title(report):
    report.title = " Excelleta Automation Report"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    extras = getattr(rep, 'extra', [])
    # only add screenshot to the report if test failed
    if rep.when == 'call' and rep.failed:
        if 'browser' in item.fixturenames:
            caplog = item._request.getfixturevalue('caplog')
            log_text = '\n'.join([record.getMessage() for record in caplog.records])
            extras.append(pytest_html.extras.text(log_text, 'log'))
            web_driver = item.funcargs['browser']
            # make the screenshot file name
            screenshot_dir = os.path.join('report', 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_file = os.path.join(screenshot_dir, f"{item.nodeid.replace('::', '_')}.png")
            web_driver.save_screenshot(screenshot_file)
            currentUrl = web_driver.current_url
            # attach the screenshot to the html report
            screenshot = screenshot_file.lstrip("/report").lstrip("\\report")
            if screenshot_file:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot
                extras.append(pytest_html.extras.url(f'{currentUrl}'))
                extras.append(pytest_html.extras.html(html))
        rep.extras = extras

