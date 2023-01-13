import time
from selenium.webdriver.common.keys import Keys
from helpers.common_helpers import *
from test_data.testdata import *
from locators.locators_file import *


def go_to_create_page(browser):
    """
    Goes to create page - clicks on New Project button
    """
    is_visible(browser, NEW_PROJECT_BTN)
    do_click(browser, NEW_PROJECT_BTN)


def search_video(browser, keyword: str):
    """
    Searches video on Create Page by keyword
    Args:
        browser: webdriver
        keyword (str): chosen search keyword
    """
    is_visible(browser, SEARCH_INPUT_MAIN, 5)
    try:
        do_clear(browser, SEARCH_INPUT_MAIN, 5)
    except NoSuchElementException:
        skip_offer_modal(browser)
        do_clear(browser, SEARCH_INPUT_MAIN, 5)
    do_send_keys(browser, SEARCH_INPUT_MAIN, keyword, 10)
    do_send_keys(browser, SEARCH_INPUT_MAIN, Keys.ENTER, 10)
    footeges_load_start_time = time.time() * 1000
    is_visible(browser, FOOTEGES_CONTAINER, 15)
    footeges_load_end_time = time.time() * 1000
    load_time(footeges_load_end_time, footeges_load_start_time, 'Footeges load time')
    assert is_visible(browser, VIDEOS_ARE_VISIBLE, 20) is True
    # assert_analytics_events(browser, create_page_google_events, create_page_mixpanel_events)


def search_video_new_user(browser, keyword: str):
    """
    Searches video on Create Page by keyword
    Args:
        browser: webdriver
        keyword (str): chosen search keyword
    """
    is_visible(browser, SEARCH_INPUT_MAIN, 5)
    do_clear(browser, SEARCH_INPUT_MAIN, 5)
    do_send_keys(browser, SEARCH_INPUT_MAIN, keyword, 10)
    do_send_keys(browser, SEARCH_INPUT_MAIN, Keys.ENTER, 10)
    time.sleep(5)
    skip_offer_modal(browser)
    assert is_visible(browser, VIDEOS_ARE_VISIBLE, 20)
    if is_visible(browser, RAW_VIDEOS_ARE_VISIBLE):
        assert get_element_text(browser, RAW_VIDEOS_ARE_VISIBLE) == keyword
    else:
        pass


def customize_chosen_template(browser):
    """
    Clicks on Customize button and goes to the Editor
    """
    if is_visible(browser, START_FROM_SCRATCH2) is True:
        start_from_scratch = browser.find_element_by_xpath(START_FROM_SCRATCH2[1])
        browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", start_from_scratch)
        time.sleep(1)
        do_hover(browser, RAW_VIDEO)
        is_visible(browser, USE_BTN)
        do_click(browser, USE_BTN)
    else:
        do_hover(browser, TEMPLATE)
        is_visible(browser, CUSTOMIZE_BTN)
        do_click(browser, CUSTOMIZE_BTN)


def preview_chosen_template(browser):
    """
    Clicks on Preview button, checks preview title and closes a preview
    Covers both Templates and raw videos
    """
    if browser.find_element_by_xpath(TEMPLATES_ARE_VISIBLE[1]).is_displayed():
        do_hover(browser, TEMPLATE, 10)
        is_visible(browser, PREVIEW_BTN, 10)
        do_click(browser, PREVIEW_BTN, 10)
        assert is_visible(browser, PREVIEW_VIDEO_TITLE_TEMPLATE, 10)
    else:
        do_hover(browser, VIDEO, 10)
    is_visible(browser, PREVIEW_BTN, 10)
    do_click(browser, PREVIEW_BTN, 10)
    assert is_visible(browser, PREVIEW_VIDEO_TITLE, 10)
    do_click(browser, PREVIEW_CLOSE_VIDEO, 10)


