import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException
from locators.locators_file import *
from locators.locators_links import *
from test_data.testdata import *
from helpers.common_helpers import *

title_list = []


def open_and_test_menu_items(browser):
    """
    Checks every main menu item by opening it and checking the title
    """
    for menu_title, menu_locator in MAIN_MENU_TITLES.items():
        browser.get(base_url)
        if is_visible(browser, menu_locator) is False:
            do_hover(browser, RESOURCES_HEADER)
            do_click(browser, menu_locator, 20)
            links_test_to_prod(browser)
            # to_delete: Rishabh FYI
            # w = browser.current_window_handle
            # tabs = browser.window_handles
            # for t in tabs:  # switch focus to child window - new tab
            #     if t != w:
            #         browser.switch_to.window(t)
            try:
                WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
            except (NoSuchElementException, TimeoutException) as e:
                pass
            get_title = browser.title
            print('Opened from Menu: ' + get_title)
            assert get_title == menu_title
            # browser.switch_to.window(w)
            # browser.close()  # close old window
            # for t in tabs:  # switch focus to child window - new tab
            #     if t != w:
            #         browser.switch_to.window(t)
        else:
            do_click(browser, menu_locator, 20)
            links_test_to_prod(browser)
            try:
                WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
            except (NoSuchElementException, Exception) as e:
                pass
            get_title = browser.title
            print('Opened from Menu: ' + get_title)
            assert get_title == menu_title
            # allure_screenshot(browser)


def open_and_test_footer_items(browser):
    """
    Checks every main footer item by opening it and checking the title
    """
    browser.get(base_url)
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH, 2) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    else:
        pass
    for menu_title, menu_locator in FOOTER_MENU_TITLES.items():
        browser.get(base_url)
        browser.refresh()
        elem = browser.find_element_by_xpath(menu_locator[1])
        try:
            browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", elem)
            do_click(browser, menu_locator, 20)
            links_test_to_prod(browser)
            try:
                WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
            except (NoSuchElementException, TimeoutException) as e:
                pass
            get_title = browser.title
            print('Opened from Footer: ' + get_title)
            assert get_title == menu_title
        except (ElementClickInterceptedException, NoSuchElementException):
            browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", elem)
            do_click(browser, menu_locator, 10)
            links_test_to_prod(browser)
            try:
                WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
            except (NoSuchElementException, TimeoutException) as e:
                pass
            get_title = browser.title
            print('Opened from Footer 2nd iteration: ' + get_title)
            assert get_title == menu_title


def open_and_test_footer_products_and_menu_tabs(browser):
    """
    Checks every main footer product item by opening it in a new tab and checking the title
    Checks every main menu item which opens in a new tab
    """
    browser.get(base_url)
    for menu_title, menu_locator in FOOTER_PRODUCT_TITLES.items():
        browser.delete_all_cookies()
        browser.get(base_url)
        browser.refresh()
        time.sleep(2)
        footer_locator = browser.find_element_by_xpath(menu_locator[1])
        browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", footer_locator)
        is_visible(browser, menu_locator, 10)
        do_click(browser, menu_locator, 20)
        try:
            time.sleep(2)
            w = browser.current_window_handle
            tabs = browser.window_handles
        except WebDriverException:
            time.sleep(2)
            w = browser.current_window_handle
            tabs = browser.window_handles
        for t in tabs:  # switch focus to child window - new tab
            if t != w:
                browser.switch_to.window(t)
                time.sleep(1)
                links_test_to_prod(browser)
            else:
                links_test_to_prod(browser)
                time.sleep(2)
        try:
            WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
        except (NoSuchElementException, TimeoutException) as e:
            pass
        get_title = browser.title
        print('Opened from Products: ' + get_title + " vs " + menu_title)
        assert get_title == menu_title
        browser.switch_to.window(w)
        time.sleep(2)
        browser.close()  # close old window
        time.sleep(3)
        tabs = browser.window_handles
        for t in tabs:  # switch focus to child window - new tab
            if t != w:
                browser.switch_to.window(t)
                time.sleep(2)


def open_and_test_footer_tools(browser):
    """
    Checks every footer tool item by opening it in a new tab and checking the title
    Checks every main menu item which opens in a new tab
    """
    for menu_title, menu_locator in TOOLS_FOOTER_TITLES.items():
        browser.delete_all_cookies()
        browser.get(base_url)
        browser.refresh()
        time.sleep(1)
        do_click(browser, menu_locator, 20)
        try:
            time.sleep(2)
            w = browser.current_window_handle
            tabs = browser.window_handles
        except WebDriverException:
            time.sleep(2)
            w = browser.current_window_handle
            tabs = browser.window_handles
        for t in tabs:  # switch focus to child window - new tab
            if t != w:
                browser.switch_to.window(t)
                time.sleep(2)
                links_test_to_prod(browser)
                time.sleep(2)
            else:
                links_test_to_prod(browser)
                time.sleep(2)
        try:
            WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
        except (NoSuchElementException, TimeoutException) as e:
            pass
        get_title = browser.title
        print('Opened from Tools: ' + get_title)
        assert get_title == menu_title
        browser.switch_to.window(w)
        time.sleep(3)
        browser.close()  # close old window
        for t in tabs:  # switch focus to child window - new tab
            if t != w:
                browser.switch_to.window(t)
                time.sleep(2)


