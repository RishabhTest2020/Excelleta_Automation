import time

from pytest_bdd import given, when, then, parsers
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from pages.home_page_login import *
from pages.main_page import *
from pages.my_account_page import *
from pages.new_login_page import *
from pages.new_sign_up_page import *
from pages.mob_home_page_login import *
import allure

user = {}


@given('I have an email')
def my_email():
    user['email'] = email


@given('I have a password')
def my_password():
    user['password'] = password


@given('I have a wrong password')
def incorrect_password():
    user['wrong_pass'] = wrong_password


@when('I go to Promo site')
def open_promo_site(browser):
    try:
        home_page_url(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, open_promo_site)


@given('I open Promo Pages')
def open_promo_pages(browser):
    try:
        promo_pages_urls(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, open_promo_site)


@when('I go to Promo site new')
def open_promo_site_new_auth(browser):
    try:
        home_page_url_new(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, open_promo_site_new_auth)


@when('I open Promo URL and check UTM')
def url_utm(browser):
    try:
        check_url_utm(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, url_utm)


@when('I click on agree and continue')
def click_accept_cookie(browser):
    try:
        accept_cookies(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_accept_cookie)


@when('I skip cookies')
def do_skip_cookies(browser):
    try:
        skip_cookies(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, do_skip_cookies)


@allure.severity(allure.severity_level.NORMAL)
@when('I click on login button')
def click_home_login(browser):
    try:
        click_home_login_button(browser)
        time.sleep(2)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_home_login)


@allure.severity(allure.severity_level.NORMAL)
@when('I enter my email')
def enter_correct_email(browser):
    try:
        enter_email(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, enter_correct_email)


@allure.severity(allure.severity_level.NORMAL)
@when('I enter my email new')
def enter_correct_email_new(browser):
    try:
        enter_email_new(browser, email)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, enter_correct_email_new)


@allure.severity(allure.severity_level.NORMAL)
@when('I enter my password')
def enter_passw(browser):
    try:
        enter_password(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, enter_passw)


@when('I enter my password new')
def enter_passw_new(browser):
    try:
        enter_password_new(browser, read_creds(password, 0))
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, enter_passw_new)


@allure.severity(allure.severity_level.NORMAL)
@when('I enter a wrong password')
def enter_wrong_passw(browser):
    try:
        enter_wrong_password(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, enter_wrong_passw)


@when('I enter a wrong password new')
def enter_wrong_passw_new(browser):
    try:
        enter_wrong_password_new(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, enter_wrong_passw_new)


@allure.severity(allure.severity_level.NORMAL)
@when('I press the login button')
def login(browser):
    try:
        click_login(browser)
        time.sleep(10)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, login)


@when('I press the login button new')
def login_new(browser):
    try:
        click_login_new(browser)
        time.sleep(10)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, login_new)


@then('I check logged username')
def check_username(browser):
    try:
        try:
            check_correct_username(browser)
        except (AssertionError, NoSuchElementException):
            home_page_url_new(browser)
            click_home_login_button(browser)
            enter_email_new(browser, email)
            enter_password_new(browser, read_creds(password, 0))
            click_login_new(browser)
            time.sleep(12)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_username)


@allure.severity(allure.severity_level.CRITICAL)
@then('I should navigated to "Create Page"')
def assert_create_page(browser):
    try:
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, assert_create_page)


@allure.severity(allure.severity_level.CRITICAL)
@then('I should get error "This field can’t be empty"')
def field_empty_error(browser):
    try:
        new_empty_textbox_error(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, field_empty_error)


@then('I should get error "Your email or password is incorrect"')
def wrong_id_pass_error(browser):
    try:
        new_wrong_login_creds_error(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, wrong_id_pass_error)


@given('User is logged in')
def logged_in(browser):
    try:
        home_page_url(browser)
        click_home_login_button(browser)
        enter_email(browser)
        enter_password(browser)
        click_login(browser)
        time.sleep(12)
        check_correct_username(browser)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in)


@given('User is logged in with new auth')
def logged_in_new(browser):
    try:
        home_page_url_new(browser)
        click_home_login_button(browser)
        time.sleep(2)
        try:
            enter_email_new(browser, email)
        except (NoSuchElementException, TimeoutException):
            home_page_url_new(browser)
            time.sleep(2)
            click_home_login_button(browser)
            enter_email_new(browser, email)
        enter_password_new(browser, read_creds(password, 0))
        click_login_new(browser)
        time.sleep(12)
        try:
            check_correct_username(browser)
        except (AssertionError, TimeoutException, NoSuchElementException):
            home_page_url_new(browser)
            click_home_login_button(browser)
            time.sleep(2)
            enter_email_new(browser, email)
            enter_password_new(browser, read_creds(password, 0))
            click_login_new(browser)
            time.sleep(12)
            check_correct_username(browser)
        time.sleep(1)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in_new)


