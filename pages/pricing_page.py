from locators.locators_file import *
from locators.locators_links import *
from helpers.common_helpers import *
from pages.editor_page import *
from pages.newcancellation_page import *
from test_data.testdata import *
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time


def goto_pricing_page(browser):
    """
    Goes to the pricing page
    """
    is_clickable(browser, MAIN_MENU_TITLES["Pricing & Plans | Promo.com | Marketing Video Maker"])
    do_click(browser, MAIN_MENU_TITLES["Pricing & Plans | Promo.com | Marketing Video Maker"], 10)
    title = browser.title
    assert title == pricing_page_title


def pricing_page_url(browser):
    """
    Opens pricing page
    If statement created for BrowserStack
    """
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    browser.get(pricing_url)


def twofa_purchase_standard_plan_old(browser):
    """
    Existed user purchases a standard plan with 2FA
    """
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX, 10)
    do_send_keys(browser, CARD_NUMBER_TXTBOX, read_creds(card_details_path, 3), 5)
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
    browser.switch_to.default_content()
    switch_to_iframe(browser, TWOFA_AUTH_FRAME, 30)
    try:
        switch_to_iframe(browser, TWOFA_AUTH_FRAME1)
    except (NoSuchElementException, TimeoutException):
        browser.switch_to.default_content()
        switch_to_iframe(browser, TWOFA_AUTH_FRAME, 30)
        switch_to_iframe(browser, TWOFA_AUTH_FRAME1)
    switch_to_iframe(browser, TWOFA_AUTH_FRAME2)
    do_click(browser, TWOFA_AUTH_BTN)
    browser.switch_to.default_content()
    assert is_visible(browser, CURRENT_PLAN, 30) is True
    time.sleep(3)
    # allure_screenshot(browser)


def twofa_purchase_standard_plan(browser):
    """
    User purchases a plan using 2FA
    """
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME_NEW, 10)
    if is_visible(browser, CARD_NUMBER_TXTBOX_NEW, 10) is True:
        do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW, read_creds(card_details_path, 0), 5)
        is_visible(browser, EXP_DATE_TXTBOX_NEW, 10)
        do_send_keys(browser, EXP_DATE_TXTBOX_NEW, read_creds(card_details_path, 1), 5)
        is_visible(browser, CVC_TXTBOX_NEW, 5)
        do_send_keys(browser, CVC_TXTBOX_NEW, read_creds(card_details_path, 2), 5)
    else:
        for n in range(19):
            do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW_2, read_creds_chars(card_details_path, 3, n), 5)
        is_visible(browser, EXP_DATE_TXTBOX_NEW_2, 10)
        for m in range(5):
            do_send_keys(browser, EXP_DATE_TXTBOX_NEW_2, read_creds_chars(card_details_path, 1, m), 5)
        is_visible(browser, CVC_TXTBOX_NEW_2, 5)
        do_send_keys(browser, CVC_TXTBOX_NEW_2, read_creds(card_details_path, 2), 5)
    browser.switch_to.default_content()
    time.sleep(3)
    browser.switch_to.default_content()
    switch_to_iframe(browser, TWOFA_AUTH_FRAME, 30)
    try:
        switch_to_iframe(browser, TWOFA_AUTH_FRAME1)
    except (NoSuchElementException, TimeoutException):
        browser.switch_to.default_content()
        switch_to_iframe(browser, TWOFA_AUTH_FRAME, 30)
        switch_to_iframe(browser, TWOFA_AUTH_FRAME1)
    switch_to_iframe(browser, TWOFA_AUTH_FRAME2)
    do_click(browser, TWOFA_AUTH_BTN)
    browser.switch_to.default_content()
    assert is_visible(browser, CURRENT_PLAN, 30) is True
    time.sleep(3)
    # allure_screenshot(browser)


def twofa_new_business_plan (browser, plan_name):
    """
    New user purchases a new pricing plan
    plan_name: starter, business, agency
    Bigger Stripe template
    """
    do_click(browser, GO_TO_PRICING)
    if is_visible(browser, TOGGLE_ON, 10) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    is_visible(browser, plan_name, 10)
    do_click(browser, plan_name, 45)
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX, 10)
    do_send_keys(browser, CARD_NUMBER_TXTBOX, read_creds(card_details_path, 3), 5)
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
    browser.switch_to.default_content()
    switch_to_iframe(browser, TWOFA_AUTH_FRAME, 30)
    try:
        switch_to_iframe(browser, TWOFA_AUTH_FRAME1)
    except (NoSuchElementException, TimeoutException):
        browser.switch_to.default_content()
        switch_to_iframe(browser, TWOFA_AUTH_FRAME, 30)
        switch_to_iframe(browser, TWOFA_AUTH_FRAME1)
    switch_to_iframe(browser, TWOFA_AUTH_FRAME2)
    do_click(browser, TWOFA_AUTH_BTN)
    browser.switch_to.default_content()
    assert is_visible(browser, CURRENT_PLAN, 30) is True


