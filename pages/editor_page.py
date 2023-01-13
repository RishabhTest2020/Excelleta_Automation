import os
from selenium.webdriver.common.keys import Keys
from locators.locators_file import *
from helpers.common_helpers import *
from pages.newcancellation_page import purchase_standard_plan_new, currencies_check, purchase_standard_plan
from test_data.testdata import *
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchFrameException, \
    WebDriverException
from selenium.webdriver import ActionChains
from pages.sign_up_page import *
from pages.create_page import *
from pages.pricing_page import *
import time


def verify_premium_asset_count_text(browser):
    """
    Verifies how many premium assets project has
    """
    premium_count_text = get_element_text(browser, ASSET_COUNT_TEXT_ON_POP_UP)
    premium_text = premium_count_text.split(' ')[-2]
    try:
        assert premium_text == "premium"
    except AssertionError:
        pass
    # # allure_screenshot(browser)


def verify_badge_and_count_text(browser):
    """
    It will check for the content_type in test_name and assert badge_text accordingly.
    """
    badge_text = get_element_text(browser, BADGE_ON_PUBLISH_PREVIEW)
    print(f"Badge Text is {badge_text}")
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    if 'editorial' in test_name:
        verify_premium_asset_count_text(browser)
        assert badge_text == 'EDITORIAL'
        # # allure_screenshot(browser)
    elif 'premium' in test_name:
        verify_premium_asset_count_text(browser)
        assert badge_text == 'PREMIUM'
        # # allure_screenshot(browser)
    else:
        pass


def check_editor_page(browser):
    """
    Checks if editor page main text is visible and correct
    Also check a load time
    """
    editor_load_start_time = time.time() * 1000
    if is_visible(browser, AUDIO_REPLACED_POPUP, 20) is True:
        do_click(browser, AUDIO_REPLACED_OK_BTN)
    else:
        pass
    skip_offer_modal(browser)
    assert is_visible(browser, RATIO_TOOLBAR, 40) is True
    editor_load_end_time = time.time() * 1000
    load_time(editor_load_end_time, editor_load_start_time, 'Editor load time')


def verify_play_n_pause_buttons(browser):
    """
    Verifies Play and Pause buttons are working
    """
    is_visible(browser, PLAY_BUTTON, 5)
    do_click(browser, PLAY_BUTTON)
    time.sleep(1)
    assert is_visible(browser, PAUSE_BUTTON, 20) is True
    time.sleep(1)
    do_click(browser, PAUSE_BUTTON)
    assert is_visible(browser, PLAY_BUTTON, 20) is True


def add_caption_helper(browser):
    """
    Add caption - helper - click Add button
    """
    is_visible(browser, CLICK_ADD_BUTTON)
    do_click(browser, CLICK_ADD_BUTTON)
    do_click(browser, CAPTION_OPTION)
    caption2 = browser.find_elements(HOVER_CAPTION[0], HOVER_CAPTION[1])
    assert len(caption2) >= 2
    do_click(browser, SECOND_CAPTION)


def add_caption(browser):
    """
    Deletes and Add Caption back in Editor
    Check if two captions are available or not
    if not Then Move to else and then increase the video size to 15 secs and add caption
    """
    caption = browser.find_elements(HOVER_CAPTION[0], HOVER_CAPTION[1])
    if len(caption) >= 2:
        do_hover(browser, HOVER_CAPTION)
        do_hover(browser, HOVER_CAPTION)
        do_click(browser, DELETE_CAPTION)
        do_click(browser, CONFIRM_BTN)
        add_caption_helper(browser)
        change_text_color_and_bg(browser)
    else:
        drag_and_drop(browser, TIMELINE_HANDLE_RIGHT, TIMELINE_HANDLE_RIGHT_15_SECS)
        add_caption_helper(browser)
        change_text_color_and_bg(browser)


def edit_actions_on_timeline(browser):
    """
    hovering over timeline, duplicate clip,
    replaces the duplicate with photo
    or when photo is a first part of a template - edit it (zoom)
    """
    is_visible(browser, HOVER_TIMELINE)
    do_hover(browser, HOVER_TIMELINE)
    if is_visible(browser, TRIM_VIDEO):
        do_click(browser, DUPLICATE_CLIP)
        assert is_visible(browser, HOVER_TIMELINE_2) is True
        do_click(browser, HOVER_TIMELINE_2)
        do_click(browser, REPLACE_CLIP)
        assert is_visible(browser, FOOTEGES_CONTAINER) is True
        do_click(browser, SORTING_FILTER_3)
        do_click(browser, PHOTOS_FILTER)
        do_hover(browser, UPLOADS_FIRST_PHOTO)
        do_click(browser, ADD_PHOTO_TO_PROJECT)
        do_click(browser, HOVER_TIMELINE_2)
        assert is_visible(browser, EDIT_PHOTO) is True
    else:
        assert is_visible(browser, EDIT_PHOTO) is True
        do_click(browser, EDIT_PHOTO)
        is_visible(browser, EDIT_PHOTO_ZOOM_IN)
        do_click(browser, EDIT_PHOTO_ZOOM_IN)
        is_visible(browser, EDIT_PHOTO_DONE_BTN)
        do_click(browser, EDIT_PHOTO_DONE_BTN)


def check_editor_page_new_user(browser):
    """
    Checks if editor page main text is visible and correct
    """
    if is_visible(browser, AUDIO_REPLACED_POPUP) is True:
        do_click(browser, AUDIO_REPLACED_OK_BTN)
    else:
        pass
    assert is_visible(browser, RATIO_TOOLBAR, 40) is True
    skip_offer_modal(browser, 10)
    try:
        switch_to_iframe(browser, ONBOARDING_APPCUES_FRAME)
        do_click(browser, ONBOARDING_APPCUES_HIDE)
        browser.switch_to.default_content()
    except (TimeoutException, NoSuchFrameException, NoSuchWindowException, NoSuchElementException):
        browser.switch_to.default_content()
        pass


def go_to_editor_tab(browser):
    """
    Goes to editor tab
    Inter-step for smoke test
    """
    do_click(browser, MODES_EDITOR)


def change_ratio(browser):
    """
    Changes ratio of the video in editor
    """
    elem = browser.find_element_by_xpath(SELECTED_RATIO[1])
    vertical_ratio = "vertical" in elem.get_attribute("class")
    is_visible(browser, SELECTED_RATIO)
    do_hover(browser, SELECTED_RATIO)
    if vertical_ratio is True:
        is_visible(browser, RATIO_WIDE)
        do_click(browser, RATIO_WIDE)
    else:
        is_visible(browser, RATIO_VERTICAL)
        do_click(browser, RATIO_VERTICAL)
    is_visible(browser, RATIO_GOT_IT_BTN)
    do_click(browser, RATIO_GOT_IT_BTN)
    # allure_screenshot(browser)


def add_characters(browser):
    """
    Add characters in text animations in editor
    """
    do_click(browser, TEXT_ANIMATION)
    do_double_click(browser, TEXT_ANIMATION_BOX)
    do_send_keys(browser, TEXT_ANIMATION_EDIT_BOX, text_animation_word)
    do_click(browser, TEXT_ANIMATION_EDIT_BOX_DONE)
    animation_text_box_text = get_element_text(browser, TEXT_ANIMATION_TEXT_BOX)
    assert animation_text_box_text == text_animation_word


