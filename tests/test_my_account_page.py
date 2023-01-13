import pytest
from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import WebDriverException
from tests.test_login import *
from pages.my_account_page import *


@then('I go to my account')
def goes_to_my_account(browser):
    try:
        go_to_my_account(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, goes_to_my_account)


@then('I delete my account new')
def delete_my_account(browser):
    try:
        delete_account_new(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, delete_my_account)


@then('I disconnect Facebook')
def disconnect_facebook(browser):
    try:
        disconnect_from_facebook(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, disconnect_facebook)


@then('I disconnect Google')
def disconnect_google(browser):
    try:
        disconnect_from_google(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, disconnect_google)


@then('I change my password')
def change_a_password(browser):
    try:
        change_password(browser)
        verify_change_success_message(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_a_password)


@then('I rechange my password')
def rechange_a_password(browser):
    try:
        rechange_password(browser)
        verify_change_success_message(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, rechange_a_password)


@then('I change my password incorrectly')
def change_a_password_incorrect(browser):
    try:
        change_password_incorrectly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_a_password_incorrect)