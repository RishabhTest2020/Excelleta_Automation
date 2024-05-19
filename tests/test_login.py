from global_libs.global_imports import *


@given('Login into Excelleta UI')
def logged_in(browser):
    user_login(browser)