def change_text_color_and_bg(browser):
    """
    Change font color and text background in editor
    It checks whether the color changes are applied or not in Editor
    If audio replaced pop-up shows up, script closes it
    """
    is_visible(browser, COLOR_PICKER)
    do_click(browser, COLOR_PICKER)
    is_visible(browser, EDIT_COLOR_TXTBOX)
    try:
        for i in range(20):
            do_send_keys(browser, EDIT_COLOR_TXTBOX, Keys.BACKSPACE)
    except (NoSuchElementException, TimeoutException):
        if is_visible(browser, AUDIO_REPLACED_POPUP) is True:
            do_click(browser, AUDIO_REPLACED_OK_BTN)
        else:
            pass
        do_hover(browser, COLOR_PICKER)
        do_click(browser, COLOR_PICKER)
        for i in range(20):
            do_send_keys(browser, EDIT_COLOR_TXTBOX, Keys.BACKSPACE)
    do_send_keys(browser, EDIT_COLOR_TXTBOX, 'rgb(117,38,38)')
    do_send_keys(browser, EDIT_COLOR_TXTBOX, Keys.ENTER)
    wait_for_ajax(browser)
    try:
        color_value = get_css_value(browser, EDITOR_TEXT_COLOR, 'fill')
    except (TimeoutException, NoSuchElementException):
        color_value = get_css_value(browser, EDITOR_TEXT_COLOR2, 'fill')
    assert color_value == 'rgb(117, 38, 38)'
    if is_visible(browser, TEXT_COLOR_BG) is True:
        do_click(browser, TEXT_COLOR_BG)
        for i in range(20):
            do_send_keys(browser, EDIT_COLOR_TXTBOX, Keys.BACKSPACE)
        do_send_keys(browser, EDIT_COLOR_TXTBOX, 'rgb(203,92,208)')
        do_send_keys(browser, EDIT_COLOR_TXTBOX, Keys.ENTER)
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        if 'test_verify_template_page_after_login' != test_name:
            bg_color_value = get_css_value(browser, EDITOR_TEXT_COLOR_BG, 'fill')
            assert bg_color_value == 'rgb(203, 92, 208)'
        else:
            bg_color_value = get_css_value(browser, EDITOR_TEXT_COLOR_BG2, 'background-color')
            try:
                assert bg_color_value == 'rgba(203, 92, 208, 1)'
            except AssertionError:
                assert bg_color_value == 'rgb(203, 92, 208)'
    do_hover(browser, EDITOR_PANE)
    if is_visible(browser, RGBA_INPUT):
        while True:
            do_click(browser, COLOR_PICKER)
            if is_visible(browser, RGBA_INPUT) is False:
                break
    else:
        pass
    # allure_screenshot(browser)


def change_text_alignment(browser):
    """
    Change text alignment in editor
    """
    elem = browser.find_element_by_xpath(ALIGN_CENTER[1])
    align_center_selected = "selected" in elem.get_attribute("class")
    if align_center_selected is True:
        is_visible(browser, ALIGN_RIGHT_NEW_2, 10)
        do_click(browser, ALIGN_RIGHT_NEW_2, 10)
    else:
        is_visible(browser, ALIGN_CENTER_NEW_2, 10)
        do_click(browser, ALIGN_CENTER_NEW_2, 10)


def change_font(browser, fontname="Lobster"):
    """
    Changes font in editor
    This one verifies font
    fontname: default is "Lobster" but other names can be used
    """
    is_visible(browser, FONTS_DROPDOWN)
    do_click(browser, FONTS_DROPDOWN)
    do_click(browser, SEARCH_EMPTY_INPUT)
    do_send_keys(browser, SEARCH_FONT_INPUT, fontname)
    is_visible(browser, LOBSTER_FONT)
    do_click(browser, LOBSTER_FONT)
    # allure_screenshot(browser)


def change_text_to_lowercase(browser):
    """
    Changes text to lowercase
    """
    is_visible(browser, CAPITALIZE_MAIN_ICON)
    do_hover(browser, CAPITALIZE_MAIN_ICON)
    do_click(browser, CAPITALIZE_MAIN_ICON)
    is_visible(browser, LOWERCASE_ICON_NEW)
    do_click(browser, LOWERCASE_ICON_NEW)


def change_text_to_uppercase(browser):
    """
    Changes text to uppercase
    """
    is_visible(browser, CAPITALIZE_MAIN_ICON)
    do_hover(browser, CAPITALIZE_MAIN_ICON)
    if is_visible(browser, UPPERCASE_ICON_NEW) is False:
        do_click(browser, CAPITALIZE_MAIN_ICON)
    else:
        pass
    is_visible(browser, UPPERCASE_ICON_NEW)
    do_click(browser, UPPERCASE_ICON_NEW)


def change_text_position(browser):
    """
    Changes text position - 9 different positions
    """
    is_visible(browser, TEXT_POSITION_BTN)
    do_hover(browser, TEXT_POSITION_BTN)
    do_click(browser, TEXT_POSITION_BTN)
    elem = browser.find_elements_by_xpath(TEXT_POSITIONS_CHANGE_BTN[1])
    print(len(elem))
    no_of_positions = len(elem)
    print(TEXT_POSITIONS_CHANGE_BTN[1] + str([no_of_positions]))
    for position_btns in range(1, no_of_positions + 1):
        print(TEXT_POSITIONS_CHANGE_BTN[1] + str([position_btns]))
        browser.find_element_by_xpath(TEXT_POSITIONS_CHANGE_BTN[1] + str([position_btns])).click()
        # allure_screenshot(browser)


def change_outro_background(browser):
    """
    Changes outro background color and image
    """
    do_click(browser, OUTRO_ON_TIMELINE)
    is_visible(browser, OUTRO_BACKGROUND_COLOR)
    do_click(browser, OUTRO_BACKGROUND_COLOR)
    do_click(browser, OUTRO_SELECTED_COLOR)
    is_visible(browser, OUTRO_UPLOAD_BACKGROUND)
    do_send_keys(browser, OUTRO_UPLOAD_BACKGROUND, os.getcwd() + upload_photo, 10)
    is_visible(browser, OUTRO_REMOVE_BACKGROUND)
    do_click(browser, OUTRO_REMOVE_BACKGROUND)


def verify_text_all_styles(browser):
    """
    Verifies all texstyle animations available
    A part of full regression
    """
    is_visible(browser, TEXT_STYLES_BTNS)
    elem = browser.find_elements_by_xpath(TEXT_STYLES_BTNS[1])
    print(len(elem))
    no_of_styles = len(elem)
    print(TEXT_STYLES_BTNS[1] + str([no_of_styles]))
    for styles_btns in range(1, no_of_styles + 1):
        print(TEXT_STYLES_BTNS[1] + str([styles_btns]))
        click_text_style = browser.find_element_by_xpath(TEXT_STYLES_BTNS[1] + str([styles_btns]))
        try:
            click_text_style.click()
        except ElementNotInteractableException:
            browser.execute_script("arguments[0].scrollIntoView();", click_text_style)
            click_text_style.click()
        time.sleep(1)
        style_selected = "selected" in click_text_style.get_attribute("class")
        assert style_selected is True
        # allure_screenshot(browser)


