import inspect
import json
import logging
import os
import sys
import time
from datetime import date, datetime
import requests
from pytz import reference
from selenium.common.exceptions import NoSuchElementException, TimeoutException, \
    WebDriverException, JavascriptException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from locators.common_locators_file import *
import inspect
import importlib


def wait_for_ajax(browser):
    wait = WebDriverWait(browser, 300)
    try:
        wait.until(lambda ajwait: browser.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass


def take_screenshot(browser, name='ss' + time.strftime("%Y%m%d-%H%M%S")):
    """
    Takes a screenshot and saves it in png file
    Args:
        browser: webdriver
        name: screenshot name
    """
    # if sys.platform == 'linux':
    try:
        path = os.getcwd() + '/screenshots/' + name + '.png'
        browser.save_screenshot(path)
        print(path)
    except (WebDriverException, Exception):
        pass
    # else:
    #     pass


def js_click_by_xpath(browser, xpath):
    """
    Clicks an element using JavaScript by its XPath without using Selenium's find_element method.

    Parameters:
    driver (webdriver): The Selenium WebDriver instance.
    xpath (str): The XPath of the element to click.
    """
    try:
        # JavaScript code to find an element by XPath and click it
        script = """
        var xpath = arguments[0];
        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) {
            element.click();
            return 'Element clicked successfully';
        } else {
            return 'Element not found';
        }
        """
        # Execute the script with the provided XPath
        result = browser.execute_script(script, xpath)
        print(result)
    except Exception as e:
        print(f"Error clicking element: {e}")


def do_click(browser, by_locator: object, sec=10):
    """
    Waits and clicks on the chosen element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    WebDriverWait(browser, sec, poll_frequency=0.4).until(
        EC.element_to_be_clickable(by_locator)).click()


def do_double_click(browser, by_locator, sec=5):
    """
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
        EC.presence_of_element_located(by_locator))
    browser.execute_script("var evt = document.createEvent('MouseEvents');" +
                           "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" +
                           "arguments[0].dispatchEvent(evt);", elem)


def do_hover(browser, by_locator, sec=5):
    """
    Hovers over element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
        EC.visibility_of_element_located(by_locator))
    ActionChains(browser).move_to_element(elem).perform()


def do_hover_offset(browser, by_locator, x, y, sec=5):
    """
    Hovers over an element with a specific offset
    Args:
        browser: webdriver
        by_locator (str): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
        x: first offset parameter
        y: second offset parameter
    """
    wait_for_ajax(browser)
    elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
        EC.presence_of_element_located(by_locator))
    ActionChains(browser).move_to_element_with_offset(elem, x, y).perform()


def do_click_offset(browser, by_locator, x, y, sec=5):
    """
    Click an element with a specific offset
    Args:
        browser: webdriver
        by_locator (str): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
        x: first offset parameter
        y: second offset parameter
    """
    wait_for_ajax(browser)
    elem = WebDriverWait(browser, sec, poll_frequency=0.4).until(
        EC.presence_of_element_located(by_locator))
    ActionChains(browser).move_to_element_with_offset(elem, x, y).click().perform()


def drag_and_drop(browser, by_locator_source, by_locator_target, sec=5):
    """
    Drag and drop from source to targeted element
    Args:
        browser: webdriver
        by_locator_source (str): chosen source locator from locators/common_locators_file.py
        by_locator_target (str): chosen target locator from locators/common_locators_file.py
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
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        text (str): text to be send
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    WebDriverWait(browser, sec, poll_frequency=0.4).until(
        EC.visibility_of_element_located(by_locator)).send_keys(text)


def get_element_text(browser, by_locator: object):
    """
    Gets text of the chosen element
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
    """
    wait_for_ajax(browser)
    elem_text = WebDriverWait(browser, 30, poll_frequency=0.4).until(
        EC.presence_of_element_located(by_locator)).text
    return elem_text


