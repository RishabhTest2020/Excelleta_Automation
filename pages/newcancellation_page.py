import time

import selenium.common.exceptions

from locators.locators_file import *
from helpers.common_helpers import *
from pages.editor_page import *
from pages.home_page_login import go_to_url, create_page_redirection
from test_data.testdata import *
from helpers.generator import *
from selenium.common.exceptions import TimeoutException
from pages.sign_up_page import *
from pages.new_login_page import *
from helpers.googlesheet import *
from pages.stripe_clock_simulation import *
import re
import math


def currencies_check(browser):
    """
    Checks different currencies
    """
    try:
        currency_ip = os.environ.get("CURRENCY_IP")
        if is_visible(browser, EMBED_PRICING_IFRAME) is True:
            switch_to_iframe(browser, EMBED_PRICING_IFRAME)
            if currency_ip == EU:
                assert len(browser.find_elements(By.XPATH, EU_DOLLAR_CURRENCY[1])) > 0
            elif currency_ip == DE:
                assert len(browser.find_elements(By.XPATH, EU_DOLLAR_CURRENCY[1])) > 0
            elif currency_ip == UK:
                assert len(browser.find_elements(By.XPATH, EU_DOLLAR_CURRENCY[1])) > 0
            elif currency_ip == PL:
                assert len(browser.find_elements(By.XPATH, EU_DOLLAR_CURRENCY[1])) > 0
            elif currency_ip == Singapur:
                assert len(browser.find_elements(By.XPATH, DOLLAR_CURRENCY[1])) > 0
            elif currency_ip == Canada:
                assert len(browser.find_elements(By.XPATH, CA_DOLLAR_CURRENCY[1])) > 0
            elif currency_ip == Australia:
                assert len(browser.find_elements(By.XPATH, AU_DOLLAR_CURRENCY[1])) > 0
            else:
                assert len(browser.find_elements(By.XPATH, DOLLAR_CURRENCY[1])) > 0
            browser.switch_to.default_content()
        else:
            if is_visible(browser, CURRENCY_ELEMENT_AN) is True:
                currency_elem = browser.find_element_by_xpath(CURRENCY_ELEMENT_AN[1])
            else:
                currency_elem = browser.find_element_by_xpath(CURRENCY_ELEMENT[1])
            if currency_ip == EU:
                eu_currency = "eu" in currency_elem.get_attribute("class")
                assert eu_currency is True
            elif currency_ip == DE:
                de_currency = "eu" in currency_elem.get_attribute("class")
                assert de_currency is True
            elif currency_ip == UK:
                uk_currency = "eu" in currency_elem.get_attribute("class")
                assert uk_currency is True
            elif currency_ip == PL:
                pl_currency = "eu" in currency_elem.get_attribute("class")
                assert pl_currency is True
            elif currency_ip == Singapur:
                singapur_currency = "undefined" in currency_elem.get_attribute("class")
                assert singapur_currency is True
            elif currency_ip == Canada:
                canada_currency = "ca" in currency_elem.get_attribute("class")
                assert canada_currency is True
            elif currency_ip == Australia:
                australia_currency = "au" in currency_elem.get_attribute("class")
                assert australia_currency is True
            else:
                try:
                    us_currency = "undefined" in currency_elem.get_attribute("class")
                    assert us_currency is True
                except AssertionError:
                    in_currency = "in" in currency_elem.get_attribute("class")
                    assert in_currency is True
    except (NameError, KeyError):
        pass


def usd_pricing(current_plan):
    """
    Checks plans and USD
    """
    if current_plan == 'Lite Plan':
        current_price = b_plan_pricing.cell(4, 3).value[1:]
        return current_price
    elif current_plan == 'B1' or current_plan == 'B1_half_price':
        current_price = b_plan_pricing.cell(5, 3).value[1:]
        return current_price
    elif current_plan == 'B2':
        current_price = b_plan_pricing.cell(6, 3).value[1:]
        return current_price
    elif current_plan == 'B3':
        current_price = b_plan_pricing.cell(8, 3).value[1:]
        return current_price
    elif current_plan == 'bi_annual':
        current_price = b_plan_pricing.cell(9, 3).value[1:]
        return current_price
    elif current_plan == 'B1_Annual' or current_plan == 'B1_Annual_Half_Price':
        current_price = b_plan_pricing.cell(5, 13).value[1:]
        return current_price
    elif current_plan == 'B2_Annual':
        current_price = b_plan_pricing.cell(6, 13).value[1:]
        return current_price
    elif current_plan == 'B3_Annual':
        current_price = b_plan_pricing.cell(8, 13).value[1:]
        return current_price