def check_all_ratios(browser):
    """
    Helper function - it verifies all ratios on preview
    """
    do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
    if is_visible(browser, PREVIEW_RATIO_VERTICAL_SELECTED):
        if is_visible(browser, PREVIEW_RATIO_SQUARE):
            do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
            do_hover(browser, PREVIEW_RATIO_VERTICAL)
            do_hover(browser, PREVIEW_RATIO_SQUARE)
            do_click(browser, PREVIEW_RATIO_SQUARE)
            assert is_visible(browser, PREVIEW_RATIO_SQUARE_SELECTED) is True
        elif is_visible(browser, PREVIEW_RATIO_WIDE):
            do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
            do_hover(browser, PREVIEW_RATIO_VERTICAL)
            do_hover(browser, PREVIEW_RATIO_WIDE)
            do_click(browser, PREVIEW_RATIO_WIDE)
            assert is_visible(browser, PREVIEW_RATIO_WIDE_SELECTED) is True
        else:
            print('Only Vertical Ratio is Available')
    elif is_visible(browser, PREVIEW_RATIO_SQUARE_SELECTED):
        if is_visible(browser, PREVIEW_RATIO_WIDE):
            do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
            do_hover(browser, PREVIEW_RATIO_SQUARE)
            do_hover(browser, PREVIEW_RATIO_WIDE)
            do_click(browser, PREVIEW_RATIO_WIDE)
            assert is_visible(browser, PREVIEW_RATIO_WIDE_SELECTED) is True
        elif is_visible(browser, PREVIEW_RATIO_VERTICAL):
            do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
            do_hover(browser, PREVIEW_RATIO_SQUARE)
            do_hover(browser, PREVIEW_RATIO_VERTICAL)
            do_click(browser, PREVIEW_RATIO_VERTICAL)
            assert is_visible(browser, PREVIEW_RATIO_VERTICAL_SELECTED) is True
        else:
            print('Only Square Ratio is Available')
    else:
        if is_visible(browser, PREVIEW_RATIO_SQUARE):
            do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
            do_hover(browser, PREVIEW_RATIO_WIDE)
            do_hover(browser, PREVIEW_RATIO_SQUARE)
            do_click(browser, PREVIEW_RATIO_SQUARE)
            assert is_visible(browser, PREVIEW_RATIO_SQUARE_SELECTED) is True
        elif is_visible(browser, PREVIEW_RATIO_VERTICAL):
            do_hover(browser, PREVIEW_WRAPPER_WHOLE_VIDEO)
            do_hover(browser, PREVIEW_RATIO_WIDE)
            do_hover(browser, PREVIEW_RATIO_VERTICAL)
            do_click(browser, PREVIEW_RATIO_VERTICAL)
            assert is_visible(browser, PREVIEW_RATIO_VERTICAL_SELECTED) is True
        else:
            print('Only Wide Ratio is Available')


def preview_and_verify_preview_functionalities_template(browser):
    """
    For templates: Clicks on Preview button, checks:
    preview title, available ratios, share button, customize button, next/previous video arrow
    """
    if browser.find_element_by_xpath(TEMPLATES_ARE_VISIBLE[1]).is_displayed():
        do_hover(browser, TEMPLATE, 10)
        is_visible(browser, PREVIEW_BTN, 10)
        do_click(browser, PREVIEW_BTN, 10)
        assert is_visible(browser, PREVIEW_VIDEO_TITLE, 10) is True
        check_all_ratios(browser)
        if is_visible(browser, PREVIEW_SHARE_BTN_SMALL):
            do_click(browser, PREVIEW_SHARE_BTN_SMALL)
            assert is_visible(browser, SHARE_POPUP) is True
            do_click(browser, SHARE_CROSS_BTN)
        else:
            do_click(browser, PREVIEW_SHARE_BTN_BIG)
            assert is_visible(browser, SHARE_POPUP) is True
            do_click(browser, SHARE_CROSS_BTN)
        assert is_visible(browser, PREVIEW_CUSTOMIZE_BTN) is True
        is_visible(browser, PREVIEW_VIDEO_TITLE)
        video_title = get_element_text(browser, PREVIEW_VIDEO_TITLE)
        is_visible(browser, PREVIEW_ARROW_NEXT)
        do_click(browser, PREVIEW_ARROW_NEXT)
        video_title2 = get_element_text(browser, PREVIEW_VIDEO_TITLE)
        assert video_title != video_title2
        is_visible(browser, PREVIEW_ARROW_PREVIOUS)
        do_click(browser, PREVIEW_ARROW_PREVIOUS)
        video_title3 = get_element_text(browser, PREVIEW_VIDEO_TITLE)
        assert video_title == video_title3
        do_click(browser, PREVIEW_CLOSE_VIDEO, 10)
    else:
        print('No template available, running on raw video')
        preview_and_verify_preview_functionalities_template(browser)


