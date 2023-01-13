from pytest_bdd import when, then
from selenium.common.exceptions import WebDriverException
from pages.editor_page import *
from pages.newcancellation_page import *


# Navigation
@then('I verify navigation to editor page')
def verify_editor_navigation(browser):
    try:
        check_editor_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_editor_navigation)


@then('I add 2nd Caption and change font color')
def add_caption_in_editor(browser):
    try:
        add_caption(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_caption_in_editor)


@then('I verify play pause buttons and timeline options')
def timeline_actions(browser):
    try:
        # verify_play_n_pause_buttons(browser)
        # to_improve: uncomment when issue with Play and Pause btn is resolved
        edit_actions_on_timeline(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, timeline_actions)


@then('I verify navigation to editor page new user')
def verify_editor_navigation_new_user(browser):
    try:
        check_editor_page_new_user(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_editor_navigation_new_user)


# Tabs
@then('I am going to editor tab')
def go_editor_tab(browser):
    try:
        go_to_editor_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_editor_tab)


@then('I am going to media tab')
def go_media_tab(browser):
    try:
        go_to_media_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_media_tab)


@then('I go to music tab')
def go_to_music(browser):
    try:
        go_to_music_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, go_to_music)


# Editor features
@allure.severity(allure.severity_level.NORMAL)
@then('I am changing ratio')
def change_ratio_in_editor(browser):
    try:
        change_ratio(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_ratio_in_editor)


@allure.severity(allure.severity_level.NORMAL)
@then('I am changing font color')
def change_font_color_in_editor(browser):
    try:
        change_text_color_and_bg(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_font_color_in_editor)


@then('I am changing outro background')
def change_outro_bg(browser):
    try:
        change_outro_background(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_outro_bg)


@then('I upload a watermark and add it')
def watermark_upload(browser):
    try:
        upload_watermark(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, watermark_upload)


@then('I upload a logo and add it')
def logo_upload(browser):
    try:
        upload_logo(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, logo_upload)


@then('I upload font and add it')
def font_upload(browser):
    try:
        upload_font(browser)
        upload_font_google(browser, 'Pridi')
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, font_upload)


@then('I add characters in text animation')
def add_characters_in_text_animation(browser):
    try:
        add_characters(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_characters_in_text_animation)


@allure.severity(allure.severity_level.NORMAL)
@then('I am changing the font')
def change_the_font(browser):
    try:
        change_font(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_the_font)


@then('I am changing text alignment')
def change_alignment(browser):
    try:
        change_text_alignment(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_alignment)


@then('I am changing capitalization style')
def change_capitalization(browser):
    try:
        change_text_to_lowercase(browser)
        change_text_to_uppercase(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_capitalization)


@then('I change text positions')
def change_text_positions(browser):
    try:
        change_text_position(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, change_text_positions)


@then('I change text style once')
def changes_text_style(browser):
    try:
        change_text_style(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, changes_text_style)


@then('I verify all text styles') # full regression step
def verify_text_style(browser):
    try:
        verify_text_all_styles(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_text_style)


# Media -  Photos
@then('I am uploading a photo and replacing')
def upload_a_photo(browser):
    try:
        go_to_media_tab(browser)
        upload_photo_in_media_tab(browser)
        # replace_added_photo(browser)  # need fixes
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, upload_a_photo)


@then('I select a photo and add it')
def promo_select_a_photo(browser):
    try:
        select_a_photo_and_add_to_project(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, promo_select_a_photo)


@then('I am previewing a photo')
def promo_photo_preview(browser):
    try:
        preview_a_photo_and_close(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, promo_photo_preview)


@then('I am adding a new clip')
def add_new_video_clip_to_project(browser):
    try:
        go_to_media_tab(browser)
        search_video_in_media_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_new_video_clip_to_project)


@then('I am adding a 4 new premium clips')
def add_new_video_clip_to_project(browser):
    try:
        add_4_pcs(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, add_new_video_clip_to_project)


@then('I am changing transitions')
def transition_changes(browser):
    try:
        change_video_transitions(browser)
        change_photo_transitions(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, transition_changes)


@then('I change outros')
def verify_outros(browser):
    try:
        changes_outros(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_outros)


