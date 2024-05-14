from global_libs.global_imports import *
import pytest


def home_page_url_new(browser):
    """
    Opens main page = environ url
    """
    window_after = browser.window_handles[0]
    browser.switch_to.window(window_after)
    browser.get(pytest.main_url)
    

