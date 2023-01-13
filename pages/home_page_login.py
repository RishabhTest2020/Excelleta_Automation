import os
import statistics

import allure
from allure_commons.types import AttachmentType
from locators.locators_file import *
from test_data.testdata import *
from helpers.common_helpers import *
from helpers.generator import *
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import pytest
import logging


def home_page_url(browser):
    """
    Opens main page
    If statement created for BrowserStack
    """
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    browser.get(base_url)


def promo_pages_urls(browser):
    """
    Opens Promo URLs and check performance
    Sends message to Slack
    """
    global back_perf_mean, front_perf_mean
    performance_data = []
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    for u in urls:
        back_perf = []
        front_perf = []
        for n in range(5):
            browser.get(u)
            wait_for_ajax(browser)
            navigationStart = browser.execute_script("return window.performance.timing.navigationStart")
            responseStart = browser.execute_script("return window.performance.timing.responseStart")
            domComplete = browser.execute_script("return window.performance.timing.domComplete")
            back_perf.append((responseStart - navigationStart)/1000)
            front_perf.append((domComplete - responseStart)/1000)
        back_perf_mean = statistics.mean(back_perf)
        front_perf_mean = statistics.mean(front_perf)
        performance_data.append(u + ': BPC: ' + str(back_perf_mean) + 's' + ', FPC: ' + str(front_perf_mean) + 's')
    print(performance_data)
    perf_srt_data = str('\n'.join(performance_data))
    if (back_perf_mean <= 1 and front_perf_mean <= 1) is True:
        slack_color = "#00FF00"
    else:
        slack_color = "#FF0000"
    slack_message(username='Promo Pages Performance', text=str(perf_srt_data), color=slack_color)
    browser.execute_script\
        ('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Performance Report sent on slack "}}')


def go_to_url(browser, url):
    """
    Opens desired url
    If statement created for BrowserStack and Headless
    """
    if os.environ['browser'] == 'headless_chrome':
        browser.get(url)
    else:
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        browser.get(url)


def click_home_login_button(browser):
    """
    Clicks on login button
    """
    try:
        do_click(browser, LOGIN_BTN, 10)
        time.sleep(2)
    except WebDriverException:
        browser.refresh()
        time.sleep(1)
        do_click(browser, LOGIN_BTN, 10)


def enter_email(browser):
    """
    Enters e-mail on login page
    """
    try:
        switch_to_iframe(browser, LOGIN_FRAME, 20)
        do_send_keys(browser, USER_EMAIL_TEXTBOX, email, 10)
    except (NoSuchElementException, TimeoutException):
        browser.refresh()
        click_home_login_button(browser)
        switch_to_iframe(browser, LOGIN_FRAME, 20)
        do_send_keys(browser, USER_EMAIL_TEXTBOX, email, 10)


def enter_password(browser):
    """
    Enters correct password
    """
    do_send_keys(browser, USER_PASSWORD_TEXTBOX, read_creds(password, 0), 10)


def enter_wrong_password(browser):
    """
    Enters wrong password, generated randomly
    """
    wrong_pass = random_password_string(7)
    do_send_keys(browser, USER_PASSWORD_TEXTBOX, wrong_pass, 10)


def click_login(browser):
    """
    Clicks login button on login page
    """
    do_click(browser, LOGIN_FRAME_BTN, 10)


def go_to_create_page(browser):
    """
    Goes to Create Page
    """
    is_visible(browser, CREATE_NOW_CTA)
    do_click(browser, CREATE_NOW_CTA, 5)
    time.sleep(3)
    # allure_screenshot(browser)


def create_page_redirection(browser):
    """
    Simulates redirection after login
    """
    try:
        browser.switch_to.default_content()
    except WebDriverException:
        pass
    title = browser.title
    assert title == create_page_title
    if is_visible(browser, HELP_US_TEXT):
        do_click(browser, CLOSE_BUTTON)
    else:
        pass
    # allure_screenshot(browser)


def check_correct_username(browser):
    """
    Checks if user is logged correctly
    """
    is_visible(browser, USERNAME_MENU, 15)
    assert get_element_text(browser, USERNAME_MENU) == fullname


def empty_textbox_error(browser):
    """
    Checks error message for empty input
    """
    error_message = get_element_text(browser, EMPTY_FIELD_ERROR)
    print(error_message)
    assert error_message == empty_textbox_message
    # allure_screenshot(browser)


def wrong_login_creds_error(browser):
    """
    Checks error message for wrong credentials
    """
    error = get_element_text(browser, WRONG_CREDS_ERROR)
    # allure_screenshot(browser)
    print(error)
    assert error == wrong_creds_message
    # allure_screenshot(browser)


def sign_out_process(browser):
    """
    Signs out from Promo account
    """
    do_hover(browser, USERNAME_MENU)
    if is_visible(browser, SIGN_OUT_NEW) is True:
        do_click(browser, SIGN_OUT_NEW)
    else:
        do_click(browser, SIGN_OUT)
    time.sleep(3)
    assert is_visible(browser, SIGNUP_BTN, 25) is True
    # allure_screenshot(browser)

