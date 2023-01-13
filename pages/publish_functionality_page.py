import platform
import time
from cgitb import text

import pytest
from dateutil.tz import gettz
from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException

from helpers.get_emails import getEmails
from pages.editor_page import *


def verify_embed_functionality(browser):
    """
    Check embed functionality of publish page
    """
    if is_visible(browser, EMBED, 10) is False:
        window_after = browser.window_handles[0]
        browser.switch_to.window(window_after)
        time.sleep(2)
    else:
        pass
    do_click(browser, EMBED, 10)
    do_click(browser, EMBED_DROPDOWN_OPTION, 10)
    time.sleep(1)
    is_visible(browser, AUTOPLAY_CHECK_BOX, 10)
    do_click(browser, AUTOPLAY_CHECK_BOX, 10)
    is_visible(browser, LOOP_CHECKBOX, 10)
    do_click(browser, LOOP_CHECKBOX, 10)
    time.sleep(2)
    assert is_visible(browser, COPY_TO_CLIPBOARD, 10) is True
    do_click(browser, COPY_TO_CLIPBOARD, 10)
    time.sleep(1)
    browser.execute_script("window.open('');")
    time.sleep(2)
    window_before = browser.window_handles[2]
    browser.switch_to.window(window_before)
    browser.get(JSfiddle)
    do_click(browser, JS_FIDDLE_HTML_INPUT, 30)
    time.sleep(2)
    keyboard_action = ActionChains(browser)
    if (platform.system() == 'Windows' and os.environ['browser'] == 'browserstack') is True:
        keyboard_action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
    elif (platform.system() == 'Windows' and os.environ['browser'] == 'chrome') is True:
        keyboard_action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    else:
        keyboard_action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
    time.sleep(5)
    do_click(browser, JS_FIDDLE_RUN_BTN, 10)
    switch_to_iframe(browser, JS_FIDDLE_IFRAME, 10)
    assert is_visible(browser, HTML_VIEWER_PROMO_VIDEO, 50) is True
    browser.switch_to.default_content()
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    if (os.environ['url'] != 'https://promo.com' and test_name ==
        'test_new_user_purchases_a_plan_and_verify_download_functionality_in_publish_page') is True:
        window_before = browser.window_handles[0]
        browser.switch_to.window(window_before)
    else:
        window_before = browser.window_handles[1]
        browser.switch_to.window(window_before)
    do_click(browser, CLOSE_BUTTON)


def download_video_functionality(browser):
    """
    Check download video functionality of publish page
    """
    is_visible(browser, DOWNLOAD_PUBLISHED_VIDEO, 10)
    do_click(browser, DOWNLOAD_PUBLISHED_VIDEO, 10)
    is_visible(browser, DOWNLOAD_HD_VIDEO, 10)
    do_click(browser, DOWNLOAD_HD_VIDEO, 10)
    time.sleep(5)
    browser.execute_script("window.open('');")
    time.sleep(1)
    window_after = browser.window_handles[2]
    browser.switch_to.window(window_after)
    browser.get(chrome_downloads)


def download_image_functionality(browser):
    """
    Check photo download functionality of publish page
    """
    if is_visible(browser, DOWNLOAD_IMAGE, 10) is False:
        window_after = browser.window_handles[0]
        browser.switch_to.window(window_after)
        time.sleep(2)
    else:
        pass
    do_click(browser, DOWNLOAD_IMAGE, 10)
    is_visible(browser, DOWNLOAD_JPEG_IMAGE, 10)
    do_click(browser, DOWNLOAD_JPEG_IMAGE, 10)
    time.sleep(2)
    is_visible(browser, EXPORT_PHOTO_BUTTON, 20)
    do_click(browser, EXPORT_PHOTO_BUTTON, 10)
    time.sleep(2)
    do_click(browser, IMAGE_EXPORT_POPUP_CLOSE, 20)
    time.sleep(5)
    window_after = browser.window_handles[2]
    browser.switch_to.window(window_after)


