from locators.mobile_locators import *
from test_data.testdata import *
from helpers.common_helpers import *


def purchase_a_plan_on_mobile(mob_browser):
    """
    Purchases a plan on mobile view
    Passes if on production
    """
    do_click(mob_browser, CHOOSE_BASIC_BTN_MOB)
    switch_to_iframe(mob_browser, PAYMENT_CARD_IFRAME_MOB_CARD, 10)
    assert is_visible(mob_browser, CARD_FIELD_MOB, 10) is True
    if os.environ['url'] != 'https://promo.com':
        do_send_keys(mob_browser, CARD_FIELD_MOB, read_creds(card_details_path, 0), 5)
        mob_browser.switch_to.default_content()
        switch_to_iframe(mob_browser, PAYMENT_CARD_IFRAME_MOB_EXP, 10)
        is_visible(mob_browser, DATE_EXP_MOB, 10)
        do_send_keys(mob_browser, DATE_EXP_MOB, read_creds(card_details_path, 1), 5)
        mob_browser.switch_to.default_content()
        switch_to_iframe(mob_browser, PAYMENT_CARD_IFRAME_MOB_CVC, 10)
        is_visible(mob_browser, CVC_MOB, 5)
        do_send_keys(mob_browser, CVC_MOB, read_creds(card_details_path, 2), 5)
        mob_browser.switch_to.default_content()
        assert is_visible(mob_browser, PURCHASED_CURRENT_PLAN) is True
    else:
        mob_browser.switch_to.default_content()


def open_pricing_on_mobile(mob_browser):
    """
    Opens the pricing page on mobile via hamburger menu
    """
    is_visible(mob_browser, PRICING_FROM_MENU)
    try:
        do_click(mob_browser, PRICING_FROM_MENU)
    except TimeoutException:
        do_click(mob_browser, HOME_HAMBURGER_ICON)
        do_click(mob_browser, PRICING_FROM_MENU)
    assert is_visible(mob_browser, PRICING_HEADER, 30) is True


