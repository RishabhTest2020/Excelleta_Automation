from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException

from pages.pricing_page import *
from pages.home_page_login import *
from test_data.testdata import *
from pages.newcancellation_page import *
from helpers.common_helpers import *


@when('I go to pricing page')
def navigate_pricing_page(browser):
    try:
        goto_pricing_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, navigate_pricing_page)


@when('I open pricing page')
def open_pricing_page(browser):
    try:
        pricing_page_url(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, open_pricing_page)


@allure.severity(allure.severity_level.NORMAL)
@when('I choose standard plan and purchase and goto Create page')
def buy_plan(browser):
    try:
        purchase_standard_plan(browser)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, buy_plan)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose standard plan and verify pop up and goto Create page')
def buy_plan_new(browser):
    try:
        purchase_standard_plan_new(browser)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, buy_plan_new)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose standard plan using 2FA auth and goto Create page')
def buy_plan_new(browser):
    try:
        twofa_purchase_standard_plan(browser)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, buy_plan_new)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose business plan using 2FA auth and goto Create page')
def buy_business_plan_new(browser):
    if is_visible(browser, business_plan) is True:
        try:
            twofa_new_business_plan(browser, business_plan)
            go_to_create_page(browser)
            create_page_redirection(browser)
        except (Exception, WebDriverException):
            bs_fail_with_traceback(browser, buy_plan_new_user)
    else:
        if is_visible(browser, TOGGLE_ON, 10) is True:
            do_click(browser, TOGGLE_BTN, 10)
        else:
            pass
        currencies_check(browser)
        do_click(browser, STANDARD_PLAN_CTA, 45)
        if is_visible(browser, PAYMENT_CARD_IFRAME) is True:
            try:
                twofa_purchase_standard_plan_old(browser)
                go_to_create_page(browser)
                create_page_redirection(browser)
            except (Exception, WebDriverException):
                bs_fail_with_traceback(browser, buy_plan_new_user)
        else:
            try:
                twofa_purchase_standard_plan(browser)
                go_to_create_page(browser)
                create_page_redirection(browser)
            except (Exception, WebDriverException):
                bs_fail_with_traceback(browser, buy_plan_new_user)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose standard plan and verify pop up')
def buy_plan_new_user(browser):
    try:
        purchase_standard_plan_new_prod(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, buy_plan_new_user)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose business monthly plan and verify pop up')
def buy_plan_new_user(browser):
    try:
        register_user_purchases_new_pricing_monthly_prod(browser, business_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, buy_plan_new_user)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose business plan and goto Create page')
def buy_c_plan_new(browser):
    if is_visible(browser, business_plan) is True:
        try:
            register_user_purchases_new_pricing_monthly(browser, business_plan)
            go_to_create_page(browser)
            create_page_redirection(browser)
        except (Exception, WebDriverException):
            bs_fail_with_traceback(browser, buy_plan_new)
    else:
        if is_visible(browser, TOGGLE_ON, 10) is True:
            do_click(browser, TOGGLE_BTN, 10)
        else:
            pass
        currencies_check(browser)
        do_click(browser, STANDARD_PLAN_CTA, 45)
        if is_visible(browser, PAYMENT_CARD_IFRAME) is True:
            try:
                purchase_standard_plan(browser)
                go_to_create_page(browser)
                create_page_redirection(browser)
            except (Exception, WebDriverException):
                bs_fail_with_traceback(browser, buy_plan_new)
        else:
            try:
                purchase_standard_plan_new(browser)
                go_to_create_page(browser)
                create_page_redirection(browser)
            except (Exception, WebDriverException):
                bs_fail_with_traceback(browser, buy_plan_new)


@allure.severity(allure.severity_level.NORMAL)
@then('I choose starter plan and goto Create page')
def buy_plan_new(browser):
    try:
        register_user_purchases_new_pricing_monthly(browser, starter_plan)
        go_to_create_page(browser)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, buy_plan_new)


@then('I close pricing page')
def close_pricing_page(browser):
    try:
        close_pricing_plans(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, close_pricing_page)