def change_text_style(browser):
    """
    Verifies changing textstyle once
    """
    is_visible(browser, TEXT_STYLES_BTN)
    do_click(browser, TEXT_STYLES_BTN)
    if is_visible(browser, REPLACE_TEXT_STYLE):
        do_click(browser, REPLACE_TEXT_STYLE)
    else:
        pass
    assert is_visible(browser, TEXT_STYLES_SELECTED) is True
    # allure_screenshot(browser)


def filter_videos_helper(browser):
    """
    Helper to re-use --> filtered videos
    """
    filtered_videos = browser.find_elements_by_xpath(FILTERED_VIDEOS[1])
    print(len(filtered_videos))
    no_of_videos = len(filtered_videos)
    premium_tags = browser.find_elements_by_xpath(PREMIUM_TAGS[1])
    print(len(premium_tags))
    no_of_tags = len(premium_tags)
    try:
        assert no_of_videos == no_of_tags
    except AssertionError:
        print('Test Failed coz:' + str(no_of_videos) and str(no_of_tags) + 'is not equal')
        pass


def filter_premium_media_search(browser):
    """
    Filters premium clips in media search
    to_improve: add a keyword as a parameter, merge 2 functions into one - premium_click and editorial_click
    """
    is_visible(browser, MEDIA_SEARCH_INPUT, 5)
    do_clear(browser, MEDIA_SEARCH_INPUT, 5)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, "fun", 10)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, Keys.ENTER, 10)
    do_hover(browser, MEDIA_SEARCH_FILTER)
    try:
        premium_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([4]))
        premium_click.click()
    except (TimeoutException, NoSuchElementException):
        do_click(browser, PREMIUM_FILTER)
    filter_videos_helper(browser)
    # allure_screenshot(browser)


def filter_editorial_media_search(browser):
    """
    Filters editorial clips in media search
    to_improve: add a keyword as a parameter, merge 2 functions into one - premium_click and editorial_click
    """
    is_visible(browser, MEDIA_SEARCH_INPUT, 5)
    do_clear(browser, MEDIA_SEARCH_INPUT, 5)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, "fun", 10)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, Keys.ENTER, 10)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, Keys.ENTER, 10)
    do_hover(browser, MEDIA_SEARCH_FILTER)
    try:
        editorial_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([5]))
        editorial_click.click()
    except (TimeoutException, NoSuchElementException):
        do_click(browser, EDITORIAL_FILTER)
    time.sleep(2)
    do_hover(browser, MEDIA_SEARCH_FILTER)
    try:
        newest_click = browser.find_element_by_xpath(SORT_DROPDOWN[1] + '/div' + str([9]))
        newest_click.click()
    except (TimeoutException, NoSuchElementException):
        do_click(browser, SORTING_OPTIONS['Newest'])
    filter_videos_helper(browser)
    # allure_screenshot(browser)


def delete_watermark_or_logo(browser):
    """
    Helper for upload_watermark and upload_logo functions
    """
    logos = browser.find_elements_by_xpath(UPLOADED_LOGOS_HOV[1])
    logos_len = len(logos)
    for x in range(1, logos_len + 1):
        do_hover(browser, UPLOADED_LOGOS_HOV)
        do_click(browser, UPLOADED_LOGOS_DEL)
        do_click(browser, DELETE_WATERMARK_CONFIRM)
        time.sleep(1)


def upload_watermark(browser):
    """
    Uploads watermark in cases: when watermark is filled up or not
    """
    if is_visible(browser, EDITOR_WATERMARK_FILLED, 5) is True:
        do_click(browser, EDITOR_WATERMARK_FILLED)
        do_click(browser, DELETE_WATERMARK)
        is_visible(browser, DELETE_WATERMARK_CONFIRM)
        do_click(browser, DELETE_WATERMARK_CONFIRM)
        do_click(browser, EDITOR_WATERMARK)
        delete_watermark_or_logo(browser)
        if is_visible(browser, UPLOADED_LOGOS_HOV) is False:
            do_click(browser, CROSS_BTN)
        if is_visible(browser, EDITOR_WATERMARK) is True:
            do_click(browser, EDITOR_WATERMARK)
        do_send_keys(browser, UPLOAD_LOGO, os.getcwd() + brand_logo)
        try:
            do_click(browser, IMAGE_DONE_BTN, 15)
        except (TimeoutException, NoSuchElementException):
            pass
        do_click(browser, ADD_TO_VIDEO_BTN)
        assert is_visible(browser, EDITOR_WATERMARK_FILLED, 25) is True
    else:
        do_click(browser, EDITOR_WATERMARK)
        do_send_keys(browser, UPLOAD_LOGO, os.getcwd() + brand_logo)
        try:
            do_click(browser, IMAGE_DONE_BTN, 15)
        except (TimeoutException, NoSuchElementException):
            pass
        do_click(browser, ADD_TO_VIDEO_BTN)
        assert is_visible(browser, EDITOR_WATERMARK_FILLED, 25) is True


def upload_logo(browser):
    """
    Uploads logo in Outro
    Refactored on Nov 2022 when React component was added
    It covers two cases:
    - when logo is added
    - when there is a placeholder
    """
    do_click(browser, OUTRO_BTN)
    if is_visible(browser, EDITOR_LOGO_DRAGGING_AREA) is True:
        do_click(browser, EDITOR_LOGO_DRAGGING_AREA)
        do_click(browser, EDITOR_UPLOAD_LOGO)
        delete_watermark_or_logo(browser)
        assert is_visible(browser, UPLOADED_LOGOS_HOV) is False
        do_click(browser, CROSS_BTN)
        time.sleep(2)
        if is_visible(browser, EDITOR_UPLOAD_LOGO) is True:
            do_click(browser, EDITOR_UPLOAD_LOGO)
        else:
            do_click(browser, EDITOR_LOGO_DRAGGING_AREA)
            do_click(browser, EDITOR_UPLOAD_LOGO)
        do_send_keys(browser, EDITOR_LOGO_UPLOAD_INPUT, os.getcwd() + brand_logo)
        if is_visible(browser, IMAGE_DONE_BTN, 10):
            do_click(browser, IMAGE_DONE_BTN, 15)
        else:
            pass
        do_click(browser, ADD_TO_VIDEO_BTN)
        assert is_visible(browser, EDITOR_LOGO_IMAGE, 25) is True
    else:
        is_visible(browser, EDITOR_LOGO_ADD_LOGO)
        do_click(browser, EDITOR_LOGO_ADD_LOGO)
        do_send_keys(browser, EDITOR_LOGO_UPLOAD_INPUT, os.getcwd() + brand_logo)
        if is_visible(browser, IMAGE_DONE_BTN, 10):
            do_click(browser, IMAGE_DONE_BTN, 15)
        else:
            pass
        do_click(browser, ADD_TO_VIDEO_BTN)
        assert is_visible(browser, EDITOR_LOGO_IMAGE, 25) is True


def upload_font(browser):
    """
    Uploads font from computer
    """
    is_visible(browser, FONTS_DROPDOWN)
    do_click(browser, FONTS_DROPDOWN)
    do_click(browser, MY_FONTS_BTN)
    font_upload = browser.find_element_by_xpath(FROM_COMPUTER_FONT[1])
    font_upload.send_keys(os.getcwd() + font_path)
    do_click(browser, FONT_UPLOAD_CHECKBOX)
    do_click(browser, FONT_UPLOAD_BTN)
    do_click(browser, FONT_UPLOAD_DONE_BTN, 20)
    do_click(browser, UPLOADED_FONT_SEL)
    time.sleep(2)
    font_family = browser.find_element_by_css_selector('div.animation-el > svg > defs > style')
    font_selected = font_name in font_family.get_attribute('f-family')
    assert font_selected is True


