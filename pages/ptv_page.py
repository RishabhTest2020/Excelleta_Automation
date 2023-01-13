from locators.locators_file import *
from locators.facebook_locators import *
from helpers.common_helpers import *
from pages.editor_page import *
from test_data.testdata import *
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time


def go_to_ptv_lp_page(browser):
    """
    Opens PTV landing page
    """
    browser.get(ptv_url)
    is_visible(browser, PTV_H1_TITLE, 10)
    get_title = browser.title
    assert get_title == ptv_lp_title


def ptv_click_new_video_btn(browser):
    """
    Clicks on Create video btn and is redirected to PTV dashboard
    Verify a title
    """
    is_visible(browser, PTV_CREATE_VIDEO_BTN)
    do_click(browser, PTV_CREATE_VIDEO_BTN)
    time.sleep(2)
    is_visible(browser, PTV_MY_VIDEOS_DASHBOARD_TITLE)
    get_title = browser.title
    assert get_title == ptv_dashboard_title


def choose_a_ptv_template(browser, no=1):
    """
    Verifies if there is some templates displayed (more than 2)
    Chooses template and clicks Next
    no (int): which of image to choose (1, 2, 3...), default is 1st
    """
    PTV_TEMPLATE = (By.XPATH, f'(//LI[@class="list-item video-grid-item"])[{no}]')
    is_visible(browser, PTV_CREATE_NEW_BTN)
    do_click(browser, PTV_CREATE_NEW_BTN)
    time.sleep(2)
    all_templates_no = browser.find_elements(PTV_SHOPIFY_TEMPLATES[0], PTV_SHOPIFY_TEMPLATES[1])
    assert len(all_templates_no) > 2
    do_click(browser, PTV_TEMPLATE, 10)
    assert is_visible(browser, PTV_CHECKMARK_ICON_SELECTED) is True
    do_click(browser, PTV_NEXT_BTN)
    assert is_visible(browser, PTV_WIZARD_STEP_2_TITLE) is True


def choose_a_ptv_image(browser, no=1):
    """
    Chooses an uploaded image and is redirected to PTV Editor
    no(int): which of image to choose (1, 2, 3...), default is 1st
    """
    PTV_UPLOADED_IMAGE = (By.XPATH, f'(//DIV[@class ="list-item resource-item"])[{no}]')
    do_click(browser, PTV_UPLOADED_IMAGE)
    assert is_visible(browser, PTV_CHECKMARK_ICON_SELECTED) is True
    do_click(browser, PTV_NEXT_BTN)
    is_visible(browser, PTV_PROJECT_NAME_EDITOR, 15)


def publish_a_ptv_video(browser):
    """
    Clicks on Publish button and verifies redirection to the PTV publish page
    """
    is_visible(browser, PTV_EDITOR_PUBLISH_BTN)
    do_click(browser, PTV_EDITOR_PUBLISH_BTN)
    is_visible(browser, PTV_GENERATION_PROCESS_TITLE, 100)
    time.sleep(4)
    assert is_visible(browser, PTV_PUBLISH_PAGE_SOCIAL_TITLE, 120) is True
    assert is_visible(browser, PTV_PUBLISH_PAGE_TITLE, 10) is True


def ptv_verify_socials(browser):
    """
    Verifies number of options and if FB account is connected
    """
    all_social_options_no = browser.find_elements(PTV_SHOPIFY_SOCIALS[0], PTV_SHOPIFY_SOCIALS[1])
    assert len(all_social_options_no) == 7
    if is_visible(browser, PTV_FB_VICTORIA_CONNECTED) is True:
        pass
    else:
        do_click(browser, PTV_SOCIALS_FB_OPTION2)
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
    fb_user = get_element_text(browser, PTV_SOCIALS_FB_USERNAME)
    assert fb_user == 'Victoria Promoautom'


def publish_a_ptv_video_on_fb(browser):
    """
    Publishes vdeo on Facebook and verify the success popup
    """
    do_click(browser, PTV_SOCIALS_FB_OPTION)
    do_click(browser, PTV_SOCIALS_FB_PUBLISH_TO_PAGE)
    do_click(browser, PTV_SOCIALS_FB_PAGE_ADDED)
    is_visible(browser, PTV_FB_DESCRIPTION_INPUT)
    do_send_keys(browser, PTV_FB_DESCRIPTION_INPUT, 'PTV Social Post')
    do_click(browser, PTV_FB_PUBLISH_POST)
    is_visible(browser, PTV_PUBLISH_SUCCESS_POPUP)
    is_visible(browser, PTV_PUBLISH_SUCCESS_POPUP_TXT)
    success_popup_txt = get_element_text(browser, PTV_PUBLISH_SUCCESS_POPUP_TXT)
    assert success_popup_txt == 'Your video was successfully published to Facebook'
    do_click(browser, PTV_PUBLISH_SUCCESS_POPUP_CLOSE)


def go_to_ptv_published_videos(browser):
    """
    Clicks on PTV header - My Videos
    """
    do_click(browser, PTV_HEADER_MY_VIDEOS)
    is_visible(browser, PTV_MY_VIDEOS_DASHBOARD_TITLE, 15)
    do_click(browser, PTV_NOT_SELECTED_TAB)


def delete_ptv_last_published_video(browser, no=1):
    """
    Deletes last published video
    no: 1 is default for 1st video on the list
    Script compares number of initially existed videos with a number after deletion (expected = 1)
    """
    PTV_DASHBOARD_PROJECT = (By.XPATH, f'(//div[@class="dashboard-grid-item"])[{no}]')
    PTV_3_DOTS = (By.XPATH, f'(//div[@class="menu-button__icon"])[{no}]')
    all_published_no = browser.find_elements(PTV_PUBLISHED_VIDEOS_ALL[0], PTV_PUBLISHED_VIDEOS_ALL[1])
    do_hover(browser, PTV_DASHBOARD_PROJECT)
    do_hover(browser, PTV_3_DOTS)
    do_click(browser, PTV_3_DOTS)
    do_click(browser, PTV_DASHBOARD_DELETE_PROJECT)
    do_click(browser, PTV_POPUP_DELETE_PROJECT_BTN)
    time.sleep(6)
    all_published_no_del = browser.find_elements(PTV_PUBLISHED_VIDEOS_ALL[0], PTV_PUBLISHED_VIDEOS_ALL[1])
    diff_no = len(all_published_no) - len(all_published_no_del)
    assert diff_no == 1


def go_back_from_ptv_to_promo(browser):
    """
    When on PTV dashboard - clicks on Back to Promo
    """
    do_click(browser, PTV_HEADER_BACK_TO_PROMO)









