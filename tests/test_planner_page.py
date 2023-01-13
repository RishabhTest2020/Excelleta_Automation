from pytest_bdd import when, then, given
from selenium.common.exceptions import WebDriverException
from pages.planner_page import *
from pages.publisher_page import *


@then('User cleaned all scheduled posts')
def clean_scheduled_posts(browser):
    try:
        clean_up_scheduled_posts(browser, 2)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, clean_scheduled_posts)


@then('User cleaned scheduled posts YT and LI')
def clean_scheduled_posts(browser):
    try:
        clean_up_scheduled_posts(browser, 3)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, clean_scheduled_posts)


@then('I go to My Calendar')
def my_cal_open(browser):
    try:
        go_to_my_cal(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_open)


@then('I open Planner')
def opens_planner(browser):
    try:
        open_planner(browser)
        go_to_my_cal(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, opens_planner)


@then('I verify My Calendar happy path')
def my_cal_happy(browser):
    try:
        my_cal_happy_path(browser, 3)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_happy)


@then('I verify My Calendar issue path')
def my_cal_issue(browser):
    try:
        my_cal_issue_path(browser, '10:00 AM')
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_issue)


@then('I verify My Calendar reschedule path')
def my_cal_edit_path(browser):
    try:
        my_cal_issue_path(browser, '01:00 PM')
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_edit_path)


@then('I verify My Calendar YT and LI')
def my_calen_yt_li(browser):
    try:
        my_cal_yt_li(browser, 1)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_calen_yt_li)


@then('I verify My Calendar YT and LI rescheduled')
def my_cal_yt_li_resched(browser):
    try:
        my_cal_yt_li(browser, 2)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_yt_li_resched)


@then('I verify My Calendar duplication')
def my_cal_post_duplication(browser):
    try:
        my_cal_happy_path(browser, 1)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_post_duplication)


@then('I verify My Calendar duplication from Planner')
def my_cal_post_planner_duplication(browser):
    try:
        my_cal_happy_path(browser, 2)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, my_cal_post_planner_duplication)


@then('I add a new post for today')
def add_new_post_today(browser):
    try:
        add_new_post_from_planner_today(browser)
        verify_fb_publisher(browser)
        post_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_new_post_today)


@then('I add a new post for today and create another post')
def add_new_post_today_create_post(browser):
    try:
        add_new_post_from_planner_today(browser)
        init_disconnect_all_socials(browser)
        connect_with_twit(browser)
        post_video(browser, PUBLISH_CREATE_POST_BTN)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_new_post_today_create_post)


@then('I add a new post for next day')
def add_new_post_tomorrow(browser):
    try:
        add_new_post_from_planner_tomorrow(browser)
        choose_first_social(browser)
        schedule_video_new_post(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_new_post_today)


@then('I duplicate a post from Planner')
def dup_post_planner(browser):
    try:
        create_duplicated_post_from_planner(browser, 0)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, dup_post_planner)


@then('I duplicate a scheduled post from Planner')
def dup_scheduled_post_planner(browser):
    try:
        create_duplicated_post_from_planner(browser, 2)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, dup_scheduled_post_planner)