def eu_pricing(current_plan):
    """
    Checks plans and Euro
    """
    if current_plan == 'B1' or current_plan == 'B1_half_price':
        current_price = b_plan_pricing.cell(16, 3).value[1:]
        return current_price
    elif current_plan == 'B2':
        current_price = b_plan_pricing.cell(17, 3).value[1:]
        return current_price
    elif current_plan == 'B3':
        current_price = b_plan_pricing.cell(19, 3).value[1:]
        return current_price
    elif current_plan == 'bi_annual':
        current_price = b_plan_pricing.cell(20, 13).value[1:]
        return current_price
    elif current_plan == 'B1_Annual':
        current_price = b_plan_pricing.cell(16, 13).value[1:]
        return current_price
    elif current_plan == 'B2_Annual':
        current_price = b_plan_pricing.cell(17, 13).value[1:]
        return current_price
    elif current_plan == 'B3_Annual':
        current_price = b_plan_pricing.cell(19, 13).value[1:]
        return current_price


def au_pricing(current_plan):
    """
    Checks plans and Australian dollar
    """
    if current_plan == 'B1':
        current_price = b_plan_pricing.cell(37, 3).value[1:]
        return current_price
    elif current_plan == 'B2':
        current_price = b_plan_pricing.cell(38, 3).value[1:]
        return current_price
    elif current_plan == 'B3':
        current_price = b_plan_pricing.cell(40, 3).value[1:]
        return current_price
    elif current_plan == 'bi_annual':
        current_price = b_plan_pricing.cell(41, 13).value[1:]
        return current_price
    elif current_plan == 'B1_Annual':
        current_price = b_plan_pricing.cell(37, 13).value[1:]
        return current_price
    elif current_plan == 'B2_Annual':
        current_price = b_plan_pricing.cell(38, 13).value[1:]
        return current_price
    elif current_plan == 'B3_Annual':
        current_price = b_plan_pricing.cell(40, 13).value[1:]
        return current_price


def ca_pricing(current_plan):
    """
    Checks plans and Canadian dollar
    """
    if current_plan == 'B1':
        current_price = b_plan_pricing.cell(47, 3).value[1:]
        return current_price
    elif current_plan == 'B2':
        current_price = b_plan_pricing.cell(48, 3).value[1:]
        return current_price
    elif current_plan == 'B3':
        current_price = b_plan_pricing.cell(50, 3).value[1:]
        return current_price
    elif current_plan == 'bi_annual':
        current_price = b_plan_pricing.cell(51, 13).value[1:]
        return current_price
    elif current_plan == 'B1_Annual':
        current_price = b_plan_pricing.cell(47, 13).value[1:]
        return current_price
    elif current_plan == 'B2_Annual':
        current_price = b_plan_pricing.cell(48, 13).value[1:]
        return current_price
    elif current_plan == 'B3_Annual':
        current_price = b_plan_pricing.cell(50, 13).value[1:]
        return current_price


def price_check(current_plan):
    """
    Function that combines currencies with the locations
    """
    ip = os.environ.get("CURRENCY_IP")
    if ip == '5.135.110.142':
        return eu_pricing(current_plan)
    elif ip == '139.99.236.163':
        return au_pricing(current_plan)
    elif ip == '192.99.54.60':
        return ca_pricing(current_plan)
    else:
        return usd_pricing(current_plan)


def currency_symbol_check():
    """
    Checks if there is a correct currency symbol
    """
    ip = os.environ.get("CURRENCY_IP")
    if ip == '5.135.110.142':
        sign = "€"
        return sign
    elif ip == '139.99.236.163':
        sign = "A$"
        return sign
    elif ip == '192.99.54.60':
        sign = "C$"
        return sign
    else:
        sign = "$"
        return sign


def check_pricing_and_publish_page_editorial(browser):
    """
    User with a plan: Checks if he sees a Publish Page
    and Editorial pop-up - editorial sanity
    """
    try:
        verify_badge_and_count_text(browser)
    except NameError:
        pass
    assert is_clickable(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN) is False
    checkb = browser.find_element_by_css_selector(EDITORIAL_PUBLISH_CHECKBOX[1])
    browser.execute_script("arguments[0].click();", checkb)
    do_click(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN, 40)


def check_pricing_and_publish_page_editorial_suite(browser):
    """
    User with a plan: Checks if he sees a Publish Page
    and Editorial pop-up - editorial suite
    """
    do_click(browser, PUBLISH_TO_SOCIAL, 30)
    is_visible(browser, BADGE_ON_PUBLISH_PREVIEW, 15)
    check_pricing_and_publish_page_editorial(browser)
    is_visible(browser, PUBLISH_TO_SOCIAL_BACK, 10)
    do_click(browser, PUBLISH_TO_SOCIAL_BACK)
    do_click(browser, SOCIAL_BACK_LEAVE)
    assert is_visible(browser, PUBLISH_TO_SOCIAL) is True


