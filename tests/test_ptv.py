from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException
from helpers.common_helpers import *
from pages.ptv_page import *


@when('I go to PTV landing page')
def navigate_ptv_lp_page(browser):
    try:
        go_to_ptv_lp_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, navigate_ptv_lp_page)


@then('I click create a new video')
def ptv_click_new_video(browser):
    try:
        ptv_click_new_video_btn(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, ptv_click_new_video)


@then('I choose a PTV template')
def choose_ptv_template(browser):
    try:
        choose_a_ptv_template(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, choose_ptv_template)


@then('I choose uploaded image')
def choose_ptv_image(browser):
    try:
        choose_a_ptv_image(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, choose_ptv_image)


@then('I publish a PTV or Shopify video')
def publish_ptv_video(browser):
    try:
        publish_a_ptv_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_ptv_video)


@then('I verify socials PTV')
def verify_socials(browser):
    try:
        ptv_verify_socials(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser,verify_socials)


@then('I publish PTV post on FB')
def publish_ptv_video_on_fb(browser):
    try:
        publish_a_ptv_video_on_fb(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_ptv_video_on_fb)


@then('I go to PTV or Shopify My published videos')
def go_to_ptv_published(browser):
    try:
        go_to_ptv_published_videos(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_to_ptv_published)


@then('I delete last published video')
def delete_last_published_video(browser):
    try:
        delete_ptv_last_published_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, delete_last_published_video)


@when('I go back from PTV to Promo')
def go_back_ptv_to_promo(browser):
    try:
        go_back_from_ptv_to_promo(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_back_ptv_to_promo)