# Media - Videos
@then('I verify added favourites media')
def verify_added_favourites(browser):
    try:
        go_to_media_tab(browser)
        verify_favourites(browser)
        remove_from_favourites(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_added_favourites)


@then('I am uploading a video')
def upload_a_video(browser):
    try:
        upload_video_in_media_tab(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, upload_a_video)


@then('I am filtering premium videos')
def premium_videos_filter(browser):
    try:
        go_to_media_tab(browser)
        filter_premium_media_search(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, premium_videos_filter)


@then('I am filtering editorial videos and photos')
def premium_videos_filter(browser):
    try:
        go_to_media_tab(browser)
        filter_editorial_media_search(browser)
        filter_editorial_media_photos_search(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, premium_videos_filter)


# Music
@then('I verify category and sub category of Music Library')
def verify_music_libraries(browser):
    try:
        go_to_music_tab(browser)
        music_filter(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_music_libraries)


@then('I upload audio and delete it')
def upload_audio_and_delete(browser):
    try:
        upload_music_and_delete(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, upload_audio_and_delete)


@then('I select an audio')  # for now not in use
def select_audio(browser):
    try:
        select_an_audio(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, select_audio)


@then('I upload an audio and select it')
def select_uploaded_audio(browser):
    try:
        upload_audio_and_select(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, select_uploaded_audio)


# Publish
@allure.severity(allure.severity_level.NORMAL)
@when('I Publish the video')
def publish_editor_video(browser):
    try:
        publish_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_editor_video)


# @then('I purchase a plan to upload watermark')
# def watermark_upload_with_plan(browser):
#     try:
#         purchase_plan_for_watermark_upload(browser)
#     except (Exception, WebDriverException):
#         bs_fail_with_traceback(browser, watermark_upload_with_plan)


@when('I Publish the video as new user')
def publish_editor_video_new_user(browser):
    try:
        publish_video_new_user(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, publish_editor_video_new_user)


@then('I edit published video from Dashboard')
def edit_published_video_dashboard(browser):
    try:
        edit_published_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, edit_published_video_dashboard)


@allure.severity(allure.severity_level.NORMAL)
@then('I verify pricing/publish navigation')
def verify_pricing_nav(browser):
    try:
        check_pricing_and_publish_page(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_pricing_nav)


@then('I make a draft as published on Publish Page')
def make_draft_as_published(browser):
    try:
        make_draft_as_published_video(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, make_draft_as_published)


@then('I go back to editor and discard the changes')
def back_to_editor_discard(browser):
    try:
        go_back_to_editor_then_discard(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, back_to_editor_discard)


@allure.severity(allure.severity_level.NORMAL)
@then('I verify pricing/publish navigation new user')
def verify_pricing_nav_new_user(browser):
    try:
        check_pricing_new_user(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_pricing_nav_new_user)


@allure.severity(allure.severity_level.NORMAL)
@then('I verify pricing/publish navigation for editorial video')
def verify_pricing_editorial_nav(browser):
    try:
        check_pricing_and_publish_page_editorial_suite(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_pricing_editorial_nav)


@allure.severity(allure.severity_level.NORMAL)
@then('I verify starter plan pricing/publish navigation for editorial video')
def verify_pricing_editorial_starter_nav(browser):
    try:
        check_starter_pricing_and_publish_page_editorial(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, verify_pricing_editorial_starter_nav)


# Brand and watermark
@allure.severity(allure.severity_level.NORMAL)
@then('I select My Brand')
def select_brand(browser):
    try:
        select_mybrand(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, select_brand)


@allure.severity(allure.severity_level.NORMAL)
@then('I change watermark and logo on editor page')
def check_brand_watermark(browser):
    try:
        change_watermark_logo(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_brand_watermark)


@allure.severity(allure.severity_level.NORMAL)
@then('Goto Brand Manager from Editor page')
def check_brand_images(browser):
    try:
        goto_brands_from_editor(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_brand_images)


@allure.severity(allure.severity_level.NORMAL)
@then('I verify brand logo and watermark synced on editor')
def check_brand_images(browser):
    try:
        assert_brand_images(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, check_brand_images)


@allure.severity(allure.severity_level.NORMAL)
@then('I change video name')
def edit_video_name(browser):
    try:
        change_video_name(browser)
    except (Exception, WebDriverException):
        bs_fail_with_traceback(browser, edit_video_name)