def purchase_standard_plan(browser):
    """
    Existed user purchases a standard plan
    """
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX, 10)
    do_send_keys(browser, CARD_NUMBER_TXTBOX, read_creds(card_details_path, 0), 5)
    browser.switch_to.default_content()
    switch_to_iframe(browser, PAYMENT_EXPDATE_IFRAME)
    is_visible(browser, EXP_DATE_TXTBOX, 10)
    do_send_keys(browser, EXP_DATE_TXTBOX, read_creds(card_details_path, 1), 5)
    browser.switch_to.default_content()
    switch_to_iframe(browser, PAYMENT_CVC_IFRAME, 10)
    is_visible(browser, CVC_TXTBOX, 5)
    do_send_keys(browser, CVC_TXTBOX, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()
    time.sleep(2)
    if is_visible(browser, PURCHASE_NOW_BTN) is True:
        do_click(browser, PURCHASE_NOW_BTN)
    else:
        pass
    time.sleep(2)
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    if (test_name != 'test_signup_verify_premium_tags_and_see_pricing'
        and 'test_signup_verify_editorial_tags_and_see_pricing'
        and 'test_new_user_purchase_plan_on_editor_to_upload_watermark'
        and 'test_new_user_purchase_plan_to_add_brand') is True:
        assert is_visible(browser, CURRENT_PLAN, 30) is True
    else:
        pass
    if test_name == 'test_signup_verify_editorial_tags_and_see_pricing':
        check_pricing_and_publish_page_editorial(browser)
    else:
        pass


def purchase_standard_plan_new(browser):
    """
    New user purchases a standard plan
    """
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    time.sleep(2)
    if (test_name == 'test_new_user_purchase_plan_on_editor_to_upload_watermark'
                     or test_name == 'test_new_user_purchase_plan_to_add_brand') is True:
        switch_to_iframe(browser, EDITOR_PAYMENT_CARD_IFRAME_NEW, 10)
    else:
        switch_to_iframe(browser, PAYMENT_CARD_IFRAME_NEW, 10)
    if is_visible(browser, CARD_NUMBER_TXTBOX_NEW, 10) is True:
        do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW, read_creds(card_details_path, 0), 5)
        is_visible(browser, EXP_DATE_TXTBOX_NEW, 10)
        do_send_keys(browser, EXP_DATE_TXTBOX_NEW, read_creds(card_details_path, 1), 5)
        is_visible(browser, CVC_TXTBOX_NEW, 5)
        do_send_keys(browser, CVC_TXTBOX_NEW, read_creds(card_details_path, 2), 5)
    else:
        for n in range(19):
            do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW_2, read_creds_chars(card_details_path, 0, n), 5)
        is_visible(browser, EXP_DATE_TXTBOX_NEW_2, 10)
        for m in range(5):
            do_send_keys(browser, EXP_DATE_TXTBOX_NEW_2, read_creds_chars(card_details_path, 1, m), 5)
        is_visible(browser, CVC_TXTBOX_NEW_2, 5)
        do_send_keys(browser, CVC_TXTBOX_NEW_2, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()
    time.sleep(4)
    if (test_name != 'test_signup_verify_premium_tags_and_see_pricing'
            and 'test_signup_verify_editorial_tags_and_see_pricing'
            and 'test_new_user_purchase_plan_on_editor_to_upload_watermark'
            and 'test_new_user_purchase_plan_to_add_brand') is True:
        assert is_visible(browser, CURRENT_PLAN, 30) is True
    else:
        pass
    if test_name == 'test_signup_verify_editorial_tags_and_see_pricing':
        check_pricing_and_publish_page_editorial(browser)
    else:
        pass
    time.sleep(3)


def add_stripe_clock_cookie(browser):
    """
    below javascript command enables stripe clock cookie for the user
     once enabled, time can be advanced from stripe clock
    """
    browser.execute_script("javascript: (() => {document.cookie='promo-enable-stripe-test-clock=1; path=/'})()")


def purchase_standard_plan_pricing_widget(browser):
    """
    New user purchases a standard plan from pricing widget
    """
    time.sleep(2)
    assert is_visible(browser, PAYMENT_CARD_IFRAME) is True
    # to_improve: coverage of purchasing from the widget (flow differs from regular pricing page)


def signup_process_for_new_pricing(browser):
    """
    Simulates the new signup process for pricing purposes
    """
    browser.get(base_url_new_pricing)
    email_pricing = random_pricing_email_generator()
    try:
        do_click(browser, SIGNUP_BTN, 10)
    except NoSuchElementException:
        time.sleep(5)
        do_click(browser, SIGNUP_BTN, 10)
    time.sleep(2)
    do_send_keys(browser, SIGNUP_EMAIL, email_pricing, 10)
    do_send_keys(browser, SIGNUP_FULL_NAME, fullname_pricing, 10)
    do_send_keys(browser, SIGNUP_PASSWORD, random_password, 10)
    is_visible(browser, SIGNUP_NEW_BTN, 10)
    do_click(browser, SIGNUP_NEW_BTN, 10)
    if is_visible(browser, CLOSE_ONBOARDING_POPUP_NEW, 30):
        do_click(browser, CLOSE_ONBOARDING_POPUP_NEW)
    else:
        do_click(browser, CLOSE_ONBOARDING_POPUP)
    time.sleep(2)
    add_stripe_clock_cookie(browser)


def logged_in_new_shorter_c_plan(browser, pricing_email):
    """

    Args:
        browser:
        pricing_email: parameter for email id

    short login flow for c plan users with email parameter

    """
    go_to_url(browser, login_url)
    try:
        enter_email_new(browser, pricing_email)
    except (NoSuchElementException, TimeoutException):
        go_to_url(browser, login_url)
        time.sleep(2)
        enter_email_new(browser, pricing_email)
    enter_password_new(browser, read_creds(password, 5))
    click_login_new(browser)
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
        pass
    time.sleep(3)
    if is_visible(browser, X_BUTTON_CLOSE_OFFER) is True:
        do_click(browser, X_BUTTON_CLOSE_OFFER)
        title = browser.title
        print(title)
        assert title == create_page_title
    else:
        pass


def register_user_purchases_new_pricing_monthly(browser, plan_name):
    """
    New user purchases a new pricing plan
    plan_name: basic, standard, pro
    Bigger Stripe template
    """
    # do_click(browser, GO_TO_PRICING)
    browser.get(pricing_url)
    time.sleep(2)
    if is_visible(browser, TOGGLE_ON, 20) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    currencies_check(browser)
    is_visible(browser, plan_name, 10)
    do_click(browser, plan_name, 45)
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX, 10)
    do_send_keys(browser, CARD_NUMBER_TXTBOX, read_creds(card_details_path, 0), 5)
    browser.switch_to.default_content()
    switch_to_iframe(browser, PAYMENT_EXPDATE_IFRAME)
    is_visible(browser, EXP_DATE_TXTBOX, 10)
    do_send_keys(browser, EXP_DATE_TXTBOX, read_creds(card_details_path, 1), 5)
    browser.switch_to.default_content()
    switch_to_iframe(browser, PAYMENT_CVC_IFRAME, 10)
    is_visible(browser, CVC_TXTBOX, 5)
    do_send_keys(browser, CVC_TXTBOX, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()
    time.sleep(1)
    if is_visible(browser, PURCHASE_NOW_BTN) is True:
        do_click(browser, PURCHASE_NOW_BTN)
    else:
        pass
    assert is_visible(browser, CURRENT_PLAN, 30) is True
    if is_visible(browser, X_BUTTON_CLOSE_OFFER):
        do_click(browser, X_BUTTON_CLOSE_OFFER, 5)
    else:
        pass
    time.sleep(1)


def register_user_purchases_b_plans_monthly(browser, plan_name):
    do_click(browser, GO_TO_PRICING)
    if is_visible(browser, TOGGLE_ON, 20) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    # to_delete: Alka FYI
    # currencies_check(browser)
    is_visible(browser, plan_name, 10)
    do_click(browser, plan_name, 45)
    fill_payment_details(browser)
    if is_visible(browser, TOGGLE_ON, 20) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    assert is_visible(browser, CURRENT_PLAN, 30) is True


def register_user_purchases_b_plans_annual(browser, plan_name):
    # accept_cookies_new(browser)
    is_visible(browser, GO_TO_PRICING)
    do_click(browser, GO_TO_PRICING)
    if is_visible(browser, TOGGLE_OFF, 10) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    # to_delete: Alka FYI
    # currencies_check(browser)
    is_visible(browser, plan_name, 10)
    do_click(browser, plan_name, 45)
    fill_payment_details(browser)
    assert is_visible(browser, CURRENT_PLAN, 30) is True


def fill_payment_details(browser):
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME_NEW, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX_NEW_2, 3)
    for n in range(19):
        do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW_2, read_creds_chars(card_details_path, 0, n), 5)
    is_visible(browser, EXP_DATE_TXTBOX_NEW_2, 10)
    for m in range(5):
        do_send_keys(browser, EXP_DATE_TXTBOX_NEW_2, read_creds_chars(card_details_path, 1, m), 5)
    is_visible(browser, CVC_TXTBOX_NEW_2, 5)
    do_send_keys(browser, CVC_TXTBOX_NEW_2, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()


def register_user_purchases_new_pricing_annual(browser, plan_name):
    """
    New user purchases a new pricing plan
    plan_name: starter, business, agency
    Bigger Stripe template
    """
    # do_click(browser, GO_TO_PRICING)
    browser.get(pricing_url)
    if is_visible(browser, TOGGLE_OFF, 10) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    is_visible(browser, plan_name, 10)
    do_click(browser, plan_name, 45)
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX, 10)
    do_send_keys(browser, CARD_NUMBER_TXTBOX, read_creds(card_details_path, 0), 5)
    browser.switch_to.default_content()
    switch_to_iframe(browser, PAYMENT_EXPDATE_IFRAME)
    is_visible(browser, EXP_DATE_TXTBOX, 10)
    do_send_keys(browser, EXP_DATE_TXTBOX, read_creds(card_details_path, 1), 5)
    browser.switch_to.default_content()
    switch_to_iframe(browser, PAYMENT_CVC_IFRAME, 10)
    is_visible(browser, CVC_TXTBOX, 5)
    do_send_keys(browser, CVC_TXTBOX, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()
    time.sleep(3)
    if is_visible(browser, PURCHASE_NOW_BTN) is True:
        do_click(browser, PURCHASE_NOW_BTN)
    else:
        pass
    assert is_visible(browser, CURRENT_PLAN, 30) is True
    if is_visible(browser, X_BUTTON_CLOSE_OFFER):
        do_click(browser, X_BUTTON_CLOSE_OFFER, 5)
    else:
        pass
    time.sleep(3)


def register_user_purchases_special_offer(browser):
    """
    Registered user purchases a special offer
    Small Stripe template
    """
    is_visible(browser, SPECIAL_OFFER_BUTTON)
    do_click(browser, SPECIAL_OFFER_BUTTON)
    # to_delete: Alka FYI
    # print(browser.title)
    # driver = browser
    p = browser.current_window_handle
    parent = browser.window_handles[0]
    # chld = driver.window_handles[1]
    spl = browser.window_handles[2]
    browser.switch_to.window(spl)
    is_visible(browser, SPECIAL_OFFER_TITLE_ON_LP)
    is_visible(browser, SPECIAL_OFFER_BUY_NOW_BUTTON)
    do_click(browser, SPECIAL_OFFER_BUY_NOW_BUTTON)
    browser.switch_to.window(spl)
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME_NEW, 10)
    # browser.switch_to_frame(1)
    is_visible(browser, CARD_NUMBER_TXTBOX_NEW, 3)
    do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW, read_creds(card_details_path, 0), 5)
    is_visible(browser, EXP_DATE_TXTBOX_NEW, 10)
    do_send_keys(browser, EXP_DATE_TXTBOX_NEW, read_creds(card_details_path, 1), 5)
    is_visible(browser, CVC_TXTBOX_NEW, 5)
    do_send_keys(browser, CVC_TXTBOX_NEW, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()
    time.sleep(3)
    if is_visible(browser, PURCHASE_NOW_BTN) is True:
        do_click(browser, PURCHASE_NOW_BTN)
    else:
        pass
    do_click(browser, CONFIRM_BTN)


def user_cancel_plan_survey_1(browser):
    """
    User cancels a plan from billing page
    Survey: choose reason from first group
    performance issues, missing content
    """
    do_hover(browser, USERNAME_MENU)
    do_click(browser, BILLING, 15)
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH, sec=5) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    is_visible(browser, CANCEL_SUBSCRIPTION_LINK)
    do_click(browser, CANCEL_SUBSCRIPTION_LINK)
    do_click(browser, CANCEL_PLAN_CHECKBOX_PERFORMANCE)
    do_click(browser, CANCEL_PLAN_NEXT_BTN)
    if is_visible(browser, CANCEL_PLAN_2) is True:
        do_click(browser, CANCEL_PLAN_2)
    else:
        do_click(browser, CANCEL_PLAN_BTN)


