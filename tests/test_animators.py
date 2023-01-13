import time

from pytest_bdd import given, when, then
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from pages.animators_page import *


@given('User enables animation playground google chrome extension')
def step_to_enable_APE_chrome_extension(browser):
    enable_APE_chrome_extension(browser)


@when('User opens a animation preview tab first half set')
def step_to_open_animation_preview_tab(browser):
    try:
        open_animation_preview_tab(browser)
        path = os.getcwd() + '/promoanimations'
        dir_list2 = os.listdir(path)
        print(dir_list2)
        run_animations(browser, 0, int(len(dir_list2)/2))
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_to_open_animation_preview_tab)


@when('User opens a animation preview tab second half set')
def step_to_open_animation_preview_tab2(browser):
    try:
        open_animation_preview_tab(browser)
        path = os.getcwd() + '/promoanimations'
        dir_list2 = os.listdir(path)
        print(dir_list2)
        run_animations(browser, int(len(dir_list2)/2), int(len(dir_list2)))
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_to_open_animation_preview_tab2)
