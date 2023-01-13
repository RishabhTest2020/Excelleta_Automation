from helpers.common_helpers import *
from locators.locators_file import *


def accept_cookies(browser):
    """
    Accepts cookies on the main page
    Currently not in use due to USA location on BrowserStack
    """
    is_clickable(browser, AGREE_COOKIES_NEW_AUTH)
    do_click(browser, AGREE_COOKIES_NEW_AUTH)
    browser.refresh()
    assert is_invisible(browser, AGREE_COOKIES_NEW_AUTH, 3) is True


def button_try_for_free(browser):
    """
    Checks if 'Try for Free' button leads to the SignUp page
    """
    is_clickable(browser, TRY_FREE)
    do_click(browser, TRY_FREE)
    switch_to_iframe(browser, AUTH_FRAME, 15)
    assert is_visible(browser, SIGNUP_FRAME_BTN)


def click_on_logo(browser, page_title):
    """
    Clicks on logo
    Args:
        browser: webdriver
        page_title: actual title of a website
        main_page_title for not logged
        create_page_title for logged user
    """
    is_visible(browser, MAIN_LOGO, 15)
    do_click(browser, MAIN_LOGO, 15)
    time.sleep(5)
    get_title = browser.title
    assert get_title == page_title


# to_delete: Rishabh do we still need these functions?
# def correct_menu_item(browser):
#     """
#     Checks every main menu item by its link's text
#     """
#     for menu_item, menu_locator in MAIN_MENU.items():
#         assert get_element_text(browser, menu_locator) == menu_item

# def correct_footer_items(browser):
#     """
#     Checks every main footer item by its link's text
#     """
#     for footer_item, footer_locator in FOOTER_MENU.items():
#         assert get_element_text(browser, footer_locator) == footer_item
