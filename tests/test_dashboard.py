from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException
from pages.dashboard_page import *


@allure.severity(allure.severity_level.NORMAL)
@then('I verify drafted video')
def check_drafted_video(browser):
    try:
        verify_drafted_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_drafted_video)


@allure.severity(allure.severity_level.NORMAL)
@then('I verify draft share buttons')
def check_share_btns(browser):
    try:
        verify_share_btns(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_share_btns)


@then('I publish drafted video')
def publish_draft_video(browser):
    try:
        publish_drafted_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_draft_video)


@then('I delete the project')
def remove_project(browser):
    try:
        delete_drafted_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, remove_project)


@then('Initially I delete the project')
def init_remove_project(browser):
    try:
        initial_delete_drafted_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, init_remove_project)


@then('I go to Dashboard Published Tab')
def go_to_published_tab(browser):
    try:
        open_dashboard_published_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_to_published_tab)


@then('I republish the published video')
def republish_the_video(browser):
    try:
        republish_the_published_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, republish_the_video)