def user_cancel_plan_survey_2(browser):
    """
    User cancels a plan from billing page
    Survey: choose reason from first group
    expensive, something else, missing features, no need more videos
    """
    do_hover(browser, USERNAME_MENU)
    do_click(browser, BILLING, 15)
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH, sec=5) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    is_visible(browser, CANCEL_SUBSCRIPTION_LINK)
    do_click(browser, CANCEL_SUBSCRIPTION_LINK, 5)
    do_click(browser, CANCEL_PLAN_CHECKBOX_EXPENSIVE)
    do_click(browser, CANCEL_PLAN_NEXT_BTN)


def user_gets_offer_half_a_price(browser):
    """
    User gets an offer half a price
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    is_visible(browser, STARTER_9_DOLLAR)


def user_upgrades_to_c2_monthly(browser):
    """
    User Upgrades to C2 Monthly with 20% OFF
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    try:
        is_visible(browser, BUSINESS_20_CENT_OFF)
    except:
        try:
            is_visible(browser, BUSINESS_20_CENT_OFF_1)
        except:
            print("Plan Card Container Error")


def user_cancel_plan_anyway(browser):
    """
    User cancels a plan anyway and returns to billing page
    """
    do_click(browser, CANCEL_PLAN_BTN)
    do_hover(browser, CHECKBOX_UNLIKELY)
    do_click(browser, CHECKBOX_UNLIKELY)
    do_click(browser, YES_CANCEL_PLAN)
    time.sleep(5)
    if is_visible(browser, OK_BTN) is True:
        do_click(browser, OK_BTN)
    # TO REPORT BROKEN AFTER CANCELING PLAN stays on that page forever, have to refresh
    browser.refresh()
    text1 = get_element_text(browser, SUB_PENDING_CANCEL)
    assert sub_pending_title_cancel == text1


