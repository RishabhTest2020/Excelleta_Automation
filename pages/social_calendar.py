import time
from datetime import date
import re
from dateutil import relativedelta
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from helpers.common_helpers import *
from locators.locators_file import *
from pages.editor_page import *
from pages.new_sign_up_page import *
from pages.new_login_page import *


def go_to_requested_month():
    """
    Goes to requested month, current month is a default
    arg value can be one of these 3 - "current", "next", "next_to_next"
    """
    try:
        if os.environ.get("MONTH") == None:
            current_date = datetime.now()
            month = current_date.strftime("%B")
            year = (current_date.strftime("%Y"))
            return month, year
        elif os.environ.get("MONTH").lower() == "next":
            next_month = date.today() + relativedelta.relativedelta(months=1)
            month = (next_month.strftime("%B"))
            year = (next_month.strftime("%Y"))
            return month, year
        elif os.environ.get("MONTH").lower() == "next_to_next":
            next_month = date.today() + relativedelta.relativedelta(months=2)
            month = (next_month.strftime("%B"))
            year = (next_month.strftime("%Y"))
            return month, year
        else:
            current_date = datetime.now()
            month = current_date.strftime("%B")
            year = (current_date.strftime("%Y"))
            return month, year
    except (KeyError, TypeError):
        pass


def check_correct_username_cal(browser):
    """
    Checks if user is logged correctly
    """
    is_visible(browser, USERNAME_MENU, 15)
    assert get_element_text(browser, USERNAME_MENU) == fullname_calendar


def choose_day_template(browser, locator):
    """
    on Social Calendar page chooses a day item and render it
    locator: value from 1 to 31 taken from feature file
    """
    DAY_CARD_LOC = (By.XPATH, f'(//DIV[@class="calendar-grid__item card  current-month"])[{locator}]')
    DAY_CARD_CUSTOMIZE_BTN = (
    By.XPATH, f'(//DIV[@class="calendar-grid__item card  current-month"])[{locator}]/div[2]/div[1]/a[2]')
    if is_visible(browser, AGREE_COOKIES_NEW_AUTH) is True:
        accept_cookies_new(browser)
    days = browser.find_elements_by_xpath(CLASS_FOR_MONTH[1])
    no_of_days = len(days)
    if (int(locator) == 31) and (27 < no_of_days < 31) is True:
        pass
    elif (int(locator) >= 30) and (27 < no_of_days < 30) is True:
        pass
    elif (int(locator) >= 29) and (27 < no_of_days < 29) is True:
        pass
    else:
        do_hover(browser, DAY_CARD_LOC)
        is_visible(browser, DAY_CARD_CUSTOMIZE_BTN, 3)
        do_click(browser, DAY_CARD_CUSTOMIZE_BTN, 10)
        publish_video(browser)
        check_pricing_and_publish_page(browser)


def navigate_to_social_calendar_page(browser):
    """
    Navigates to Social Calendar page and goes to desired month
    """
    if is_visible(browser, HEADER_CALENDAR_BTN) is True:
        do_click(browser, HEADER_CALENDAR_BTN)
    else:
        time.sleep(3)
        do_click(browser, HEADER_CALENDAR_BTN)
    try:
        if os.environ.get("MONTH") == None:
            pass
        elif os.environ.get("MONTH").lower() == "next":
            if is_visible(browser, NAV_NEXT) is True:
                do_click(browser, NAV_NEXT)
            else:
                print("Next Month is not Published yet")
        elif os.environ.get("MONTH").lower() == "next_to_next":
            do_click(browser, NAV_NEXT)
            time.sleep(2)
            if is_visible(browser, NAV_NEXT) is True:
                do_click(browser, NAV_NEXT)
            else:
                raise Exception("Next Month is not Published yet")
        else:
            pass
    except KeyError:
        pass
    month, year = go_to_requested_month()
    time.sleep(2)
    title = browser.title
    current_page_title = f"{month} {year} Social Media Content Calendar | Promo.com"
    print(f"expected: {title}, actual: {current_page_title}")
    assert title == current_page_title