def upload_font_google(browser, google_font_name):
    """
    Uploads font from Google library
    Checks if Pride font is already added or not
    If is added - uses it and verifies if it is applied
    If it is not added - adds it and verifies if it is applied
        google_font_name: name of a Google font, example: "Pridi"
    """
    is_visible(browser, FONTS_DROPDOWN)
    do_click(browser, FONTS_DROPDOWN)
    do_click(browser, MY_FONTS_BTN)
    do_send_keys(browser, GOOGLE_SEARCH_FONT_INPUT_DROPDOWN, google_font_name)
    if is_visible(browser, CUSTOM_FONT_NO_RESULTS) is True:
        do_click(browser, CLEAR_SEARCH_MY_FONTS)
        do_hover(browser, ADD_FONTS_BTN)
        do_click(browser, ADD_FONTS_BTN)
        do_hover(browser, FROM_GOOGLE_FONT)
        do_click(browser, FROM_GOOGLE_FONT)
        do_send_keys(browser, GOOGLE_SEARCH_FONT_INPUT_POPUP, google_font_name)
        do_click(browser, GOOGLE_CHOSEN_FONT)
        add_btn_color = browser.find_element_by_css_selector("button[class='bm-promo-google-fonts__button']").value_of_css_property('background-color')
        assert add_btn_color == "rgba(0, 172, 255, 1)"  # equal to #00acff - verifies if btn has a correct color
        do_hover(browser, GOOGLE_FONT_ADD_BUTTON)
        do_click(browser, GOOGLE_FONT_ADD_BUTTON)
        time.sleep(2)
        font_family = browser.find_element_by_css_selector('div.animation-el > svg > defs > style')
        font_selected = font_name_pridi in font_family.get_attribute('f-family')
        assert font_selected is True
    else:
        do_hover(browser, GOOGLE_PRIDI_FONT_CHOSEN)
        do_click(browser, GOOGLE_PRIDI_BOLD_CHOOSE)
        time.sleep(2)
        font_family = browser.find_element_by_css_selector('div.animation-el > svg > defs > style')
        font_selected = font_name_pridi in font_family.get_attribute('f-family')
        assert font_selected is True


def filter_editorial_media_photos_search(browser):
    """
    Filters editorial photos in media search
    # to_improve: parameter for keyword
    """
    is_visible(browser, MEDIA_SEARCH_INPUT, 5)
    do_clear(browser, MEDIA_SEARCH_INPUT, 5)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, "fun", 10)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, Keys.ENTER, 10)
    if is_visible(browser, VIDEOS_PHOTOS_DROPDOWN) is True:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
        do_click(browser, DROPDOWN_SELECT_VIDEOS)
    else:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
        do_click(browser, DROPDOWN_SELECT_VIDEOS_OLD)
    filter_videos_helper(browser)
    # allure_screenshot(browser)


def verify_favourites(browser):
    """
    Verifies favourites media
    """
    do_click(browser, MEDIA_LIBRARY_TAB)
    if is_visible(browser, VIDEOS_PHOTOS_DROPDOWN) is True:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
        do_click(browser, DROPDOWN_SELECT_VIDEOS)
    else:
        do_hover(browser, PHOTOS_VIDEOS_HOVER)
        do_click(browser, SELECT_VIDEOS_CAT)
    do_hover(browser, CHOSEN_VIDEO_TO_FAV)
    if is_visible(browser, ADD_FAVOURITES) is False:
        is_visible(browser, MEDIA_FAVORITES_TAB)
        do_click(browser, MEDIA_FAVORITES_TAB)
        time.sleep(1)
        selected_favourite = browser.find_element_by_xpath(FAVOURITE_SELECTED[1])
        favourite_selected = "is-favorite" in selected_favourite.get_attribute("class")
        assert favourite_selected is True
    else:
        do_click(browser, ADD_FAVOURITES)
        is_visible(browser, MEDIA_FAVORITES_TAB)
        do_click(browser, MEDIA_FAVORITES_TAB)
        time.sleep(1)
        selected_favourite = browser.find_element_by_xpath(FAVOURITE_SELECTED[1])
        favourite_selected = "is-favorite" in selected_favourite.get_attribute("class")
        assert favourite_selected is True


def remove_from_favourites(browser):
    """
    Remove a video from favourites
    """
    do_click(browser, MEDIA_LIBRARY_TAB)
    do_hover(browser, CHOSEN_VIDEO_TO_FAV)
    do_click(browser, REMOVE_FAVOURITES)


def changes_outros(browser):
    """
    Changes outros in a loop
    """
    is_visible(browser, OUTRO_BTN)
    do_click(browser, OUTRO_BTN)
    elem = browser.find_elements_by_xpath(SELECT_OUTROS[1])
    print(len(elem))
    no_of_outros = len(elem)
    print(SELECT_OUTROS[1] + str([no_of_outros]))
    for outros_btns in range(1, no_of_outros + 1):
        print(SELECT_OUTROS[1] + str([outros_btns]))
        click_outros = browser.find_element_by_xpath(SELECT_OUTROS[1] + str([outros_btns]))
        try:
            click_outros.click()
        except ElementNotInteractableException:
            browser.execute_script("arguments[0].scrollIntoView();", click_outros)
            click_outros.click()
        time.sleep(1)
        outros_selected = "selected" in click_outros.get_attribute("class")
        assert outros_selected is True
        # allure_screenshot(browser)


# Tabs
def go_to_editor_tab(browser):
    """
    Goes to Editor tab in Editor
    """
    is_visible(browser, EDITOR_TAB)
    do_click(browser, EDITOR_TAB)


def go_to_media_tab(browser):
    """
    Goes to Media tab in Editor
    Also covers production Appcues pop-ups
    """
    try:
        switch_to_iframe(browser, ONBOARDING_APPCUES_FRAME)
        do_click(browser, ONBOARDING_APPCUES_HIDE)
        browser.switch_to.default_content()
    except (TimeoutException, NoSuchFrameException, NoSuchWindowException, NoSuchElementException):
        browser.switch_to.default_content()
        pass
    try:
        is_visible(browser, MEDIA_TAB, 10)
        do_click(browser, MEDIA_TAB, 10)
    except ElementClickInterceptedException:
        is_visible(browser, RATIO_GOT_IT_BTN)
        do_click(browser, RATIO_GOT_IT_BTN)
        if is_visible(browser, USE_BTN_ON_PREVIEW) is True:
            do_click(browser, USE_BTN_ON_PREVIEW)
        do_click(browser, MEDIA_TAB, 10)


def go_to_music_tab(browser):
    """
    Goes to Music tab in Editor
    """
    is_visible(browser, MUSIC_TAB)
    do_click(browser, MUSIC_TAB)


