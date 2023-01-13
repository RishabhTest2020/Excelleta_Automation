import time
from locators.locators_file import *
from locators.facebook_locators import *
from helpers.common_helpers import *
from test_data.testdata import *
from pages.pricing_page import *
import pdb


# helpers

def discard_post(browser, post):
    """
    Discards a post draft in Publisher
    post - int (post number), 0 - 1st post, 1 - 2nd post etc.
    """
    DISCARD_POST = (By.XPATH, f'//BUTTON[@data-qaid="pub-discard-post-{post}"]')
    do_click(browser, DISCARD_POST)
    do_click(browser, DISCARD_POST_POPUP_BTN)


def connect_tt_from_popup(browser):
    """
    Connects Twitter from popup
    Mainly - to reuse
    """
    do_click(browser, PUB_TWIT_PLATFORM)
    connect_with_twit(browser)


# specific functions
def add_video_to_post(browser):
    """
    Adds video to post when there is no video
    """
    if is_visible(browser, ADD_VIDEO_TO_POST) is True:
        do_click(browser, ADD_VIDEO_TO_POST)
        do_click(browser, ADD_VIDEO_POP_UP_PUBLISHER_SELECT)
        assert is_visible(browser, ADD_VIDEO_TO_POST) is False
    else:
        pass


def click_publish_btn(browser, status, button):
    """
    Clicks on Publish button
    status: expected status - Ready to schedule / Ready to publish
    depending on the chosen flow
    button: clicks PUBLISH_VIEW_PLANNER_BTN or PUBLISH_CREATE_POST_BTN
    depending on the chosen flow
    """
    if status == publish_status:
        if is_visible(browser, PUBLISH_POST_NOW) is True:
            assert is_visible(browser, PUBLISH_POST_NOW_CHECKED) is True
        else:
            pass
    else:
        if is_visible(browser, SCHEDULE_POST_FOR_LATER) is True:
            assert is_visible(browser, SCHEDULE_POST_FOR_LATER_CHECKED) is True
        else:
            pass
    do_click(browser, PUBLISH_POST_BTN)
    is_visible(browser, PUBLISH_REVIEW_H1, 10)
    assert is_visible(browser, PUBLISH_READY_MARK) is True
    publish_ready = get_element_text(browser, PUBLISH_READY_MARK)
    assert publish_ready == status
    do_click(browser, FINAL_PUBLISH_POST_BTN)
    assert is_visible(browser, VIDEO_POSTED, 80) is True
    do_click(browser, button, 30)


def post_video(browser, button=PUBLISH_VIEW_PLANNER_BTN):
    """
    Perform: Post video on social platforms
    Adds caption to the post
    button: clicks PUBLISH_VIEW_PLANNER_BTN or PUBLISH_CREATE_POST_BTN
    depending on the chosen flow, default is PUBLISH_VIEW_PLANNER_BTN
    """
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_FOR_FB_POST, description_text_publisher)
    fb_post_text = get_element_text(browser, ADD_TEXT_FOR_FB_POST)
    assert fb_post_text == description_text_publisher
    time.sleep(2)
    click_publish_btn(browser, publish_status, button)


def init_disconnect_all_socials(browser):
    """
    Disconnects all socials connected to Publisher
    """
    account_dropdowns = browser.find_elements(By.XPATH, FB_PUB_ACCOUNTS_DETAILS_DROPDOWN[1])
    account_dropdowns_len = len(account_dropdowns)
    for a in range(account_dropdowns_len):
        do_hover(browser, FB_PUB_ACCOUNTS_DETAILS_DROPDOWN)
        do_click(browser, FB_PUB_ACCOUNTS_REMOVE)
        do_click(browser, PUB_ACCOUNTS_DISCONNECT)
        time.sleep(2)