def preview_and_verify_preview_functionalities_raw(browser):
    """
    For raw videos: Clicks on Preview button, checks:
    preview title, available ratios, share button, customize button, next video arrow
    """
    do_hover(browser, VIDEO, 10)
    is_visible(browser, PREVIEW_BTN, 10)
    do_click(browser, PREVIEW_BTN, 10)
    assert is_visible(browser, PREVIEW_VIDEO_TITLE, 10)
    check_all_ratios(browser)
    assert is_visible(browser, PREVIEW_USE_BTN) is True
    is_visible(browser, PREVIEW_RAW_TIME_DISPLAY)
    do_click(browser, PREVIEW_CLOSE_VIDEO, 10)


def filter_premium_media(browser, keyword: str):
    """
    Filters premium media on Create Page
    If there is no premiums available, script is looking for another keyword
    Args:
        browser: webdriver
        keyword (str): chosen search keyword
    """
    global no_of_tags
    skip_offer_modal(browser)
    if is_visible(browser, ALL_MEDIA_FILTER_NEW) is True:
        do_hover(browser, ALL_MEDIA_FILTER_NEW)
        premium_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([4]))
        try:
            premium_click.click()
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, ALL_MEDIA_FILTER_NEW)
            premium_click.click()
    else:
        do_hover(browser, ALL_MEDIA_FILTER)
        try:
            do_click(browser, PREMIUM_FILTER)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, ALL_MEDIA_FILTER)
            do_click(browser, PREMIUM_FILTER)
    filtered_videos = browser.find_elements_by_xpath(FILTERED_VIDEOS[1])
    print(len(filtered_videos))
    no_of_videos = len(filtered_videos)
    try:
        if no_of_videos == 0:
            do_clear(browser, SEARCH_INPUT_MAIN, 5)
            do_send_keys(browser, SEARCH_INPUT_MAIN, keyword, 10)
            do_send_keys(browser, SEARCH_INPUT_MAIN, Keys.ENTER, 10)
        else:
            premium_tags = browser.find_elements_by_xpath(PREMIUM_TAGS[1])
            print(len(premium_tags))
            no_of_tags = len(premium_tags)
            assert no_of_videos == no_of_tags
            # allure_screenshot(browser)
    except AssertionError:
        print('Test Failed coz:' + str(no_of_videos) + 'and' + str(no_of_tags) + 'is not equal')
        pass


