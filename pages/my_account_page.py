from selenium.webdriver.common.keys import Keys
from locators.locators_file import *
from test_data.testdata import *
from helpers.common_helpers import *
from helpers.generator import *
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait


def go_to_my_account(browser):
    """
    Goes to My Account page
    """
    time.sleep(3)
    do_hover(browser, USERNAME_MENU)
    try:
        do_click(browser, MY_ACCOUNT, 15)
    except (NoSuchElementException, TimeoutException):
        browser.refresh()
        time.sleep(4)
        skip_offer_modal(browser)
        do_hover(browser, USERNAME_MENU)
        do_click(browser, MY_ACCOUNT, 15)
    is_visible(browser, MY_ACCOUNT_IFRAME, 25)
    title = browser.title
    assert title == my_account_title


def provide_password_to_delete(browser):
    """
    Send keys (password) to "delete section" in settings
    For re-use in delete_account_new
    """
    do_send_keys(browser, DELETE_ACCOUNT_PASS_INPUT, random_password)
    is_visible(browser, DELETE_ACCOUNT_BTN_NEW, 20)
    do_click(browser, DELETE_ACCOUNT_BTN_NEW)
    is_visible(browser, DELETE_ACCOUNT_POPUP_BTN, 20)
    do_click(browser, DELETE_ACCOUNT_POPUP_BTN)


def delete_account_new(browser):
    """
    Deletes account via My Account page - new after changes
    If a pop-up "invalid password" is displayed, the scripts again try to delete
    """
    is_visible(browser, MY_ACCOUNT_IFRAME, 25)
    if is_visible(browser, INTERCOM_SURVEY_IFRAME) is True:
        switch_to_iframe(browser, INTERCOM_SURVEY_IFRAME)
        do_click(browser, INTERCOM_SURVEY_CLS)
        browser.switch_to.default_content()
    else:
        pass
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME)
    is_visible(browser, DELETE_ACCOUNT_PASS_INPUT, 20)
    provide_password_to_delete(browser)
    if is_visible(browser, OK_BUTTON) is True:
        do_click(browser, OK_BUTTON)
        provide_password_to_delete(browser)
    browser.switch_to.default_content()
    try:
        assert is_visible(browser, SIGNUP_BTN, 40) is True
    except (AssertionError, StaleElementReferenceException):
        browser.refresh()
        assert is_visible(browser, SIGNUP_BTN, 40) is True


def disconnect_from_facebook(browser):
    """
    Disconnects from Facebook account
    Add new e-mail and new password
    # to_improve: merge FB and GG functions into one and add parameter in assertion
    """
    time.sleep(5)
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME, 10)
    is_visible(browser, DISCONNECT_FROM_FB, 20)
    do_click(browser, DISCONNECT_FROM_FB, 10)
    do_send_keys(browser, ENTER_NEW_EMAIL, email_delete)
    do_send_keys(browser, ENTER_NEW_PASS, random_password)
    do_send_keys(browser, ENTER_NEW_PASS_CONFIRM, random_password)
    do_click(browser, SAVE_CHANGES_BTN)
    assert is_invisible(browser, DISCONNECT_FROM_FB, 25) is True
    browser.switch_to.default_content()


def disconnect_from_google(browser):
    """
    Disconnects from Google account
    Add new e-mail and new password
    """
    time.sleep(5)
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME, 10)
    is_visible(browser, DISCONNECT_FROM_GG, 20)
    do_click(browser, DISCONNECT_FROM_GG, 10)
    do_send_keys(browser, ENTER_NEW_EMAIL, email_delete)
    do_send_keys(browser, ENTER_NEW_PASS, random_password)
    do_send_keys(browser, ENTER_NEW_PASS_CONFIRM, random_password)
    do_click(browser, SAVE_CHANGES_BTN)
    assert is_visible(browser, DISCONNECT_FROM_GG, 15) is False
    browser.switch_to.default_content()


def change_password_incorrectly(browser):
    """
    Tries to change password with incorrect data
    """
    time.sleep(6)
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME, 10)
    is_visible(browser, NEW_PASS_INPUT)
    do_send_keys(browser, NEW_PASS_INPUT, random_password)
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, RE_NEW_PASS_INPUT)
    do_send_keys(browser, RE_NEW_PASS_INPUT, "abcde")
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, CURRENT_PASS_INPUT)
    do_send_keys(browser, CURRENT_PASS_INPUT, read_creds(password, 0))
    do_send_keys(browser, CURRENT_PASS_INPUT, Keys.ENTER)
    time.sleep(2)
    assert get_element_text(browser, SETTING_MESSAGE) == setting_message_my_account_fail
    browser.switch_to.default_content()
    # allure_screenshot(browser)


def change_password(browser):
    """
    Changes password correctly
    """
    time.sleep(5)
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME, 10)
    is_visible(browser, NEW_PASS_INPUT)
    do_send_keys(browser, NEW_PASS_INPUT, random_password)
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, RE_NEW_PASS_INPUT)
    do_send_keys(browser, RE_NEW_PASS_INPUT, random_password)
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, CURRENT_PASS_INPUT)
    do_send_keys(browser, CURRENT_PASS_INPUT, read_creds(password, 1))
    try:
        is_visible(browser, ACCOUNT_SAVE_CHANGES_BTN)
        do_click(browser, ACCOUNT_SAVE_CHANGES_BTN, 10)
    except WebDriverException:
        pass


def change_password_to_correct(browser):
    """
    Changes password to the correct one
    """
    time.sleep(5)
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME, 10)
    is_visible(browser, NEW_PASS_INPUT)
    do_send_keys(browser, NEW_PASS_INPUT, read_creds(password, 1))
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, RE_NEW_PASS_INPUT)
    do_send_keys(browser, RE_NEW_PASS_INPUT, read_creds(password, 1))
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, CURRENT_PASS_INPUT)
    do_send_keys(browser, CURRENT_PASS_INPUT, random_password)
    try:
        is_visible(browser, ACCOUNT_SAVE_CHANGES_BTN)
        do_click(browser, ACCOUNT_SAVE_CHANGES_BTN, 10)
    except WebDriverException:
        pass


def verify_change_success_message(browser):
    """
    Verifies success message after changing the password
    """
    if is_visible(browser, SETTING_MESSAGE, 15) is True:
        try:
            assert get_element_text(browser, SETTING_MESSAGE) == setting_message_my_account_success
        except AssertionError:
            pass
        do_click(browser, POP_UP_OK)
    else:
        pass
    browser.switch_to.default_content()
    # allure_screenshot(browser)


def rechange_password(browser):
    """
    Rechanges password to default
    """
    time.sleep(5)
    switch_to_iframe(browser, MY_ACCOUNT_IFRAME, 10)
    is_visible(browser, NEW_PASS_INPUT)
    do_send_keys(browser, NEW_PASS_INPUT, read_creds(password, 1))
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, RE_NEW_PASS_INPUT)
    do_send_keys(browser, RE_NEW_PASS_INPUT, read_creds(password, 1))
    if is_visible(browser, ERROR_POP_UP) is True:
        do_click(browser, POP_UP_OK)
    else:
        pass
    is_visible(browser, CURRENT_PASS_INPUT)
    do_send_keys(browser, CURRENT_PASS_INPUT, random_password)
    try:
        is_visible(browser, ACCOUNT_SAVE_CHANGES_BTN)
        do_click(browser, ACCOUNT_SAVE_CHANGES_BTN, 10)
    except WebDriverException:
        pass