def verify_fb_publisher(browser):
    """
    Perform: Publisher test for Facebook
    as well as deletes the existing social accounts at the first phase
    """
    is_visible(browser, PUBLISH_TO_SOCIAL)
    wait_for_ajax(browser)
    try:
        do_click(browser, PUBLISH_TO_SOCIAL)
    except WebDriverException:
        time.sleep(2)
        try:
            do_click(browser, PUBLISH_TO_SOCIAL)
        except WebDriverException:
            pass
    if is_visible(browser, FB_CONNECT_BTN, 10) is False:
        init_disconnect_all_socials(browser)
        do_click(browser, FB_CONNECT_BTN)
    else:
        do_click(browser, FB_CONNECT_BTN)
    if is_visible(browser, FB_ACCEPT_ALL_COOKIES) is True:
        do_click(browser, FB_ACCEPT_ALL_COOKIES)
    else:
        pass
    do_send_keys(browser, FB_EMAIL_INPUT, email)
    do_send_keys(browser, FB_PASS_INPUT, read_creds(password, 2))
    try:
        do_click(browser, FB_LOGIN_BTN)
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        if is_visible(browser, COOKIES_ALLOW) is True:
            do_click(browser, COOKIES_ALLOW)
            try:
                do_click(browser, FB_LOGIN_BTN)
            except (NoSuchElementException, TimeoutException):
                pass
        pass
    if is_visible(browser, FB_CONTINUE_AS_VICTORIA_SHORT):
        do_click(browser, FB_CONTINUE_AS_VICTORIA_SHORT)
    else:
        pass
    # added twice because FB shows is twice sometimes
    for i in range(2):
        if is_visible(browser, FB_CONTINUE_BTN_ON_APP_REQUEST):
            do_click(browser, FB_CONTINUE_BTN_ON_APP_REQUEST)
        else:
            pass
    is_visible(browser, FB_SELECT_PAGE_POP_UP)
    is_visible(browser, FB_SELECT_PAGE)
    do_click(browser, FB_SELECT_PAGE)
    is_clickable(browser, FB_PAGE_SELECT_BTN)
    do_click(browser, FB_PAGE_SELECT_BTN)
    time.sleep(4)
    title = browser.title
    assert title == publisher_page_title


def connect_with_ig(browser):
    """
    Perform: Publisher test for Instagram
    """
    if is_visible(browser, PUBLISH_TO_SOCIAL):
        do_click(browser, PUBLISH_TO_SOCIAL)
    else:
        pass
    is_visible(browser, PUB_IG_PLATFORM, 15)
    do_click(browser, PUB_IG_PLATFORM)
    is_visible(browser, APPLY_BRAND_POP_UP_CTN_BTN)
    do_click(browser, APPLY_BRAND_POP_UP_CTN_BTN)
    time.sleep(2)
    if is_visible(browser, FB_PASS_INPUT2) is True:
        do_send_keys(browser, FB_PASS_INPUT2, read_creds(password, 2), 15)
        try:
            do_click(browser, FB_CONNECT_BTN)
        except TimeoutException:
            pass
    else:
        pass
    is_visible(browser, FB_CONTINUE_AS_VICTORIA, 15)
    do_click(browser, LOGIN_ANOTHER_ACCOUNT)
    time.sleep(2)
    do_clear(browser, FB_EMAIL_INPUT)
    do_send_keys(browser, FB_EMAIL_INPUT, ig_email)
    do_send_keys(browser, FB_PASS_INPUT, read_creds(password, 3), 15)
    try:
        do_click(browser, FB_LOGIN_BTN)
    except TimeoutException:
        pass
    time.sleep(2)
    is_visible(browser, FB_CONTINUE_AS_KASIA, 15)
    do_click(browser, FB_CONTINUE_AS_KASIA)
    time.sleep(4)
    if is_visible(browser, IG_PUB_ACCOUNT, 20):
        pass
    else:
        do_click(browser, IG_BUSINESS_POPUP_ALL_ASSETS)
        do_click(browser, IG_BUSINESS_POPUP_NEXT_BTN)
        time.sleep(1)
        do_click(browser, IG_BUSINESS_POPUP_ALL_ASSETS)
        do_click(browser, IG_BUSINESS_POPUP_NEXT_BTN)
        do_click(browser, IG_BUSINESS_POPUP_DONE_BTN)
        do_click(browser, IG_BUSINESS_POPUP_OK_BTN)
    do_click(browser, IG_PUB_ACCOUNT)
    is_clickable(browser, FB_PAGE_SELECT_BTN)
    do_click(browser, FB_PAGE_SELECT_BTN)


