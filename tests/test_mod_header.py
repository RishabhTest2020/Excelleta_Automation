from pages.modheader_page import *
from pytest_bdd import given, then


@given('I update headers through ModHeader')
def place_header_in_modheader(browser):
    enable_modheader_incognito(browser)
    goto_modheader_html(browser)
    enter_headers_in_modheader(browser)


@then('I close ModHeader tab')
def close_modheader(browser):
    close_modheader_tab(browser)