def get_css_value(browser, by_locator, property_name):
    """
    Gets text of the chosen element
    Args:
        property_name: add css property name
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
    """
    wait_for_ajax(browser)
    elem = WebDriverWait(browser, 30, poll_frequency=0.4).until(
        EC.presence_of_element_located(by_locator))
    elem_value = elem.value_of_css_property(property_name)
    return elem_value


def is_visible(browser, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is visible
    Args:
        browser: webdriver
        by_locator(tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    elem = False
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=1, ignored_exceptions=WebDriverException).until(
            EC.visibility_of_element_located(by_locator))
    except (WebDriverException, Exception, TimeoutException):
        # take_screenshot(browser)
        return bool(elem)
    return bool(elem)


def should_be_invisible(browser, by_locator, msg, sec=5):
    invisi = is_invisible(browser, by_locator, sec)
    if invisi is True:
        logging.info(msg + ' is invisible')
    else:
        logging.info(msg + ' is not invisible')
        sys.exit(1)


def should_be_visible(browser, by_locator, msg, sec=5):
    visi = is_visible(browser, by_locator, sec)
    if visi is True:
        logging.info(msg + ' is visible')
    else:
        logging.info(msg + ' is not visible')
        sys.exit(1)


def is_invisible(browser, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is invisible
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    wait_for_ajax(browser)
    elem = False
    try:
        elem = WebDriverWait(browser, sec, poll_frequency=0.4, ignored_exceptions=[WebDriverException]).until(
            EC.invisibility_of_element_located(by_locator))
    except (WebDriverException, Exception):
        return bool(elem)
    return bool(elem)


def is_clickable(browser, by_locator, sec=5) -> bool:
    """
    Waits and checks if element is clickable
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
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
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    """
    WebDriverWait(browser, sec, poll_frequency=0.4).until(EC.frame_to_be_available_and_switch_to_it(by_locator))


def do_clear(browser, by_locator, sec=5):
    """
    Clears textfield or input
    Args:
        browser: webdriver
        by_locator (tuple): chosen locator from locators/common_locators_file.py
        sec (int): default time to wait
    """
    wait_for_ajax(browser)
    WebDriverWait(browser, sec, poll_frequency=0.4).until(EC.visibility_of_element_located(by_locator)).clear()


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
        if entry['level'] == 'SEVERE' or entry['level'] == 'ERROR' or entry['level'] == 'CRITICAL' or entry[
            'level'] == 'INFO':
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


class ElementStillVisibleException(Exception):
    pass


def loader_should_be_invisile(browser, sec):
    val = is_invisible(browser, loader_loc, sec)
    if val is False:
        logging.info(f'Loader is taking more than {str(sec)} secs to be disappear')
        raise ElementStillVisibleException(f'Loader is taking more than {str(sec)} secs to be disappear')


# Function to get XPath of an element
def get_element_xpath(driver, element: WebElement) -> str:
    if element.get_attribute("id"):
        return f'id("{element.get_attribute("id")}")'

    components = []
    child = element if element.tag_name != 'html' else None
    while child:
        parent = child.find_element(By.XPATH, "..")
        siblings = parent.find_elements(By.XPATH, f"./{child.tag_name}")
        if len(siblings) == 1:
            components.append(child.tag_name)
        else:
            index = 1
            for i in range(len(siblings)):
                if siblings[i] == child:
                    components.append(f'{child.tag_name}[{index}]')
                    break
                index += 1
        child = parent if parent.tag_name != 'html' else None

    components.reverse()
    return f"/{'/'.join(components)}"


# Function to switch to an iframe and collect XPaths within it
def collect_iframe_xpaths(driver, iframe_element):
    driver.switch_to.frame(iframe_element)
    iframe_xpaths = get_all_xpaths(driver)
    driver.switch_to.default_content()
    return iframe_xpaths


# Function to get all XPaths of elements in the page
def get_all_xpaths(driver):
    all_elements = driver.find_elements(By.XPATH, "//*")
    xpaths = [get_element_xpath(driver, elem) for elem in all_elements]

    # Check for iframes and collect XPaths within them
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    for iframe in iframes:
        iframe_xpaths = collect_iframe_xpaths(driver, iframe)
        xpaths.extend(iframe_xpaths)

    return xpaths


def replace_in_tuple(tpl, index, value):
    """
    Replace an element in a tuple at a specific index with a new value.

    Parameters:
    tpl (tuple): The original tuple.
    index (int): The index of the element to replace.
    value (any): The new value to insert at the specified index.

    Returns:
    tuple: A new tuple with the replaced value.
    """
    if index < 0 or index >= len(tpl):
        raise IndexError("Index out of range")

    # Create a new tuple with the replaced value
    new_tuple = tpl[:index] + (value,) + tpl[index + 1:]
    return new_tuple


def get_text_by_js_xpath(browser, xpath):
    """
    Gets the text content of an element using JavaScript by its XPath.

    Parameters:
    driver (webdriver): The Selenium WebDriver instance.
    xpath (str): The XPath of the element.

    Returns:
    str: The text content of the element.
    """
    try:
        # JavaScript code to find an element by XPath and get its text content
        script = """
        var xpath = arguments[0];
        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        return element ? element.textContent : null;
        """
        # Execute the script with the provided XPath
        text_content = browser.execute_script(script, xpath)
        return text_content
    except Exception as e:
        print(f"Error getting text content: {e}")
        return None


def pdb_apply():
    import pdb
    pdb.set_trace()


def get_list_of_elems_attributes_value(browser, locatortype, locator, attribute):
    names_value = []
    elems = browser.find_elements(locatortype, locator)
    for elem in elems:
        name_attr = elem.get_attribute(attribute)
        if name_attr != '':
            names_value.append(name_attr)

    print(names_value)
    return names_value


def get_list_of_elems_text(browser, locatortype, locator):
    text_values = []
    elems = browser.find_elements(locatortype, locator)
    for elem in elems:
        name_attr = elem.text
        name_attr = name_attr.rstrip(' ')
        name_attr = name_attr.lstrip(' ')
        if name_attr != '':
            text_values.append(name_attr)
    logging.info(text_values)
    return text_values


def scroll_into_the_view(browser, locator_type, locator):
    element = browser.find_element(locator_type, locator)
    # Scroll the element into view using JavaScript
    browser.execute_script("arguments[0].scrollIntoView(true);", element)


def get_class_global_variables_dict(MyClass):
    class_dict = MyClass.__dict__
    class_vars = {}
    for k, v in class_dict.items():
        if not callable(v) and not k.startswith('__'):
            class_vars[k] = v

    return class_vars


def list_val_type_to_str(lst: list):
    for i in lst:
        if (type(i) is int) or (type(i) is float):
            index = lst.index(i)
            lst[index] = str(i)
        elif type(i) is list:
            for j in i:
                if (type(j) is int) or (type(j) is float):
                    index = i.index(j)
                    i[index] = str(j)
    return lst


def comprehension_range(start_num, max_num):
    # Initialize an empty list to hold the sequence
    sequence = []

    # Use a loop to append each number twice
    for i in range(start_num, max_num + 1):
        sequence.extend([i, i])
    return sequence


def get_methods(cls):
    methods = []
    for name, obj in inspect.getmembers(cls):
        if inspect.isfunction(obj) or inspect.ismethod(obj):
            methods.append(str(cls.__name__) + '.' + name + '()')

    methods_str = "\n".join(methods)
    return methods_str


def get_classes_in_module(module):
    # Get all class members in the module
    return [name for name, obj in inspect.getmembers(module, inspect.isclass) if obj.__module__ == module.__name__]


def delete_class_vars(cls):
    for var in list(cls.__dict__.keys()):
        if not var.startswith('__'):  # Skip built-in attributes
            delattr(cls, var)


def process_module(module):
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:  # Ensure the class is defined in this module
            delete_class_vars(obj)


def delete_all_class_vars_in_project(project_directory):
    for root, dirs, files in os.walk(project_directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.relpath(os.path.join(root, file), project_directory)
                module_name = module_path.replace(os.sep, '.')[:-3]  # Convert file path to module name
                try:
                    module = importlib.import_module(module_name)
                    process_module(module)
                except Exception as e:
                    pass

