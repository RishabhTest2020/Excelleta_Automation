from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException
from pages.templates_page import *
from pages.new_sign_up_page import *
from pages.editor_page import *
from pages.new_login_page import *


@when('I open Templates page')
def open_templates_page(browser):
    try:
        template_page_url(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, open_templates_page)


@then('I go to Templates page')
def go_to_templates_page(browser):
    try:
        navigate_templates_page(browser)
        skip_cookies_next(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_to_templates_page)


@then('I search templates with valid and invalid keys')
def search_templates(browser):
    try:
        search_temps_with_invalid_input(browser)
        time.sleep(1)
        search_valid_temps(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, search_templates)


@then('I browse templates category and verify breadcrumbs')
def browse_templates_category(browser):
    try:
        verify_categories_and_breadcrumbs(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, browse_templates_category)


@then('I customize video and verify redirection to signup page')
def customize_and_redirected_to_sign_up(browser):
    try:
        customize_template(browser)
        get_signup_title(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, customize_and_redirected_to_sign_up)


@then('I customize template')
def customize_a_template(browser):
    try:
        customize_template(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, customize_a_template)


@then('I preview template and verify share buttons')
def preview_template_verify_share(browser):
    try:
        preview_template_and_share(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, preview_template_verify_share)


@then('I change ratios and verify')
def change_ratios_verify(browser):
    try:
        change_ratios(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_ratios_verify)


@then('I verify Always Wide category')
def verify_predefined_ratios(browser):
    try:
        predefined_ratios(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_predefined_ratios)