def download_gif_image_functionality(browser):
    """
    Check gif functionality of publish page
    """
    if is_visible(browser, DOWNLOAD_IMAGE, 10) is False:
        window_after = browser.window_handles[0]
        browser.switch_to.window(window_after)
        time.sleep(2)
    else:
        pass
    do_click(browser, DOWNLOAD_IMAGE, 10)
    is_visible(browser, DOWNLOAD_GIF_IMAGE, 10)
    do_click(browser, DOWNLOAD_GIF_IMAGE, 10)
    time.sleep(2)
    is_visible(browser, EXPORT_GIF_BUTTON, 20)
    do_click(browser, EXPORT_GIF_BUTTON, 10)
    time.sleep(2)
    do_click(browser, IMAGE_EXPORT_POPUP_CLOSE, 20)
    time.sleep(5)
    window_after = browser.window_handles[2]
    browser.switch_to.window(window_after)


def downloaded(browser, search_downloaded):
    """
    Returns: Boolean of downloaded stuff present or not
    """
    elem = False
    try:
        elem = browser.page_source.find(search_downloaded)
    except (WebDriverException, Exception):
        return bool(elem)
    return bool(elem)


def verify_download_functionality(browser, search_downloaded):
    """
    search_downloaded: Value of downloaded stuff format and check presence explicitly
    """
    start_time = time.time()
    while time.time() <= start_time + 200:
        time.sleep(5)
        if downloaded(browser, search_downloaded) is True:
            assert browser.page_source.find(search_downloaded)
            window_before = browser.window_handles[1]
            browser.switch_to.window(window_before)
            break


def change_aspect_ratio(browser):
    """
    aspect_ratio: to change aspect ratio to square,vertical or wide as per the user.
    """
    assert is_visible(browser, EDIT_VIDEO, 10) is True
    unrendered_aspect_ratios = browser.find_elements(By.XPATH, PUBLISHED_ASPECT_RATIOS[1])
    len_unrendered_aspect_ratios = len(unrendered_aspect_ratios)
    for i in range(len_unrendered_aspect_ratios):
        unrendered_aspect_ratios2 = browser.find_elements(By.XPATH,  PUBLISHED_ASPECT_RATIOS[1])
        unrendered_aspect_ratios2[0].click()
        is_visible(browser, SAVE_AND_PREVIEW_BTN, 20)
        do_click(browser, SAVE_AND_PREVIEW_BTN, 20)
        is_visible(browser, PUBLISH_READY, 380)
        get_title = browser.title
        assert get_title == publish_page_title
        unrendered_aspect_ratios3 = browser.find_elements(By.XPATH,  PUBLISHED_ASPECT_RATIOS[1])
        assert len(unrendered_aspect_ratios3) == len(unrendered_aspect_ratios) - (i+1)


def signin_to_dropbox(browser, email, password):
    """
    Args:
        browser:
        email: dropbox email
        password: dropbox pass

    Returns: login into dropbox

    """
    is_visible(browser, DROPBOX_EMAIL, 10)
    do_send_keys(browser, DROPBOX_EMAIL, email)
    is_visible(browser, DROPBOX_PASSWORD, 10)
    do_send_keys(browser, DROPBOX_PASSWORD, password)
    if is_visible(browser, DROPBOX_OTP_ENTER, 40) is True:
        pass
    else:
        if is_visible(browser, DROPBOX_EMAIL_ERROR) is True:
            do_send_keys(browser, DROPBOX_EMAIL, email)
            if is_visible(browser, DROPBOX_OTP_ENTER, 30) is True:
                pass
            else:
                try:
                    do_click(browser, DROPBOX_SIGNIN_BTN)
                except (TimeoutException, ElementClickInterceptedException):
                    pass


def signin_to_hubspot(browser, email, password):
    """
    Args:
        browser:
        email: hubspot email
        password: hubspot pass

    Returns: login into hubspot

    """
    is_visible(browser, HUBSPOT_EMAIL_TXT, 10)
    do_send_keys(browser, HUBSPOT_EMAIL_TXT, email)
    is_visible(browser, HUBSPOT_PASS_TXT, 10)
    do_send_keys(browser, HUBSPOT_PASS_TXT, password)
    if is_clickable(browser, HUBSPOT_SIGNIN_BTN) is True:
        do_click(browser, HUBSPOT_SIGNIN_BTN, 10)
    else:
        do_send_keys(browser, HUBSPOT_EMAIL_TXT, email)
        do_click(browser, HUBSPOT_SIGNIN_BTN, 10)