# Video
def search_video_in_media_tab(browser):
    """
    Searches video by keyword
    Checks if video was added to timeline
    # to_improve: parameter for keywords
    """
    if is_visible(browser, VIDEOS_PHOTOS_DROPDOWN) is True:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
        do_click(browser, DROPDOWN_SELECT_VIDEOS)
    else:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
        do_click(browser, DROPDOWN_SELECT_VIDEOS_OLD)
    is_visible(browser, MEDIA_SEARCH_INPUT, 15)
    do_clear(browser, MEDIA_SEARCH_INPUT)
    do_send_keys(browser, MEDIA_SEARCH_INPUT, "cats")
    do_send_keys(browser, MEDIA_SEARCH_INPUT, Keys.ENTER)
    try:
        do_hover(browser, CHOSEN_VIDEO)
    except StaleElementReferenceException:
        do_send_keys(browser, MEDIA_SEARCH_INPUT, Keys.ENTER)
        time.sleep(1)
        do_hover(browser, CHOSEN_VIDEO)
    is_visible(browser, PREVIEW_BTN)
    do_click(browser, PREVIEW_BTN)
    is_visible(browser, USE_BTN_ON_PREVIEW, 15)
    do_click(browser, USE_BTN_ON_PREVIEW)
    is_visible(browser, IS_VIDEO_ADDED, 35)


def add_4_pcs(browser):
    """

    Args:
        browser:

    Add 4 premium clips from editor media tab

    """
    time.sleep(1)
    for i in range(1, 5):
        wait_for_ajax(browser)
        do_hover(browser, (By.XPATH, CHOSEN_VIDEO[1] + str([i])))
        try:
            do_click(browser, (By.XPATH, USE_BTN[1] + str([i])))
        except TimeoutException:
            do_hover(browser, (By.XPATH, CHOSEN_VIDEO[1] + str([i])))
            do_click(browser, (By.XPATH, USE_BTN[1] + str([i])))
        is_visible(browser, IS_VIDEO_ADDED, 35)


def change_video_transitions(browser):
    """
    Changes transition option for video
    """
    do_click(browser, EDITOR_TAB)
    is_visible(browser, TRANSITION_BTN, 10)
    do_hover(browser, TRANSITION_BTN)
    elem = browser.find_element_by_xpath(NONE_TRANSITION[1])
    fade_not_selected = "selected" in elem.get_attribute("class")
    if fade_not_selected is False:
        pass
    else:
        do_click(browser, TRANSITIONS["FADE_TRANSITION"])
        elem2 = browser.find_element_by_xpath(TRANSITIONS["FADE_TRANSITION"])
        fade_is_selected = "selected" in elem2.get_attribute("class")
        assert fade_is_selected is True
    # allure_screenshot(browser)


def upload_video_in_media_tab(browser):
    """
    Uploads a video, checks if uploaded correctly
    For local use only
    At the end the script deletes the video
    to_improve: when changes in upload video are done, try to re-use it on BrowserStack
    """
    is_visible(browser, MEDIA_UPLOAD_BTN)
    do_hover(browser, MEDIA_UPLOAD_BTN)
    elem = browser.find_element_by_xpath(MEDIA_UPLOAD_VIDEO2[1])
    elem.send_keys(os.getcwd() + upload_video)
    assert is_visible(browser, UPLOAD_IN_PROGRESS_POPUP, 30) is True
    title = get_element_text(browser, UPLOAD_TITLE_ON_POPUP)
    assert title == 'Upload in progress' or title == 'Processing file'
    do_hover(browser, UPLOADS_FIRST_VIDEO, 20)
    do_click(browser, ADD_VIDEO_TO_PROJECT_BTN, 60)
    assert is_visible(browser, VIDEO_ADDED_IN_TEMPLATE, 10) is True
    do_hover(browser, UPLOADS_FIRST_VIDEO, 20)
    do_click(browser, UPLOAD_VIDEO_DELETE, 20)
    do_click(browser, UPLOADS_POPUP_DELETE)


# Photo
def upload_photo_in_media_tab(browser):
    """
    Uploads a photo, checks if uploaded correctly
    At the end, the script deletes the photo
    """
    is_visible(browser, MEDIA_UPLOAD_BTN)
    do_hover(browser, MEDIA_UPLOAD_BTN)
    elem = browser.find_element_by_xpath(MEDIA_UPLOAD_PHOTO[1])
    elem.send_keys(os.getcwd() + upload_photo)
    is_visible(browser, UPLOAD_COMPLETED_WIDGET, 35)
    if is_visible(browser, UPLOAD_COMPLETED_WIDGET_CLOSE) is True:
        do_click(browser, UPLOAD_COMPLETED_WIDGET_CLOSE)
    else:
        pass
    do_hover(browser, UPLOADS_FIRST_PHOTO)
    do_click(browser, ADD_PHOTO_TO_PROJECT)


def change_photo_transitions(browser):
    """
    Changes transition option for photo
    """
    for transitions_name, transitions_path in TRANSITIONS.items():
        is_visible(browser, TRANSITION_BTN2)
        do_hover(browser, TRANSITION_BTN2)
        do_click(browser, transitions_path)
        time.sleep(4)
        if is_visible(browser, TRANSITION_BTN2) is False:
            time.sleep(4)
            do_hover(browser, TRANSITION_BTN2)
        else:
            do_hover(browser, TRANSITION_BTN2)
        transition = browser.find_element_by_xpath(transitions_path[1])
        print(transition.get_attribute("class"))
        transition_is_selected = "selected" in transition.get_attribute("class")
        print(transition_is_selected)
        assert transition_is_selected is True
        # allure_screenshot(browser)


def select_a_photo_and_add_to_project(browser):
    """
    Selects a photo from library and adds to the project
    """
    if is_visible(browser, VIDEOS_PHOTOS_DROPDOWN) is True:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN)
        do_click(browser, DROPDOWN_SELECT_PHOTOS)
    else:
        do_hover(browser, VIDEOS_PHOTOS_DROPDOWN_OLD)
        do_click(browser, DROPDOWN_SELECT_PHOTOS_OLD)
    do_hover(browser, PHOTO_HOVERED)
    is_visible(browser, SELECT_PHOTO_CIRCLE)
    do_click(browser, SELECT_PHOTO_CIRCLE)
    is_visible(browser, ADD_PHOTO_TO_PROJECT_FROM_BAR)
    do_click(browser, ADD_PHOTO_TO_PROJECT_FROM_BAR)


def preview_a_photo_and_close(browser):
    """
    Opens preview mode for photo and closes it
    """
    do_hover(browser, PHOTO_HOVERED)
    is_visible(browser, ZOOM_PHOTO_ICON)
    do_click(browser, ZOOM_PHOTO_ICON)
    is_visible(browser, CLOSE_PHOTO_PREVIEW)
    do_click(browser, CLOSE_PHOTO_PREVIEW)


def replace_added_photo(browser):
    """
    Replaces added photo in Editor
    """
    try:
        do_hover(browser, ADDED_MEDIA)
        do_hover(browser, ADDED_MEDIA_EDIT_BUTTON)
        do_click(browser, ADDED_MEDIA_REPLACE_BTN)
        do_click(browser, MEDIA_LIBRARY_TAB)
        do_hover(browser, PHOTOS_VIDEOS_HOVER)
        do_click(browser, SELECT_PHOTOS_CAT)
        do_hover(browser, LIB_PIC_HOV)
        do_click(browser, REPLACE_MEDIA_BTN)
    except WebDriverException:
        pass


