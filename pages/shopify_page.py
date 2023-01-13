from locators.locators_file import *
from locators.facebook_locators import *
from helpers.common_helpers import *
from pages.ptv_page import *
from pages.modheader_page import *
from test_data.testdata import *
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time


def login_to_shopify(browser):
    """
    Login to Shopify - QA-poland shop
    """
    browser.get(shopify_admin_url)
    close_additional_tab(browser, 1, 0)
    do_send_keys(browser, SHOPIFY_EMAIL_INPUT, email)
    do_click(browser, SHOPIFY_CONTINUE_WITH_EMAIL, 15)
    do_send_keys(browser, SHOPIFY_PASS_INPUT, read_creds(password, 0), 10)
    do_click(browser, SHOPIFY_CONTINUE_WITH_EMAIL, 15)
    time.sleep(2)
    assert is_visible(browser, SHOPIFY_LOGO_IN_SHOP, 20) is True


def login_fb_to_shopify(browser):
    """
    Login to Shopify - QA-poland shop
    """
    browser.get(shopify_admin_url)
    close_additional_tab(browser, 1, 0)
    do_click(browser, SHOPIFY_CONTINUE_WITH_FB, 15)
    if is_visible(browser, FB_ACCEPT_COOKIES) is True:
        do_click(browser, FB_ACCEPT_COOKIES)
    else:
        pass
    if is_visible(browser, FB_ACCEPT_ALL_COOKIES) is True:
        do_click(browser, FB_ACCEPT_ALL_COOKIES)
    else:
        pass
    do_send_keys(browser, FB_EMAIL_INPUT, email)
    do_send_keys(browser, FB_PASS_INPUT, read_creds(password, 2))
    if is_visible(browser, FB_LOGIN_BTN) is True:
        do_click(browser, FB_LOGIN_BTN)
    else:
        pass
    time.sleep(2)
    assert is_visible(browser, SHOPIFY_LOGO_IN_SHOP, 20) is True


def choose_env_shopify(browser, env):
    """
    Chooses an environment - clicks on the relevant app
    env: locator which redirects to a chosen app on a chosen env
    """
    do_click(browser, SHOPIFY_ADMIN_APPS, 30)
    do_click(browser, env, 30)


def redirect_shopify(browser):
    """
    Checks if a user is redirected to Shopify app
    """
    is_visible(browser, SHOPIFY_MYVIDEO_HEADER)


def shopify_click_new_video_btn(browser):
    """
    Clicks on Create video btn and is redirected to Shopify wizard
    Verify a title
    """
    is_visible(browser, SHOPIFY_CREATE_NEW_BTN)
    do_click(browser, SHOPIFY_CREATE_NEW_BTN)
    time.sleep(2)
    is_visible(browser, SHOPIFY_WIZARD_MAIN_TITLE)
    title_shop = get_element_text(browser, SHOPIFY_WIZARD_MAIN_TITLE)
    assert title_shop == 'Choose a video for your product'


def choose_a_shopify_template(browser, no=2):
    """
    Verifies if there is some templates displayed (more than 2)
    Chooses template and clicks Next
    no (int): which of image to choose (1, 2, 3...), default is 2nd
    """
    SHOPIFY_TEMPLATE = (By.XPATH, f'(//LI[@class="list-item video-grid-item"])[{no}]')
    all_templates_no = browser.find_elements(PTV_SHOPIFY_TEMPLATES[0], PTV_SHOPIFY_TEMPLATES[1])
    assert len(all_templates_no) > 2
    do_click(browser, SHOPIFY_TEMPLATE, 10)
    assert is_visible(browser, PTV_CHECKMARK_ICON_SELECTED) is True
    do_click(browser, PTV_NEXT_BTN)
    assert is_visible(browser, SHOPIFY_WIZARD_SEARCH_PRODUCT) is True


def shopify_verify_socials(browser):
    """
    Verifies number of social options
    Expected: 5 options - Shopify, FB, Instagram, YT, Twitter
    """
    all_social_options_no = browser.find_elements(PTV_SHOPIFY_SOCIALS[0], PTV_SHOPIFY_SOCIALS[1])
    assert len(all_social_options_no) == 5
    shopify_user = get_element_text(browser, SHOPIFY_USERNAME)
    assert shopify_user == shopify_fb_username


def create_a_draft_as_new_user(browser):
    """
    Only for new users - it executes the flow from a Welcome screen
    """
    if is_visible(browser, SHOPIFY_MAKE_A_VIDEO) is True:
        do_click(browser, SHOPIFY_MAKE_A_VIDEO)
        time.sleep(3)
        choose_a_shopify_template(browser, 2)
        choose_a_ptv_image(browser)
        do_click(browser, SHOPIFY_SAVE_BTN)
        is_visible(browser, SHOPIFY_SAVE_BTN_SAVED_STATE, 15)
        do_click(browser, SHOPIFY_MYVIDEO_HEADER)
    else:
        pass


def cleans_all_shopify_drafts(browser, no):
    """
    Closes an additional tab
    Cleans drafts if any
    """
    close_additional_tab(browser, 1, 0)
    PTV_DASHBOARD_PROJECT = (By.XPATH, f'(//div[@class="dashboard-grid-item"])[{no}]')
    PTV_3_DOTS = (By.XPATH, f'(//div[@class="menu-button__icon"])[{no}]')
    create_a_draft_as_new_user(browser)
    if is_visible(browser, SHOPIFY_NO_VIDEOS_TITLE) is False:
        while True:
            do_hover(browser, PTV_DASHBOARD_PROJECT)
            do_hover(browser, PTV_3_DOTS)
            do_click(browser, PTV_3_DOTS)
            do_click(browser, PTV_DASHBOARD_DELETE_PROJECT)
            do_click(browser, PTV_POPUP_DELETE_PROJECT_BTN)
            if is_visible(browser, SHOPIFY_NO_VIDEOS_TITLE) is True:
                break
    else:
        pass
