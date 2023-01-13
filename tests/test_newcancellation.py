from pytest_bdd import when, then, given, parsers
from selenium.common.exceptions import WebDriverException

from pages.pricing_page import *
from pages.home_page_login import *
from pages.newcancellation_page import *
from pages.assertion_page import *
from pages.stripe_clock_simulation import *
from test_data.testdata import *


def geo_email_format():
    currency_ip = os.environ.get("CURRENCY_IP")
    if currency_ip == EU:
        email_second_format = 'europe'
    elif currency_ip == DE:
        email_second_format = 'europe'
    elif currency_ip == UK:
        email_second_format = 'unitedk'
    elif currency_ip == PL:
        email_second_format = 'europe'
    elif currency_ip == Singapur:
        email_second_format = 'singapur'
    elif currency_ip == Canada:
        email_second_format = 'canada'
    elif currency_ip == Australia:
        email_second_format = 'australia'
    else:
        email_second_format = ''
    return email_second_format


@given('User with Starter Monthly is logged in')
def starter_mnthly_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_monthly(browser, starter_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_mnthly_logged_in)


@given('User with Business Monthly is logged in')
def starter_buss_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_monthly(browser, business_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_buss_logged_in)


@given('User with Basic Monthly is logged in')
def basic_monthly_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_monthly(browser, basic_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, basic_monthly_logged_in)

@given('I simulate time using stripe clock')
def advance_stripe_clock(browser):
    try:
        advance_time_from_stripe_clock(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, advance_stripe_clock)


@given('User with Standard Monthly is logged in')
def standard_monthly_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_monthly(browser, standard_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, standard_monthly_logged_in)


@given('User with Pro Monthly is logged in')
def pro_monthly_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_monthly(browser, pro_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, pro_monthly_logged_in)


@given('User with Basic Annual is logged in')
def basic_annual_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_annual(browser, basic_plan_an)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, basic_annual_logged_in)


@given('User with Standard Annual is logged in')
def standard_annual_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_annual(browser, standard_plan_an)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, standard_annual_logged_in)


@given('User with Pro Annual is logged in')
def pro_annual_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_annual(browser, pro_plan_an)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, pro_annual_logged_in)


TYPES = {'d': str }
@given(parsers.cfparse('User with C plan is logged in "{email_pricing_format:d}"', extra_types=TYPES))
@given('User with C plan is logged in "<email_pricing_format>"')
def pro_annual_logged_in_2(browser, email_pricing_format):
    try:
        email_pricing = email_pricing_format + geo_email_format() + "@promo.com"
        logged_in_new_shorter_c_plan(browser, email_pricing)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, pro_annual_logged_in)


@given('User with C plan cancellation offer <email_pricing_format>')
def pro_annual_logged_in_3(browser, email_pricing_format):
    try:
        email_pricing = email_pricing_format + geo_email_format() + "@promo.com"
        if email_pricing_format == 'cplanstartermonthly':
            if geo_email_format == 'EURO':
                pass
            logged_in_new_shorter_c_plan(browser, email_pricing)
        elif email_pricing_format == 'cplanbusinessmonthly':
            logged_in_new_shorter_c_plan(browser, email_pricing)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, pro_annual_logged_in)


@given('User with Agency Monthly is logged in')
def starter_agency_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_monthly(browser, agency_plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_agency_logged_in)


@given('User with Starter Annual is logged in')
def starter_mnthly_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_annual(browser, starter_plan_an)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_mnthly_logged_in)


@given('User with Business Annual is logged in')
def starter_buss_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_annual(browser, business_plan_an)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_buss_logged_in)


@given('User with Agency Annual is logged in')
def starter_agency_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_new_pricing_annual(browser, agency_plan_an)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_agency_logged_in)


@given('User with Special Offer is logged in')
def starter_agency_logged_in(browser):
    try:
        signup_process_for_new_pricing(browser)
        register_user_purchases_special_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, starter_agency_logged_in)


@when('User chooses plan survey from 1st group')
def user_cancels_a_plan_1(browser):
    try:
        advance_time_from_stripe_clock(browser)
        user_cancel_plan_survey_1(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_cancels_a_plan_1)


@when('User cancels a plan survey 2nd group')
def user_cancels_a_plan_2(browser):
    try:
        advance_time_from_stripe_clock(browser)
        user_cancel_plan_survey_2(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_cancels_a_plan_2)


