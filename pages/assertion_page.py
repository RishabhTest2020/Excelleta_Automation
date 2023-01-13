from selenium.common.exceptions import TimeoutException
from helpers.common_helpers import *
from locators.locators_file import *
from locators.mobile_locators import *
from locators.facebook_locators import *
from test_data.testdata import *
from pytest_bdd import when, then, given, scenario, scenarios


def assertion_main_logo(browser):
    """
    BrowserStack assertion for main logo test
    """
    if browser.title == create_page_title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Main logo. Title matched!"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Main logo. Title not matched"}}')


def assertion_url_utm(browser):
    """
    BrowserStack assertion for URL assertion
    """
    import ast
    storage = browser.execute_script("return window.localStorage;")
    utm = storage['firstImpressionsUTMs']
    utm_value = ast.literal_eval(utm)['firstVisit_source']
    if utm_value == 'organicdirect':
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "UTM value is visible"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "UTM value is not visible"}}')


def assertion_cookies(browser):
    """
    BrowserStack assertion for visibility of cookies
    """
    if is_invisible(browser, AGREE_COOKIES_BUTTON, 3) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Cookies accepted!"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Cookies still visible"}}')


def assertion_links(browser):
    """
    BrowserStack assertion for links on main page
    """
    if browser.title == 'Create inspiring videos for NPOs with a free plan | Promo.com':
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title is correct"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title is not correct"}}')


def assertion_tools_links(browser):
    """
    BrowserStack assertion for tools links on main page
    """
    if browser.title == 'YouTube Money Calculator | Promo.com':
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title is correct"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title is not correct"}}')


def assertion_templates_footer_links(browser):
    """
    BrowserStack assertion for footer links on promo-next page
    """
    # if browser.title == 'TikTok Video Editor | TikTok for Business | Promo.com':
    if browser.title.find('ERROR') == -1:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Link Redirection Passed"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Link Redirection Failed"}}')


def assertion_templates_header_links(browser):
    """
        BrowserStack assertion for header links on promo-next page
        """
    # if browser.title == 'Aspect Ratio: Everything You Need to Know for 2022 | Promo.com':
    if browser.title.find('ERROR') == -1:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Link Redirection Passed"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Link Redirection Failed"}}')


def assertion_create_page(browser):
    """
    BrowserStack assertion for links on main page
    """
    if browser.title == create_page_title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title is correct"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title is not correct"}}')


def assertion_login_error_empty(browser):
    """
    BrowserStack assertion for empty login
    """
    if get_element_text(browser, NEW_EMPTY_FIELD_ERROR) == empty_textbox_message:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Empty textboxt error visible"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Empty textbox error is not visible"}}')


def assertion_wrong_login(browser):
    """
    BrowserStack assertion for wrong login creds
    """
    if get_element_text(browser, NEW_WRONG_CREDS_ERROR) == wrong_creds_message:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Wrong credential error visible"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong credential error is not visible"}}')


def assertion_publish_video(browser):
    """
    BrowserStack assertion for correctly publish a video
    """
    if browser.title == publish_page_title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Publish page is visible"}}')
    elif is_visible(browser, PRICING_TEXT) is True:
        elem = get_element_text(browser, PRICING_TEXT)
        assert elem == pricing_page_main_text
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Pricing page is visible"}}')
    elif browser.title == planner_title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "My Calendar Page is visible"}}')
    elif is_visible(browser, VIDEO_IFRAME, 30) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Publish functionalities are working fine"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Incorrect page is visible"}}')


def assertion_logged_out_account(browser):
    """
    BrowserStack assertion for correctly deleted account
    """
    if is_visible(browser, TRY_FREE, 40) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "User logged out correctly"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "User not logged out"}}')


def assertion_draft_deleted(browser):
    """
    BrowserStack assertion for correctly logged out user
    """
    if is_visible(browser, DRAFT_TAB) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Draft deleted correctly"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Draft has been not deleted"}}')


def assertion_brand_deleted(browser):
    """
    BrowserStack assertion for correctly deleted brand
    """
    if is_visible(browser, SAVED_BRAND_ASSERT) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Brand has not been deleted"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Brand deleted correctly"}}')


def assertion_changes_in_my_account(browser):
    """
    BrowserStack assertion for correctly changed settings in My Account
    """
    if is_visible(browser, MY_ACCOUNT_TITLE) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "My account settings changed"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "My account settings changes failed"}}')


