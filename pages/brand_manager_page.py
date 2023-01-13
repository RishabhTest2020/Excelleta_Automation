import time

from selenium.common.exceptions import TimeoutException
from helpers.common_helpers import *
from locators.locators_file import *
from pages.newcancellation_page import *
from test_data.testdata import *


def goto_bm_page(browser):
    """
    Goes to the dashboard - brand manager tab
    """
    is_visible(browser, MY_WORKSPACE_OR_VIDEOS, 10)
    do_hover(browser, MY_WORKSPACE_OR_VIDEOS)
    is_clickable(browser, MY_VIDEOS_BRANDS, 10)
    do_click(browser, MY_VIDEOS_BRANDS)
    time.sleep(3)
    title = browser.title
    assert title == dashboard_title


def no_brand_is_visible(browser):
    """
    Verifies if no brand is visible on Dashboard
    """
    assert is_visible(browser, AT_LEAST_ONE_BRAND_DISPLAYED) is False


def add_brand_name_first_brand(browser):
    """
    User with a not relevant plan adds a brand and sees the pricing widget
    """
    is_clickable(browser, ADD_BRAND_BTN, 15)
    do_click(browser, ADD_BRAND_BTN)
    switch_to_iframe(browser, EMBED_PRICING_IFRAME)
    assert is_visible(browser, EMBED_PRICING_POPUP) is True
    browser.switch_to.default_content()
    currencies_check(browser)
    switch_to_iframe(browser, EMBED_PRICING_IFRAME)
    do_click(browser, CHOOSE_STANDARD_PUB)
    browser.switch_to.default_content()
    time.sleep(5)


def add_brand_name(browser):
    """
    Creates a new brand and adds its name
    If user has plan without brands - upgrades it
    """
    is_clickable(browser, ADD_BRAND_BTN, 15)
    do_click(browser, ADD_BRAND_BTN)
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    time.sleep(2)
    try:
        is_visible(browser, UPGRADE_PRO_BTN)
        do_click(browser, UPGRADE_PRO_BTN)
        do_click(browser, CONFIRM_BTN)
        time.sleep(5)
    except (TimeoutException, NoSuchElementException):
        pass
    if test_name == 'test_verify_brand_manager_functionalities_basic':
        try:
            is_visible(browser, CREATE_BRAND_POPUP, 30)
            do_click(browser, CREATE_BRAND_SKIP)
            is_visible(browser, BRAND_NAME_TXTBOX)
            do_send_keys(browser, BRAND_NAME_TXTBOX, brand_name)
            is_visible(browser, BRAND_NEXT_BTN)
            do_click(browser, BRAND_NEXT_BTN)
            if is_visible(browser, BRAND_LOGO_POPUP) is True:
                do_click(browser, BRAND_NEXT_BTN)
            else:
                pass
            if is_visible(browser, BRAND_WATERMARK_POPUP) is True:
                do_click(browser, BRAND_NEXT_BTN)
            else:
                pass
            if is_visible(browser, BRAND_FONT_POPUP) is True:
                do_click(browser, BRAND_NEXT_BTN)
            else:
                pass
            is_visible(browser, BRAND_DONE_BTN)
            do_click(browser, BRAND_DONE_BTN)
        except (TimeoutException, NoSuchElementException):
            pass
    else:
        pass
    # allure_screenshot(browser)


