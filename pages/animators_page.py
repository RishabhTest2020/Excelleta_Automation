import os
import time
from os import scandir
from _pytest import pathlib
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.remote.file_detector import LocalFileDetector

from helpers.common_helpers import *
from test_data.testdata import *
from locators.locators_file import *


def enable_APE_chrome_extension(browser):
    """

    Args:
        browser:

    Open chrome extension page and enable developer mode

    """
    browser.get(chrome_extension_url)
    browser.switch_to.window(browser.window_handles[1])
    browser.execute_script('document.querySelector("body > extensions-manager").shadowRoot.querySelector("extensions-toolbar").shadowRoot.querySelector("#devMode").click();')


def open_animation_preview_tab(browser):
    """

    Args:
        browser:

    Open all animation tabs

    """
    browser.execute_script("window.open('');")
    window_after = browser.window_handles[2]
    browser.switch_to.window(window_after)
    browser.get(animation_preview_tab_A)
    browser.execute_script("window.open('');")
    window_after = browser.window_handles[3]
    browser.switch_to.window(window_after)
    browser.get(animation_preview_tab_B)
    browser.execute_script("window.open('');")
    window_after = browser.window_handles[4]
    browser.switch_to.window(window_after)
    time.sleep(2)
    browser.get(ape_url)
    is_visible(browser, CONNECT_BUTTON, 10)
    time.sleep(2)
    do_click(browser, CONNECT_BUTTON, 10)
    is_visible(browser, CHOOSE_FILE_BUTTON, 10)


def animations_send_keys_path(item, elem):
    """

    Args:
        item: Animation folder
        elem: send_keys function to upload files

    Returns:

    """
    files_path = os.getcwd() + '/promoanimations/' + item
    dir_list_json = os.listdir(files_path)
    json_files = []
    for js_file in dir_list_json:
        json_files.append(f"{os.getcwd()}/promoanimations/{item}/{js_file}")
    # animation_files = ', '.join('"' + i + '"' for i in json_files)
    if len(dir_list_json) == 3:
        elem.send_keys(f"{json_files[0]}", "\n", f"{json_files[1]}", "\n", f"{json_files[2]}")
    elif len(dir_list_json) == 1:
        elem.send_keys(f"{json_files[0]}")
    elif len(dir_list_json) == 6:
        elem.send_keys(f"{json_files[0]}", "\n", f"{json_files[1]}", "\n", f"{json_files[2]}", "\n", f"{json_files[3]}"
                       , "\n", f"{json_files[4]}", "\n", f"{json_files[5]}")
    elif len(dir_list_json) == 9:
        elem.send_keys(f"{json_files[0]}", "\n", f"{json_files[1]}", "\n", f"{json_files[2]}", "\n", f"{json_files[3]}"
                       , "\n", f"{json_files[4]}", "\n", f"{json_files[5]}", "\n", f"{json_files[6]}"
                       , "\n", f"{json_files[7]}", "\n", f"{json_files[8]}")
    else:
        print(item + ' has ' + str(len(dir_list_json)) + ' json files')


def refresh_all_tabs(browser):
    """

    Args:
        browser:

    To refresh all tabs

    """
    Windows = browser.window_handles
    for window in Windows:
        browser.switch_to.window(window)
        browser.refresh()
        time.sleep(2)


def run_animations(browser, start_range, end_range):
    """

    Args:
        end_range: animation folder end len
        start_range: animation folder start len
        browser:

    Returns: check animations and send slack notification

    """
    path = os.getcwd() + '/promoanimations'
    dir_list = os.listdir(path)
    print(dir_list)
    nwnanimation = []
    for i in range(start_range, end_range):
        print(len(dir_list))
        item = dir_list[i]
        try:
            refresh_all_tabs(browser)
            window_after = browser.window_handles[4]
            browser.switch_to.window(window_after)
        except UnexpectedAlertPresentException:
            browser.switch_to.alert.accept()
            browser.refresh()
        time.sleep(2)
        do_click(browser, CONNECT_BUTTON, 10)
        elem = browser.find_element(By.XPATH, CHOOSE_FILE_BUTTON[1])
        browser.execute_script("arguments[0].removeAttribute('webkitdirectory');", elem)
        browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", elem, "multiple", "")
        animations_send_keys_path(item, elem)
        start_time = time.time()
        while time.time() <= start_time + 400:
            time.sleep(2)
            print('animation in process...')
            if is_alert_present(browser) is True:
                time.sleep(2)
                alert_message = browser.switch_to.alert
                alert_message_text = alert_message.text
                print("Alert" + alert_message_text)
                if alert_message_text == 'Finished!':
                    print('animation completed')
                    browser.switch_to.alert.accept()
                else:
                    browser.switch_to.alert.accept()
                    nwnanimation.append(item)
                break
    code_green = '#00FF00'
    code_red = '#FF0000'
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    if 'first' in test_name:
        username = 'Animation Test first half'
    else:
        username = 'Animation Test second half'
    if len(nwnanimation) == 0:
        slack_message(username, f'all {len(dir_list)/2} passed :tada:', code_green, environment="Promo Animations")
    else:
        not_working = (', '.join(nwnanimation))
        print(not_working)
        errors = get_error_console_logs(browser)
        error_string = str(', '.join(errors))
        slack_message(username, f'Failed Animations: {not_working} \n {error_string}', code_red, environment="Promo Animation")
