def connect_with_li(browser):
    """
    Perform: Publisher test for LinkedIn
    Connects both: private account and organization page
    to_improve: Currently not in use - blocked by captcha
    """
    is_visible(browser, PUB_LI_PLATFORM, 15)
    do_click(browser, PUB_LI_PLATFORM)
    time.sleep(2)
    is_visible(browser, LI_EMAIL_TXT)
    do_send_keys(browser, LI_EMAIL_TXT, li_email)
    do_send_keys(browser, LI_PASS_TXT, read_creds(password, 3), 15)
    do_click(browser, LI_SIGN_IN_BTN)
    if is_visible(browser, LI_ALLOW_BTN) is True:
        do_click(browser, LI_ALLOW_BTN)
    else:
        pass
    is_visible(browser, LI_CHOOSE_PRIV_ACCOUNT_CHECKBX)
    do_click(browser, LI_CHOOSE_PRIV_ACCOUNT_CHECKBX)
    is_visible(browser, LI_CHOOSE_PAGE_CHECKBX)
    do_click(browser, LI_CHOOSE_PAGE_CHECKBX)
    is_clickable(browser, FB_PAGE_SELECT_BTN)
    do_click(browser, FB_PAGE_SELECT_BTN)
    time.sleep(4)
    title = browser.title
    assert title == publisher_page_title
    time.sleep(4)


def connect_with_twit(browser):
    """
    Perform: Publisher test for twitter
    """
    try:
        do_click(browser, PUB_TWIT_PLATFORM)
    except:
        pass
    if is_visible(browser, TW_CONNECT_BTN):
        do_click(browser, TW_CONNECT_BTN)
    else:
        pass
    time.sleep(2)
    is_visible(browser, TWIT_EMAIL_TXT)
    do_send_keys(browser, TWIT_EMAIL_TXT, twit_email)
    do_send_keys(browser, TWIT_PASS_TXT, read_creds(password, 3))
    try:
        do_click(browser, TWIT_AUTHIRIZE_BTN)
    except TimeoutException:
        pass
    if is_visible(browser, TWIT_CHALLENGE) is True:
        do_send_keys(browser, TWIT_CHALLENGE, read_creds(password, 4))
        try:
            do_click(browser, TWIT_CHALLENGE_SUBMIT)
        except (TimeoutException, ElementClickInterceptedException):
            pass
        if is_visible(browser, TWIT_AUTHIRIZE_APP) is True:
            do_click(browser, TWIT_AUTHIRIZE_APP)
        else:
            pass
        time.sleep(4)
    else:
        pass
    if is_visible(browser, TWIT_NEW_POPUP_LOGIN_INPUT) is True:
        do_send_keys(browser, TWIT_NEW_POPUP_LOGIN_INPUT, twit_email)
        do_click(browser, TWIT_NEXT_BTN)
        do_send_keys(browser, TWIT_NEW_POPUP_LOGIN_INPUT, twit_username)
        do_click(browser, TWIT_NEXT_BTN)
        do_send_keys(browser, TWIT_NEW_POPUP_PASS_INPUT, read_creds(password, 3))
        if is_visible(browser, TWIT_NEW_LOGIN_BTN) is True:
            do_click(browser, TWIT_NEW_LOGIN_BTN)
        else:
            pass
        if is_visible(browser, TWIT_AUTHIRIZE_APP) is True:
            do_click(browser, TWIT_AUTHIRIZE_APP)
        else:
            pass
    else:
        pass


