from global_libs.global_imports import *


@given('Login into Excelleta UI')
def logged_in(browser):
    user_login(browser)


@given(parsers.parse('Login with invalid creds {email} {password} into Excelleta UI'))
def logged_in(browser, email, password):
    user_login(browser, email=email, password=password, type='fail')


@when(parsers.parse('Navigate to {tab_name} tab'))
def navigate_to_tab(browser, tab_name):
    goto_tab(browser, tab_name)