def signin_to_wistia(browser, email, password):
    """
    Args:
        browser:
        email: wistia email
        password: wistia pass

    Returns: login into wistia

    """
    try:
        is_visible(browser, WISTIA_EMAIL, 10)
        do_send_keys(browser, WISTIA_EMAIL, email)
        is_visible(browser, WISTIA_PASS, 10)
        time.sleep(1)
        do_send_keys(browser, WISTIA_PASS, password)
        do_click(browser, WISTIA_SIGNIN_BTN, 10)
    except:
        pass
    if is_visible(browser, WISTIA_AUTHORIZE, 10) is True:
        do_click(browser, WISTIA_AUTHORIZE)
    else:
        pass


def delete_wistia_videos(browser):
    """
    Returns: login into wistia and delete all projects
    """
    browser.execute_script("window.open('');")
    time.sleep(1)
    try:
        window_before = browser.window_handles[4]
    except IndexError:
        window_before = browser.window_handles[3]
    browser.switch_to.window(window_before)
    browser.get(wistia_login_url)
    signin_to_wistia(browser, drop_box_email, read_creds(password, 6).capitalize().strip("\n"))
    if is_visible(browser, WISTIA_POP_UP_CLOSE, 10) is True:
        do_click(browser, WISTIA_POP_UP_CLOSE)
    else:
        pass
    if is_visible(browser, WISTIA_VIDEOS) is True:
        wistia_videos = browser.find_elements(By.XPATH, WISTIA_VIDEOS[1])
        for i in range(len(wistia_videos)):
            do_hover(browser, WISTIA_VIDEOS)
            do_click(browser, WISTIA_VIDEOS_DEL)
            time.sleep(1)
            do_click(browser, WISTIA_VIDEOS_DEL_CONF)
            time.sleep(1)
    else:
        pass
    window_before = browser.window_handles[1]
    browser.switch_to.window(window_before)
    if browser.title != publish_page_title:
        window_before = browser.window_handles[0]
        browser.switch_to.window(window_before)
    else:
        pass