def return_to_publisher_main_page(browser):
    """
    Verifies number of connected socials - for old tid
    For new tid 60620221 - verifies if we are on My Calendar Page
    to_improve: change if condition when COR1-3916 is Done
    """
    time.sleep(2)
    title = browser.title
    if title == publisher_page_title:
        pass
    else:
        assert title == planner_title
        browser.get(publisher_url_new_post)


def verify_if_planner_is_opened(browser):
    """
    Verifies if we are on My Calendar Page after publish
    """
    time.sleep(5)
    title = browser.title
    assert title == planner_title


def click_schedule_a_post(browser):
    """
    Click on Publish and verify the status of scheduled post
    """
    do_click(browser, PUBLISH_POST_BTN)
    is_visible(browser, PUBLISH_REVIEW_H1, 10)
    assert is_visible(browser, PUBLISH_READY_MARK) is True
    do_click(browser, FINAL_PUBLISH_POST_BTN)
    assert is_visible(browser, VIDEO_POSTED, 60) is True
    scheduled_text = get_element_text(browser, PUBLISH_SUMMARY_1ST_POSTED_ITEM_STATUS)
    assert scheduled_text == "Scheduled"
    do_click(browser, PUBLISH_VIEW_PLANNER_BTN)


def schedule_video(browser):
    """
    Perform: Schedule video on social platforms
    Adds caption to the post
    """
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_FOR_FB_POST, description_text_scheduler)
    post_text = get_element_text(browser, ADD_TEXT_FOR_FB_POST)
    assert post_text == description_text_scheduler
    time.sleep(2)
    is_visible(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, SCHEDULE_CALENDAR_ICON)
    do_click(browser, DATE_PICKER_NEXT_MONTH_ARROW)
    do_click(browser, DATE_PICKER_NEXT_MONTH_ARROW)
    do_click(browser, DATE_PICKER_1ST_DAY_OF_MONTH)
    assert is_visible(browser, DATE_PICKER_1ST_DAY_OF_MONTH_SELECTED) is True
    do_click(browser, DATE_PICKER_SET_TIME_DROPDOWN)
    do_click(browser, DATE_PICKER_CHOOSE_TIME_10AM)
    do_click(browser, DATE_PICKER_SCHEDULE_BTN)
    click_schedule_a_post(browser)


def schedule_video_new_post(browser):
    """
    Perform: Schedule video on social platforms created using New post btn
    Adds caption to the post
    """
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_FOR_FB_POST, 'Promo Social Schedule Testing New Post')
    post_text = get_element_text(browser, ADD_TEXT_FOR_FB_POST)
    assert post_text == 'Promo Social Schedule Testing New Post'
    time.sleep(2)
    is_visible(browser, SCHEDULE_POST_FOR_LATER)
    hour = get_element_text(browser, SCHEDULE_POST_FOR_LATER_DATE)
    assert ("12:00" in hour) is True
    click_schedule_a_post(browser)


def schedule_review_publish_flow(browser):
    """
    Covers steps from clicking on Publish button to Done button
    Used in: schedule_edited_post and reschedule_scheduled_post
    """
    do_click(browser, PUBLISH_POST_BTN)
    is_visible(browser, PUBLISH_REVIEW_H1, 10)
    assert is_visible(browser, PUBLISH_READY_MARK) is True
    ready_schedule = get_element_text(browser, PUBLISH_READY_MARK)
    assert ready_schedule == schedule_status
    do_click(browser, FINAL_PUBLISH_POST_BTN)
    assert is_visible(browser, VIDEO_POSTED, 60) is True
    scheduled_text = get_element_text(browser, PUBLISH_SUMMARY_1ST_POSTED_ITEM_STATUS)
    assert scheduled_text == "Scheduled"
    do_click(browser, PUBLISH_VIEW_PLANNER_BTN)


