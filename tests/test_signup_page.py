from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException

from pages.home_page_login import *
from pages.new_sign_up_page import *
from pages.new_login_page import *
from pages.my_account_page import *
from pages.onboarding_page import *


@allure.severity(allure.severity_level.NORMAL)
@when('I create a new account')
def create_new_user(browser):
    try:
        home_page_url(browser)
        signup_process_steps(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_new_user)


@when('I create a new account new auth')
def create_new_user_new_auth(browser):
    try:
        home_page_url_new(browser)
        new_signup_process_steps_email(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_new_user_new_auth)


@when('I create a new account new auth shorter')
def create_new_user_new_auth(browser):
    try:
        new_signup_process_steps_email_short(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_new_user_new_auth)


@when('I select video preference')
def video_preference(browser):
    try:
        select_video_preferences(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, video_preference)


@when('I create a new account new auth with Facebook')
def create_new_user_new_auth_fb(browser):
    try:
        home_page_url_new(browser)
        new_signup_process_facebook(browser)
        skip_video_preferences_and_appcues(browser)
        skip_onboarding(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_new_user_new_auth_fb)


@when('I create a new account with Facebook onboarding')
def create_new_user_fb(browser):
    try:
        home_page_url_new(browser)
        new_signup_process_facebook(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_new_user_fb)


@when('I create a new account new auth with Google')
def create_new_user_new_auth_google(browser):
    try:
        home_page_url_new(browser)
        new_signup_process_google(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_new_user_new_auth_google)


@given('I sign up and log in with deleted credentials')
def logged_with_deleted_account(browser):
    try:
        random_email = random_promo_email_generator()
        home_page_url_new(browser)
        signup_process_steps_email(browser, random_email)
        select_video_preferences(browser)
        go_to_my_account(browser)
        delete_account_new(browser)
        click_home_login_button(browser)
        enter_deleted_credentials(browser, random_email)
        click_login_new(browser)
        time.sleep(12)
        new_wrong_login_creds_error(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_with_deleted_account)