@then('User gets offer Half a Price')
def offer_half_a_price(browser):
    try:
        user_gets_offer_half_a_price(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, offer_half_a_price)


@then('User gets offer c2 monthly 20 percent off')
def upgrade_to_c2_monthly(browser):
    try:
        user_upgrades_to_c2_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, upgrade_to_c2_monthly)


@then(parsers.cfparse('Monthly User gets first offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('Monthly User gets first offer <email_pricing_format>')
def verify_first_offer(browser, email_pricing_format):
    try:
        if email_pricing_format == 'cplanstartermonthly+test01':
            user_upgrades_to_c2_monthly(browser)
        elif email_pricing_format == 'cplanbusinessmonthly+test01':
            user_gets_offer_half_a_price(browser)
        elif email_pricing_format == 'cplanagencymonthly+test01':
            user_gets_offer_downgrade_to_starter_or_business(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_first_offer)

@then(parsers.cfparse('Monthly User gets second offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('Monthly user gets second offer <email_pricing_format>')
def verify_second_offer(browser, email_pricing_format):
    try:
        if email_pricing_format == 'cplanstartermonthly+test01':
            user_gets_offer_half_a_price(browser)
        elif email_pricing_format == 'cplanbusinessmonthly+test01':
            user_gets_offer_downgrade_to_starter(browser)
        elif email_pricing_format == 'cplanagencymontly+test01':
            user_gets_offer_unlimited_6_months(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_second_offer)

@then(parsers.cfparse('Annual User gets first offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('Annual User gets first offer "<email_pricing_format>"')
def verify_first_offer_for_annual_user(browser, email_pricing_format):
    try:
        if email_pricing_format == 'cplanstarterannual+test01':
            user_offer_downgrade_annual_to_monthly(browser)
        elif email_pricing_format == 'cplanbusinessannual+test01':
            user_offer_downgrade_annual_to_monthly(browser)
        elif email_pricing_format == 'cplanagencyannual+test01':
            user_offer_downgrade_annual_to_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_first_offer_for_annual_user)


@then(parsers.cfparse('Annual User gets second offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('Annual User gets second offer "<email_pricing_format>"')
def verify_second_offer_for_annual_user(browser, email_pricing_format):
    try:
        if email_pricing_format == 'cplanstarterannual+test01':
            user_switches_to_offer_business_monthly(browser)
        elif email_pricing_format == 'cplanbusinessannual+test01':
            user_gets_offer_downgrade_to_starter(browser)
        elif email_pricing_format == 'cplanagencyannual+test01':
            user_gets_offer_downgrade_to_starter_or_business(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_second_offer_for_annual_user)


@then('User cancels anyway')
def user_cancel_a_plan(browser):
    try:
        user_cancel_plan_anyway(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_cancel_a_plan)


@then('User declines an offer')
def user_decline_offer(browser):
    try:
        user_declines_an_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_decline_offer)


@then('User accepts special offer')
def user_accept_6_monthly_offer(browser):
    try:
        user_accept_special_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accept_6_monthly_offer)


@then('User closes the offer')
def user_closes_an_offer(browser):
    try:
        user_close_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_closes_an_offer)


@then('User accepts the offer')
def user_accepts_an_offer(browser):
    try:
        user_accept_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_an_offer)


@then('User accepts half price b1 monthly offer')
def user_accepts_discounted_offer(browser):
    try:
        user_accept_half_price_b1_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_discounted_offer)

# @then('User accepts pending offer')
# def user_accepts_pending_offer(browser):
#     try:
#         user_accept_pending_offer(browser)
#     except (Exception, WebDriverException):
#         bs_fail_with_traceback(browser, user_accepts_pending_offer)

@then('User accepts the downgrade offer')
def user_accepts_downgrade_offer(browser):
    try:
        user_accept_basic_monthly_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_downgrade_offer)


@then('User gets offer Downgrade to Starter Monthly')
def offer_starter_downgrade(browser):
    try:
        user_gets_offer_downgrade_to_starter(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, offer_starter_downgrade)


@then('User gets offer Half Price Starter Annual')
def offer_half_a_price_starter_annual(browser):
    try:
        user_gets_offer_half_a_price_starter_annual(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, offer_half_a_price_starter_annual)


@then('User gets offer Downgrade to Starter or Business Monthly')
def offer_half_a_price_starter_annual(browser):
    try:
        user_gets_offer_downgrade_to_starter_or_business(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, offer_half_a_price_starter_annual)


@then('User gets Special Offer Unlimited 6 Months')
def offer_half_a_price_starter_annual(browser):
    try:
        user_gets_offer_unlimited_6_months(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, offer_half_a_price_starter_annual)


@then('User gets Offer Half Price C1 Monthly')
def offer_half_a_price_starter_monthly(browser):
    try:
        user_gets_offer_half_a_price_1_month(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, offer_half_a_price_starter_monthly)


@then('User accepts Starter offer')
def user_accepts_starter_offer(browser):
    try:
        user_accept_starter_or_business_offer(browser, ACCEPT_OFFER_STARTER)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_starter_offer)