@when('I am logged in with a mobile user')
def login_mob_user(browser):
    try:
        go_to_url(browser, login_url)
        enter_email_new(browser, email_mobile)
        enter_password_new(browser, random_password)
        click_login_new(browser)
        time.sleep(8)
        verify_if_mobile_user_exists(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, login_mob_user)


@given('User is logged in with shorter new auth')
def logged_in_new_shorter(browser):
    try:
        go_to_url(browser, login_url)
        try:
            enter_email_new(browser, email)
        except (NoSuchElementException, TimeoutException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email)
        enter_password_new(browser, read_creds(password, 0))
        click_login_new(browser)
        time.sleep(12)
        try:
            check_correct_username(browser)
        except (AssertionError, TimeoutException, NoSuchElementException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email)
            enter_password_new(browser, read_creds(password, 0))
            click_login_new(browser)
            time.sleep(12)
            check_correct_username(browser)
        time.sleep(1)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in_new_shorter)


TYPES = {'d': str}


@given(parsers.parse('User is logged in "{env:d}" with shorter new auth', extra_types=TYPES))
@given('User is logged in "<env>" with shorter new auth')
def logged_in_new_shorter(browser, env):
    try:
        if env == 'prod':
            go_to_url(browser, f'https://promo.com/login')
        elif env == 'staging':
            go_to_url(browser, f'https://staging-php7.slide.ly/login')
        else:
            go_to_url(browser, f'https://{env}.promo.com/login')
        try:
            enter_email_new(browser, email)
        except (NoSuchElementException, TimeoutException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email)
        enter_password_new(browser, read_creds(password, 0))
        click_login_new(browser)
        time.sleep(12)
        try:
            check_correct_username(browser)
        except (AssertionError, TimeoutException, NoSuchElementException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email)
            enter_password_new(browser, read_creds(password, 0))
            click_login_new(browser)
            time.sleep(12)
            check_correct_username(browser)
        time.sleep(1)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in_new_shorter)


@given('User is logged in with new auth - change pass separate account')
def logged_in_new_pass_change(browser):
    try:
        home_page_url_new(browser)
        click_home_login_button(browser)
        time.sleep(2)
        try:
            enter_email_new(browser, email_pass_change)
        except NoSuchElementException:
            home_page_url_new(browser)
            click_home_login_button(browser)
            time.sleep(2)
            enter_email_new(browser, email_pass_change)
        time.sleep(1)
        enter_password_new(browser, read_creds(password, 1))
        click_login_new(browser)
        if is_visible(browser, NEW_WRONG_CREDS_ERROR) is True:
            browser.refresh()
            time.sleep(2)
            enter_email_new(browser, email_pass_change)
            enter_password_new(browser, random_password)
            click_login_new(browser)
            time.sleep(12)
            create_page_redirection(browser)
            go_to_my_account(browser)
            change_password_to_correct(browser)
            verify_change_success_message(browser)
            do_click(browser, NEW_PROJECT_BTN)
            time.sleep(6)
        else:
            time.sleep(12)
            try:
                create_page_redirection(browser)
            except WebDriverException:
                home_page_url_new(browser)
                click_home_login_button(browser)
                time.sleep(2)
                enter_email_new(browser, email_pass_change)
                time.sleep(1)
                enter_password_new(browser, read_creds(password, 1))
                click_login_new(browser)
                time.sleep(12)
                create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in_new_pass_change)


@then('I sign out')
def sign_out(browser):
    try:
        sign_out_process(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, sign_out)


@then('I login with changed password')
def logged_with_changed_password(browser):
    try:
        click_home_login_button(browser)
        time.sleep(2)
        enter_email_new(browser, email_pass_change)
        enter_password_changed(browser)
        click_login_new(browser)
        time.sleep(12)
        # check_correct_username(browser)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_with_changed_password)


@then('I login with old password')
def logged_with_old_password(browser):
    try:
        click_home_login_button(browser)
        time.sleep(2)
        enter_email_new(browser, email_pass_change)
        enter_password_changed(browser)
        click_login_new(browser)
        time.sleep(12)
        new_wrong_login_creds_error(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_with_old_password)