def schedule_edited_post(browser):
    """
    User has returned to Publisher
    User edit a post (changes a text)
    """
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_FOR_FB_POST, ' EDITED')
    post_text = get_element_text(browser, ADD_TEXT_FOR_FB_POST)
    assert post_text == 'Promo Social Schedule Testing EDITED'
    time.sleep(2)
    is_visible(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, SCHEDULE_CALENDAR_ICON)
    assert is_visible(browser, DATE_PICKER_1ST_DAY_OF_MONTH_SELECTED) is True
    do_click(browser, DATE_PICKER_SCHEDULE_BTN)
    schedule_review_publish_flow(browser)


def reschedule_scheduled_post(browser):
    """
    User has returned to Publisher
    User edit a post (changes date and time)
    """
    time.sleep(2)
    assert is_visible(browser, DATE_PICKER_1ST_DAY_OF_MONTH_SELECTED) is True
    do_click(browser, DATE_PICKER_2ND_DAY_OF_MONTH)
    do_click(browser, DATE_PICKER_SET_TIME_DROPDOWN)
    do_click(browser, DATE_PICKER_CHOOSE_TIME_1PM)
    do_click(browser, DATE_PICKER_SCHEDULE_BTN)
    do_click(browser, SCHEDULE_POST_FOR_LATER)
    schedule_review_publish_flow(browser)


def schedule_to_past_date(browser):
    """
    Perform: Schedule video to past date
    Result: not possible
    # to_improve: when bug COR1-4013 is fixed, cover it here - last 2 lines to removal
    """
    verify_fb_publisher(browser)
    time.sleep(2)
    is_visible(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, SCHEDULE_CALENDAR_ICON)
    assert is_visible(browser, DATE_PICKER_PREV_MONTH_DISABLED_ARROW) is True
    do_click(browser, DATE_PICKER_CANCEL_BTN)
    do_click(browser, SCHEDULE_POST_FOR_LATER)
    do_click(browser, DATE_PICKER_CANCEL_BTN)
    do_click(browser, PUBLISH_POST_NOW)


def publish_empty(browser):
    """
    Tries to publish post without any video
    """
    verify_fb_publisher(browser)
    time.sleep(2)
    if is_visible(browser, PUBLISHER_REMOVE_VIDEO) is True:
        do_click(browser, PUBLISHER_REMOVE_VIDEO)
        assert is_visible(browser, ADD_VIDEO_TO_POST) is True
    else:
        pass
    do_click(browser, PUBLISH_POST_BTN)
    is_visible(browser, PUBLISH_REVIEW_H1, 10)
    status = get_element_text(browser, PUBLISH_REVIEW_TITLE)
    assert status == 'No Video Selected'
    do_click(browser, PUBLISH_REVIEW_BACK_TO_EDIT)


def add_drafts_connected_accounts(browser):
    """
    For YT and LinkedIn only
    (accounts always connected to promo.test.automation+socials@gmail.com)
    Add drafts of posts to Publisher
    """
    do_click(browser, PUBLISH_TO_SOCIAL)
    do_click(browser, MAIN_PUBLISHER_PG_2ND_SOCIAL_BTN)
    do_click(browser, ADD_MULTIPLE_POSTS)
    do_click(browser, MAIN_PUBLISHER_PG_1ST_SOCIAL_BTN)
    do_click(browser, ADD_MULTIPLE_POSTS)
    do_click(browser, MAIN_PUBLISHER_PG_3RD_SOCIAL_BTN)


def add_draft_connected_linkedin(browser):
    """
    Add a LinkedIn draft with already connected private account
    (account always connected to promo.test.automation+socials@gmail.com)
    """
    do_click(browser, PUBLISH_TO_SOCIAL)
    do_click(browser, MAIN_PUBLISHER_PG_2ND_SOCIAL_BTN)


