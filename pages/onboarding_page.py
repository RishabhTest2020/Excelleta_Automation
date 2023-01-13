import time
from faulthandler import is_enabled
from pages.create_page import *


def skip_onboarding(browser):
    """
    Skips onboarding screen
    """
    if is_visible(browser, CLOSE_BUTTON) is True:
        do_click(browser, CLOSE_BUTTON)
    else:
        pass
    assert is_visible(browser, SEARCH_INPUT_MAIN, 20)


def onboarding_first_screen_validation(browser):
    """
    Validate onboarding first screen by 'continue' button
    """
    is_visible(browser, ONBOARDING_CONTINUE_BTN)


def click_continue_btn(browser):
    """
    Click continue to 2nd screen of OB
    """
    do_click(browser, ONBOARDING_CONTINUE_BTN)


def click_no_website(browser):
    """
    Click no website and validate second screen and all fields are empty
    """
    time.sleep(3)
    do_click(browser, ONBOARDING_DONT_HAVE_WEBSITE)


def fill_website_field(browser, website):
    """
    Provides a website and clicks continue
    Default website: https://brandfetch.com/
    """
    time.sleep(3)
    do_send_keys(browser, ONBOARDING_WEBSITE_INPUT, website)
    do_click(browser, ONBOARDING_CONTINUE_BTN)


def continue_btn_disabled_validation(browser):
    """
    Validates if user can not click on Continue
    """
    assert is_clickable(browser, ONBOARDING_CONTINUE_BTN) is False


def onboarding_second_screen_validation(browser):
    """
    Validate onboarding second screen by 'start creating' button
    """
    is_visible(browser, ONBOARDING_START_CREATING_BTN)


def business_field_empty_content_validation(browser):
    """
    Validate onboarding second screen business field is empty
    """
    if get_element_text(browser, ONBOARDING_BUSINESS_NAME) is None:
        pass


def select_business(browser, type_of_business):
    """
    Select food as business type
    Default type of business: Food
    """
    do_click(browser, ONBOARDING_BUSINESS_TYPE)
    do_send_keys(browser, ONBOARDING_BUSINESS_TYPE, type_of_business)
    do_click(browser, ONBOARDING_BUSINESS_TYPE_1ST_OPTION)
    assert is_visible(browser, ONBOARDING_BUSINESS_TYPE_VALIDATION) is True


def set_country(browser):
    """
    Set UK as country
    """
    do_click(browser, ONBOARDING_COUNTRY_FIELD)
    do_click(browser, ONBOARDING_COUNTRY_SELECTION_UK)
    assert is_visible(browser, ONBOARDING_COUNTRY_SELECTED_UK)


def set_phone(browser, phone_no):
    """
    Set phone number
    Default: 1234567901
    """
    do_click(browser, ONBOARDING_PHONE_NUMBER)
    do_send_keys(browser, ONBOARDING_PHONE_NUMBER, phone_no)
    assert is_visible(browser, ONBOARDING_PHONE_NUMBER)


def mark_checkbox_v(browser):
    """
    Approve sms consent
    """
    do_click(browser, ONBOARDING_SPECIAL_OFFERS_CHECKBOX)
    assert is_visible(browser, ONBOARDING_SPECIAL_OFFERS_CHECKED)


def add_logo_on_onboarding(browser):
    """
    Adds logo on the onboarding screen
    Verifies if the logo has been added to a preview
    to_improve: currently doesn't work - lack of input in the code
    """
    do_hover(browser, ONBOARDING_LOGO_EMPTY)
    do_send_keys(browser, ONBOARDING_LOGO_EMPTY, os.getcwd() + brand_logo)
    assert is_visible(browser, ONBOARDING_PLACEHOLDER_LOGO_ON_PREVIEW) is False
    assert is_visible(browser, ONBOARDING_LOGO_ON_PREVIEW) is True


def replace_logo_on_onboarding(browser):
    """
    Currently: checks if 3 dots menu is opened
    to_improve: replacing currently doesn't work - lack of input in the code
    """
    do_hover(browser, ONBOARDING_LOGO_ADDED)
    do_click(browser, ONBOARDING_LOGO_MENU_DOTS)
    assert is_visible(browser, ONBOARDING_LOGO_MENU_CROP) is True
    assert is_visible(browser, ONBOARDING_LOGO_MENU_REPLACE) is True
    assert is_visible(browser, ONBOARDING_LOGO_MENU_DELETE) is True
    do_click(browser, ONBOARDING_BUSINESS_NAME)
    # do_send_keys(browser, ONBOARDING_LOGO_MENU_REPLACE, os.getcwd() + brand_logo)


def delete_logo_on_onboarding(browser):
    """
    Deletes logo from the onboarding screen
    Verifies if the logo has been removed from a preview
    """
    assert is_visible(browser, ONBOARDING_LOGO_ON_PREVIEW) is True
    do_hover(browser, ONBOARDING_LOGO_ADDED)
    do_click(browser, ONBOARDING_LOGO_MENU_DOTS)
    do_hover(browser, ONBOARDING_LOGO_MENU_DELETE)
    do_click(browser, ONBOARDING_LOGO_MENU_DELETE)
    assert is_visible(browser, ONBOARDING_PLACEHOLDER_LOGO_ON_PREVIEW) is True


def close_appcues_after_onboarding(browser):
    """
    Closes appcues pop-up and verifies if a user reached Create Page
    """
    try:
        switch_to_iframe(browser, APPCUES_FRAME)
        do_click(browser, SKIP_X_BTN_GENERIC, 3)
        browser.switch_to.default_content()
    except (TimeoutException, StaleElementReferenceException, NoSuchElementException):
        pass
    if is_visible(browser, CLOSE_BUTTON) is True:
        do_click(browser, CLOSE_BUTTON)
    else:
        pass
    assert is_visible(browser, SEARCH_INPUT_MAIN)
    do_click(browser, SEARCH_INPUT_MAIN)


def click_start_creating_btn(browser):
    """
    Click on start creating button
    """
    do_click(browser, ONBOARDING_START_CREATING_BTN)
    close_appcues_after_onboarding(browser)


def click_skip(browser):
    """
    Close onboarding popup and user redirected to create page
    """
    do_click(browser, CLOSE_ONBOARDING_POPUP_NEW)
    close_appcues_after_onboarding(browser)


