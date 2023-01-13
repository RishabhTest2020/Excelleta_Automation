from pytest_bdd import when, then, given, parsers
from selenium.common.exceptions import WebDriverException
from pages.social_calendar import *
from pages.home_page_login import *
from pages.new_login_page import *
from pages.new_sign_up_page import *
import allure

TYPES = {'d': str}


@given('User is logged in with shorter new auth calendar')
def logged_in_new_shorter_cal(browser):
    try:
        go_to_url(browser, login_url)
        try:
            enter_email_new(browser, email_calendar)
        except (NoSuchElementException, TimeoutException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email_calendar)
        enter_password_new(browser, read_creds(password, 0))
        click_login_new(browser)
        time.sleep(12)
        try:
            check_correct_username_cal(browser)
        except (AssertionError, TimeoutException, NoSuchElementException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email_calendar)
            enter_password_new(browser, read_creds(password, 0))
            click_login_new(browser)
            time.sleep(12)
            check_correct_username_cal(browser)
        time.sleep(1)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in_new_shorter_cal)


@when('I navigate to Social Calendar Page')
def go_to_calendar_page(browser):
    try:
        navigate_to_social_calendar_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_to_calendar_page)


@then(parsers.parse('I render a video from calendar day "{locator:d}"', extra_types=TYPES))
@then('I render a video from calendar day "<locator>"')
def select_and_render_template(browser, locator):
    try:
        choose_day_template(browser, locator)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, select_and_render_template)
