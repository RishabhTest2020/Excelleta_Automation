from global_libs.global_imports import *


def user_login(browser):
    """
    Opens main page = environ url
    """
    browser.get(globalEnvs.main_url)
    wait_for_ajax(browser)
    is_visible(browser, excelleta_logo)
    do_send_keys(browser, email_text_box, globalEnvs.user_email)
    do_send_keys(browser, password_text_box, globalEnvs.user_password)
    do_click(browser, login_btn)
    is_visible(browser, dashboard_txt, 10)
    