def user_close_offer(browser):
    """
    User closes an offer during cancellation flow
    """
    do_click(browser, CLOSE_CANCELLATION_OFFER)
    assert is_visible(browser, CANCEL_SUBSCRIPTION_LINK) is True


def user_accept_offer(browser):
    """
    User accepts an offer and returns to billing page
    """
    user_accepts_the_offer_and_moves_on(browser)
    text2 = get_element_text(browser, SUB_PENDING_UPDATE)
    assert sub_pending_title_downgrade == text2
    assert is_visible(browser, BILLING_UPDATE_GREEN_ICON)


def user_accept_special_offer(browser):
    user_accepts_the_offer_and_moves_on(browser)
    time.sleep(2)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_pending_title_downgrade in text2
    current_plan = "bi_annual"
    bi_annual = price_check(current_plan)
    next_charge = int(bi_annual)
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accept_half_price_b1_monthly(browser):
    """
    User accepts discount on current plan offer, returns to billing page and verifies accepted offer price
    """
    user_accepts_the_offer_and_moves_on(browser)
    browser.refresh()
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_will_renew in text2
    next_charge = half_price_b1(browser)
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accept_lite_plan_offer(browser):
    """
    User accepts an offer, returns to billing page and verifies offer price
    """
    user_accepts_the_offer_and_moves_on(browser)
    browser.refresh()
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_pending_title_downgrade in text2
    next_charge = lite_plan(browser)
    # math.ceil will round up the price from 9.99 to 10 as this is how price is displayed on billing page
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accept_half_price_basic_annual_offer(browser):
    user_accepts_the_offer_and_moves_on(browser)
    browser.refresh()
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_will_renew in text2
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    if test_name == 'test_basic_annual_user_accepts_second_offer_half_price_basic_annual':
        next_charge = int(basic_annual(browser))/2
    else:
        next_charge = int(basic_annual(browser))
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accept_downgrade_to_basic_monthly_offer(browser):
    user_accepts_the_offer_and_moves_on(browser)
    if is_clickable(browser, AGREE_COOKIES_NEW_AUTH) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_will_renew in text2
    next_charge = int(basic_monthly(browser))
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accept_downgrade_to_standard_monthly_offer(browser):
    user_accepts_the_offer_and_moves_on(browser)
    if is_clickable(browser, AGREE_COOKIES_NEW_AUTH) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_will_renew in text2
    next_charge = int(standard_monthly(browser))
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accept_downgrade_to_pro_monthly_offer(browser):
    user_accepts_the_offer_and_moves_on(browser)
    if is_clickable(browser, AGREE_COOKIES_NEW_AUTH) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_will_renew in text2
    next_charge = int(pro_monthly(browser))
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_accepts_the_offer_and_moves_on(browser):
    """
    User accepts an offer and clicks OK
    """
    is_visible(browser, YES_I_WANT_THIS_BTN)
    do_click(browser, YES_I_WANT_THIS_BTN)
    is_visible(browser, PURCHASE_OFFER_TITLE, sec=5)
    text1 = get_element_text(browser, PURCHASE_OFFER_TITLE)
    assert cancellation_flow_offer_title == text1
    time.sleep(5)
    if is_visible(browser, OK_BTN, sec=7) is True:
        do_click(browser, OK_BTN)


