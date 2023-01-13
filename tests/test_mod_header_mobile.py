from pages.modheader_mobile_page import *
from pytest_bdd import given


@given('I update headers through ModHeader mob')
def place_header_in_modheader_mob(mob_browser):
    enable_modheader_incognito_mob(mob_browser)
    goto_modheader_html_mob(mob_browser)
    enter_headers_in_modheader_mob(mob_browser)