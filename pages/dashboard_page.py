import time

from selenium.common.exceptions import TimeoutException
from helpers.common_helpers import *
from test_data.testdata import *
from locators.locators_file import *


def verify_drafted_video(browser):
    """
    Verifies drafted video name
    """
    draft_name = get_element_text(browser, DRAFTED_VIDEO_NAME)
    assert draft_name == drafted_video_name
    # allure_screenshot(browser)


def verify_share_btns(browser):
    """
    Verifies that share buttons exist and are visible
    """
    is_visible(browser, DRAFT_SHARE_BTN, 10)
    do_click(browser, DRAFT_SHARE_BTN)
    # allure_screenshot(browser)
    assert is_visible(browser, FACEBOOK_SHARE_BTN) is True
    assert is_visible(browser, FBMESSENGER_SHARE_BTN) is True
    assert is_visible(browser, TWITTER_SHARE_BTN) is True
    assert is_visible(browser, WHATSAPP_SHARE_BTN) is True
    assert is_visible(browser, LINKDIN_SHARE_BTN) is True
    assert is_visible(browser, EMAIL_SHARE_BTN) is True
    assert is_visible(browser, COPY_LINK_BTN) is True
    is_visible(browser, SHARE_CROSS_BTN)
    do_click(browser, SHARE_CROSS_BTN)


def publish_drafted_video(browser):
    """
    Publishes drafted video from dashboard
    """
    is_visible(browser, DRAFT_PUBLISH_BTN, 10)
    do_click(browser, DRAFT_PUBLISH_BTN)
    if is_visible(browser, PUBLISH_READY, 180) is True or is_visible(browser, CREATE_POST_BTN, 180) is True:
        get_title = browser.title
        assert get_title == publish_page_title
    else:
        if is_visible(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN) is True:
            do_click(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN)
        else:
            do_click(browser, VIDEO_IS_READY_CONTINUE_BTN)
        try:
            is_visible(browser, PRICING_TEXT, 10)
            pricing = get_element_text(browser, PRICING_TEXT)
            assert pricing == pricing_page_main_text
        except (TimeoutException, NoSuchElementException) as PT:
            pass


def delete_drafted_video(browser):
    """
    Deletes drafted video from dashboard
    """
    while is_visible(browser, DRAFTED_VIDEO_NAME) is True:
        do_hover(browser, DELETE_DRAFT_VIDEO)
        time.sleep(1)
        do_click(browser, DELETE_DRAFT_VIDEO)
        is_visible(browser, DELETE_PROJECT_BTN)
        time.sleep(1)
        do_click(browser, DELETE_PROJECT_BTN)
    assert is_visible(browser, DRAFTED_VIDEO_NAME) is False


def initial_delete_drafted_video(browser):
    """
    Deletes drafted video from dashboard at the beginning of the test
    """
    if is_visible(browser, DRAFTED_VIDEO_NAME) is True:
        do_hover(browser, DRAFT_HOVER)
        time.sleep(1)
        do_click(browser, DELETE_DRAFT_VIDEO)
        is_visible(browser, DELETE_PROJECT_BTN)
        time.sleep(1)
        do_click(browser, DELETE_PROJECT_BTN)
        try:
            assert is_visible(browser, DRAFTED_VIDEO_NAME) is False
        except AssertionError:
            while is_visible(browser, DRAFTED_VIDEO_NAME) is True:
                time.sleep(1)
                do_hover(browser, DRAFT_HOVER)
                time.sleep(1)
                if is_visible(browser, DELETE_DRAFT_VIDEO) is False:
                    break
                do_click(browser, DELETE_DRAFT_VIDEO)
                is_visible(browser, DELETE_PROJECT_BTN)
                time.sleep(1)
                do_click(browser, DELETE_PROJECT_BTN)
                browser.refresh()
                time.sleep(4)
            else:
                pass
    else:
        pass


def open_dashboard_published_tab(browser):
    """
    Opens Dashboard - Published Tab from main menu
    """
    is_visible(browser, MY_WORKSPACE_OR_VIDEOS)
    do_hover(browser, MY_WORKSPACE_OR_VIDEOS)
    time.sleep(4)
    do_click(browser, MY_VIDEOS_PUBLISHED)


def republish_the_published_video(browser):
    """
    Republish already published video from Dashboard
    """
    is_visible(browser, REPUBLISH_BUTTON)
    do_click(browser, REPUBLISH_BUTTON)
