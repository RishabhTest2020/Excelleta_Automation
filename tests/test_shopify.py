from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException
from helpers.common_helpers import *
from pages.shopify_page import *


@given('User is logged in to Shopify QA Poland Shop')
def login_shopify(browser):
    try:
        login_to_shopify(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, login_shopify)


@given('User is fb logged in to Shopify QA Poland Shop')
def login_fb_shopify(browser):
    try:
        login_fb_to_shopify(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, login_fb_shopify)


@when('User chooses an environment')
def chooses_env_shopify(browser):
    if os.environ['url'] == 'https://promo.com':
        environment = SHOPIFY_ADMIN_APP_PROD
    elif os.environ['url'] == 'https://test01.promo.com':
        environment = SHOPIFY_ADMIN_APP_TEST01
    elif os.environ['url'] == 'https://test02.promo.com':
        environment = SHOPIFY_ADMIN_APP_TEST02
    elif os.environ['url'] == 'https://test03.promo.com':
        environment = SHOPIFY_ADMIN_APP_TEST03
    elif os.environ['url'] == 'https://test04.promo.com':
        environment = SHOPIFY_ADMIN_APP_TEST04
    elif os.environ['url'] == 'https://test05.promo.com':
        environment = SHOPIFY_ADMIN_APP_TEST05
    elif os.environ['url'] == 'https://poland01.promo.com':
        environment = SHOPIFY_ADMIN_APP_POLAND01
    else:
        environment = SHOPIFY_ADMIN_APP_STAGING
    try:
        choose_env_shopify(browser, environment)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, chooses_env_shopify)


@then('User is redirected to the Shop')
def redirect_to_shopify(browser):
    try:
        redirect_shopify(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, redirect_to_shopify)


@then('I click create a new Shopify video')
def shopify_click_new_video(browser):
    try:
        shopify_click_new_video_btn(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, shopify_click_new_video)


@then('I choose a Shopify template')
def choose_shopify_template(browser):
    try:
        choose_a_shopify_template(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, choose_shopify_template)


@then('User cleans all drafts')
def cleans_all_drafts(browser):
    try:
        cleans_all_shopify_drafts(browser, 1)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, cleans_all_drafts)


@then('I verify socials Shopify')
def shop_verify_socials(browser):
    try:
        shopify_verify_socials(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, shop_verify_socials)