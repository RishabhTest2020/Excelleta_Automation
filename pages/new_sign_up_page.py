import time

from locators.google_locators import *
from locators.facebook_locators import *
from pages.sign_up_page import *


def get_signup_title(browser):
    """
    Gets the title of the new signup page and assert
    """
    signup_page_title = browser.title
    assert signup_page_title == title_signup_page


def is_signup_link_exists(browser):
    """
    Checks if signup link exists
    Returns:
        True or False
    """
    is_visible(browser, SIGNUP_BTN, 10)


def new_signup_process_steps_email(browser):
    """
    Simulates the new signup process
    """
    random_email = random_promo_email_generator()
    is_visible(browser, SIGNUP_BTN, 10)
    do_click(browser, SIGNUP_BTN, 10)
    time.sleep(2)
    do_send_keys(browser, SIGNUP_FULL_NAME, fullname, 10)
    do_send_keys(browser, SIGNUP_EMAIL, random_email, 10)
    do_send_keys(browser, SIGNUP_PASSWORD, random_password, 10)
    is_visible(browser, SIGNUP_NEW_BTN, 10)
    do_click(browser, SIGNUP_NEW_BTN, 10)


def new_signup_process_steps_email_short(browser):
    """
    Simulates the new signup process directly from signup page
    """
    random_email = random_promo_email_generator()
    browser.get(signup_url)
    do_send_keys(browser, SIGNUP_FULL_NAME, fullname, 10)
    do_send_keys(browser, SIGNUP_EMAIL, random_email, 10)
    do_send_keys(browser, SIGNUP_PASSWORD, random_password, 10)
    is_visible(browser, SIGNUP_NEW_BTN, 10)
    do_click(browser, SIGNUP_NEW_BTN, 10)


def signup_process_steps_email(browser, random_email):
    """
    Simulates the new signup process - for deleting purposes
    """
    is_visible(browser, SIGNUP_BTN, 10)
    do_click(browser, SIGNUP_BTN, 10)
    time.sleep(2)
    do_send_keys(browser, SIGNUP_FULL_NAME, fullname, 10)
    do_send_keys(browser, SIGNUP_EMAIL, random_email, 10)
    do_send_keys(browser, SIGNUP_PASSWORD, random_password, 10)
    is_visible(browser, SIGNUP_NEW_BTN, 10)
    do_click(browser, SIGNUP_NEW_BTN, 10)


def new_signup_process_facebook(browser):
    """
    Signs up via Facebook account
    """
    is_visible(browser, SIGNUP_BTN, 10)
    do_click(browser, SIGNUP_BTN, 10)
    time.sleep(2)
    is_visible(browser, CONTINUE_FACEBOOK_BTN)
    do_click(browser, CONTINUE_FACEBOOK_BTN)
    if is_visible(browser, FB_ACCEPT_COOKIES) is True:
        do_click(browser, FB_ACCEPT_COOKIES)
    else:
        pass
    if is_visible(browser, FB_ACCEPT_ALL_COOKIES) is True:
        do_click(browser, FB_ACCEPT_ALL_COOKIES)
    else:
        pass
    do_send_keys(browser, FB_EMAIL_INPUT, email)
    do_send_keys(browser, FB_PASS_INPUT, read_creds(password, 2))
    try:
        do_click(browser, FB_LOGIN_BTN)
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        if is_visible(browser, COOKIES_ALLOW) is True:
            do_click(browser, COOKIES_ALLOW)
            try:
                do_click(browser, FB_LOGIN_BTN)
            except (NoSuchElementException, TimeoutException):
                pass
        pass
    try:
        do_click(browser, FB_OK_BTN)
    except (NoSuchElementException, TimeoutException):
        pass
    except ElementClickInterceptedException:
        if is_visible(browser, COOKIES_ALLOW) is True:
            do_click(browser, COOKIES_ALLOW)
        else:
            pass
    try:
        select_video_preferences(browser)
    except (NoSuchElementException, TimeoutException):
        pass
    try:
        switch_to_iframe(browser, APPCUES_FRAME)
        do_click(browser, SKIP_X_BTN_GENERIC, 3)
        browser.switch_to.default_content()
    except (TimeoutException, StaleElementReferenceException, NoSuchElementException):
        pass


def skip_video_preferences_and_appcues(browser):
    """
    Skips onboarding and appcues pop-up after sign up
    """
    try:
        select_video_preferences(browser)
    except (NoSuchElementException, TimeoutException):
        pass
    try:
        switch_to_iframe(browser, APPCUES_FRAME)
        do_click(browser, SKIP_X_BTN_GENERIC, 3)
        browser.switch_to.default_content()
    except (TimeoutException, StaleElementReferenceException, NoSuchElementException):
        pass


def new_signup_process_facebook(browser):
    """
    Signs up via Facebook account
    """
    is_visible(browser, SIGNUP_BTN, 10)
    do_click(browser, SIGNUP_BTN, 10)
    time.sleep(2)
    is_visible(browser, CONTINUE_FACEBOOK_BTN)
    do_click(browser, CONTINUE_FACEBOOK_BTN)
    if is_visible(browser, FB_ACCEPT_COOKIES) is True:
        do_click(browser, FB_ACCEPT_COOKIES)
    else:
        pass
    if is_visible(browser, FB_ACCEPT_ALL_COOKIES) is True:
        do_click(browser, FB_ACCEPT_ALL_COOKIES)
    else:
        pass
    do_send_keys(browser, FB_EMAIL_INPUT, email)
    do_send_keys(browser, FB_PASS_INPUT, read_creds(password, 2))
    try:
        do_click(browser, FB_LOGIN_BTN)
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        if is_visible(browser, COOKIES_ALLOW) is True:
            do_click(browser, COOKIES_ALLOW)
            try:
                do_click(browser, FB_LOGIN_BTN)
            except (NoSuchElementException, TimeoutException):
                pass
        pass
    try:
        do_click(browser, FB_OK_BTN)
    except (NoSuchElementException, TimeoutException):
        pass
    except ElementClickInterceptedException:
        if is_visible(browser, COOKIES_ALLOW) is True:
            do_click(browser, COOKIES_ALLOW)
        else:
            pass


def new_signup_process_google(browser):
    """
    Signs up via Google account
    """
    is_visible(browser, SIGNUP_BTN, 10)
    do_click(browser, SIGNUP_BTN, 10)
    is_visible(browser, CONTINUE_GOOGLE_BTN)
    do_click(browser, CONTINUE_GOOGLE_BTN)
    do_send_keys(browser, GG_EMAIL_INPUT, gmail_email)
    do_click(browser, GG_NEXT_BTN)
    do_send_keys(browser, GG_PASS_INPUT, read_creds(password, 2), 10)
    do_click(browser, GG_NEXT_BTN)
    time.sleep(3)
    try:
        select_video_preferences(browser)
    except (NoSuchElementException, TimeoutException):
        pass
    try:
        switch_to_iframe(browser, APPCUES_FRAME)
        do_click(browser, SKIP_X_BTN_GENERIC, 3)
        browser.switch_to.default_content()
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
        pass
    if is_visible(browser, CLOSE_BUTTON) is True:
        do_click(browser, CLOSE_BUTTON)
    else:
        pass
    assert is_visible(browser, SEARCH_INPUT_MAIN, 20)