def upload_video_to_drive(browser, choose_drive):
    """

    Args:
        browser:
        choose_drive: online drives names

    Returns: upload promo project to chosen drive

    """

    try:
        if is_visible(browser, UPLOAD_TO_BTN, 10) is True:
            do_click(browser, UPLOAD_TO_BTN, 10)
    except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
        browser.refresh()
        time.sleep(2)
        do_click(browser, UPLOAD_TO_BTN, 10)
    selected_drive = choose_drive.strip('\"')
    if selected_drive == 'dropbox':
        if is_visible(browser, DROPBOX_CONNECT_BTN, 10) is False:
            do_click(browser, DROPBOX_DISCONNECT_BTN)
            do_click(browser, DROPBOX_CONNECT_BTN, 10)
        else:
            do_click(browser, DROPBOX_CONNECT_BTN, 10)
            time.sleep(2)
        signin_to_dropbox(browser, drop_box_email, read_creds(password, 6))
        current_time = str(datetime.now(gettz('America/New_York'))).split(".")[0].split(" ")[1]
        today_date = str(datetime.now(gettz('America/New_York')).strftime("%d-%b-%Y")).lstrip("0")
        start_time = time.time()
        if is_visible(browser, DROPBOX_OTP_ENTER, 20) is True:
            sender, subject, body, otp = getEmails(selected_drive, current_time, today_date, start_time)
            if otp == 'OTP not received':
                skip_test(browser, 'Dropbox otp not received')
            else:
                try:
                    do_send_keys(browser, DROPBOX_OTP_FIELD, otp)
                except TimeoutException:
                    skip_test(browser, 'Dropbox otp not received')
                do_click(browser, DROPBOX_OTP_ENTER)
        elif is_title_true(browser, publish_page_title, 10) is True:
            do_click(browser, UPLOAD_TO_BTN, 10)
            time.sleep(2)
            assert is_visible(browser, DROPBOX_UPLOAD_FILE_ICON, 10) is True
            do_click(browser, DROPBOX_UPLOAD_FILE_ICON, 10)
            if is_visible(browser, DROPBOX_FOLDER) is True:
                folder = get_element_text(browser, DROPBOX_FOLDER)
                assert folder == './Promo.com'
            else:
                do_click(browser, DROPBOX_FOLDER_PROMO)
            do_click(browser, FILE_UPLOAD_BTN)
            assert is_visible(browser, FILE_UPLOADED, 60) is True
            do_click(browser, UPLOAD_DONE_BTN)
        else:
            if is_visible(browser, DROPBOX_CAPTCHA_IFRAME, 30) is True:
                skip_test(browser, 'captcha appeared in the middle')
            else:
                skip_test(browser, 'Something new appeared in between dropbox flow')
    elif selected_drive == 'hubspot':
        if is_visible(browser, HUBSPOT_CONNECT_BTN, 10) is False:
            do_click(browser, HUBSPOT_DISCONNECT_BTN, 10)
            do_click(browser, HUBSPOT_CONNECT_BTN, 10)
        else:
            is_visible(browser, HUBSPOT_CONNECT_BTN, 10)
            do_click(browser, HUBSPOT_CONNECT_BTN, 10)
        current_time = str(datetime.now(gettz('America/New_York'))).split(".")[0].split(" ")[1]
        today_date = str(datetime.now(gettz('America/New_York')).strftime("%d-%b-%Y")).lstrip("0")
        signin_to_hubspot(browser, hubspot_email, read_creds(password, 6).capitalize().strip("\n"))
        start_time = time.time()
        if is_visible(browser, HUBSPOT_OTP_FIELD, 20) is True:
            do_click(browser, HUBSPOT_OTP_FIELD)
            sender, subject, body, otp = getEmails(selected_drive, current_time, today_date, start_time)
            if otp == 'OTP not received':
                skip_test(browser, 'HubSpot otp not received')
            else:
                do_send_keys(browser, HUBSPOT_OTP_FIELD, otp)
                if is_visible(browser, HUBSPOT_LOGIN_BTN) is True:
                    do_click(browser, HUBSPOT_LOGIN_BTN)
                is_visible(browser, CHOOSE_HUBSPOT_RADIO_BTN, 20)
                do_click(browser, CHOOSE_HUBSPOT_RADIO_BTN)
                do_click(browser, CHOOSE_ACCOUNT_BTN)
                if is_visible(browser, HUBSPOT_CONNECT_APP, 15) is True:
                    do_click(browser, HUBSPOT_CONNECT_APP)
        else:
            is_visible(browser, CHOOSE_HUBSPOT_RADIO_BTN, 20)
            do_click(browser, CHOOSE_HUBSPOT_RADIO_BTN, 20)
            do_click(browser, CHOOSE_ACCOUNT_BTN, 20)
        start_time = time.time()
        while time.time() <= start_time + 60:
            time.sleep(2)
            if browser.title == publish_page_title:
                break
        do_click(browser, UPLOAD_TO_BTN, 10)
        do_click(browser, HUBSPOT_UPLOAD_FILE_ICON, 10)
        assert is_visible(browser, HUBSPOT_FILE_UPLOADED, 30) is True
    elif selected_drive == 'wistia':
        delete_wistia_videos(browser)
        if is_visible(browser, WISTIA_CONNECT_BTN, 10) is False:
            do_click(browser, WISTIA_DISCONNECT)
            do_click(browser, WISTIA_CONNECT_BTN, 10)
        else:
            do_click(browser, WISTIA_CONNECT_BTN, 10)
            time.sleep(2)
        signin_to_wistia(browser, drop_box_email, read_creds(password, 6).capitalize().strip("\n"))
        start_time = time.time()
        while time.time() <= start_time + 100:
            time.sleep(2)
            if browser.title == publish_page_title:
                break
        do_click(browser, UPLOAD_TO_BTN, 10)
        time.sleep(2)
        assert is_visible(browser, WISTIA_UPLOAD_FILE_ICON, 10) is True
        do_click(browser, WISTIA_UPLOAD_FILE_ICON, 10)
        assert is_visible(browser, WISTIA_FILE_UPLOADED, 60) is True
    elif selected_drive == 'googledrive':
        if is_visible(browser, GOOGLEDRIVE_CONNECT_BTN, 10) is False:
            do_click(browser, GOOGLEDRIVE_DISCONNECT)
            do_click(browser, GOOGLEDRIVE_CONNECT_BTN, 10)
        else:
            is_visible(browser, GOOGLEDRIVE_CONNECT_BTN, 10)
            do_click(browser, GOOGLEDRIVE_CONNECT_BTN, 10)
    else:
        print('No upload type selected')
        pass


def get_share_link(browser):
    """
    Args:
        browser:

    Returns: video share link from publish page
    """
    do_click(browser, EMBED, 10)
    do_click(browser, COPY_LINK_OPTION, 10)
    share_link = get_element_text(browser, GET_LINK)
    return share_link