# Music
def music_filter(browser):
    """
    Verifies if music filters work correctly
    Test for categories and it cleans the settings at the end
    """
    music_cat = browser.find_elements_by_xpath(MUSIC_DROPDOWN[1])
    print(len(music_cat))
    no_of_mcats = len(music_cat)
    sub_cats_no = (3, 25, 40, 44)
    for music_catg, music_subcatg in zip(range(1, no_of_mcats + 1), sub_cats_no):
        print(MUSIC_DROPDOWN[1] + str([music_catg]))
        music_cat_btn = browser.find_element_by_xpath(MUSIC_DROPDOWN[1] + str([music_catg]))
        music_cat_hover = ActionChains(browser).move_to_element(music_cat_btn)
        music_cat_hover.perform()
        print(MUSIC_SUB_CAT[1] + str([music_subcatg]))
        music_subcat_btn = browser.find_element_by_xpath(MUSIC_SUB_CAT[1] + str([music_subcatg]))
        music_subcat_btn.click()
        time.sleep(1)
        music_subcat_is_selected = "selected" in music_subcat_btn.get_attribute("class")
        assert music_subcat_is_selected is True
        # allure_screenshot(browser)
        clear_btn = browser.find_element_by_xpath(SUB_CAT_CLEAR_BTN[1] + str([music_catg]))
        clear_btn.click()


def upload_music_and_delete(browser):
    """
    Upload own music file
    Not in use due to filters problems
    to_improve: this function currently doesn't work
    to_improve: add a keyword as a parameter
    """
    do_click(browser, MUSIC_TAB)
    do_click(browser, MUSIC_UPLOADS_TAB)
    while is_visible(browser, SAMPLE_AUDIO, 10) is True:
        do_hover(browser, UPLOADED_AUDIO, 15)
        do_click(browser, DELETE_UPLOADED_MUSIC)
        do_click(browser, DELETE_TRACK_CONFIRM, 10)
    else:
        pass
    elem = browser.find_element_by_xpath(AUDIO_UPLOAD[1])
    elem.send_keys(os.getcwd() + upload_audio)
    assert is_visible(browser, SAMPLE_AUDIO, 20) is True
    do_click(browser, MUSIC_LIBRARY_TAB)
    time.sleep(1)
    do_send_keys(browser, MUSIC_SEARCH, 'high')
    do_send_keys(browser, MUSIC_SEARCH, Keys.ENTER)
    if is_invisible(browser, MUSIC_AUDIO_GRID) is True:
        browser.refresh()
        if is_alert_present(browser) is True:
            browser.switch_to.alert.accept()
        time.sleep(3)
        do_click(browser, MUSIC_TAB)
        do_click(browser, MUSIC_LIBRARY_TAB)
    else:
        pass
    do_click(browser, MUSIC_LIBRARY_TAB)
    try:
        do_hover(browser, HOVER_MUSIC_BG_1)
    except StaleElementReferenceException:
        do_hover(browser, HOVER_MUSIC_BG_2)
    except NoSuchElementException:
        browser.refresh()
        if is_alert_present(browser) is True:
            browser.switch_to.alert.accept()
        time.sleep(3)
        do_click(browser, MUSIC_TAB)
        do_click(browser, MUSIC_LIBRARY_TAB)
        do_hover(browser, HOVER_MUSIC_BG_2)
    do_click(browser, USE_TRACK_BTN)
    do_click(browser, MUSIC_UPLOADS_TAB)
    time.sleep(1)
    do_hover(browser, UPLOADED_AUDIO, 15)
    do_click(browser, DELETE_UPLOADED_MUSIC)
    do_click(browser, DELETE_TRACK_CONFIRM, 10)
    assert is_invisible(browser, SAMPLE_AUDIO) is True


def select_an_audio(browser):
    """
    Selects audio in Editor
    Not in use due to filters problems
    to_improve: this function currently doesn't work
    to_improve: add a keyword as a parameter
    """
    skip_offer_modal(browser)
    do_click(browser, MUSIC_TAB)
    if is_invisible(browser, MUSIC_LIBRARY_TAB_SELECTED) is True:
        do_click(browser, MUSIC_LIBRARY_TAB)
        for i in range(6):
            do_send_keys(browser, MUSIC_SEARCH, Keys.BACKSPACE)
    else:
        pass
    do_send_keys(browser, MUSIC_SEARCH, 'high')
    do_send_keys(browser, MUSIC_SEARCH, Keys.ENTER)
    do_send_keys(browser, MUSIC_SEARCH, Keys.ENTER)
    time.sleep(3)
    if is_visible(browser, MUSIC_AUDIO_GRID) is False:
        browser.refresh()
        if is_alert_present(browser) is True:
            browser.switch_to.alert.accept()
        time.sleep(3)
        do_click(browser, MUSIC_TAB)
        do_click(browser, MUSIC_LIBRARY_TAB)
    else:
        pass
    try:
        do_hover(browser, HOVER_MUSIC_BG_1)
    except StaleElementReferenceException:
        time.sleep(1)
        do_hover(browser, HOVER_MUSIC_BG_2)
    except NoSuchElementException:
        browser.refresh()
        if is_alert_present(browser) is True:
            browser.switch_to.alert.accept()
        time.sleep(3)
        do_click(browser, MUSIC_TAB)
        do_click(browser, MUSIC_LIBRARY_TAB)
        if is_visible(browser, MUSIC_AUDIO_GRID) is False:
            browser.refresh()
            time.sleep(5)
        else:
            pass
        do_hover(browser, HOVER_MUSIC_BG_2)
    do_click(browser, USE_TRACK_BTN)


def verify_trimming_of_uploaded_audio(browser):
    """
    Opens the trimming pop-up and verifies if trimming options are available
    blocked by AUTOM-360
    """
    do_hover(browser, SAMPLE_AUDIO)
    is_visible(browser, TRIM_TRACK_BTN)
    do_click_offset(browser, TRIM_TRACK_BTN, 238, 212)
    is_visible(browser, TRIM_TRACK_INDICATOR_START)
    is_visible(browser, TRIM_TRACK_INDICATOR_END)
    is_visible(browser, TRIM_CANCEL_BTN)
    do_click(browser, TRIM_CANCEL_BTN)


def upload_audio_and_select(browser):
    """
    Currently in use instead of two funcs above
    Deletes previously uploaded file, upload a new audio file
    """
    try:
        switch_to_iframe(browser, ONBOARDING_APPCUES_FRAME)
        do_click(browser, ONBOARDING_APPCUES_HIDE)
        browser.switch_to.default_content()
    except (TimeoutException, NoSuchFrameException, NoSuchWindowException, NoSuchElementException):
        browser.switch_to.default_content()
        pass
    do_click(browser, MUSIC_TAB)
    do_click(browser, MUSIC_UPLOADS_TAB)
    while is_visible(browser, SAMPLE_AUDIO, 10) is True:
        do_hover(browser, UPLOADED_AUDIO, 15)
        do_click(browser, DELETE_UPLOADED_MUSIC)
        do_click(browser, DELETE_TRACK_CONFIRM, 10)
        time.sleep(1)
    else:
        pass
    elem = browser.find_element_by_xpath(AUDIO_UPLOAD[1])
    elem.send_keys(os.getcwd() + upload_audio)
    assert is_visible(browser, SAMPLE_AUDIO, 55) is True