def user_accept_basic_monthly_offer(browser):
    do_click(browser, DOWNGRADE_BTN)
    is_visible(browser, PURCHASE_OFFER_TITLE)
    text1 = get_element_text(browser, PURCHASE_OFFER_TITLE)
    assert cancellation_flow_offer_title == text1
    time.sleep(5)
    if is_clickable(browser, OK_BTN, 7) is True:
        do_click(browser, OK_BTN)
    browser.refresh()
    if is_clickable(browser, AGREE_COOKIES_NEW_AUTH, 10) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_pending_title_downgrade in text2
    next_charge = int(basic_monthly(browser))
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def user_declines_an_offer(browser):
    """
    General function for declining an offer
    """
    do_click(browser, CANCEL_PLAN_BTN)


def user_gets_offer_downgrade_to_starter(browser):
    """
    User gets offer - downgrade to starter
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    is_visible(browser, STARTER_18_DOLLAR)


def user_gets_offer_half_a_price_starter_annual(browser):
    """
    User gets offer - half a price for starter annual
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    is_visible(browser, STARTER_ANNUAL_DOLLAR)


def user_gets_offer_downgrade_to_starter_or_business(browser):
    """
    User gets double offer - downgrade to starter or business
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    is_visible(browser, STARTER_AND_BUSINESS_TWO_OFFER)


def user_gets_offer_unlimited_6_months(browser):
    """
    User gets offer - special unlimited clips for 6 months
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    text1 = text.split()[:5]  # text on website contains two lines, comparing only 5 first words
    final = ' '.join([str(elem) for elem in text1])
    assert final == special_6_months_offer_title
    is_visible(browser, UNLIMITED_CLIPS_6_MONTHS)
    price = get_element_text(browser, PRICE_OFFERED_TO_USER_3)
    cs = get_element_text(browser, CURRENCY_SYMBOL_3)
    cs_1 = currency_symbol_check()
    current_plan = "bi_annual"
    bi_annual = price_check(current_plan)
    # allure_screenshot(browser)
    assert cs == cs_1
    assert price == bi_annual
    print("Amount shown to the User, " + cs + price + ", is verified")


