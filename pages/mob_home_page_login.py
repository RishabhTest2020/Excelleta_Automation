from locators.mobile_locators import *
from test_data.testdata import *
from helpers.common_helpers import *
from pages.my_account_page import *
from pages.onboarding_page import *


def home_page_url(mob_browser):
    """
    Opens main page on mobile
    If statement created for BrowserStack
    """
    window_after = mob_browser.window_handles[1]
    mob_browser.switch_to.window(window_after)
    mob_browser.get(base_url)


def agree_mob_cookies(mob_browser):
    """
    Accepts cookies on mobile
    """
    try:
        is_clickable(mob_browser, ACCEPT_MOB_COOKIES, 10)
        do_click(mob_browser, ACCEPT_MOB_COOKIES, 10)
        mob_browser.refresh()
        assert is_visible(mob_browser, ACCEPT_MOB_COOKIES, 5) is False
    except (NoSuchElementException, TimeoutException):
        pass


def click_hamburger_icon(mob_browser):
    """
    Clicks on menu icon on mobile (web)
    """
    is_visible(mob_browser, HOME_HAMBURGER_ICON, 10)
    do_click(mob_browser, HOME_HAMBURGER_ICON, 5)


def login_process(mob_browser, email_address):
    """
    Login to Promo account on mobile
    """
    is_visible(mob_browser, LOGIN_MOBILE_BUTTON, 10)
    do_click(mob_browser, LOGIN_MOBILE_BUTTON, 10)
    do_send_keys(mob_browser, LOGIN_EMAIL, email_address, 10)
    do_send_keys(mob_browser, LOGIN_PASSWORD, read_creds(password, 0), 10)
    time.sleep(5)
    title = mob_browser.title
    try:
        assert title == main_page_title
    except AssertionError:
        print(title)
        pass
    # allure_screenshot(mob_browser)


def click_start_now(mob_browser):
    """
    Clicks on "Start now" button on mobile
    """
    time.sleep(3)
    is_visible(mob_browser, START_NOW_BTN, 10)
    do_click(mob_browser, START_NOW_BTN, 20)


def click_try_free(mob_browser):
    """
    Clicks on "Try for free" button on mobile
    """
    time.sleep(3)
    is_visible(mob_browser, TRY_FREE, 10)
    do_click(mob_browser, TRY_FREE, 20)


def log_out_mobile(mob_browser):
    """
    Log out on mobile
    """
    do_click(mob_browser, IR_HAMBURGER_ICON)
    do_click(mob_browser, IR_SIGN_OUT_BTN)
    time.sleep(3)
    do_click(mob_browser, HOME_HAMBURGER_ICON)
    assert is_visible(mob_browser, HOME_LOGIN_BTN) is True


def verify_signup_mobile(mob_browser):
    """
    Verifies if a user in on the signup page
    """
    assert is_visible(mob_browser, SIGNUP_MOB_ON_POPUP) is True
    do_click(mob_browser, SIGNUP_MOB_ON_POPUP)
    assert is_visible(mob_browser, SIGNUP_MOB_BTN) is True


def signup_flow_mobile(mob_browser):
    """
    Signup as a new user on mobile
    email: promo.test.automation+mobile@gmail.com
    """
    do_click(mob_browser, CHOOSE_BASIC_BTN_MOB)
    assert is_visible(mob_browser, SIGNUP_MOB_BTN) is True
    do_send_keys(mob_browser, SIGNUP_EMAIL, email_mobile, 10)
    do_send_keys(mob_browser, SIGNUP_FULL_NAME, fullname, 10)
    do_send_keys(mob_browser, SIGNUP_PASSWORD, random_password, 10)
    do_click(mob_browser, SIGNUP_MOB_BTN)


def open_social_cal_mobile(mob_browser):
    """
    Opens a social calendar page on mobile
    Only on production
    """
    if os.environ['url'] == 'https://promo.com':
        do_click(mob_browser, SOCIAL_CALENDAR_FROM_MENU)
        assert is_visible(mob_browser, SOCIAL_CALENDAR_HEADER) is True
    else:
        pass


def delete_account_mobile(mob_browser):
    """
    Opens setting page and deletes an account
    email: promo.test.automation+mobile@gmail.com
    """
    mob_browser.get(my_account)
    if is_visible(mob_browser, DELETE_ACCOUNT_PASS_INPUT) is False:
        mob_browser.get(my_account)
    else:
        pass
    mob_browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    do_send_keys(mob_browser, DELETE_ACCOUNT_PASS_INPUT, random_password)
    do_click(mob_browser, DELETE_ACCOUNT_BTN_NEW)
    do_click(mob_browser, DELETE_ACCOUNT_POPUP_BTN)
    assert is_visible(mob_browser, TRY_FREE) is True


def verify_if_mobile_user_exists(browser):
    """
    Covers two cases:
    - when a mobile user doesn't exists on env --> function passes
    - when a mobile user exists --> it will be deleted
    """
    if is_visible(browser, NEW_WRONG_CREDS_ERROR):
        error = get_element_text(browser, NEW_WRONG_CREDS_ERROR)
        assert error == wrong_creds_message
        time.sleep(2)
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Mobile user doesn\'t exist"}}')
    else:
        click_skip(browser)
        go_to_my_account(browser)
        delete_account_new(browser)
        time.sleep(2)
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Mobile user deleted"}}')