def edit_published_video(browser):
    """
    Edits published video from Dashboard
    Asserts if two main condition is fulfilled
    1. changed Save and Preview button, 2. ratios dropdown invisible
    """
    do_hover(browser, FIRST_PUBLISHED_VIDEO)
    do_click(browser, EDIT_PUBLISHED_VIDEO_DASHBOARD)
    is_visible(browser, SAVE_AND_PREVIEW_BTN)
    button_text = get_element_text(browser, SAVE_AND_PREVIEW_BTN)
    assert button_text == "Save & Publish"
    assert is_visible(browser, RATIO_TOOLBAR, 10) is False


def publish_video(browser):
    """
    Publishes a video from editor
    Sleeps are needed for rendering
    """
    global start_rendering_time
    is_visible(browser, SAVE_AND_PREVIEW_BTN, 20)
    do_click(browser, SAVE_AND_PREVIEW_BTN, 10)
    start_rendering_time = time.time() * 1000
    time.sleep(10)
    # allure_screenshot(browser)


def publish_video_new_user(browser):
    """
    Publishes a video from editor - for new users
    Sleeps are needed for rendering
    """
    global start_rendering_time_new
    browser.refresh()
    is_visible(browser, SAVE_AND_PREVIEW_BTN, 20)
    do_click(browser, SAVE_AND_PREVIEW_BTN, 10)
    start_rendering_time_new = time.time() * 1000
    time.sleep(10)


def make_draft_as_published_video(browser):
    """
    On Publish Page: Makes draft published
    """
    assert is_visible(browser, EDIT_PUBLISHED_ICON_PUBLISH_PG, 10) is False
    is_visible(browser, SELECTED_DRAFT_VIDEO)
    if is_visible(browser, BLUE_TICK_ICON) is True:
        do_click(browser, BLUE_TICK_ICON)
        assert is_visible(browser, EDIT_PUBLISHED_ICON_PUBLISH_PG) is True
    else:
        do_click(browser, DOWNLOAD_PUBLISHED_VIDEO)
        do_click(browser, DOWNLOAD_HD_VIDEO)


def check_pricing_and_publish_page(browser):
    """
    User with a plan: Checks if a user sees the Publish Page
    """
    # to_delete: when new Publish Page is open to 100% + 1 month
    if is_visible(browser, PUBLISH_READY, 380) is True or is_visible(browser, CREATE_POST_BTN, 380) is True:
        get_title = browser.title
        assert get_title == publish_page_title
        print(browser.title)
        # try:
        #     # allure_screenshot(browser)
        # except WebDriverException:
        #     pass
    else:
        if is_visible(browser, PUBLISH_BTN, 28) is True:
            end_rendering_time = time.time() * 1000
            load_time(end_rendering_time, start_rendering_time, 'Rendering load time')
            do_click(browser, PUBLISH_BTN, 28)
        elif is_visible(browser, PUBLISH_BTN_NEW, 28) is True:
            end_rendering_time = time.time() * 1000
            load_time(end_rendering_time, start_rendering_time, 'Rendering load time')
            do_click(browser, PUBLISH_BTN_NEW, 40)
        elif is_visible(browser, PUBLISH_ERROR_POP_UP) is True:
            do_click(browser, PUBLISH_ERROR_POP_UP)
            do_click(browser, NEW_PROJECT_BTN)
            time.sleep(4)
            customize_chosen_template(browser)
            check_editor_page(browser)
            change_ratio(browser)
            change_text_color_and_bg(browser)
            change_font(browser)
            change_text_alignment(browser)
            publish_video(browser)
            assert (is_visible(browser, PUBLISH_READY, 280) is True or is_visible(browser, CREATE_POST_BTN,
                                                                                  180) is True)
        if is_visible(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN, 20) is True:
            if is_clickable(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN) is False:
                checkb = browser.find_element_by_css_selector(EDITORIAL_PUBLISH_CHECKBOX[1])
                browser.execute_script("arguments[0].click();", checkb)
                do_click(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN, 40)
            else:
                do_click(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN, 40)
                is_visible(browser, FOLLOW_US_PUB, 10)
                is_visible(browser, CREATE_POST_BTN, 280)
                get_title = browser.title
                assert get_title == publish_page_title
        else:
            do_click(browser, VIDEO_IS_READY_CONTINUE_BTN, 40)
            is_visible(browser, FOLLOW_US_PUB, 10)
            is_visible(browser, CREATE_POST_BTN, 280)
            get_title = browser.title
            assert get_title == publish_page_title
    # allure_screenshot(browser)


def go_back_to_editor_then_discard(browser):
    """
    Goes to the Editor to edit video and discards changes
    If a Replace Audio pop-up shows up, script closes it
    Covers two flows:
    - when there is at least one caption
    - when there is only Outro to_delete: when fix is done COR1-3402
    """
    is_visible(browser, EDIT_VIDEO, 260)
    do_click(browser, EDIT_VIDEO)
    is_visible(browser, RATIO_TOOLBAR, 40)
    if is_visible(browser, FIRST_CAPTION):
        assert is_visible(browser, DISCARD_BUTTON_DISABLED, 5) is True
        change_text_alignment(browser)
        assert is_visible(browser, DISCARD_BUTTON_DISABLED, 5) is False
    else:  # to_delete: when fix is done COR1-3402
        change_text_alignment(browser)
        assert is_visible(browser, DISCARD_BUTTON_DISABLED, 5) is False
    do_click(browser, DISCARD_BUTTON)
    do_click(browser, YES_DISCARD_BTN_ON_POP_UP)
    if is_visible(browser, AUDIO_REPLACED_POPUP) is True:
        do_click(browser, AUDIO_REPLACED_OK_BTN)
    else:
        pass
    assert is_visible(browser, DISCARD_BUTTON_DISABLED, 5) is True
    do_click(browser, SAVE_AND_PREVIEW_BTN)
    # allure_screenshot(browser)


def check_pricing_new_user(browser):
    """
    User without a plan: Checks if pricing page main text is visible and correct
    """
    if is_visible(browser, PUBLISH_READY, 380) is True:
        do_click(browser, PUBLISH_TO_SOCIAL)
        # to_improve: this if should be removed (first condition), it covers an old pricing
        if is_visible(browser, PRICING_POPUP) is True:
            assert is_visible(browser, PRICING_POPUP) is True
            if is_visible(browser, TOGGLE_ON, 10) is True:
                do_click(browser, TOGGLE_BTN, 10)
            else:
                pass
            do_click(browser, STANDARD_PLAN_CTA, 45)
            if os.environ['url'] != 'https://promo.com':
                if is_visible(browser, PAYMENT_CARD_IFRAME) is True:
                    purchase_standard_plan(browser)
                else:
                    purchase_standard_plan_new(browser)
            else:
                pass
        else:
            switch_to_iframe(browser, EMBED_PRICING_IFRAME)
            assert is_visible(browser, EMBED_PRICING_POPUP) is True
            browser.switch_to.default_content()
            currencies_check(browser)
            switch_to_iframe(browser, EMBED_PRICING_IFRAME)
            do_click(browser, CHOOSE_STANDARD_PUB)
            browser.switch_to.default_content()
            if os.environ['url'] != 'https://promo.com':
                purchase_standard_plan(browser)
            else:
                pass
        if os.environ['url'] != 'https://promo.com':
            is_visible(browser, PUBLISH_TO_SOCIAL_BACK, 30)
            do_click(browser, PUBLISH_TO_SOCIAL_BACK)
            is_visible(browser, SOCIAL_BACK_LEAVE)
            do_click(browser, SOCIAL_BACK_LEAVE)
            time.sleep(4)
        else:
            pass
        # allure_screenshot(browser)
    else:
        if is_visible(browser, PUBLISH_BTN, 28) is True:
            do_click(browser, PUBLISH_BTN, 20)
        else:
            is_visible(browser, PUBLISH_BTN_NEW, 28)
            do_click(browser, PUBLISH_BTN_NEW, 40)
        try:
            is_visible(browser, EDITORIAL_UPGRADE_NOW_BTN)
            is_visible(browser, BADGE_ON_PUBLISH_PREVIEW)
            verify_badge_and_count_text(browser)
            do_click(browser, EDITORIAL_UPGRADE_NOW_BTN)
        except (TimeoutException, NoSuchElementException):
            is_visible(browser, PRICING_TEXT, 10)
            pricing = get_element_text(browser, PRICING_TEXT)
            assert pricing == pricing_page_main_text
    # allure_screenshot(browser)


