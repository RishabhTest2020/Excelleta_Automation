from time import sleep

from global_libs.global_imports import *


def user_login(browser, email=globalEnvs.user_email, password=globalEnvs.user_password, type='pass'):
    """
    Opens main page = environ url
    """
    browser.get(globalEnvs.main_url)
    wait_for_ajax(browser)
    is_visible(browser, excelleta_logo)
    do_send_keys(browser, email_text_box, email)
    do_send_keys(browser, password_text_box, password)
    do_click(browser, login_btn)
    if type == 'fail':
        should_be_visible(browser, invalid_creds_message, )
    else:
        pass
        # should_be_visible(browser, dashboard_txt, 'dashboard heading', 10)


def goto_tab(browser, tab_name):
    sleep(2)
    do_hover(browser, sidebar_hov)
    do_click(browser, sidebar_button)
    tab_loc = menu_tab_loc.replace("tab_name", tab_name)
    do_click(browser, (By.XPATH, tab_loc))
    page_name = pages_name_loc.replace("tab_name", tab_name)
    should_be_visible(browser, (By.XPATH, page_name), tab_name, 10)
    

