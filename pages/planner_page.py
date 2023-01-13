import time
from locators.locators_file import *
from helpers.common_helpers import *
from test_data.testdata import *
from pages.pricing_page import *


def open_planner(browser):
    """
    Opens planner page
    """
    do_hover(browser, MY_WORKSPACE_OR_VIDEOS)
    do_click(browser, MY_VIDEOS_PLANNER)


def go_to_my_cal(browser):
    """
    Verifies if we are on My Calendar page
    """
    time.sleep(2)
    get_title = browser.title
    assert get_title == planner_title


def my_cal_happy_path(browser, no_scheduled):
    """
    Verifies My Calendar with scheduled posts
    it should find [no_scheduled] posts
    """
    do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    time.sleep(4)
    scheduled_items = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_posts = len(scheduled_items)
    assert no_of_posts == no_scheduled
    for i in range(no_of_posts):
        is_visible(browser, MY_CAL_1ST_POST_ITEM, 30)
        do_click(browser, MY_CAL_1ST_POST_ITEM, 40)
        is_visible(browser, MY_CAL_DELETE_POST, 30)
        do_click(browser, MY_CAL_DELETE_POST, 20)
        is_visible(browser, MY_CAL_YES_DELETE_BTN, 30)
        do_click(browser, MY_CAL_YES_DELETE_BTN, 20)
    time.sleep(2)
    scheduled_items_del = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_del_posts = len(scheduled_items_del)
    assert no_of_del_posts == 0


def my_cal_issue_path(browser, hour):
    """
    Verifies My Calendar with scheduled or rescheduled posts and correct time
    """
    do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    if hour == '10:00 AM':
        do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    else:
        pass
    time.sleep(2)
    scheduled_items = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_posts = len(scheduled_items)
    assert no_of_posts == 1
    is_visible(browser, MY_CAL_1ST_POST_ITEM_HOUR)
    scheduled_time = get_element_text(browser, MY_CAL_1ST_POST_ITEM_HOUR)
    assert scheduled_time == hour
    do_click(browser, MY_CAL_1ST_POST_ITEM)
    is_visible(browser, MY_CAL_DELETE_POST)
    do_click(browser, MY_CAL_DELETE_POST)
    is_visible(browser, MY_CAL_YES_DELETE_BTN)
    do_click(browser, MY_CAL_YES_DELETE_BTN)
    time.sleep(2)
    scheduled_items_del = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_del_posts = len(scheduled_items_del)
    assert no_of_del_posts == 0


def my_cal_yt_li(browser, no_scheduled):
    """
    Verifies My Calendar with scheduled YT and LI posts (no_scheduled)
    At the end deletes it
    """
    for i in range(3):
        do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    time.sleep(2)
    scheduled_items = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_posts = len(scheduled_items)
    assert no_of_posts == no_scheduled
    for i in range(no_of_posts):
        is_visible(browser, MY_CAL_1ST_POST_ITEM, 20)
        do_click(browser, MY_CAL_1ST_POST_ITEM, 20)
        is_visible(browser, MY_CAL_DELETE_POST, 20)
        do_click(browser, MY_CAL_DELETE_POST, 20)
        is_visible(browser, MY_CAL_YES_DELETE_BTN, 20)
        do_click(browser, MY_CAL_YES_DELETE_BTN, 20)
    time.sleep(2)
    scheduled_items_del = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_del_posts = len(scheduled_items_del)
    assert no_of_del_posts == 0


def edit_or_reschedule_scheduled_post(browser, no_month, icon):
    """
    Clicks on edit icon of chosen, scheduled post
    icon: edit or reschedule icon MY_CAL_EDIT_POST / MY_CAL_RESCHEDULE_POST
    depending on what we want to do
    """
    for i in range(no_month):
        do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    time.sleep(4)
    is_visible(browser, MY_CAL_1ST_POST_ITEM, 20)
    do_click(browser, MY_CAL_1ST_POST_ITEM, 20)
    is_visible(browser, icon, 20)
    do_click(browser, icon, 20)
    title = browser.title
    assert title == publisher_page_title


def clean_up_scheduled_posts(browser, no_month):
    """
    Cleans My Calendar at the beginning
    no_month = 0 - current month, 1 - next etc
    """
    browser.get(my_calendar_url)
    get_title_2 = browser.title
    assert get_title_2 == planner_title
    for i in range(no_month):
        do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    time.sleep(3)
    scheduled_items = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_posts = len(scheduled_items)
    for i in range(no_of_posts):
        is_visible(browser, MY_CAL_1ST_POST_ITEM, 30)
        do_click(browser, MY_CAL_1ST_POST_ITEM, 20)
        is_visible(browser, MY_CAL_DELETE_POST, 20)
        do_click(browser, MY_CAL_DELETE_POST, 20)
        is_visible(browser, MY_CAL_YES_DELETE_BTN, 20)
        do_click(browser, MY_CAL_YES_DELETE_BTN, 20)
    time.sleep(3)
    scheduled_items_del = browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_del_posts = len(scheduled_items_del)
    assert no_of_del_posts == 0


def add_new_post_from_planner_today(browser):
    """
    Clicks on current day New post button
    """
    do_hover(browser, MY_CAL_CURRENT_DAY)
    is_visible(browser, MY_CAL_NEW_POST_ITEM_TODAY)
    do_click(browser, MY_CAL_NEW_POST_ITEM_TODAY)
    is_visible(browser, PUBLISHER_MAIN_HEADER, 10)
    get_title = browser.title
    assert get_title == publisher_page_title


def add_new_post_from_planner_tomorrow(browser):
    """
    Clicks on tomorrow's New post button
    if else - it covers case when current day is a last day of the month
    """
    if is_visible(browser, MY_CAL_TOMORROW_DAY):
        do_hover(browser, MY_CAL_TOMORROW_DAY)
    else:
        do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
        do_hover(browser, MY_CAL_1ST_DAY_OF_MONTH)
    is_visible(browser, MY_CAL_NEW_POST_ITEM_TOMORROW, 5)
    do_click(browser, MY_CAL_NEW_POST_ITEM_TOMORROW)
    is_visible(browser, PUBLISHER_MAIN_HEADER, 10)
    get_title = browser.title
    assert get_title == publisher_page_title


def create_duplicated_post_from_planner(browser, no_month):
    """
    On Planner - hover on a post and duplicate it
    no_month: 0 - current month in Planner, 1 - next month etc
    """
    browser.get(my_calendar_url)
    for i in range(no_month):
        do_click(browser, MY_CAL_NEXT_MONTH_ARROW)
    time.sleep(3)
    is_visible(browser, MY_CAL_1ST_POST_ITEM, 30)
    do_click(browser, MY_CAL_1ST_POST_ITEM, 20)
    is_visible(browser, MY_CAL_DUPLICATE_POST, 20)
    do_click(browser, MY_CAL_DUPLICATE_POST, 20)
