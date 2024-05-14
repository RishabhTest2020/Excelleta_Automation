from global_libs.global_imports import *

@given('User is logged in with new auth')
def logged_in_new(browser):
    home_page_url_new(browser)