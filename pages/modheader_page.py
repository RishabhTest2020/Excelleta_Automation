from helpers.common_helpers import *


def goto_modheader_html(browser):
    """
    Goes to ModHeader Chrome extension source
    """
    # to_delete: Rishabh FYI
    # Browser = os.environ['browser']
    # if Browser == 'browserstack':
    window_after = browser.window_handles[0]
    browser.switch_to.window(window_after)
    browser.get(mod_header_url)
    # else:
    #     browser.get(mod_header_url)


def enable_modheader_incognito(browser):
    """
    Enables ModHeader extension
    """
    browser.get(mob_header_extension_url)
    browser.execute_script(INCOGNITO_TOGGLE_MODHEADER_IN_CHROME_EXTENSION_PAGE_JSPATH)


def enter_headers_in_modheader(browser):
    """
    Enters access headers to ModHeader plugin
    Needed on test environments
    """
    header_name = browser.find_element_by_xpath(HEADER_NAME[1])
    browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_name, "type", "password")
    do_send_keys(browser, HEADER_NAME, cf_client_id[0])
    header_value = browser.find_element_by_xpath(HEADER_VALUE[1])
    browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_value, "type", "password")
    do_send_keys(browser, HEADER_VALUE, cf_client_secret[0])
    time.sleep(2)
    do_click(browser, MODHEADER_OPTION_BTN)
    do_click(browser, HEADER_ADD_BTN)
    header_name2 = browser.find_element_by_xpath(HEADER_NAME2[1])
    browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_name2, "type", "password")
    do_send_keys(browser, HEADER_NAME2, cf_client_id[1])
    header_value2 = browser.find_element_by_xpath(HEADER_VALUE2[1])
    browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", header_value2, "type", "password")
    do_send_keys(browser, HEADER_VALUE2, cf_client_secret[1])
    do_click(browser, HEADER_BODY_CLICK)
    time.sleep(1)
    browser.execute_script('''window.open("about:blank");''')
    browser.refresh()
    browser.close()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)


def close_modheader_tab(browser):
    try:
        main = browser.window_handles[0]
    except WebDriverException:
        time.sleep(2)
        main = browser.window_handles[0]
    mod = browser.window_handles[1]
    browser.switch_to.window(mod)
    browser.close()  # close mod window
    browser.switch_to.window(main)

