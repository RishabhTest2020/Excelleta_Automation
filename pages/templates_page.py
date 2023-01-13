import time
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from helpers.common_helpers import *
from test_data.testdata import *
from locators.locators_file import *


def navigate_templates_page(browser):
    """
    Navigates to Templates page
    """
    if is_visible(browser, HEADER_TEMPLATES_BTN) is True:
        do_click(browser, HEADER_TEMPLATES_BTN)
    else:
        do_click(browser, HEADER_TEMPLATES_BTN_OLD)
    time.sleep(3)
    title = browser.title
    assert title == title_templates_page


def template_page_url(browser):
    """
    Opens templates page
    If statement created for BrowserStack
    """
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    browser.get(templates_url)


def search_valid_temps(browser):
    """
    Searches templates by valid keyword
    """
    is_visible(browser, SEARCH_TEMPLATES)
    do_clear(browser, SEARCH_TEMPLATES)
    do_send_keys(browser, SEARCH_TEMPLATES, home_temp)
    do_send_keys(browser, SEARCH_TEMPLATES, Keys.ENTER)
    try:
        assert is_visible(browser, TEMPLATES_GRID_PRESENCE) is True
    except AssertionError:
        print('Templates are not available with the inserted keyword')
        pass


def search_temps_with_invalid_input(browser):
    """
    Searches templates with invalid keyword
    """
    is_visible(browser, SEARCH_TEMPLATES)
    do_clear(browser, SEARCH_TEMPLATES)
    do_send_keys(browser, SEARCH_TEMPLATES, invalid_input)
    do_send_keys(browser, SEARCH_TEMPLATES, Keys.ENTER)
    error_mess = get_element_text(browser, TEMPLATES_NOT_FOUND)
    assert error_mess == TEMPLATES_NOT_FOUND_MESS


def verify_categories_and_breadcrumbs(browser):
    """
    Verifies categories and breadcrumbs by their names
    """
    is_visible(browser, TEMPS_CATEGORIES)
    categories = browser.find_elements_by_xpath(TEMPS_CATEGORIES[1])
    print(len(categories))
    categories_len = len(categories)
    for category_no in range(1, categories_len+1):
        category_btn = browser.find_element_by_xpath(TEMPS_CATEGORIES[1] + str([category_no]))
        try:
            browser.execute_script("arguments[0].scrollIntoView();", category_btn)
            wait_for_ajax(browser)
            do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
            cat_name = get_element_text(browser, (By.XPATH, TEMPS_CATEGORIES[1] + str([category_no])))
            print(cat_name)
        except (ElementNotInteractableException, ElementNotVisibleException):
            category_btn_dec = browser.find_element_by_xpath(TEMPS_CATEGORIES[1] + str([category_no]))
            browser.execute_script\
                ("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", category_btn_dec)
            try:
                do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
            except ElementClickInterceptedException:
                category_btn_dec = browser.find_element_by_xpath(TEMPS_CATEGORIES[1] + str([category_no]))
                browser.execute_script\
                    ("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", category_btn_dec)
                do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
            cat_name = get_element_text(browser, (By.XPATH, TEMPS_CATEGORIES[1] + str([category_no])))
            print(cat_name)
        except StaleElementReferenceException:
            browser.refresh()
            try:
                do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
            except (ElementClickInterceptedException, StaleElementReferenceException):
                try:
                    browser.execute_script\
                        ("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", category_btn)
                except StaleElementReferenceException:
                    pass
                try:
                    do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
                except StaleElementReferenceException:
                    browser.refresh()
                    try:
                        do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
                    except (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException):
                        browser.execute_script\
                            ("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center' });", category_btn)
                        time.sleep(5)
                        do_click(browser, (By.XPATH, TEMPS_CATEGORIES_NEW[1] + str([category_no])))
            cat_name = get_element_text(browser, (By.XPATH, TEMPS_CATEGORIES[1] + str([category_no])))
            print(cat_name)
        time.sleep(5)
        is_visible(browser, BREADCRUMBS_NAME)
        breadcrum_name = get_element_text(browser, BREADCRUMBS_NAME)
        print(breadcrum_name)
        try:
            assert cat_name == breadcrum_name
        except AssertionError:
            print(cat_name + 'and' + breadcrum_name + 'is not matching')
            pass


