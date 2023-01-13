from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException
from pages.links_page import *
from pages.main_page import *


@allure.severity(allure.severity_level.NORMAL)
@then('I check main menu links')
def check_menu_links(browser):
    try:
        open_and_test_menu_items(browser)
        open_and_test_menu_new_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_menu_links)


@allure.severity(allure.severity_level.NORMAL)
@then('I check footer links')
def check_footer_links(browser):
    try:
        open_and_test_footer_items(browser)
        open_and_test_footer_products_and_menu_tabs(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_footer_links)


@then('I check tools links')
def check_tools_links(browser):
    try:
        open_and_test_footer_tools(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_logos_links)


@then('I check templates footer links')
def check_templates_footer_links(browser):
    try:
        open_templates_and_test_footer_links(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_templates_footer_links)


@then('I check templates header links')
def check_templates_header_links(browser):
    try:
        open_templates_and_test_header_links(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_templates_header_links)



@then('I check logos links')
def check_logos_links(browser):
    try:
        check_partner_logos_links(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_logos_links)


@then('I click on main logo as logged in')
def click_on_logo_and_go_to_main_page_logged(browser):
    try:
        click_on_logo(browser, create_page_title)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_on_logo_and_go_to_main_page_logged)


@then('I click on main logo as not logged in')
def click_on_logo_and_go_to_main_page_not_logged(browser):
    try:
        click_on_logo(browser, main_page_title)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_on_logo_and_go_to_main_page_not_logged)
