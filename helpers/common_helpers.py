import binascii
import json
import os
import pdb
import sys
import time
import traceback
from datetime import date, datetime

import pytest
import requests
from google.auth.exceptions import TransportError
from gspread.exceptions import APIError, GSpreadException
from pytz import reference
import allure
from allure_commons.types import AttachmentType
from requests import ReadTimeout
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException, \
    NoSuchWindowException, ElementClickInterceptedException, WebDriverException, InvalidArgumentException, \
    NoSuchFrameException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators_file import *


try:
    from helpers.googlesheet import *
except (TransportError, APIError, GSpreadException, ReadTimeout):
    pass
except:
    pass
import slack
try:
    Browser = os.environ['browser']
except KeyError:
    pass


def wait_for_ajax(browser):
    wait = WebDriverWait(browser, 300)
    try:
        wait.until(lambda ajwait: browser.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass


def take_screenshot(browser):
    """
    Takes a screenshot and saves it in png file
    Args:
        browser: webdriver
    """
    if sys.platform == 'linux':
        try:
            browser.save_screenshot(os.getcwd() + '/files/' + 'ss' + time.strftime("%Y%m%d-%H%M%S") + '.png')
        except (WebDriverException, Exception):
            pass
    else:
        pass


def do_click(browser, by_locator: object, sec=10):
    """
    Waits and clicks on the chosen element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    try:
        WebDriverWait(browser, sec, poll_frequency=0.4).until(
            EC.element_to_be_clickable(by_locator)).click()
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e
    # except (ElementClickInterceptedException, TimeoutException) as dcc:
    #     print(str(dcc))
    #     switch_to_iframe(browser, SKIP_OFFER_MODAL_FRAME, sec)
    #     do_click(browser, SKIP_OFFER_MODAL_BTN)
    #     browser.switch_to.default_content()
    #     WebDriverWait(browser, sec).until(
    #         EC.element_to_be_clickable(by_locator)).click()


def do_double_click(browser, by_locator, sec=5):
    """
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        browser.execute_script("var evt = document.createEvent('MouseEvents');" +
        "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" +
        "arguments[0].dispatchEvent(evt);", elem)
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def do_hover(browser, by_locator, sec=5):
    """
    Hovers over element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        ActionChains(browser).move_to_element(elem).perform()
    except AttributeError as e:
        if str(e) == "move_to requires a WebElement":
            raise NoSuchElementException
        else:
            raise e
    # take_screenshot(browser)


def do_hover_offset(browser, by_locator, x, y, sec=5):
    """
    Hovers over an element with a specific offset
    Args:
        browser: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
        x: first offset parameter
        y: second offset parameter
    """
    wait_for_ajax(browser)
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        ActionChains(browser).move_to_element_with_offset(elem, x, y).perform()
    except AttributeError as e:
        if str(e) == "move_to requires a WebElement":
            raise NoSuchElementException
        else:
            raise e


def do_click_offset(browser, by_locator, x, y, sec=5):
    """
    Click an element with a specific offset
    Args:
        browser: webdriver
        by_locator (str): chosen locator from locators/locators_file.py
        sec (int): default time to wait
        x: first offset parameter
        y: second offset parameter
    """
    wait_for_ajax(browser)
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        ActionChains(browser).move_to_element_with_offset(elem, x, y).click().perform()
    except AttributeError as e:
        if str(e) == "move_to requires a WebElement":
            raise NoSuchElementException
        else:
            raise e


def drag_and_drop(browser, by_locator_source, by_locator_target, sec=5):
    """
    Drag and drop from source to targeted element
    Args:
        browser: webdriver
        by_locator_source (str): chosen source locator from locators/locators_file.py
        by_locator_target (str): chosen target locator from locators/locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    source = WebDriverWait(browser, sec).until(
        EC.visibility_of_element_located(by_locator_source))
    target = WebDriverWait(browser, sec).until(
        EC.visibility_of_element_located(by_locator_target))
    action = ActionChains(browser)
    action.drag_and_drop(source, target).perform()


def do_send_keys(browser, by_locator, text, sec=5):
    """
    Sends keys to the chosen element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        text (str): text to be send
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    try:
        WebDriverWait(browser, sec, poll_frequency=0.4).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def get_element_text(browser, by_locator: object):
    """
    Gets text of the chosen element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
    """
    wait_for_ajax(browser)
    try:
        elem_text = WebDriverWait(browser, 30, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator)).text
        return elem_text
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        elif str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def get_css_value(browser, by_locator, property_name):
    """
    Gets text of the chosen element
    Args:
        property_name: add css property name
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
    """
    wait_for_ajax(browser)
    try:
        elem = WebDriverWait(browser, 30, poll_frequency=0.4).until(
            EC.presence_of_element_located(by_locator))
        elem_value = elem.value_of_css_property(property_name)
        return elem_value
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        elif str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def is_visible(browser, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is visible
    Args:
        browser: webdriver
        by_locator(tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    wait_for_ajax(browser)
    if Browser != "headless_chrome":
        take_screenshot(browser)
    else:
        pass
    elem = False
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4, ignored_exceptions=WebDriverException).until(EC.visibility_of_element_located(by_locator))
    except (WebDriverException, Exception, TimeoutException):
        return bool(elem)
    return bool(elem)


def is_invisible(browser, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is invisible
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    wait_for_ajax(browser)
    elem = False
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4, ignored_exceptions=WebDriverException).until(EC.invisibility_of_element_located(by_locator))
    except (WebDriverException, Exception):
        return bool(elem)
    return bool(elem)


def is_clickable(browser, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is clickable
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    wait_for_ajax(browser)
    elem = False
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(EC.element_to_be_clickable(by_locator))
    except (TimeoutException, NoSuchElementException, AttributeError):
        return bool(elem)
    return bool(elem)


def switch_to_iframe(browser, by_locator, sec=10):
    """
    Switches to the chosen iframe
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
    try:
        WebDriverWait(browser, sec, poll_frequency=0.4).until(EC.frame_to_be_available_and_switch_to_it(by_locator))
    except InvalidArgumentException as e:
        if ("Message: invalid argument: missing 'ELEMENT'" in str(e)) is True:
            raise NoSuchElementException
        else:
            raise e


def do_clear(browser, by_locator, sec=5):
    """
    Clears textfield or input
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    try:
        WebDriverWait(browser, sec, poll_frequency=0.4).until(EC.visibility_of_element_located(by_locator)).clear()
    except AttributeError as e:
        if str(e) == "'dict' object has no attribute 'is_displayed'":
            raise NoSuchElementException
        else:
            raise e


def is_alert_present(browser, sec=5) -> bool:
    """
    Waits and checks if alert is present
    Args:
        browser: webdriver
        sec (int): default time to wait
    Returns:
        True or False
    """
    elem = False
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(EC.alert_is_present())
    except (TimeoutException, NoSuchElementException):
        return bool(elem)
    return bool(elem)


def is_title_true(browser, title, sec=5) -> bool:
    elem = False
    try:
        elem = WebDriverWait(browser, sec).until(lambda x: title in browser.title)
    except (NoSuchElementException, TimeoutException) as e:
        return bool(elem)
    return bool(elem)


# def allure_screenshot(browser):
#     """
#     Args:
#         browser: webdriver
#
#     Returns: Takes a screenshot and saves it in png file and represent in allure reports
#
#     """
#     try:
#         allure.attach(browser.get_screenshot_as_png(), name='ss' + time.strftime("%Y%m%d-%H%M%S") + '.png',
#                       attachment_type=AttachmentType.PNG)
#     except binascii.Error:
#         pass


def read_creds(file_dir: str, line_num: int) -> str:
    """
    Reads credential information from the file
    Args:
        file_dir (str): path to the file
        line_num (int): line number we want to use
    Returns:
        Credentials (str)
    """
    f = open(os.getcwd() + file_dir, "r")
    read = f.readlines()
    return read[line_num]


def read_creds_chars(file_dir: str, line_num: int, char_num: int) -> str:
    """
    Reads credential information and characters from the file
    Args:
        line_num (int): line number we want to use
        char_num(int): char number we want to use
        file_dir (str): path to the file
    Returns:
        Credentials (str)
    """
    f = open(os.getcwd() + file_dir, "r")
    read = f.readlines()
    read_char = read[line_num]
    return read_char[char_num]


def skip_offer_modal(browser, sec=15):
    """
    Skips any marketing modals by clicking on X
    """
    try:
        switch_to_iframe(browser, SKIP_OFFER_MODAL_FRAME, sec)
        do_click(browser, SKIP_OFFER_MODAL_BTN)
        browser.switch_to.default_content()
    except (TimeoutException, NoSuchWindowException, NoSuchElementException, StaleElementReferenceException,
            ElementClickInterceptedException, InvalidArgumentException) as som:
        pass


def load_time(end_load_time, start_load_time, load_time_name):
    """
    Prints a load time
    Args:
        end_load_time: time when load ended
        start_load_time: time when load started
        load_time_name: name of the load time
    """
    result_rendering_time = end_load_time - start_load_time
    print(load_time_name, result_rendering_time, 'milliseconds')


def today_date():
    """
    Returns current date and time
    """
    dt = date.today()
    ht = datetime.now()
    tz = reference.LocalTimezone()
    time_zone = tz.tzname(ht)
    date_and_time = dt.strftime("%d/%m/%Y") + " " + ht.strftime("%H:%M") + " " + time_zone
    return date_and_time


def get_error_console_logs(browser):
    """
    Args:
        browser:
    Returns: Error logs
    """
    error_logs = []
    browser_logs = browser.get_log('browser')
    for entry in browser_logs:
        if entry['level'] == 'SEVERE' or entry['level'] == 'ERROR' or entry['level'] == 'CRITICAL' or entry['level'] == 'INFO':
            if entry['source'] == 'javascript':
                error_logs.append(entry['message'])
            else:
                pass
        else:
            pass
    return error_logs


def slack_message(username, text, color, environment="Promo Production"):
    """
    Function sends Slack alerts and reports
    Username: Add custom slack username
    Text: the text message as string
    Environment: Promo ENV details default it's Promo Production
    """
    token = os.environ["SLACK_WEBHOOK"]
    url = token
    message = (text)
    title = (environment + ' ' + today_date())
    slack_data = {
        "username": username,
        # "icon_emoji": ":satellite:", # keeping this code for reference
        "attachments": [
            {
                "color": color,
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


def bs_fail_with_traceback(browser, main_func):
    """
    Function injects a failed step to Browser Stack
    Args:
        browser: webdriver
        main_func: name of the function
    """
    func_name = main_func.__name__
    if os.environ['browser'] == 'browserstack':
        errors = get_error_console_logs(browser)
        error_string = str(', '.join(errors))
        step_logs = func_name + ", LOGs: " + error_string
        print(error_string)
        import pprint
        pprint.pprint(error_string)
        take_screenshot(browser)
        try:
            browser.execute_script(
                f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": "Failed Step: {step_logs}"}}}}')
        except WebDriverException:
            try:
                browser.execute_script(
                    f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": "Failed Step: {func_name}"}}}}')
            except WebDriverException:
                browser.execute_script(
                    'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Test failed"}}')
    else:
        take_screenshot(browser)
        errors = get_error_console_logs(browser)
        print(errors)
        import pprint
        pprint.pprint(errors)
        pass
    raise AssertionError(func_name, traceback)


def google_analytics(browser):
    """
    Function returns a list of  Google events displayed in console
    """
    google_events = []
    goog_data = []
    analytics_data = browser.execute_script("return analitycDebug;")
    ad_sent_len = len(analytics_data['sent'])
    for n in range(int(ad_sent_len)):
        events_service = analytics_data['sent'][n]['service']
        events_data = analytics_data['sent'][n]['eventData']
        event_name = analytics_data['sent'][n]['eventName']
        goog_data.append(events_service + ': ' + event_name + ' - ' + str(events_data))
        if events_service == 'google':
            google_events.append(event_name)
        else:
            pass
    return google_events
    # data_string = str('\n'.join(data))
    # har_file = open(os.getcwd() + '/files/analytics_data.txt', 'w') Keeping this code to get events in file
    # har_file.write(data_string)
    # har_file.close()


def mixpanel_analytics(browser):
    """
    Function returns a list of Mixpanel events displayed in console
    """
    mixpanel_events = []
    mix_data = []
    analytics_data = browser.execute_script("return analitycDebug;")
    ad_sent_len = len(analytics_data['sent'])
    for n in range(int(ad_sent_len)):
        events_service = analytics_data['sent'][n]['service']
        events_data = analytics_data['sent'][n]['eventData']
        event_name = analytics_data['sent'][n]['eventName']
        mix_data.append(events_service + ': ' + event_name + ' - ' + str(events_data))
        if events_service == 'google':
            mixpanel_events.append(event_name)
        else:
            pass
    return mixpanel_events


def assert_analytics_events(browser, page_google_events, page_mixpanel_events):
    """
    Function compares actual list with expected list
    Args:
        browser: webdriver
        page_google_events: list of Google events
        page_mixpanel_events: list of Mixpanel events
    """
    google_events = google_analytics(browser)
    mixpanel_events = mixpanel_analytics(browser)
    for g in page_google_events:
        for ge in google_events:
            if g == ge:
                print('Google events triggered')
                break
        else:
            print(g + ' is not triggered')
            for nn in range(0, 1):
                try:
                    new_insert_row(events_sheet)
                except APIError:
                    pass
            new_format_cells(events_sheet, "A1:C1", "blue", 50, True)
            new_update_cell(events_sheet, 1, 1, 'Date')
            new_update_cell(events_sheet, 1, 2, 'Event Name')
            new_update_cell(events_sheet, 1, 3, 'Event Service')
            new_format_cells(events_sheet, "A2:C2", "green", 50, True)
            new_update_cell(events_sheet, 2, 1, today_date())
            new_update_cell(events_sheet, 2, 2, g)
            new_update_cell(events_sheet, 2, 3, 'Google Service')
            pass
    for m in page_mixpanel_events:
        for me in mixpanel_events:
            if m == me:
                print('Mixpanel events triggered')
                break
        else:
            print(m + ' is not triggered')
            for nn in range(0, 1):
                try:
                    new_insert_row(events_sheet)
                except APIError:
                    pass
            new_format_cells(events_sheet, "A1:C1", "blue", 50, True)
            new_update_cell(events_sheet, 1, 1, 'Date')
            new_update_cell(events_sheet, 1, 2, 'Event Name')
            new_update_cell(events_sheet, 1, 3, 'Event Service')
            new_format_cells(events_sheet, "A2:C2", "green", 50, True)
            new_update_cell(events_sheet, 2, 1, today_date())
            new_update_cell(events_sheet, 2, 2, m)
            new_update_cell(events_sheet, 2, 3, 'Mixpanel Service')
            pass


def assert_analytics_events_with_slack(google_events, page_google_events, mixpanel_events,
                                       page_mixpanel_events, Scenario):
    """
    Function compares actual list with expected list
    Args:
        Scenario: To specify the events of scenario
        page_google_events: list of Google events
        page_mixpanel_events: list of Mixpanel events
        Send report on slack
    """
    url = os.environ['url']
    ge_not_triggered = []
    me_not_triggered = []
    for g in page_google_events:
        for ge in google_events:
            if g == ge:
                print('Google events triggered')
                break
        else:
            print(g + ' is not triggered')
            ge_not_triggered.append(g)
    for m in page_mixpanel_events:
        for me in mixpanel_events:
            if m == me:
                print('Mixpanel events triggered')
                break
        else:
            print(m + ' is not triggered')
            me_not_triggered.append(m)
    if (len(ge_not_triggered) == 0 and len(me_not_triggered) == 0) is True:
        slack_color = "#00FF00"
        slack_test = "All analytics events triggered successfully"
    else:
        slack_color = "#FF0000"
        ge_not_triggered_events = str('\n'.join(ge_not_triggered))
        me_not_triggered_events = str('\n'.join(me_not_triggered))
        slack_test = str("Google Events:" + '\n' + ge_not_triggered_events + "\n" + "\n" +
                         "Mixpanel Events:" + "\n" + me_not_triggered_events)
    slack_message(username=f'Promo Analytics Report {Scenario}', text=slack_test, color=slack_color, environment=url)


def links_test_to_prod(browser):
    """
    When env is not a prod, the test changes urls with parameters and redirect to prod
    """
    if os.environ["url"] != "https://promo.com":
        current_url = browser.current_url
        len_url_param = len(current_url.split("?")[0].split("/"))
        if len_url_param == 6:
            url_parameter5 = current_url.split("?")[0].split("/")[5]
            url_parameter4 = current_url.split("?")[0].split("/")[4]
            url_parameter3 = current_url.split("?")[0].split("/")[3]
            if current_url.split("?")[0].split("/")[2].split(".")[0] == 'support':
                browser.get(f"https://support.promo.com/{url_parameter3}/{url_parameter4}/{url_parameter5}")
            else:
                browser.get(f"https://promo.com/{url_parameter3}/{url_parameter4}/{url_parameter5}")
        elif len_url_param == 5:
            url_parameter4 = current_url.split("?")[0].split("/")[4]
            url_parameter3 = current_url.split("?")[0].split("/")[3]
            if current_url.split("?")[0].split("/")[2].split(".")[0] == 'support':
                browser.get(f"https://support.promo.com/{url_parameter3}/{url_parameter4}")
            else:
                browser.get(f"https://promo.com/{url_parameter3}/{url_parameter4}")
        else:
            url_parameter = current_url.split("?")[0].split("/")[3]
            if current_url.split("?")[0].split("/")[2].split(".")[0] == 'support':
                browser.get(f"https://support.promo.com/{url_parameter}")
            else:
                browser.get(f"https://promo.com/{url_parameter}")
    else:
        pass


def skip_test(browser, message):
    """
    BrowserStack skip helper for upload tests and other 3rd party tools
    """
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Test Skipped due to expected failure of 3rd party tools"}}')
    pytest.skip(message)


def close_additional_tab(browser, tab1: int, tab2: int):
    """
    Closes a chosen tab
    tab1: tab to stay open
    tab2: tab to be closed
    example: when tab1 = 1 and tab2 = 0, the script closes ...
    """
    try:
        main = browser.window_handles[tab1]
    except WebDriverException:
        time.sleep(2)
        main = browser.window_handles[tab1]
    mod = browser.window_handles[tab2]
    browser.switch_to.window(mod)
    browser.close()  # close mod window
    browser.switch_to.window(main)
