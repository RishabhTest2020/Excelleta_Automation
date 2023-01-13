from locators.locators_file import *
from helpers.common_helpers import *
from test_data.testdata import *
from helpers.generator import *
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import time
from pages.pricing_page import close_pricing_plans


def is_signup_link_exists(browser):
    """
    Checks if signup link exists
    """
    signup_page_title = browser.title
    assert signup_page_title == title_signup_page


def signup_process_steps(browser):
    """
    Simulates the signup process
    Please do not overuse on production
    Generator is used to generate random e-mail @promo.com
    """
    random_email = random_promo_email_generator()
    is_visible(browser, SIGNUP_BTN, 10)
    do_click(browser, SIGNUP_BTN, 10)
    try:
        switch_to_iframe(browser, AUTH_FRAME, 20)
        do_send_keys(browser, FULL_NAME_INPUT, fullname, 10)
    except (NoSuchElementException, TimeoutException):
        browser.refresh()
        is_visible(browser, SIGNUP_BTN, 10)
        do_click(browser, SIGNUP_BTN, 10)
    do_send_keys(browser, EMAIL_INPUT, random_email, 10)
    do_send_keys(browser, PASS_INPUT, random_password, 10)
    do_click(browser, SIGNUP_FRAME_BTN, 10)
    browser.switch_to.default_content()
    # allure_screenshot(browser)


def select_video_preferences(browser):
    """
    Selects industry/business preferences while signing up
    """
    if is_visible(browser, CLOSE_ONBOARDING_POPUP_NEW, 40) is True:
        try:
            skip_offer_modal(browser)
            do_click(browser, CLOSE_ONBOARDING_POPUP_NEW)
        except ElementClickInterceptedException:
            is_visible(browser, PRICING_INTERCOM_IFRAME, 3)
            switch_to_iframe(browser, PRICING_INTERCOM_IFRAME)
            do_click(browser, PRICING_INTERCOM_IFRAME_CLS)
            browser.switch_to.default_content()
            do_click(browser, CLOSE_ONBOARDING_POPUP_NEW)
    else:
        try:
            browser.refresh()
            do_click(browser, CLOSE_ONBOARDING_POPUP_NEW)
        except ElementClickInterceptedException:
            is_visible(browser, PRICING_INTERCOM_IFRAME, 3)
            switch_to_iframe(browser, PRICING_INTERCOM_IFRAME)
            do_click(browser, PRICING_INTERCOM_IFRAME_CLS)
            browser.switch_to.default_content()
            do_click(browser, CLOSE_ONBOARDING_POPUP_NEW)
        skip_offer_modal(browser)
    time.sleep(3)
    browser.refresh()
    time.sleep(3)
    if is_visible(browser, SKIP_OFFER_MODAL_FRAME) is True:
        skip_offer_modal(browser)
        title = browser.title
        print(title)
        assert title == create_page_title
    else:
        pass



