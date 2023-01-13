from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException
from pages.new_login_page import *
from pages.new_sign_up_page import *
from pages.onboarding_page import  *
from pages.templates_page import *
from pages.my_account_page import *


@then('I reach to onboarding first screen')
def reach_onboarding_first_screen(browser):
    try:
        onboarding_first_screen_validation(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, reach_onboarding_first_screen)


@then('I click to skip onboarding flow')
def skip_onboarding_flow(browser):
    try:
        click_skip(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, skip_onboarding_flow)


@then('I click continue')
def click_continue(browser):
    try:
        click_continue_btn(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_continue)


@then('I reach to onboarding second screen')
def reach_onboarding_second_screen(browser):
    try:
        onboarding_second_screen_validation(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, reach_onboarding_second_screen)


@then('I click on no website option')
def click_on_no_website_option(browser):
    try:
        click_no_website(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_on_no_website_option)


@then('I fill out a website')
def fill_out_website_field(browser):
    try:
        continue_btn_disabled_validation(browser)
        fill_website_field(browser, 'https://brandfetch.com/')
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, fill_out_website_field)


@then('I can not click on continue')
def can_not_click_on_continue(browser):
    try:
        continue_btn_disabled_validation(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, can_not_click_on_continue)


@then('Business field is empty')
def business_field_is_empty(browser):
    try:
        business_field_empty_content_validation(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, business_field_is_empty)


@then('I select business type')
def select_business_type(browser):
    try:
        select_business(browser, 'Food')
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, select_business_type)


@then('I set country and phone number')
def set_phone_number(browser):
    try:
        set_country(browser)
        set_phone(browser, '1234567901')
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, set_phone_number)


@then('I add logo to onboarding')
def add_logo_onboarding(browser):
    try:
        add_logo_on_onboarding(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_logo_onboarding)


@then('I click to replace logo')
def click_to_replace_logo(browser):
    try:
        replace_logo_on_onboarding(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_to_replace_logo)


@then('I delete logo')
def delete_logo(browser):
    try:
        delete_logo_on_onboarding(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, delete_logo)


@then('I mark checkbox')
def mark_checkbox(browser):
    try:
        mark_checkbox_v(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, mark_checkbox)


@then('I click on start creating')
def click_start_creating(browser):
    try:
        click_start_creating_btn(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, click_start_creating)


@when('I customize template from on templates page')
def customize_template_from_templates_page(browser):
    try:
        template_page_url(browser)
        customize_template(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, customize_template_from_templates_page)


@then('I customize a template')
def non_logged_user_selects_to_customize_template(browser):
    try:
        customize_template(browser)
        get_signup_title(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, non_logged_user_selects_to_customize_template)
