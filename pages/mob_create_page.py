from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from locators.mobile_locators import *
from test_data.testdata import *
from helpers.common_helpers import *


def click_start_now(mob_browser):
    """
    Clicks on "Start now" button on mobile
    """
    time.sleep(3)
    is_visible(mob_browser, START_NOW_BTN, 10)
    do_click(mob_browser, START_NOW_BTN, 20)


def select_category(mob_browser):
    """
    Selects a video category on mobile
    """
    is_visible(mob_browser, SELECT_HEALTH_BTN, 10)
    do_click(mob_browser, SELECT_HEALTH_BTN, 5)


def select_and_use_vid(mob_browser, keyword: str):
    """
    Selects a video by searching a keyword and triggers sending an e-mail with a magic link
    Args:
        mob_browser: browser
        keyword: chosen keyword for video search
    """
    try:
        is_visible(mob_browser, SELECT_VID_BTN, 10)
        do_click(mob_browser, SELECT_VID_BTN, 5)
        time.sleep(3)
    except TimeoutException:
        is_visible(mob_browser, SEARCH_BOX_DUMMY, 10)
        do_send_keys(mob_browser, SEARCH_BOX_DUMMY, Keys.ENTER, 10)
        is_visible(mob_browser, SEARCH_ICON_SUBMIT_BTN, 10)
        do_click(mob_browser, SEARCH_ICON_SUBMIT_BTN, 10)
        is_visible(mob_browser, SEARCH_BOX, 10)
        do_send_keys(mob_browser, SEARCH_BOX, keyword, 10)
        do_click(mob_browser, SEARCH_SUBMIT_BTN, 10)
        is_visible(mob_browser, SELECT_VID_BTN)
        do_click(mob_browser, SELECT_VID_BTN)
    is_visible(mob_browser, USE_THIS_VID_BTN, 10)
    do_click(mob_browser, USE_THIS_VID_BTN, 5)
    time.sleep(2)
    assert is_visible(mob_browser, THANK_YOU_GIF) is True


def open_shared_video(mob_browser, link):
    """
    link: url to open
    open shared link in mobile view
    """
    if os.environ['url'] == 'https://promo.com':
        tabs = mob_browser.window_handles[1]
        mob_browser.switch_to.window(tabs)
    else:
        pass
    mob_browser.get(link)
    time.sleep(3)
    assert is_visible(mob_browser, SHARED_VIDEO, 15) is True