def filter_editorial_media(browser, keyword: str):
    """
    Filters editorial media on Create Page
    If there is no editorial available, script is looking for another keyword
    Args:
        browser: webdriver
        keyword (str): chosen search keyword
    """
    global no_of_tags
    if is_visible(browser, VIDEOS_PHOTOS_DROPDOWN) is True:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
        try:
            do_click(browser, DROPDOWN_SELECT_VIDEOS)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
            do_click(browser, DROPDOWN_SELECT_VIDEOS)
    else:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
        try:
            do_click(browser, DROPDOWN_SELECT_VIDEOS_OLD)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
            do_click(browser, DROPDOWN_SELECT_VIDEOS_OLD)
    if is_visible(browser, EDITORIAL_MEDIA_FILTER_NEW) is True:
        do_hover(browser, EDITORIAL_MEDIA_FILTER_NEW)
        pass
    elif is_visible(browser, ALL_MEDIA_FILTER_NEW) is True:
        do_hover(browser, ALL_MEDIA_FILTER_NEW)
        editorial_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([5]))
        try:
            editorial_click.click()
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, ALL_MEDIA_FILTER_NEW)
            editorial_click.click()
    else:
        do_hover(browser, ALL_MEDIA_FILTER)
        try:
            do_click(browser, EDITORIAL_FILTER)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, ALL_MEDIA_FILTER)
            do_click(browser, EDITORIAL_FILTER)
    if is_visible(browser, SORTING_FILTER2) is True:
        do_hover(browser, SORTING_FILTER2)
        sort_click = browser.find_element_by_xpath(SORT_DROPDOWN2[1] + str([3]) + '/div' + str([3]))
        try:
            sort_click.click()
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, SORTING_FILTER2)
            sort_click.click()
    elif is_visible(browser, SORTING_FILTER) is True:
        do_hover(browser, SORTING_FILTER)
        sort_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([3]))
        try:
            sort_click.click()
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, SORTING_FILTER)
            sort_click.click()
    else:
        do_hover(browser, SORTING_FILTER_OLD)
        try:
            do_click(browser, SORTING_OPTIONS['Newest'])
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, SORTING_FILTER_OLD)
            do_click(browser, SORTING_OPTIONS['Newest'])
    filtered_videos = browser.find_elements_by_xpath(FILTERED_VIDEOS[1])
    print(len(filtered_videos))
    no_of_videos = len(filtered_videos)
    try:
        if no_of_videos == 0:
            do_clear(browser, SEARCH_INPUT_MAIN, 5)
            do_send_keys(browser, SEARCH_INPUT_MAIN, keyword, 10)
            do_send_keys(browser, SEARCH_INPUT_MAIN, Keys.ENTER, 10)
        else:
            editorial_tags = browser.find_elements_by_xpath(EDITORIAL_TAGS[1])
            print(len(editorial_tags))
            no_of_tags = len(editorial_tags)
            assert no_of_videos == no_of_tags
            # allure_screenshot(browser)
    except AssertionError:
        print('Test Failed coz:' + str(no_of_videos) + 'and' + str(no_of_tags) + 'is not equal')
        pass


def filter_editorial_media_photos(browser, keyword: str):
    """
    Filters editorial media photos on Create Page
    If there is no editorial available, script is looking for another keyword
    Args:
        browser: webdriver
        keyword (str): chosen search keyword
    """
    global no_of_tags
    skip_offer_modal(browser)
    time.sleep(1)
    if is_visible(browser, VIDEOS_PHOTOS_DROPDOWN) is True:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
        try:
            do_click(browser, DROPDOWN_SELECT_PHOTOS)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
            do_click(browser, DROPDOWN_SELECT_PHOTOS)
    else:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
        try:
            do_click(browser, DROPDOWN_SELECT_PHOTOS_OLD)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
            do_click(browser, DROPDOWN_SELECT_PHOTOS_OLD)
    if is_visible(browser, PHOTOS_ALL_MEDIA_FILTER_NEW) is True:
        do_hover(browser, PHOTOS_ALL_MEDIA_FILTER_NEW)
        editorial_click = browser.find_element_by_xpath(SORT_DROPDOWN2[1] + str([4]) + '/div' + str([5]))
        try:
            editorial_click.click()
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, PHOTOS_ALL_MEDIA_FILTER_NEW)
            editorial_click.click()
    else:
        do_hover(browser, PHOTOS_ALL_MEDIA_FILTER)
        try:
            do_click(browser, PHOTOS_EDITORIAL_FILTER)
        except ElementClickInterceptedException:
            time.sleep(4)
            do_hover(browser, PHOTOS_ALL_MEDIA_FILTER)
            do_click(browser, PHOTOS_EDITORIAL_FILTER)
    filtered_videos = browser.find_elements_by_xpath(FILTERED_PHOTOS[1])
    print(len(filtered_videos))
    no_of_videos = len(filtered_videos)
    try:
        if no_of_videos == 0:
            do_clear(browser, SEARCH_INPUT_MAIN, 5)
            do_send_keys(browser, SEARCH_INPUT_MAIN, keyword, 10)
            do_send_keys(browser, SEARCH_INPUT_MAIN, Keys.ENTER, 10)
        else:
            editorial_tags = browser.find_elements_by_xpath(PHOTOS_EDITORIAL_TAGS[1])
            print(len(editorial_tags))
            no_of_tags = len(editorial_tags)
            assert no_of_videos == no_of_tags
            # allure_screenshot(browser)
    except AssertionError:
        print('Test Failed coz:' + str(no_of_videos) + 'and' + str(no_of_tags) + 'is not equal')
        pass


