from selenium.common.exceptions import WebDriverException
from pages.mob_home_page_login import *
from pages.mob_create_page import *
from pages.mob_planner_page import *
from pages.mob_purchase_page import *
from pages.modheader_page import *
from pytest_bdd import when, then, given
from tests.test_publisher_page import *


@given('Homepage has been opened')
def mob_homepage(mob_browser):
    try:
        home_page_url(mob_browser)
        agree_mob_cookies(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_homepage)


@allure.severity(allure.severity_level.NORMAL)
@given('User is logged in on mobile browser')
def mob_logged_in(mob_browser):
    try:
        click_hamburger_icon(mob_browser)
        login_process(mob_browser, email)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_logged_in)


@given('Linkedin user is logged in on mobile browser')
def li_mob_logged_in(mob_browser):
    try:
        click_hamburger_icon(mob_browser)
        login_process(mob_browser, email_socials)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, li_mob_logged_in)


@when('I click on Start Now')
def start_now(mob_browser):
    try:
        click_start_now(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, start_now)


@then('I log out on mobile')
def log_out_mob(mob_browser):
    try:
        log_out_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, log_out_mob)


@then('I verify redirection to the mobile signup page')
def signup_mob(mob_browser):
    try:
        verify_signup_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, signup_mob)


@allure.severity(allure.severity_level.NORMAL)
@when('I select video and use that')
def select_and_use_video(mob_browser):
    try:
        select_category(mob_browser)
        select_and_use_vid(mob_browser, "fun")
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, select_and_use_video)


@then('I verify open shared link is playing in mobile view')
def check_shared_video(mob_browser, request):
    """
    request: pytest function as an argument to call
    """
    try:
        promo_env = os.environ['url'].split('/')[2].split('.')[0]
        share_link = request.config.cache.get(f'shared{promo_env}', None)
        open_shared_video(mob_browser, share_link)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, check_shared_video)


@then('I go to Planner on mobile')
def open_planner_mobile(mob_browser):
    """
    Opens a Planner in mobile view
    """
    try:
        open_planner_mob(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, open_planner_mobile)


@then('I preview and delete a scheduled LI post')
def planner_prev_del_mob(mob_browser):
    """
    Preview a scheduled post and deletes it on mobile view
    """
    try:
        planner_preview_delete_mobile(mob_browser, 3)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, planner_prev_del_mob)


@when('I click on Try for free')
def mob_try_free(mob_browser):
    try:
        click_try_free(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_try_free)


@when('I open a hamburger menu')
def mob_hamb_menu(mob_browser):
    try:
        click_hamburger_icon(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_hamb_menu)


@when('I open a social calendar on mobile')
def mob_social_cal(mob_browser):
    try:
        open_social_cal_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_social_cal)


@when('I open pricing page on mobile')
def mob_pricing(mob_browser):
    try:
        open_pricing_on_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_pricing)


@then('I sign up on mobile')
def mob_signup(mob_browser):
    try:
        signup_flow_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_signup)


@then('I purchase a plan on mobile')
def mob_purchase_plan(mob_browser):
    try:
        purchase_a_plan_on_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_purchase_plan)


@then('I delete account on mobile')
def mob_delete_account(mob_browser):
    try:
        delete_account_mobile(mob_browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(mob_browser, mob_delete_account)