def customize_template(browser):
    """
    Clicks on Customize button
    """
    elem = browser.find_element_by_xpath(ALL_TEMPLATES_CTA[1])
    template_cta = "selected" in elem.get_attribute("class")
    if template_cta is False:
        template_page_header = browser.find_element_by_xpath(TEMPLATE_PAGE_HEADER_TITLE[1])
        all_templates_btn = browser.find_element_by_xpath(ALL_TEMPLATES_CTA[1])
        try:
            all_templates_btn.location_once_scrolled_into_view()
        except TypeError:
            pass
        try:
            template_page_header.location_once_scrolled_into_view()
        except TypeError:
            pass
    else:
        pass
    do_click(browser, ALL_TEMPLATES_CTA)
    try:
        do_hover_offset(browser, HOVER_TEMPLATE, 5, 5)
    except StaleElementReferenceException:
        time.sleep(1)
        do_hover_offset(browser, HOVER_TEMPLATE, 2, 2)
    try:
        do_click(browser, CUSTOMIZE_TEMP_BTN)
    except (StaleElementReferenceException, TimeoutException):
        time.sleep(1)
        do_hover(browser, HOVER_TEMPLATE)
        do_click(browser, CUSTOMIZE_TEMP_BTN)
    time.sleep(6)


def preview_template_and_share(browser):
    """
    Previews templates and verifies share button
    """
    do_hover(browser, HOVER_TEMPLATE)
    do_click(browser, NEXT_PREVIEW_BTN)
    is_visible(browser, SHARE_BTN, 10)
    do_click(browser, SHARE_BTN)
    for share_types, share_path in TEMP_SHARE_BTN.items():
        assert is_visible(browser, share_path) is True
    do_click(browser, CLOSE_SHARE_POP_UP)
    # allure_screenshot(browser)


def change_ratios(browser):
    """
    Changes different ratio filters
    """
    for ratio_index, (ratio_name, ratio_path) in zip(range(1, 4), RATIOS.items()):
        time.sleep(3)
        ratio_btn = browser.find_element_by_xpath(RATIOS_HOV[1] + f'[text()="{ratio_name}"]')
        hov = ActionChains(browser).move_to_element(ratio_btn)
        hov.perform()
        ratio_dict_value = RATIOS.values()
        ratio_dict_value_list = list(ratio_dict_value)
        ratio_dict_list = list(RATIOS)
        do_click(browser, ratio_dict_value_list[ratio_index])
        time.sleep(1)
        ratio_text = get_element_text(browser, ratio_dict_value_list[ratio_index])
        print(ratio_text)
        assert ratio_text == ratio_dict_list[ratio_index]


def predefined_ratios(browser):
    """
    Verifies if predefined ratios (from admin) are shown correctly
    As we don't have such categories on prod, it is valid only for test envs
    Test envs: Always Wide category
    """
    if is_visible(browser, ALWAYS_WIDE_CATEGORY):
        do_click(browser, ALWAYS_WIDE_CATEGORY)
    else:
        do_click(browser, ALWAYS_WIDE_CATEGORY2)
    assert is_visible(browser, DROPDOWN_RATIO_SELECTED_WIDE) is True
    do_click(browser, RATIO_DROPDOWN)
    do_click(browser, SQUARE_RATIO_ON_DROPDOWN)
    assert is_visible(browser, DROPDOWN_RATIO_SELECTED_SQUARE) is True
    do_click(browser, MAIN_LOGO_TEMPLATE_PAGE)