def go_back_to_publish_page(browser):
    """
    Verifies going back from Publisher to Publish Page and again returns to the Publisher
    """
    do_click(browser, PUBLISH_TO_SOCIAL_BACK)
    do_click(browser, SOCIAL_BACK_LEAVE)
    assert is_visible(browser, PUBLISH_TO_SOCIAL) is True
    do_click(browser, PUBLISH_TO_SOCIAL, 20)
    get_title = browser.title
    assert get_title == publish_page_title
    do_click(browser, MAIN_PUBLISHER_PG_1ST_SOCIAL_BTN)


def publish_and_schedule_posts(browser):
    """
    Publishes one post and schedules another
    """
    # to_improve: when bug COR1-4013 is fixed, cover it here
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_TO_1ST_POST, 'Promo Social Schedule and Publish Testing Facebook')
    post_text = get_element_text(browser, ADD_TEXT_TO_1ST_POST)
    assert post_text == 'Promo Social Schedule and Publish Testing Facebook'
    do_click(browser, ADD_MULTIPLE_POSTS)
    do_click(browser, PUB_TWIT_PLATFORM)
    connect_with_twit(browser)
    do_send_keys(browser, ADD_TEXT_TO_1ST_POST, 'Promo Social Schedule and Publish Testing Twitter')
    post_text2 = get_element_text(browser, ADD_TEXT_FOR_FB_POST)
    assert post_text2 == 'Promo Social Schedule and Publish Testing Twitter'
    time.sleep(2)
    schedule_ready_draft(browser, 1)
    click_publish_btn(browser, schedule_status, PUBLISH_VIEW_PLANNER_BTN)


def schedule_ready_draft(browser, param):
    """
    Schedule drafts: 1st day of next+3 month, 10:00 AM
    param: number of posts do you want to schedule
    to_improve: when COR1-4076 is fixed, remove if part
    """
    if is_visible(browser, PUBLISHER_FIRST_AVATAR) is True:
        for c in range(2):
            do_click(browser, PUBLISHER_FIRST_AVATAR)
    else:
        pass
    for i in range(param):
        no = i+1
        is_visible(browser, (By.XPATH, f'(//INPUT[@data-qaid="radio-button-schedule"])[{no}]'))
        do_click(browser, (By.XPATH, f'(//INPUT[@data-qaid="radio-button-schedule"])[{no}]'), 10)
        if is_visible(browser, DATE_PICKER_WHOLE_COMPONENT) is True:
            pass
        else:
            do_click(browser, (By.XPATH, f'(//INPUT[@data-qaid="radio-button-schedule"])[{no}]'), 10)
        if is_visible(browser, DATE_PICKER_1ST_DAY_OF_MONTH_SELECTED) is True:
            mon = 2
        else:
            mon = 3
        for m in range(mon):
            do_click(browser, DATE_PICKER_NEXT_MONTH_ARROW)
        do_click(browser, DATE_PICKER_1ST_DAY_OF_MONTH)
        do_click(browser, DATE_PICKER_SET_TIME_DROPDOWN)
        do_click(browser, DATE_PICKER_CHOOSE_TIME_10AM)
        do_click(browser, DATE_PICKER_SCHEDULE_BTN)


def publish_and_schedule_posts_yt_li(browser):
    """
    Publishes one post and schedules another to YT and LI
    Social account are always connected, this test doesn't cover the connection flow
    """
    # to_improve: when bug COR1-4013 is fixed, cover it here
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_TO_1ST_POST, 'Promo Social Schedule and Publish Testing YT and LinkedIn 1')
    post_text = get_element_text(browser, ADD_TEXT_TO_1ST_POST)
    assert post_text == 'Promo Social Schedule and Publish Testing YT and LinkedIn 1'
    do_send_keys(browser, ADD_TEXT_TO_YT_DESCRIPTION, 'Promo Social Schedule and Publish Testing YT')
    post_text2 = get_element_text(browser, ADD_TEXT_TO_YT_DESCRIPTION)
    assert post_text2 == 'Promo Social Schedule and Publish Testing YT'
    time.sleep(2)
    schedule_ready_draft(browser, 1)
    click_publish_btn(browser, schedule_status, PUBLISH_VIEW_PLANNER_BTN)