def assertion_signup_redirection(browser):
    """
    BrowserStack assertion for correctly logged out user
    """
    if is_visible(browser, SIGNUP_NEW_BTN, 10) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Redirected to Signup page"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not Redirected to Signup page"}}')


def assertion_logo_and_watermark_sync(browser):
    """
    BrowserStack assertion for correctly logo sync
    """
    if is_visible(browser, EDITOR_LOGO_IMAGE) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "BM thourgh Wizard passed"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "BM thourgh Wizard passed"}}')


def assertion_shopify_dashboard(browser):
    """
    BrowserStack assertion on Shopify dashboard
    """
    if is_visible(browser, SHOPIFY_REVIEW_BTN) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Shopify scenario passed"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Shopify scenario failed"}}')


# Mobile view assertions

def assertion_mobile_path(mob_browser):
    """
    BrowserStack assertion for correctly executed mobile funnel
    """
    if is_visible(mob_browser, THANK_YOU_GIF) is True:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Mobile funnel completed"}}')
    else:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Mobile funnel failed"}}')


def assertion100a(mob_browser):
    """
    BrowserStack assertion for correctly executed mobile funnel
    """
    if is_visible(mob_browser, SHARED_VIDEO, 10) is True:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Mobile view video completed"}}')
    else:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Mobile view video failed"}}')


def assertion101a(mob_browser):
    """
    BrowserStack assertion for a correctly logged out user
    """
    if is_visible(mob_browser, HOME_LOGIN_BTN, 10) is True:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Correctly logged out on mobile"}}')
    else:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Incorrectly ended mobile test"}}')


def assertion102a(mob_browser):
    """
    BrowserStack assertion for a signup page on mobile
    """
    if is_visible(mob_browser, SIGNUP_MOB_BTN, 10) is True:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Signup page correctly shown on mobile"}}')
    else:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Incorrectly ended mobile test"}}')


def assertion103a(mob_browser):
    """
    BrowserStack assertion for a Planner on mobile (expected: no posts)
    """
    scheduled_items_del = mob_browser.find_elements_by_css_selector('div.post-menu-item')
    no_of_del_posts = len(scheduled_items_del)
    if no_of_del_posts == 0:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Post successfully previewed and deleted on mobile"}}')
    else:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Incorrectly ended mobile Planner test"}}')


def assertion104a(mob_browser):
    """
    BrowserStack assertion pricing page on mobile
    """
    if is_visible(mob_browser, PRICING_HEADER):
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Homepage on mobile displayed"}}')
    else:
        mob_browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Homepage on mobile not displayed"}}')


def assertion_logos_links(browser):
    """
       BrowserStack assertion for correctly executed logos links test
       """
    if is_visible(browser, MAIN_LOGO) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Partners logos links work fine"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Partners logos links dont work fine"}}')


def assertion_full_preview(browser):
    """
       BrowserStack assertion for correctly executed full preview scenario (template, raw)
       """
    get_title = browser.title
    if get_title == create_page_title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Preview of video succeeded"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Preview of video didnt succeeded"}}')


def assertion_my_calendar(browser):
    """
    BrowserStack assertion for My Calendar page
    """
    get_title = browser.title
    if get_title == planner_title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "My Calendar Page opened"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "My Calendar Page is not opened"}}')


def assertion_publisher(browser):
    """
    BrowserStack assertion for Publisher main page
    """
    if is_visible(browser, PUBLISHER_MAIN_HEADER):
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Publisher Page opened"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Publisher Page is not opened"}}')

# Naming a tests via JavaScript (for BrowserStack purposes)