def preview_a_template(browser):
    """

    """
    if is_visible(browser, HEADER_TEMPLATES_BTN) is True:
        do_click(browser, HEADER_TEMPLATES_BTN)
    else:
        do_click(browser, HEADER_TEMPLATES_BTN_OLD)
    time.sleep(2)
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH) is True:
        do_click(browser, AGREE_COOKIES_NEW_AUTH)
    else:
        pass
    do_hover(browser, HOVER_TEMPLATE)
    do_click(browser, NEXT_PREVIEW_BTN)


def open_new_tab_and_verify_each_link(browser, link):
    browser.execute_script("window.open('');")
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[2])
    time.sleep(1)
    browser.get(link)
    time.sleep(2)
    links_test_to_prod(browser)
    print(browser.title)
    assert (browser.title.find('ERROR') == -1) is True
    wait_for_ajax(browser)
    title = browser.title
    browser.close()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    return title


def open_templates_and_test_footer_links(browser):
    preview_a_template(browser)
    el = browser.find_elements_by_xpath('//a[@class="footer-links__link text-title-micro"]')
    len_el = int(((len(el)) / 2) + 1)
    for el_num in range(1, len_el):
        link_cta = browser.find_element_by_xpath('(//a[@class="footer-links__link text-title-micro"])' + str([el_num]))
        link = link_cta.get_attribute("href")
        if link != 'mailto:support@promo.com':
            title = open_new_tab_and_verify_each_link(browser, link)
            title_list.append(title)


def open_templates_and_test_header_links(browser):
    preview_a_template(browser)
    el = browser.find_elements_by_xpath('//a[@class="header-links__link"]')
    len_el = int(((len(el)) / 2) + 1)
    for el_num in range(1, len_el):
        link_cta = browser.find_element_by_xpath('(//a[@class="header-links__link"])' + str([el_num]))
        link = link_cta.get_attribute("href")
        title = open_new_tab_and_verify_each_link(browser, link)
        title_list.append(title)


def open_and_test_menu_new_tab(browser):
    """
    Checks every menuitem by opening it in a new tab and checking the title
    Checks every main menu item which opens in a new tab
    """
    for menu_title, menu_locator in MAIN_MENU_TAB_TITLES.items():
        browser.delete_all_cookies()
        browser.get(base_url)
        browser.refresh()
        time.sleep(1)
        if is_visible(browser, menu_locator) is False:
            do_hover(browser, RESOURCES_HEADER)
            do_click(browser, menu_locator, 20)
        else:
            do_click(browser, menu_locator, 20)
        time.sleep(2)
        w = browser.current_window_handle
        tabs = browser.window_handles
        for t in tabs:  # switch focus to child window - new tab
            if t != w:
                browser.switch_to.window(t)
                time.sleep(2)
                links_test_to_prod(browser)
                time.sleep(2)
            else:
                links_test_to_prod(browser)
                time.sleep(2)
        try:
            WebDriverWait(browser, 20).until(lambda x: menu_title in browser.title)
        except (NoSuchElementException, TimeoutException) as e:
            pass
        get_title = browser.title
        print('Opened from Main Menu: ' + get_title)
        assert get_title == menu_title
        browser.switch_to.window(w)
        time.sleep(2)
        # browser.close()  # close old window
        for t in tabs:  # switch focus to child window - new tab
            if t != w:
                browser.switch_to.window(t)


def check_partner_logos_links(browser):
    """
    Checks every partner's logo on the main page
    """
    for partner_name, partner_locator in PARTNERS_LOGOS.items():
        browser.get(base_url)
        print('Checked from Main Page: ' + partner_name)
        assert is_visible(browser, partner_locator) is True


def assert_links_title_with_slack():
    """
    Function compares actual list with expected list
    Args:
        Check links title and return non existing or changed links titles
        Send report on slack
    """
    links_title_not_appeared = []
    for g in title_list:
        for ge in header_and_footers_links_title:
            if g == ge:
                break
        else:
            print(g + ' is not present or changed')
            links_title_not_appeared.append(g)
    # for lts in header_and_footers_links_title:
    #     for lt in title_list:
    #         if lts == lt:
    #             break
    #     else:
    #         print(lts + ' is not present or changed')
    #         links_title_not_appeared.append(lts)
    return links_title_not_appeared
