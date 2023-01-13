import ast
import time

from locators.locators_file import *
from helpers.common_helpers import *
from test_data.testdata import *
from helpers.generator import *
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.common.exceptions import StaleElementReferenceException


def home_page_url_new(browser):
    """
    Opens main page = environ url
    """
    window_after = browser.window_handles[0]
    browser.switch_to.window(window_after)
    browser.get(base_url_new)


def check_url_utm(browser):
    """
    Opens base url and check UTM
    """
    window_after = browser.window_handles[0]
    browser.switch_to.window(window_after)
    browser.get(base_url_new)
    time.sleep(7)
    storage = browser.execute_script("return window.localStorage;")
    try:
        utm = storage['firstImpressionsUTMs']
        utm_value = ast.literal_eval(utm)['firstVisit_source']
        assert utm_value == 'organicdirect'
    except Exception:
        browser.refresh()
        time.sleep(7)
        utm = storage['firstImpressionsUTMs']
        utm_value = ast.literal_eval(utm)['firstVisit_source']
        assert utm_value == 'organicdirect'


def get_login_title(browser):
    """
    Gets the title of the new login page
    """
    login_title = browser.title
    assert login_title == title_new_login


def is_login_link_exists(browser):
    """
    Checks if login link exists
    """
    return is_visible(browser, LOGIN_BTN, 10)


def accept_cookies_new(browser):
    """
    Accepts cookies on new Login Page
    """
    is_clickable(browser, AGREE_COOKIES_NEW_AUTH, 10)
    do_click(browser, AGREE_COOKIES_NEW_AUTH)
    browser.refresh()
    assert is_invisible(browser, AGREE_COOKIES_NEW_AUTH, 2)


def skip_cookies(browser):
    """
    Skip cookies on new Login Page
    """
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    else:
        pass


def skip_cookies_next(browser):
    """
    Skip cookies on next branches
    """
    if is_visible(browser, AGREE_COOKIES_NEXT) is True:
        do_click(browser, AGREE_COOKIES_NEXT)
    else:
        pass


def enter_email_new(browser, email_id):
    """
    Enters e-mail on new login page
    """
    do_send_keys(browser, LOGIN_EMAIL, email_id, 10)


def enter_password_new(browser, password_str):
    """
    Enters correct password on new login page
    """
    do_send_keys(browser, LOGIN_PASSWORD, password_str, 10)


def enter_password_changed(browser):
    """
    Enters changed password on new login page
    """
    do_send_keys(browser, LOGIN_PASSWORD, random_password, 10)


def enter_wrong_password_new(browser):
    """
    Enters wrong password, generated randomly
    """
    wrong_pass = random_password_string(7)
    do_send_keys(browser, LOGIN_PASSWORD, wrong_pass, 10)


def click_login_new(browser):
    """
    Clicks login button on new login page
    """
    try:
        do_click(browser, LOGIN_NEW_BTN, 10)
    except StaleElementReferenceException as cln:
        print(str(cln))
        pass
    except NoSuchElementException as clnn:
        print(str(clnn))
        pass
    except TimeoutException as clnnn:
        print(str(clnnn))
        pass


def login_process_steps_email(browser):
    """
    Simulates the new login process with an e-mail
    """
    is_visible(browser, USERNAME_MENU, 10)
    assert get_element_text(browser, USERNAME_MENU) == username_menu_text


def forgot_password_steps(browser):
    """
    Reminds forgotten password
    """
    is_visible(browser, LOGIN_BTN, 10)
    do_click(browser, LOGIN_BTN, 10)
    do_click(browser, FORGOT_PASSWORD, 10)
    text = get_element_text(browser, FORGOT_PASSWORD_TEXT)
    assert text == forget_password_text
    do_send_keys(browser, LOGIN_EMAIL, email, 10)
    do_click(browser, FORGOT_PASSWORD_SEND_EMAIL_BTN, 10)
    text2 = get_element_text(browser, FORGOT_PASSWORD_SENT)
    assert text2 == request_sent_text


def new_empty_textbox_error(browser):
    """
    Checks error message for empty input
    to_improve: merge this function and new_wrong_login_creds_error into one and add parameters for errors
    """
    error_message = get_element_text(browser, NEW_EMPTY_FIELD_ERROR)
    print(error_message)
    assert error_message == empty_textbox_message
    # allure_screenshot(browser)


def new_wrong_login_creds_error(browser):
    """
    Checks error message for wrong credentials
    """
    error = get_element_text(browser, NEW_WRONG_CREDS_ERROR)
    print(error)
    assert error == wrong_creds_message
    # allure_screenshot(browser)


def enter_deleted_credentials(browser, random_email):
    """
    Enters deleted account credentials
    """
    do_send_keys(browser, LOGIN_EMAIL, random_email, 10)
    do_send_keys(browser, LOGIN_PASSWORD, random_password, 10)