@then('User accepts Basic Offer')
def user_accepts_basic_plan_offer(browser):
    try:
        user_accept_basic_or_standard_offer(browser, ACCEPT_OFFER_BASIC)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_basic_plan_offer)


@then('User accepts Standard Offer')
def user_accepts_standard_plan_offer(browser):
    try:
        user_accept_basic_or_standard_offer(browser, ACCEPT_OFFER_STANDARD)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_standard_plan_offer)


@then('User accepts Business offer')
def user_accepts_business_offer(browser):
    try:
        user_accept_starter_or_business_offer(browser, ACCEPT_OFFER_BUSINESS)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_business_offer)


@then('User gets offer Switch to Business Monthly')
def user_switches_to_business_monthly(browser):
    try:
        user_switches_to_offer_business_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_switches_to_business_monthly)


@then('User gets offer Starter Half a Price Annual')
def user_gets_half_price_annual(browser):
    try:
        user_gets_starter_half_a_price_annual(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_gets_half_price_annual)


@then('User gets offer Downgrade from Annual to Monthly')
def user_get_offer_down_starter_monthly(browser):
    try:
        user_offer_downgrade_annual_to_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_get_offer_down_starter_monthly)


@then('User accepts lite plan offer')
def user_accepts_downgraded_offer(browser):
    try:
        user_accept_lite_plan_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_downgraded_offer)


@then('User accepts basic annual for half price offer')
def user_accepts_half_price_basic_annual(browser):
    try:
        user_accept_half_price_basic_annual_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_half_price_basic_annual)


@then('User accepts basic monthly Offer')
def user_accepts_downgrade_to_basic_monthly_offer(browser):
    try:
        user_accept_downgrade_to_basic_monthly_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_downgrade_to_basic_monthly_offer)


@then('User accepts standard monthly Offer')
def user_accepts_downgrade_to_standard_monthly_offer(browser):
    try:
        user_accept_downgrade_to_standard_monthly_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_downgrade_to_standard_monthly_offer)


@then('User accepts pro monthly Offer')
def user_accepts_downgrade_to_pro_monthly_offer(browser):
    try:
        user_accept_downgrade_to_pro_monthly_offer(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_accepts_downgrade_to_pro_monthly_offer)


@then('User gets offer basic monthly half a price')
def user_get_basic_monthly_for_half_a_price(browser):
    try:
        user_gets_offer_basic_plan_for_half_price(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_get_basic_monthly_for_half_a_price)


@then('User gets offer to switch to light plan monthly')
def user_get_offer_lite_plan_monthly(browser):
    try:
        user_gets_offer_to_switch_to_lite_plan(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_get_offer_lite_plan_monthly)


@then('User gets offer Downgrade to Basic Monthly')
def user_gets_offer_downgrade_to_basic_monthly(browser):
    try:
        user_get_offer_downgrade_to_basic_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_gets_offer_downgrade_to_basic_monthly)


@then('User gets offer half price basic annual')
def user_gets_offer_to_switch_to_half_price_basic_annual(browser):
    try:
        user_gets_offer_basic_annual_for_half_price(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_gets_offer_to_switch_to_half_price_basic_annual)


@then('User gets offer Downgrade to Basic or Standard Monthly')
def user_gets_offer_to_downgrade_to_basic_or_standard_monthly(browser):
    try:
        user_get_offer_to_downgrade_to_basic_or_standard_monthly(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_gets_offer_to_downgrade_to_basic_or_standard_monthly)


@then(parsers.parse('Try to publish and upgrade plan {plan}'))
def change_plan_on_pricing_widget(browser, plan):
    try:
        change_plan_on_publish_pricing(browser, plan)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_plan_on_pricing_widget)