def schedule_posts_yt_and_li(browser):
    """
    Discard one of LI posts, schedule one YT post and one LI post
    """
    time.sleep(2)
    discard_post(browser, 0)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_TO_YT_DESCRIPTION, 'Promo Social Schedule Testing YT')
    post_text2 = get_element_text(browser, ADD_TEXT_TO_YT_DESCRIPTION)
    assert post_text2 == 'Promo Social Schedule Testing YT'
    do_send_keys(browser, ADD_TEXT_TO_3RD_POST, 'Promo Social Schedule Testing LinkedIn')
    post_text = get_element_text(browser, ADD_TEXT_TO_3RD_POST)
    assert post_text == 'Promo Social Schedule Testing LinkedIn'
    time.sleep(2)
    schedule_ready_draft(browser, 2)
    click_publish_btn(browser, schedule_status, PUBLISH_VIEW_PLANNER_BTN)


def schedule_post_li(browser):
    """
    Schedule one LI post
    """
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_TO_1ST_POST, 'Promo Social Mobile View Testing')
    post_text = get_element_text(browser, ADD_TEXT_TO_1ST_POST)
    assert post_text == description_mobile_post
    schedule_ready_draft(browser, 1)
    click_publish_btn(browser, schedule_status, PUBLISH_VIEW_PLANNER_BTN)


def choose_first_social(browser):
    """
    Clicks on first social from the list - Publisher main page
    "if" related to Verify a new post button
    """
    if is_visible(browser, MAIN_PUBLISHER_PG_1ST_SOCIAL_BTN):
        do_click(browser, MAIN_PUBLISHER_PG_1ST_SOCIAL_BTN)
    else:
        pass


def create_fb_post_draft(browser):
    """
    Connects to FB and create FB draft
    """
    verify_fb_publisher(browser)
    time.sleep(2)
    add_video_to_post(browser)
    do_send_keys(browser, ADD_TEXT_TO_1ST_POST, 'Social Duplicated Post')
    post_text = get_element_text(browser, ADD_TEXT_TO_1ST_POST)
    assert post_text == 'Social Duplicated Post'
    schedule_ready_draft(browser, 1)


def duplicate_first_post(browser):
    """
    Clicks on duplicate icon and verify if pop-up is displayed
    """
    do_click(browser, DUPLICATE_1ST_POST_ICON)
    assert is_visible(browser, PUB_TWIT_PLATFORM, 10) is True
    connect_tt_from_popup(browser)
    post_text1 = get_element_text(browser, ADD_TEXT_TO_1ST_POST)
    post_text2 = get_element_text(browser, ADD_TEXT_TO_2ND_POST)
    assert post_text1 == 'Social Duplicated Post'
    assert post_text2 == 'Social Duplicated Post'
    assert is_visible(browser, SCHEDULE_POST_FOR_LATER_1) is True
    assert is_visible(browser, SCHEDULE_POST_FOR_LATER_2) is True


def publish_duplicated_post(browser):
    """
    Publishes duplicated post
    """
    click_publish_btn(browser, schedule_status, PUBLISH_VIEW_PLANNER_BTN)


def publish_duplicated_post_from_planner(browser, status, description):
    """
    Publishes duplicate post from Planner
    Checks if duplicated draft has relevant description (possible only for scheduled)
    """
    if is_visible(browser, MAIN_PUBLISHER_PG_1ST_SOCIAL_BTN):
        do_click(browser, MAIN_PUBLISHER_PG_1ST_SOCIAL_BTN)
    else:
        pass
    if status == schedule_status:
        post_text = get_element_text(browser, ADD_TEXT_TO_1ST_POST)
        assert post_text == description
    else:
        pass