def user_gets_offer_half_a_price_1_month(browser):
    """
    User gets offer - special half a price 1 month
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_1_month_offer_title


def user_accept_starter_or_business_offer(browser, accept_starter_or_business):
    """
    User accepts one of the offers
    accept_starter_or_business: ACCEPT_OFFER_STARTER, ACCEPT_OFFER_BUSINESS
    """
    do_click(browser, accept_starter_or_business)
    do_click(browser, DOWNGRADE_BTN)
    is_visible(browser, PURCHASE_OFFER_TITLE)
    text1 = get_element_text(browser, PURCHASE_OFFER_TITLE)
    assert cancellation_flow_offer_title == text1
    is_clickable(browser, OK_BTN)
    do_click(browser, OK_BTN)
    is_visible(browser, SUB_PENDING_UPDATE)
    text2 = get_element_text(browser, SUB_PENDING_UPDATE)
    assert sub_pending_title_downgrade == text2
    assert is_visible(browser, BILLING_DOWNGRADE_GREEN_ICON)


def user_switches_to_offer_business_monthly(browser):
    """
    User gets offer - Switch to C2 Monthly
    """
    assert is_visible(browser, MONTHLY_BUSINESS)


def user_gets_starter_half_a_price_annual(browser):
    """
    User gets an offer - Starter Annual for a half price
    """
    is_visible(browser, STARTER_ANNUAL_72)


def user_offer_downgrade_annual_to_monthly(browser):
    """
    User gets an offer - Switch to monthly from annual
    """
    is_visible(browser, SWITCH_TO_MONTHLY_PLAN_TITLE)
    text1 = get_element_text(browser, SWITCH_TO_MONTHLY_PLAN_TITLE)
    assert text1 == switch_to_monthly_plan


def half_price_b1(browser):
    """
    reads prices from google sheet and returns price for the plan, used at multiple places
    """
    current_plan = "B1_half_price"
    b1 = price_check(current_plan)
    b1_half_price = int(b1) / 2
    return b1_half_price


def lite_plan(browser):
    """
    this reads prices from google sheet and returns here, used at multiple places
    """
    current_plan = "Lite Plan"
    lite_price = price_check(current_plan)
    return int(lite_price)


def basic_monthly(browser):
    current_plan = "B1"
    b1 = price_check(current_plan)
    return b1


def standard_monthly(browser):
    current_plan = "B2"
    b2 = price_check(current_plan)
    return b2


def pro_monthly(browser):
    current_plan = "B3"
    b3 = price_check(current_plan)
    return b3


def basic_annual(browser):
    current_plan = "B1_Annual_Half_Price"
    b1_annual = price_check(current_plan)
    # b1_annual_half_price = f'{float(int(b1_annual) / 2):g}'
    return b1_annual


def user_gets_offer_basic_plan_for_half_price(browser):
    """
    User gets offer - special half a price 1 month
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    is_visible(browser, BASIC_MONTHLY_HALF_PRICE)
    price = get_element_text(browser, PRICE_OFFERED_TO_USER)
    cs = get_element_text(browser, CURRENCY_SYMBOL)
    cs_1 = currency_symbol_check()
    b1_half_price = math.ceil(half_price_b1(browser))
    assert cs == cs_1
    assert price == str(b1_half_price)
    print("Amount shown to the User, " + cs + price + ", is verified")


def user_gets_offer_to_switch_to_lite_plan(browser):
    """
    User gets offer - lite plan monthly
    """
    is_visible(browser, lITE_PLAN_OFFER_TITLE)
    text = get_element_text(browser, lITE_PLAN_OFFER_TITLE)
    assert text == lite_plan_offer_title
    is_visible(browser, lITE_PLAN)
    price = get_element_text(browser, PRICE_OFFERED_TO_USER)
    cs = get_element_text(browser, CURRENCY_SYMBOL)
    cs_1 = currency_symbol_check()
    l1 = lite_plan(browser)
    assert cs == cs_1
    assert int(round(float(price))) == int(l1)
    print("Amount shown to the User, " + cs + price + ", is verified")


