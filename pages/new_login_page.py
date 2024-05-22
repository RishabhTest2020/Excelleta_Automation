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
        is_visible(browser, invalid_creds_message)
    else:
        is_visible(browser, dashboard_txt, 10)
    import pdb; pdb.set_trace()
    all_element_xpaths = get_all_xpaths(browser)
    