def verify_sorting(browser):
    """
    Verify the sorting on create page
    """
    if is_visible(browser, ALL_MEDIA_FILTER_NEW) is True:
        for sort_index in (3, 2, 1):
            do_hover(browser, SORTING_FILTER2)
            sort_click = browser.find_element_by_xpath(SORT_DROPDOWN2[1] + str([3]) + '/div' + str([sort_index]))
            try:
                sort_click.click()
            except ElementClickInterceptedException:
                time.sleep(4)
                do_hover(browser, SORTING_FILTER2)
                sort_click.click()
            time.sleep(4)
            do_hover(browser, SORTING_FILTER2)
            time.sleep(2)
            sort_text = browser.find_element_by_xpath(SORT_DROPDOWN2[1] + str([3]) + '/div' + str([sort_index]) + SORT_DROPDOWN_TEXT[1])
            sort_click_text = sort_text.text
            main_container_text = get_element_text(browser, SORTING_FILTER2)
            assert sort_click_text == main_container_text
    elif is_visible(browser, ALL_MEDIA_FILTER_NEW) is False:
        for sort_index in (3, 2, 1):
            do_hover(browser, SORTING_FILTER)
            sort_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([sort_index]))
            try:
                sort_click.click()
            except ElementClickInterceptedException:
                time.sleep(4)
                do_hover(browser, SORTING_FILTER)
                sort_click.click()
            time.sleep(4)
            do_hover(browser, SORTING_FILTER)
            time.sleep(2)
            sort_text = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([sort_index]) + SORT_DROPDOWN_TEXT[1])
            sort_click_text = sort_text.text
            main_container_text = get_element_text(browser, SORTING_FILTER)
            assert sort_click_text == main_container_text
    else:
        for sort_index2 in (4, 5, 3):
            do_hover(browser, SORTING_FILTER_OLD)
            sort_click2 = browser.find_element_by_xpath(SORT_DROPDOWN_OLD[1] + str([sort_index2]))
            try:
                sort_click2.click()
            except ElementClickInterceptedException:
                time.sleep(4)
                do_hover(browser, SORTING_FILTER_OLD)
                sort_click2.click()
            time.sleep(3)
            do_hover(browser, SORTING_FILTER_OLD)
            time.sleep(2)
            sort_text2 = browser.find_element_by_xpath(SORTING_FILTER_OLD[1])
            sort_click_text2 = sort_text2.text
            main_container_text = get_element_text(browser, SORTING_FILTER_OLD)
            assert sort_click_text2 == main_container_text


def goto_draft_page(browser):
    """
    Goes to the dashboard - drafts tab
    """
    is_visible(browser, MY_WORKSPACE_OR_VIDEOS, 10)
    do_hover(browser, MY_WORKSPACE_OR_VIDEOS)
    is_clickable(browser, MY_VIDEOS_DRAFTS, 10)
    do_click(browser, MY_VIDEOS_DRAFTS)
    time.sleep(3)
    title = browser.title
    assert title == dashboard_title


def verify_special_offer_btn(browser):
    """
    Verifies if Special Offer button is visible
    """
    assert is_visible(browser, SPECIAL_OFFER_BUTTON, 30)


# Photo
def upload_photo_on_create_page(browser):
    """
    Uploads a photo, checks if uploaded correctly
    Create a video from uploaded photo
    """
    is_visible(browser, MEDIA_UPLOAD_BTN)
    do_hover(browser, MEDIA_UPLOAD_BTN)
    elem = browser.find_element_by_xpath(MEDIA_UPLOAD_PHOTO_ON_CREATE[1])
    elem.send_keys(os.getcwd() + upload_photo)
    is_visible(browser, UPLOAD_COMPLETED_WIDGET, 35)
    do_click(browser, ADD_PHOTO_TO_PROJECT_FROM_WIDGET)
    time.sleep(7)


def use_uploaded_video_to_create(browser):
    """
    Because uploading video is blocked, we use already uploaded video here
    """
    do_click(browser, MEDIA_UPLOADS_TAB)
    do_click(browser, UPLOAD_VIDEO_TAB)
    do_hover(browser, UPLOADED_VIDEO_1ST)
    do_click(browser, UPLOADED_VIDEO_USE_BTN)