def purchase_standard_plan_new_prod(browser):
    """
    Purchases a plan on prod
    """
    if is_visible(browser, TOGGLE_ON, 10) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    is_visible(browser, STANDARD_PLAN_CTA, 10)
    do_click(browser, STANDARD_PLAN_CTA, 45)
    switch_to_iframe(browser, PAYMENT_CARD_IFRAME_NEW, 10)
    is_visible(browser, CARD_NUMBER_TXTBOX_NEW, 10)
    do_send_keys(browser, CARD_NUMBER_TXTBOX_NEW, read_creds(card_details_path, 0), 5)
    is_visible(browser, EXP_DATE_TXTBOX_NEW, 10)
    do_send_keys(browser, EXP_DATE_TXTBOX_NEW, read_creds(card_details_path, 1), 5)
    is_visible(browser, CVC_TXTBOX_NEW, 5)
    do_send_keys(browser, CVC_TXTBOX_NEW, read_creds(card_details_path, 2), 5)
    is_visible(browser, PROD_CARD_DECLINE_MESSAGE)
    do_click(browser, PAYMENT_POPUP_CLOSE_BTN)
    browser.switch_to.default_content()
    # allure_screenshot(browser)


def register_user_purchases_new_pricing_monthly_prod(browser, plan_name):
    """
    New user purchases a new pricing plan
    plan_name: starter, business, agency
    Bigger Stripe template
    """
    if is_visible(browser, TOGGLE_ON, 10) is True:
        do_click(browser, TOGGLE_BTN, 10)
    else:
        pass
    try:
        assert is_visible(browser, STANDARD_PLAN_CTA, 10) is True
    except AssertionError:
        assert is_visible(browser, plan_name, 10) is True
    # to_delete: Rishabg FYI
    # is_visible(browser, plan_name, 10)
    # do_click(browser, plan_name, 45)
    # switch_to_iframe(browser, PAYMENT_CARD_IFRAME, 10)
    # is_visible(browser, CARD_NUMBER_TXTBOX, 10)
    # do_send_keys(browser, CARD_NUMBER_TXTBOX, read_creds(card_details_path, 0), 5)
    # browser.switch_to.default_content()
    # switch_to_iframe(browser, PAYMENT_EXPDATE_IFRAME)
    # is_visible(browser, EXP_DATE_TXTBOX, 10)
    # do_send_keys(browser, EXP_DATE_TXTBOX, read_creds(card_details_path, 1), 5)
    # browser.switch_to.default_content()
    # switch_to_iframe(browser, PAYMENT_CVC_IFRAME, 10)
    # is_visible(browser, CVC_TXTBOX, 5)
    # do_send_keys(browser, CVC_TXTBOX, read_creds(card_details_path, 2), 5)
    # time.sleep(3)
    # if is_visible(browser, PURCHASE_NOW_BTN) is True:
    #     do_click(browser, PURCHASE_NOW_BTN)
    # else:
    #     is_visible(browser, PROD_CARD_DECLINE_MESSAGE)
    #     do_click(browser, PAYMENT_POPUP_CLOSE_BTN)
    #     browser.switch_to.default_content()
    #     # allure_screenshot(browser)


def close_pricing_plans(browser):
    """
    Closes pricing plans pop-up
    """
    time.sleep(3)
    try:
        if is_visible(browser, PRICING_INTERCOM_IFRAME, 3) is True:
            switch_to_iframe(browser, PRICING_INTERCOM_IFRAME)
            do_click(browser, PRICING_INTERCOM_IFRAME_CLS)
            browser.switch_to.default_content()
            if is_visible(browser, EMBED_PRICING_IFRAME) is True:
                do_click(browser, EMBED_PRICING_POPUP_CLS)
                browser.switch_to.default_content()
            else:
                do_click(browser, PRICING_CLOSE_BTN, 10)
        elif is_visible(browser, PRICING_INTERCOM_IFRAME_BS, 2):
            switch_to_iframe(browser, PRICING_INTERCOM_IFRAME_BS, 2)
            do_click(browser, PRICING_INTERCOM_IFRAME_CLS)
            browser.switch_to.default_content()
            if is_visible(browser, EMBED_PRICING_IFRAME) is True:
                do_click(browser, EMBED_PRICING_POPUP_CLS)
                browser.switch_to.default_content()
            else:
                do_click(browser, PRICING_CLOSE_BTN, 10)
        # to_delete: Alka FYI
        # elif is_visible(browser, PRICING_POPUP):
        #     # add switch to frame here
        #     do_click(browser, PRICING_CLOSE_BTN)
    except (TimeoutException, NoSuchElementException) as pif:
        if is_visible(browser, EMBED_PRICING_IFRAME) is True:
            do_click(browser, EMBED_PRICING_POPUP_CLS)
            browser.switch_to.default_content()
        else:
            do_click(browser, PRICING_CLOSE_BTN, 10)
