from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException
from pages.brand_manager_page import *


@when('I go to Brand Manager page')
def nav_bm_page(browser):
    try:
        goto_bm_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, nav_bm_page)


@allure.severity(allure.severity_level.NORMAL)
@when('I add Brand Name')
def insert_brand_name(browser):
    try:
        add_brand_name(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, insert_brand_name)


@allure.severity(allure.severity_level.NORMAL)
@when('I add first Brand Name')
def add_brand_name_1st_brand(browser):
    try:
        add_brand_name_first_brand(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_brand_name_1st_brand)


@then('No brand is added')
def no_brand_added(browser):
    try:
        no_brand_is_visible(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, no_brand_added)


@allure.severity(allure.severity_level.NORMAL)
@when('I choose brand logo and watermark')
def brand_logo_and_watermark(browser):
    try:
        select_brand_logo_watermark(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, brand_logo_and_watermark)


@allure.severity(allure.severity_level.NORMAL)
@when('I add Brand components')
def add_brand_components(browser):
    try:
        add_brand_comps(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_brand_components)


@allure.severity(allure.severity_level.NORMAL)
@then('I delete the brand')
def del_brand(browser):
    try:
        delete_brand(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, del_brand)


@allure.severity(allure.severity_level.NORMAL)
@then('I initially delete brands')
def init_del_brand(browser):
    try:
        init_delete_brand(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, init_del_brand)


@when('I create a new project')
def create_a_project(browser):
    try:
        create_new_project(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_a_project)