def user_get_offer_downgrade_to_basic_monthly(browser):
    """
    User gets a downgrade offer - There is a better way
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == there_is_a_better_way
    is_visible(browser, BASIC_PLAN_OFFER)
    price = get_element_text(browser, PRICE_OFFERED_TO_USER)
    cs = get_element_text(browser, CURRENCY_SYMBOL)
    cs_1 = currency_symbol_check()
    b1 = basic_monthly(browser)
    assert cs == cs_1
    assert price == b1
    print("Amount shown to the User, " + cs + price + ", is verified")


def user_gets_offer_basic_annual_for_half_price(browser):
    """
    User gets an offer 50% for basic annual
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == special_offer_title
    is_visible(browser, BASIC_ANNUAL_HALF_PRICE)
    price = get_element_text(browser, PRICE_OFFERED_TO_USER)
    cs = get_element_text(browser, CURRENCY_SYMBOL)
    cs_1 = currency_symbol_check()
    b1_annual = basic_annual(browser)
    # converts the string to int, divides, drops the trailing zero and then converts to string
    b1_annual_half_price = f'{float(int(b1_annual) / 2):g}'
    assert cs == cs_1
    assert price == b1_annual_half_price
    print("Amount shown to the User, " + cs + price + ", is verified")


def user_get_offer_to_downgrade_to_basic_or_standard_monthly(browser):
    """
    User gets double offer - downgrade to basic or standard
    """
    is_visible(browser, SPECIAL_OFFER_TITLE)
    text = get_element_text(browser, SPECIAL_OFFER_TITLE)
    assert text == there_is_a_better_way
    is_visible(browser, BASIC_AND_STANDARD_TWO_OFFERS)
    price1 = get_element_text(browser, PRICE_OFFERED_TO_USER)
    price2 = get_element_text(browser, PRICE_OFFERED_TO_USER_2)
    current_plan_1 = "B1"
    current_plan_2 = "B2"
    cs = get_element_text(browser, CURRENCY_SYMBOL)
    cs1 = get_element_text(browser, CURRENCY_SYMBOL_2)
    cs_1 = currency_symbol_check()
    b1 = price_check(current_plan_1)
    b2 = price_check(current_plan_2)
    assert cs == cs_1 == cs1
    assert price1 == b1 and price2 == b2
    print("Amount shown to the User, " + cs + price1 + " & " + cs + price2 + ", is verified")


def user_accept_basic_or_standard_offer(browser, accept_basic_or_standard):
    """
    User accepts one of the offers
    accept_basic_or_standard: ACCEPT_OFFER_BASIC, ACCEPT_OFFER_STANDARD
    Verifies amount on Billing page
    """
    do_click(browser, accept_basic_or_standard)
    do_click(browser, DOWNGRADE_BTN)
    is_visible(browser, PURCHASE_OFFER_TITLE)
    text1 = get_element_text(browser, PURCHASE_OFFER_TITLE)
    assert cancellation_flow_offer_title == text1
    time.sleep(5)
    is_clickable(browser, OK_BTN, sec=7)
    do_click(browser, OK_BTN)
    browser.refresh()
    if is_clickable(browser, AGREE_COOKIES_NEW_AUTH, sec=2) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    assert sub_pending_title_downgrade in text2
    if accept_basic_or_standard == ('xpath', "//div[@class='ncf-plan-card ncf-plan-card--downgrade']"):
        current_plan = "B1"
    else:
        current_plan = "B2"
    next_charge = int(price_check(current_plan))
    assert f'you will be charged {currency_symbol_check()}{math.ceil(next_charge)}' in text2


def change_plan_on_publish_pricing(browser, plan):
    """

    Args:
        browser:
        plan: Plan tile comes from step definition

    upgrade plan on Publish pricing widget

    """
    is_visible(browser, PUBLISH_TO_SOCIAL)
    wait_for_ajax(browser)
    try:
        do_click(browser, PUBLISH_TO_SOCIAL)
    except WebDriverException:
        time.sleep(2)
        try:
            do_click(browser, PUBLISH_TO_SOCIAL)
        except WebDriverException:
            pass
    switch_to_iframe(browser, EMBED_PRICING_IFRAME)
    assert is_visible(browser, EMBED_PRICING_POPUP) is True
    browser.switch_to.default_content()
    currencies_check(browser)
    switch_to_iframe(browser, EMBED_PRICING_IFRAME)
    toggle_text = get_element_text(browser, PRICING_WIDGET_TOGGLE_ON)
    if toggle_text == 'Annual':
        do_click(browser, PRICING_WIDGET_TOGGLE_OFF)
    else:
        pass
    current_plan = get_element_text(browser, PRICING_WIDGET_CURRENT_PLAN)
    assert current_plan == 'Basic'
    do_click(browser, PRICING_WIDGET_TOGGLE_OFF)
    do_click(browser, (By.XPATH, f'//SPAN[text()={plan}]/following-sibling::button'))
    time.sleep(1)
    do_click(browser, CHANGE_PLAN_CONF_BTN)
    browser.switch_to.default_content()
    assert is_visible(browser, PUBLISH_TO_SOCIAL_BACK, 40) is True
    do_click(browser, PUBLISH_TO_SOCIAL_BACK)
    is_visible(browser, SOCIAL_BACK_LEAVE)
    do_click(browser, SOCIAL_BACK_LEAVE)
    time.sleep(4)