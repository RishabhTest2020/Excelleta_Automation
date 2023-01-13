from locators.mobile_locators import *
from test_data.testdata import *
from helpers.common_helpers import *


def open_planner_mob(mob_browser):
    """
    Opens Planner directly
    """
    mob_browser.get(my_calendar_url)
    get_title = mob_browser.title
    assert get_title == planner_title


def planner_preview_delete_mobile(mob_browser, no_month):
    """
    Preview a scheduled post on mobile and delete it
    no_month = 0 - current month, 1 - next etc
    """
    for i in range(no_month):
        do_click(mob_browser, MY_CAL_NEXT_MONTH_ARROW)
    time.sleep(3)
    is_visible(mob_browser, MY_CAL_1ST_POST_ITEM, 30)
    do_click(mob_browser, MY_CAL_1ST_POST_ITEM, 20)
    desc = get_element_text(mob_browser, POST_DESCRIPTION_MOB)
    assert desc == description_mobile_post
    is_visible(mob_browser, MY_CAL_DELETE_POST, 20)
    do_click(mob_browser, MY_CAL_DELETE_POST, 20)
    is_visible(mob_browser, MY_CAL_YES_DELETE_BTN, 20)
    do_click(mob_browser, MY_CAL_YES_DELETE_BTN, 20)
    time.sleep(3)
    scheduled_items_del = mob_browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_del_posts = len(scheduled_items_del)
    assert no_of_del_posts == 0