def add_brand_comps(browser):
    """
    Adds all brand components:
    logo, colors, fonts, business information
    """
    is_visible(browser, LOGO_TAB)
    do_click(browser, LOGO_TAB, 15)
    is_visible(browser, ADD_LOGO_BTN)
    do_send_keys(browser, ADD_LOGO_BTN, os.getcwd() + brand_logo)
    time.sleep(3)
    is_visible(browser, COLOR_TAB)
    do_click(browser, COLOR_TAB)
    is_visible(browser, ADD_COLOR_BTN)
    do_click(browser, ADD_COLOR_BTN, 10)
    do_click(browser, COLOR_TXTBOX)
    do_clear(browser, COLOR_TXTBOX)
    do_send_keys(browser, COLOR_TXTBOX, green_color)
    try:
        do_click(browser, COLOR_SUBMIT_BTN)
    except (NoSuchElementException, StaleElementReferenceException):
        try:
            do_click(browser, COLOR_SUBMIT_BTN)
        except (StaleElementReferenceException, NoSuchElementException, TimeoutException):
            pass
    time.sleep(2)
    is_visible(browser, FONT_TAB)
    do_click(browser, FONT_TAB)
    is_visible(browser, ADD_FONT_BTN)
    do_click(browser, ADD_FONT_BTN)
    do_click(browser, GOOGLE_FONT_BTN)
    do_send_keys(browser, BM_SEARCH_FONT_INPUT, 'Goldman')
    is_visible(browser, GOLDMAN_GOOGLE_FONT)
    do_click(browser, GOLDMAN_GOOGLE_FONT, 10)
    is_visible(browser, FONT_SUBMIT_BTN)
    do_click(browser, FONT_SUBMIT_BTN)
    time.sleep(1)
    is_visible(browser, BUSINESSINFO_TAB)
    do_click(browser, BUSINESSINFO_TAB)
    for (k, text), (k1, textbox) in zip(BRAND_INFO_TEXT.items(), BRAND_INFO_TXTBOX.items()):
        do_send_keys(browser, textbox, text)
        time.sleep(1)
    is_visible(browser, DONE_BTN)
    do_click(browser, DONE_BTN)
    time.sleep(3)
    brand_name_text = get_element_text(browser, SAVED_BRAND_ASSERT)
    assert brand_name_text == brand_name
    # allure_screenshot(browser)


def delete_brand(browser):
    """
    Deletes a brand
    """
    do_hover(browser, BRAND_DEL_BTN, 10)
    do_click(browser, BRAND_DEL_BTN)
    is_visible(browser, CONFIRM_DEL_BTN)
    do_click(browser, CONFIRM_DEL_BTN)
    time.sleep(10)
    assert is_visible(browser, SAVED_BRAND_ASSERT, 10) is False
    # allure_screenshot(browser)


def init_delete_brand(browser):
    """
    Deletes a brands if any exists at the beginning of a test
    """
    while is_visible(browser, FIRST_EDIT_BRAND_BTN) is True:
        do_hover(browser, BRAND_DEL_BTN, 10)
        if is_visible(browser, BRAND_DEL_BTN) is False:
            break
        do_click(browser, BRAND_DEL_BTN)
        is_visible(browser, CONFIRM_DEL_BTN)
        do_click(browser, CONFIRM_DEL_BTN)
        time.sleep(5)
    else:
        pass


def create_new_project(browser):
    """
    Clicks on the New Project button - main menu
    """
    is_visible(browser, NEW_PROJECT_BTN)
    do_click(browser, NEW_PROJECT_BTN)


def select_brand_logo_watermark(browser):
    """
    Select Logo and Watermark on Brand configuration page
    """
    if is_visible(browser, ADD_BRAND_BTN, 10) is True:
        do_click(browser, ADD_BRAND_BTN)
    try:
        is_visible(browser, UPGRADE_PRO_BTN)
        do_click(browser, UPGRADE_PRO_BTN)
        do_click(browser, CONFIRM_BTN)
        time.sleep(5)
    except (TimeoutException, NoSuchElementException):
        pass
    is_visible(browser, CREATE_BRAND_POPUP)
    do_click(browser, CREATE_BRAND_SKIP)
    is_visible(browser, BRAND_NAME_TXTBOX)
    do_send_keys(browser, BRAND_NAME_TXTBOX, brand_name2)
    is_visible(browser, BRAND_NEXT_BTN)
    do_click(browser, BRAND_NEXT_BTN)
    if is_visible(browser, BRAND_LOGO_POPUP, 15) is True:
        do_hover(browser, CHOOSE_IMAGE)
        do_click(browser, CHOOSE_IMAGE)
        do_click(browser, BRAND_NEXT_BTN)
    else:
        pass
    if is_visible(browser, BRAND_WATERMARK_POPUP, 10) is True:
        do_hover(browser, CHOOSE_IMAGE2)
        do_click(browser, CHOOSE_IMAGE2)
        do_click(browser, BRAND_NEXT_BTN)
    else:
        pass
    if is_visible(browser, BRAND_FONT_POPUP, 10) is True:
        do_click(browser, BRAND_NEXT_BTN)
    # allure_screenshot(browser)
    is_visible(browser, BRAND_DONE_BTN)
    do_click(browser, BRAND_DONE_BTN)
    time.sleep(4)
    is_visible(browser, DONE_BTN)
    do_click(browser, DONE_BTN, 10)
    # allure_screenshot(browser)
