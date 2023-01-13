import os

from pytest_bdd import when, then, given, parsers
from selenium.common.exceptions import WebDriverException
from pages.publisher_page import *
from pages.publish_functionality_page import *
from pages.planner_page import *
from pages.home_page_login import *


@then('I verify FB publisher')
def fb_publisher(browser):
    try:
        verify_fb_publisher(browser)
        post_video(browser)
        return_to_publisher_main_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, fb_publisher)


@then('I verify IG publisher')
def ig_publisher(browser):
    try:
        connect_with_ig(browser)
        post_video(browser)
        return_to_publisher_main_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, ig_publisher)


@then('I connect and schedule TT publisher')
def tt_connect(browser):
    try:
        is_visible(browser, PUBLISH_TO_SOCIAL)
        do_click(browser, PUBLISH_TO_SOCIAL)
        connect_with_twit(browser)
        schedule_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, tt_connect)


@then('I verify LI publisher')
def li_publisher(browser):
    try:
        connect_with_li(browser)
        post_video(browser)
        return_to_publisher_main_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, li_publisher)


@then('I connect tt account from popup')
def connect_tt_popup(browser):
    try:
        connect_tt_from_popup(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, connect_tt_popup)


# note: TWIT step should be always the last one in scenario because it verifies no of connected accounts
@then('I verify TWIT publisher')
def twit_publisher(browser):
    try:
        connect_with_twit(browser)
        post_video(browser)
        verify_if_planner_is_opened(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, twit_publisher)


@then('I schedule a FB post')
def schedule_fb(browser):
    try:
        verify_fb_publisher(browser)
        schedule_video(browser)
        return_to_publisher_main_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_fb)


@then('I schedule a IG post')
def schedule_ig(browser):
    try:
        connect_with_ig(browser)
        schedule_video(browser)
        return_to_publisher_main_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_ig)


@then('I schedule a TWIT post')
def schedule_tt(browser):
    try:
        connect_with_twit(browser)
        schedule_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_tt)


@then('I publish and schedule two posts')
def publish_and_schedule(browser):
    try:
        publish_and_schedule_posts(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_and_schedule)


@then('I publish and schedule YT and LI posts')
def publish_and_schedule_yt_li(browser):
    try:
        publish_and_schedule_posts_yt_li(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_and_schedule_yt_li)


@then('I schedule YT and LI posts')
def schedule_yt_li(browser):
    try:
        schedule_posts_yt_and_li(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_yt_li)


@then('I schedule a LI post')
def schedule_li(browser):
    try:
        schedule_post_li(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_li)


@then('I reschedule YT or LI post')
def reschedule_post_yt_li(browser):
    try:
        edit_or_reschedule_scheduled_post(browser, 3, MY_CAL_RESCHEDULE_POST)
        reschedule_scheduled_post(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, reschedule_post_yt_li)


@then('I schedule to past date')
# to_improve: uncomment it when COR1-4074 is fixed
def schedule_past_date(browser):
    try:
        schedule_to_past_date(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_past_date)


@then('I publish empty post')
def schedule_empty_post(browser):
    try:
        publish_empty(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_empty_post)


@then('I create fb draft')
def create_fb_drafts(browser):
    try:
        create_fb_post_draft(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, create_fb_drafts)


@then('I duplicate first post and delete second')
def duplicate_post(browser):
    try:
        duplicate_first_post(browser)
        discard_post(browser, 1)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, duplicate_post)


@then('I publish duplicated post')
def publish_dup_posts(browser):
    try:
        publish_duplicated_post(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_dup_posts)


@then('I publish a post duplicated from Planner')
def publish_dup_post_from_planner(browser):
    try:
        publish_duplicated_post_from_planner(browser, publish_status, description_text_publisher)
        click_publish_btn(browser, publish_status, PUBLISH_VIEW_PLANNER_BTN)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_dup_post_from_planner)


@then('I publish a scheduled post duplicated from Planner')
def publish_dup_sched_post_from_planner(browser):
    try:
        publish_duplicated_post_from_planner(browser, schedule_status, description_text_scheduler)
        click_publish_btn(browser, schedule_status, PUBLISH_VIEW_PLANNER_BTN)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_dup_sched_post_from_planner)


@then('I add drafts YT and LI')
def add_drafts_yt_li(browser):
    try:
        add_drafts_connected_accounts(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_drafts_yt_li)


@then('I add draft LI')
def add_draft_li(browser):
    try:
        add_draft_connected_linkedin(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_draft_li)


@then('I schedule a post and edit it')
def schedule_edit_post(browser):
    try:
        verify_fb_publisher(browser)
        schedule_video(browser)
        edit_or_reschedule_scheduled_post(browser, 2, MY_CAL_EDIT_POST)
        schedule_edited_post(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, schedule_edit_post)


@then('I reschedule a post')
def reschedule_post(browser):
    try:
        edit_or_reschedule_scheduled_post(browser, 2, MY_CAL_RESCHEDULE_POST)
        reschedule_scheduled_post(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, reschedule_post)


@then('I go back to Publish Page')
def go_back_publish_page(browser):
    try:
        go_back_to_publish_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_back_publish_page)


# PUBLISH FUNCTIONALITY
@then('I verify embed functionality')
def step_def_verify_embed_functionality(browser):
    try:
        verify_embed_functionality(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_def_verify_embed_functionality)


@when('I am using download video functionality')
def step_def_video_download_functionality(browser):
    try:
        download_video_functionality(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_def_video_download_functionality)


@when('I am using download JPEG image functionality')
def step_def_jpeg_image_download_functionality(browser):
    try:
        download_image_functionality(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_def_jpeg_image_download_functionality)


@when('I am using download GIF image functionality')
def step_def_jpeg_image_download_functionality(browser):
    try:
        download_gif_image_functionality(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_def_jpeg_image_download_functionality)


@then(parsers.parse('verify download functionality for {search_downloaded}'))
def step_def_verify_gif_download_functionality(browser, search_downloaded):
    try:
        verify_download_functionality(browser, search_downloaded)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, step_def_verify_gif_download_functionality)


@when('I check the aspect ratio functionalities')
def user_changes_aspect_ratio(browser):
    try:
        change_aspect_ratio(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, user_changes_aspect_ratio)


@when(parsers.parse('I use upload functionality with {choose_drive}'))
def upload_video_functionality(browser, choose_drive):
    try:
        upload_video_to_drive(browser, choose_drive)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, upload_video_functionality)


@given('User is logged in with shorter new auth socials')
def logged_in_new_shorter_social(browser):
    try:
        go_to_url(browser, login_url)
        try:
            enter_email_new(browser, email_socials)
        except (NoSuchElementException, TimeoutException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email_socials)
        enter_password_new(browser, read_creds(password, 0))
        click_login_new(browser)
        time.sleep(12)
        try:
            check_correct_username(browser)
        except (AssertionError, TimeoutException, NoSuchElementException):
            go_to_url(browser, login_url)
            time.sleep(2)
            enter_email_new(browser, email_socials)
            enter_password_new(browser, read_creds(password, 0))
            click_login_new(browser)
            time.sleep(12)
            check_correct_username(browser)
        time.sleep(1)
        create_page_redirection(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logged_in_new_shorter_social)


@then('I copy video share link')
def copy_share_link(browser, request):
    """
    Args:
        browser:
        request: pytest function as an argument to call
    """
    try:
        promo_env = os.environ['url'].split('/')[2].split('.')[0]
        share_link = get_share_link(browser)
        request.config.cache.set(f'shared{promo_env}', share_link)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, copy_share_link)