def name_a_test1(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify cookies bar"}}')


def name_a_test2(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify clicking main logo"}}')


def name_a_test3(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Check menu and footer links"}}')


def name_a_test4(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Successful new Login to the Promo"}}')


def name_a_test5(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Empty Login fields error"}}')


def name_a_test6(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Wrong ID and password in login"}}')


def name_a_test7(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Customize video and publish it"}}')


def name_a_test8(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Add media to video and publish it"}}')


def name_a_test9(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify the new signup process"}}')


def name_a_test10(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify the new fb signup process"}}')


def name_a_test10b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify the new google signup process"}}')


def name_a_test10a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Signup verify premium tags and see pricing"}}')


def name_a_test10c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "New user purchases a plan after uploading a watermark"}}')


def name_a_test10d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "New user purchases plan after adding a brand"}}')


def name_a_test10e(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "New user try to purchases plan for watermark and Brand"}}')


def name_a_test11(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify the sign out process"}}')


def name_a_test12(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Drafted video and publish"}}')


def name_a_test13(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Drafted video and delete"}}')


def name_a_test14(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Brand Manager Functionalities Basic"}}')


def name_a_test15(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Brand Manager Functionalities through Wizard"}}')


def name_a_test16(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify password changes"}}')


def name_a_test16cb(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Get video share link"}}')


def name_a_test16a(mob_browser):
    mob_browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify shared video in mobile view"}}')


def name_a_test16ab(mob_browser):
    mob_browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Mobile Funnel"}}')


def name_a_test16ac_web(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Test planner on mobile phase web"}}')


def name_a_test16ac_mob(mob_browser):
    mob_browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Test planner on mobile phase mobile"}}')


def name_a_test16c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"status":"passed", "reason": "Test Completed"}}')


def name_a_test17(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify incorrect change of password"}}')


def name_a_test18(mob_browser):
    mob_browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Magic Link Functionality"}}')


def name_a_test19(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "New user purchases a plan and verify download functionality in publish page"}}')


def name_a_test20(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify template page without login"}}')


def name_a_test20_ir(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify image resizer without login"}}')


def name_a_test20_ir_2(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify image resizer after login"}}')


def name_a_test20_ir_3(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify a mobile view of image resizer page after login"}}')


def name_a_test20_ir_4(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify a mobile view of image resizer page without login"}}')


def name_a_test21(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify template page after login"}}')


def name_a_test22(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Try to login with deleted account"}}')


def name_a_test23(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Check tools links"}}')


def name_a_test_24(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Check partner logos links"}}')


def name_a_test25(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "New user purchases a plan with 2FA"}}')


def name_a_test25e(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "User with B1 Plan upgrade to Annual B1 on Publish Page"}}')


def name_a_test26(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "New user Starter Annual purchases a plan and cancels it"}}')


def name_a_test28(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Signup verify editorial tags and see pricing"}}')


def name_a_test27(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Signup purchase business plan and verify editorial tags and Publish pop up"}}')


def name_a_test29(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "User with starter plan see upgrade now pop while publishing the editorial"}}')


def name_a_test30(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify UTM on Promo URL"}}')


def name_a_test31(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Promo Performance Tests"}}')


def name_a_test31a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Promo Animation Tests using APE tool first half set"}}')


def name_a_test31b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Promo Animation Tests using APE tool second half set"}}')


def name_a_test32(browser):
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Create video from uploaded photo and verify functionalities of publish page"}}')


def name_a_test33(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Check All Footer Links on Templates Page"}}')


def name_a_test34(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Check All Header Links on Templates Page"}}')


def name_a_test35(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Edit video starting from Dashboard"}}')


def name_a_test35a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify aspect ratio functionalities"}}')


def name_a_test36(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Full preview of a video"}}')


def name_a_test_37(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Publisher Functionalities"}}')


def name_a_test_38(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Scheduler functionalities happy path"}}')


def name_a_test_39(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Scheduler functionalities with issues"}}')


def name_a_test_40(browser, env):
    browser.execute_script(f'browserstack_executor: {{"action": "setSessionName", "arguments": {{"name": "Generate video and publish {env}"}}}}')


def name_a_test_41(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Scheduler functionalities reschedule and edit"}}')


def name_a_test_42(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify publish and schedule for YT and LI"}}')


def name_a_test_43(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify reschedule YT and LI"}}')


def name_a_test_44(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify a new post button"}}')


def name_a_test_45(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify post duplication and deletion"}}')


def name_a_test_46(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify duplication a published post from planner"}}')


def name_a_test_47(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify duplication a scheduled post from planner"}}')


def name_a_test_48(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify create another post from publish summary"}}')


def name_a_test_49(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify predefined ratios on category page"}}')


def name_a_test_50(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Create video from uploaded video"}}')


def name_a_test51(mob_browser):
    mob_browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Mobile view basics for not logged user - mobile part"}}')


def name_a_test52(mob_browser):
    mob_browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Mobile view basics for not logged - web part"}}')


# Onboarding test names
def name_a_test_ob1(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Onboarding: basics - form skipped"}}')


def name_a_test_ob2(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Onboarding: basics - filled out with Branchfetch"}}')


def name_a_test_ob3(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Onboarding: leaving onboarding form empty"}}')


def name_a_test_ob4(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Onboarding: FB user completes onboarding"}}')


def name_a_test_ob5(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Onboarding: reach onboarding from templates page"}}')


def name_a_test_ob6(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Onboarding: basics filled out and add logo"}}')

# Test names - Cancellation Flow


def name_a_test_pricing1a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing1b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing2a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Accepts the Offer - Survey 1st Group"}}')


def name_a_test_pricing2b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Accepts First Offer - Survey 2nd Group"}}')


def name_a_test_pricing2c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Accepts Second Offer - Survey 2nd Group"}}')


def name_a_test_pricing3a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Closes the Offer - Survey 1st Group"}}')


def name_a_test_pricing3b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Monthly Closes the Offer - Survey 2nd Group"}}')


def name_a_test_pricing4a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Monthly Cancels the Offer - Survey 1st Group"}}')


def name_a_test_pricing4b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Monthly Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing5a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Monthly Accepts First Offer - Survey 1st Group"}}')


def name_a_test_pricing5b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Monthly Accepts First Offer - Survey 2nd Group"}}')


def name_a_test_pricing6a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Monthly Accepts Second Offer - Survey 1st Group"}}')


def name_a_test_pricing6b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Monthly Accepts Second Offer - Survey 2nd Group"}}')


def name_a_test_pricing7a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Cancels the Offer - Survey 1st Group"}}')


def name_a_test_pricing7b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing8a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Accepts an Offer A - Survey 1st Group"}}')


def name_a_test_pricing8b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Accepts First Offer Starter Monthly - Survey 2nd Group"}}')


def name_a_test_pricing9a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Accepts an Offer B - Survey 1st Group"}}')


def name_a_test_pricing9b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Accepts First Offer Business Monthly - Survey 2nd Group"}}')


def name_a_test_pricing10a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Accepts 2nd Offer - Survey 1st Group"}}')


def name_a_test_pricing10b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Monthly Accepts Second Offer - Survey 2nd Group"}}')


def name_a_test_pricing11a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Cancels the Offer - Survey 1st Group"}}')


def name_a_test_pricing11b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing12a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Accepts an Offer A - Survey 1st Group"}}')


def name_a_test_pricing12b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Accepts 1st Offer A - Survey 2nd Group"}}')


def name_a_test_pricing13a1(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Accepts an Offer B - Survey 1st Group"}}')


def name_a_test_pricing13b1(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Accepts 1st Offer B - Survey 2nd Group"}}')


def name_a_test_pricing13a2(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Accepts 2nd Offer - Survey 1st Group"}}')


def name_a_test_pricing13b2(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Special Offer User Accepts 2nd Offer- Survey 2nd Group"}}')


def name_a_test_pricing14a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Annual Cancels the Offer - Survey 1st Group"}}')


def name_a_test_pricing14b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Annual Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing15a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Annual Accepts an Offer - Survey 1st Group"}}')


def name_a_test_pricing15b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Annual Accepts First Offer - Survey 2nd Group"}}')


def name_a_test_pricing16a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Annual Accepts 2nd Offer - Survey 1st Group"}}')


def name_a_test_pricing16b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Starter Annual Accepts Second Offer - Survey 2nd Group"}}')


def name_a_test_pricing17a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Annual Cancels the Offer - Survey 1st Group"}}')


def name_a_test_pricing17b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Annual Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing18a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Annual Accepts an Offer - Survey 1st Group"}}')


def name_a_test_pricing18b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Annual Accepts First Offer - Survey 2nd Group"}}')


def name_a_test_pricing19a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Annual Accepts 2nd Offer - Survey 1st Group"}}')


def name_a_test_pricing19b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Business Annual Accepts Second Offer - Survey 2nd Group"}}')


def name_a_test_pricing20a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual Cancels the Offer - Survey 1st Group"}}')


def name_a_test_pricing20b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual Cancels the Offer - Survey 2nd Group"}}')


def name_a_test_pricing21a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual User Accepts an Offer - Survey 1st Group"}}')


def name_a_test_pricing21b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual User Accepts First Offer - Survey 2nd Group"}}')


def name_a_test_pricing22a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual Accepts 2nd Offer A - Survey 1st Group"}}')


def name_a_test_pricing22b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual Accepts Second Offer Starter Monthly - Survey 2nd Group"}}')


def name_a_test_pricing23a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual Accepts 2nd Offer B - Survey 1st Group"}}')


def name_a_test_pricing23b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Agency Annual Accepts Second Offer Business Monthly - Survey 2nd Group"}}')


def name_a_test_pricing24a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Monthly User Accepts First Offer Basic Monthly Half Price"}}')


def name_a_test_pricing24b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Monthly User Accepts Second Offer Lite Plan Monthly"}}')


def name_a_test24c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Monthly User Cancels the Offer"}}')


def name_a_test24d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Monthly User Closes the Offer"}}')


def name_a_test25a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Monthly User Accepts First Offer Basic Monthly"}}')


def name_a_test25b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Monthly User Accepts Second Offer Half Price Basic Annual"}}')


def name_a_test25c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Monthly User Cancels the Offer"}}')


def name_a_test25d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Monthly User Closes the Offer"}}')


def name_a_test26a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Monthly User Accepts First Offer Basic Monthly"}}')


def name_a_test26b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Monthly User Accepts First Offer Standard Monthly"}}')


def name_a_test26c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Monthly User Accepts Second Offer Semi Annual Offer"}}')


def name_a_test26d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Monthly User Cancels the Offer"}}')


def name_a_test26e(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Monthly User Closes the Offer"}}')


def name_a_test27a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Annual User Accepts First Offer Switch to Monthly"}}')


def name_a_test27b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Annual User Accepts Second Offer Half Price Basic Annual"}}')


def name_a_test27c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Annual User Cancels the Offer"}}')


def name_a_test27d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Basic Annual User Closes the Offer"}}')


def name_a_test28a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Annual User Accepts First Offer Switch to Monthly"}}')


def name_a_test_28b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Annual User Accepts Second Offer Basic Monthly"}}')


def name_a_test_28c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Annual User Cancels the Offer"}}')


def name_a_test_28d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Standard Annual User Closes the Offer"}}')


def name_a_test_29a(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Annual User Accepts First Offer Switch to Monthly"}}')


def name_a_test_29b(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Annual User Accepts Second Offer Basic Monthly"}}')


def name_a_test_29c(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Annual User Accepts Second Offer Standard Monthly"}}')


def name_a_test_29d(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Annual User Cancels the Offer"}}')


def name_a_test_29e(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Pro Annual User Closes the Offer"}}')


def name_a_test_41a(browser, email_pricing_format):
    browser.execute_script(f'browserstack_executor: {{"action": "setSessionName", "arguments": {{"name": "Verify First offer for {email_pricing_format} user"}}}}')


def name_a_test_41b(browser, email_pricing_format):
    browser.execute_script(f'browserstack_executor: {{"action": "setSessionName", "arguments": {{"name": "Verify Second offer for {email_pricing_format} user"}}}}')


def name_a_test_41c(browser, email_pricing_format):
    browser.execute_script(f'browserstack_executor: {{"action": "setSessionName", "arguments": {{"name": "Verify First offer for {email_pricing_format} user"}}}}')


def name_a_test_41d(browser, email_pricing_format):
    browser.execute_script(f'browserstack_executor: {{"action": "setSessionName", "arguments": {{"name": "Verify Second offer for {email_pricing_format} user"}}}}')


def name_a_test_cal1(browser, day):
    browser.execute_script(f'browserstack_executor: {{"action": "setSessionName", "arguments": {{"name": "Test Social Media Calendar for a month day: {day}"}}}}')


# PTV Photo to Video and Shopify
def name_ptv_01(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify PTV functionalities"}}')


def name_shop_01(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Verify Shopify functionalities"}}')


# Assertions for New Cancellation
def assertion_cancellation(browser):
    """
    BrowserStack assertion for correctly executed cancellation test - cancel offer
    """
    is_visible(browser, SUB_PENDING_CANCEL, 3)
    text = get_element_text(browser, SUB_PENDING_CANCEL)
    if (sub_pending_title_cancel == text) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Cancellation flow pending"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Cancellation flow not pending"}}')


def assertion_cancellation2(browser):
    """
       BrowserStack assertion for correctly executed cancellation test - accept offer
       """
    is_visible(browser, SUB_WILL_RENEW, 3)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    if (sub_will_renew in text2) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Offer Accepted"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Failed to Accept Offer"}}')


def assertion_cancellation3(browser):
    """
       BrowserStack assertion for correctly executed cancellation test - close offer
       """
    if is_visible(browser, CANCEL_SUBSCRIPTION_LINK, 3) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Cancellation not started"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Cancellation not correct"}}')


def assertion_cancellation4(browser):
    """
       BrowserStack assertion for correctly executed cancellation test - downgrade offer
       """
    is_visible(browser, SUB_WILL_RENEW)
    text2 = get_element_text(browser, SUB_WILL_RENEW)
    if (sub_pending_title_downgrade in text2) is True:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Downgrade success"}}')
    else:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Downgrade failed"}}')


def animation_test_completed(browser):
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Animation tests completed"}}')


def assertion_monthly_plan_first_offer(browser, email_pricing_format):
    if email_pricing_format == 'cplanstartermonthly+test01':
        if is_visible(browser, BUSINESS_20_CENT_OFF) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C2 at 20% off displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C2 at 20% off not displayed"}}')
    elif email_pricing_format == 'cplanbusinessmonthly+test01':
        if is_visible(browser, BUSINESS_20_CENT_OFF) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C2 at 20% off displayed"}}')
        elif is_visible(browser, BUSINESS_20_CENT_OFF_1) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C2 at 20% off displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C2 at 20% off not displayed"}}')
    elif email_pricing_format == 'cplanagencymonthly+test01':
        if is_visible(browser, STARTER_AND_BUSINESS_TWO_OFFER) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C1/C2 displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C1/C2 not displayed"}}')


def assertion_monthly_plan_second_offer(browser, email_pricing_format):
    if email_pricing_format == 'cplanstartermonthly+test01':
        if is_visible(browser, STARTER_9_DOLLAR) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C1 at Half Price displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C1 at Half Price not displayed"}}')
    elif email_pricing_format == 'cplanbusinessmonthly+test01':
        if is_visible(browser, STARTER_18_DOLLAR) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C1 displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C1 not displayed"}}')
    elif email_pricing_format == 'cplanagencymonthly+test01':
        if is_visible(browser, UNLIMITED_CLIPS_6_MONTHS) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Special Offer displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Special Offer not displayed"}}')


def assertion_annual_plan_first_offer(browser, email_pricing_format):
    if email_pricing_format == 'cplanstarterannual+test01':
        if is_visible(browser, SWITCH_TO_MONTHLY_PLAN_TITLE) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Switch to Monthly displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Switch to Monthly not displayed"}}')
    elif email_pricing_format == 'cplanbusinessannual+test01':
        if is_visible(browser, SWITCH_TO_MONTHLY_PLAN_TITLE) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Switch to Monthly displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Switch to Monthly not displayed"}}')
    elif email_pricing_format == 'cplanagencyannual+test01':
        if is_visible(browser, SWITCH_TO_MONTHLY_PLAN_TITLE) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Switch to Monthly displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Switch to Monthly not displayed"}}')


def assertion_annual_plan_second_offer(browser, email_pricing_format):
    if email_pricing_format == 'cplanstarterannual+test01':
        if is_visible(browser, MONTHLY_BUSINESS) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C2 Monthly displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C2 Monthly not displayed"}}')
    elif email_pricing_format == 'cplanbusinessannual+test01':
        if is_visible(browser, STARTER_18_DOLLAR) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C1 displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C1 not displayed"}}')
    elif email_pricing_format == 'cplanagencyannual+test01':
        if is_visible(browser, STARTER_AND_BUSINESS_TWO_OFFER) is True:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "C1/C2 displayed"}}')
        else:
            browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "C1/C2 not displayed"}}')


def assertion_calendar_page_displayed(browser):
    if publish_page_title in browser.title:
        browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Rendering Successful"}}')
    elif social_calendar_title in browser.title:
        browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "This day doesnt exist in current month"}}')
    else:
        browser.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Rendering Unsuccessful"}}')