def check_starter_pricing_and_publish_page_editorial(browser):
    """
    User with a plan: Checks if he sees a Publish Page - editorial sanity
    """
    is_visible(browser, PUBLISH_BTN, 380)
    do_click(browser, PUBLISH_BTN, 40)
    assert is_visible(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN, 10) is False
    do_click(browser, EDITORIAL_UPGRADE_NOW_BTN)
    do_click(browser, EDITORIAL_UPGRADE_BUSINESS_PLAN)
    do_click(browser, CONFIRM_BTN)
    time.sleep(4)
    is_visible(browser, BADGE_ON_PUBLISH_PREVIEW)
    verify_badge_and_count_text(browser)
    assert is_clickable(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN) is False
    checkb = browser.find_element_by_css_selector(EDITORIAL_PUBLISH_CHECKBOX[1])
    browser.execute_script("arguments[0].click();", checkb)
    do_click(browser, EDITORIAL_VIDEO_IS_READY_CONTINUE_BTN, 40)
    is_visible(browser, FOLLOW_US_PUB, 10)
    is_visible(browser, CREATE_POST_BTN, 280)
    get_title = browser.title
    assert get_title == publish_page_title
    # allure_screenshot(browser)


def select_mybrand(browser):
    """
    Selects brand in the editor
    """
    is_visible(browser, MY_BRANDS_CTA)
    do_click(browser, MY_BRANDS_CTA)
    is_visible(browser, SELECT_BRAND)
    do_click(browser, SELECT_BRAND)
    time.sleep(2)
    if is_invisible(browser, EDITOR_WATERMARK) is True:
        assert is_invisible(browser, EDITOR_WATERMARK) is True
    else:
        pass
    # allure_screenshot(browser)
    if is_visible(browser, APPLY_BRAND_POP_UP) is True:
        do_click(browser, APPLY_BRAND_POP_UP_CTN_BTN)
        time.sleep(4)
    else:
        pass


def change_watermark_logo(browser):
    """
    Change Watermark and logo on Editor Page
    """
    action = ActionChains(browser)
    try:
        is_visible(browser, EDITOR_WATERMARK)
        do_click(browser, EDITOR_WATERMARK)
    except (TimeoutException, NoSuchElementException):
        is_visible(browser, EDITOR_WATERMARK_IMAGE)
        for logo_btn in range(2):
            do_click(browser, EDITOR_WATERMARK_IMAGE)
        for logo_btnn in range(2):
            do_click(browser, EDITOR_WATERMARK_IMAGE_AGAIN)
    is_visible(browser, UPLOAD_IMAGE)
    do_send_keys(browser, UPLOAD_IMAGE, os.getcwd() + watermark_image)
    is_visible(browser, IMAGE_DONE_BTN)
    do_click(browser, IMAGE_DONE_BTN)
    # allure_screenshot(browser)
    is_visible(browser, CROSS_BTN)
    do_click(browser, CROSS_BTN)
    is_visible(browser, OUTRO_BTN)
    do_click(browser, OUTRO_BTN)
    try:
        is_visible(browser, LOGO_EDITOR_BTN)
        for logo_btn in range(2):
            do_click(browser, LOGO_EDITOR_BTN)
        action.double_click(on_element=browser.find_element_by_xpath(LOGO_EDITOR_BTN[1])).perform()
    except (NoSuchElementException, TimeoutException):
        is_visible(browser, EDITOR_LOGO_IMAGE)
        for logo_btn in range(2):
            do_click(browser, EDITOR_LOGO_IMAGE)
        action.double_click(on_element=browser.find_element_by_xpath(EDITOR_LOGO_IMAGE[1])).perform()
    do_send_keys(browser, UPLOAD_IMAGE, os.getcwd() + logo_image)
    # allure_screenshot(browser)
    is_visible(browser, CROSS_BTN)
    do_click(browser, CROSS_BTN)


def goto_brands_from_editor(browser):
    """
    Goto Brand Manager Tab from Editor page
    """
    is_visible(browser, MY_BRANDS_CTA)
    do_click(browser, MY_BRANDS_CTA)
    try:
        is_visible(browser, ADD_BRAND_EDITOR)
        do_click(browser, ADD_BRAND_EDITOR)
        is_visible(browser, CREATE_BRAND_EDITOR)
        do_click(browser, CREATE_BRAND_EDITOR)
    except (TimeoutException, NoSuchElementException):
        is_visible(browser, MANAGE_BRANDS_CTA)
        do_click(browser, MANAGE_BRANDS_CTA)
        is_visible(browser, MANAGE_BRAND_CONF)
        do_click(browser, MANAGE_BRAND_CONF)
    # allure_screenshot(browser)


def assert_brand_images(browser):
    """
    Verify the Brand Watermark and Logo is Synced on Editor or not
    """
    assert is_visible(browser, EDITOR_WATERMARK_IMAGE) is True
    # allure_screenshot(browser)
    do_click(browser, OUTRO_BTN)
    assert is_visible(browser, EDITOR_LOGO_IMAGE) is True
    # allure_screenshot(browser)


def change_video_name(browser):
    """
    Changes video name
    """
    if is_visible(browser, PUBLISH_READY, 380) is True or is_visible(browser, CREATE_POST_BTN, 380) is True:
        assert browser.title == publish_page_title
        if is_visible(browser, DRAFT_VIDEO_NAME):
            do_clear(browser, DRAFT_VIDEO_NAME)
            do_send_keys(browser, DRAFT_VIDEO_NAME, drafted_video_name)
    else:
        if is_visible(browser, VIDEO_NAME_EDIT_NEW, 28) is True:
            for i in range(30):
                do_send_keys(browser, VIDEO_NAME_EDIT_NEW, Keys.BACKSPACE)
            do_send_keys(browser, VIDEO_NAME_EDIT_NEW, drafted_video_name)
            time.sleep(1)
            do_send_keys(browser, VIDEO_NAME_EDIT_NEW, Keys.ENTER)
        else:
            is_visible(browser, VIDEO_NAME_EDIT, 28)
            for i in range(30):
                do_send_keys(browser, VIDEO_NAME_EDIT, Keys.BACKSPACE)
            do_send_keys(browser, VIDEO_NAME_EDIT, drafted_video_name)
            time.sleep(1)
            do_send_keys(browser, VIDEO_NAME_EDIT, Keys.ENTER)
        # allure_screenshot(browser)
