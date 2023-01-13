from locators.locators_file import *
from test_data.testdata import *
from helpers.common_helpers import *
from selenium.webdriver.common.keys import Keys


def goto_modheader_html_mob(mob_browser):
    """
    Goes to ModHeader Chrome extension source
    """
    window_after = mob_browser.window_handles[0]
    mob_browser.switch_to.window(window_after)
    mob_browser.get(mod_header_url)


def enable_modheader_incognito_mob(mob_browser):
    """
    Enables ModHeader extension
    """
    mob_browser.get(mob_header_extension_url)
    mob_browser.execute_script(INCOGNITO_TOGGLE_MODHEADER_IN_CHROME_EXTENSION_PAGE_JSPATH)


def enter_headers_in_modheader_mob(mob_browser):
    """
    Enters access headers to ModHeader plugin
    Needed on test environments
    """
    header_name = mob_browser.find_element_by_xpath(HEADER_NAME[1])
    mob_browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_name, "type", "password")
    do_send_keys(mob_browser, HEADER_NAME, cf_client_id[0])
    header_value = mob_browser.find_element_by_xpath(HEADER_VALUE[1])
    mob_browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_value, "type", "password")
    do_send_keys(mob_browser, HEADER_VALUE, cf_client_secret[0])
    time.sleep(2)
    do_click(mob_browser, MODHEADER_OPTION_BTN_MOB)
    do_click(mob_browser, HEADER_ADD_BTN_MOB)
    header_name2 = mob_browser.find_element_by_xpath(HEADER_NAME2[1])
    mob_browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_name2, "type", "password")
    do_send_keys(mob_browser, HEADER_NAME2, cf_client_id[1])
    header_value2 = mob_browser.find_element_by_xpath(HEADER_VALUE2[1])
    mob_browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_value2, "type", "password")
    do_send_keys(mob_browser, HEADER_VALUE2, cf_client_secret[1])
    do_click(mob_browser, HEADER_BODY_CLICK)
    time.sleep(1)
    mob_browser.execute_script('''window.open("about:blank");''')
    mob_browser.refresh()
    mob_browser.close()
    window_after = mob_browser.window_handles[1]
    mob_browser.switch_to.window(window_after)
