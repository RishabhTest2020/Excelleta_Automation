from pytest_bdd import when, then, given, parsers
from pages.assertion_page import *
from pages.assertion_smoke_page import *


@then('I check assertion main logo as logged')
def assertion1(browser):
    assertion_main_logo(browser)


@then('I check assertion URL UTM')
def assertion30(browser):
    assertion_url_utm(browser)


@then('I check assertion cookies')
def assertion2(browser):
    assertion_cookies(browser)


@then('I check assertion links')
def assertion3(browser):
    assertion_links(browser)


@then('I check assertion tool links')
def assertion3a(browser):
    assertion_tools_links(browser)


@then('I check assertion templates Footer links')
def assertion14(browser):
    assertion_templates_footer_links(browser)


@then('I check assertion templates Header links')
def assertion15(browser):
    assertion_templates_header_links(browser)


@then('I check assertion logos links')
def assertion3b(browser):
    assertion_logos_links(browser)


@then('I check assertion create page')
def assertion4(browser):
    assertion_create_page(browser)


@then('I check assertion empty textbox error')
def assertion5(browser):
    assertion_login_error_empty(browser)


@then('I check assertion wrong login')
def assertion6(browser):
    assertion_wrong_login(browser)


@then('I check assertion publish video')
def assertion7(browser):
    assertion_publish_video(browser)


@then('I check assertion deleted/logged out account')
def assertion8(browser):
    assertion_logged_out_account(browser)


@then('I check assertion draft deleted')
def assertion9(browser):
    assertion_draft_deleted(browser)


@then('I check assertion brand deleted')
def assertion10(browser):
    assertion_brand_deleted(browser)


@then('I check assertion changes in my account')
def assertion11(browser):
    assertion_changes_in_my_account(browser)


@then('I check assertion signup redirection')
def assertion12(browser):
    assertion_signup_redirection(browser)


@then('I check assertion logo and watermark sync')
def assertion13(browser):
    assertion_logo_and_watermark_sync(browser)


@then('I check assertion full preview')
def assertion14(browser):
    assertion_full_preview(browser)


@then('I check assertion My Calendar')
def assertion15(browser):
    assertion_my_calendar(browser)


@then('I check assertion Publisher')
def assertion16(browser):
    assertion_publisher(browser)


@then('I check assertion Shopify')
def assertion17(browser):
    assertion_shopify_dashboard(browser)


@then('I check assertion mobile path')
def assertion99(mob_browser):
    assertion_mobile_path(mob_browser)


@then('I check assertion video in mobile view')
def assertion100(mob_browser):
    assertion100a(mob_browser)


@then('I check assertion logged out on mobile')
def assertion101(mob_browser):
    assertion101a(mob_browser)


@then('I check assertion signup on mobile')
def assertion102(mob_browser):
    assertion102a(mob_browser)


@then('I check assertion of Planner in mobile view')
def assertion103(mob_browser):
    assertion103a(mob_browser)


@then('I check assertion pricing mobile')
def assertion104(mob_browser):
    assertion104a(mob_browser)

# JS script for naming the tests


@given('I name a test cookies')
def give_name1(browser):
    name_a_test1(browser)


@given('I name a test main logo')
def give_name2(browser):
    name_a_test2(browser)


@given('I name a test links')
def give_name3(browser):
    name_a_test3(browser)


@given('I name a test new login')
def give_name4(browser):
    name_a_test4(browser)


@given('I name a test empty login')
def give_name5(browser):
    name_a_test5(browser)


@given('I name a test wrong login')
def give_name6(browser):
    name_a_test6(browser)


@given('I name a test publish video')
def give_name7(browser):
    name_a_test7(browser)


@given('I name a test add media')
def give_name8(browser):
    name_a_test8(browser)


@given('I name a test signup')
def give_name9(browser):
    name_a_test9(browser)


@given('I name a test fb signup')
def give_name10(browser):
    name_a_test10(browser)


@given('I name a test google signup')
def give_name10b(browser):
    name_a_test10b(browser)


@given('I name a test filters')
def give_name10a(browser):
    name_a_test10a(browser)


@given('I name a test purchase a plan for watermark')
def give_name10c(browser):
    name_a_test10c(browser)


@given('I name a test purchase a plan for BM')
def give_name10d(browser):
    name_a_test10d(browser)


@given('I name a test purchase a plan for BM and watermark')
def give_name10e(browser):
    name_a_test10e(browser)


@given('I name a test sign out')
def give_name11(browser):
    name_a_test11(browser)


@given('I name a test draft publish')
def give_name12(browser):
    name_a_test12(browser)


@given('I name a test draft delete')
def give_name13(browser):
    name_a_test13(browser)


@given('I name a test brand manager basic')
def give_name14(browser):
    name_a_test14(browser)


@given('I name a test brand manager wizard')
def give_name15(browser):
    name_a_test15(browser)


@given('I name a test change password')
def give_name16(browser):
    name_a_test16(browser)


@given('I name get video share link')
def give_name16cb(browser):
    name_a_test16cb(browser)


@given('I name mobile view shared video test')
def give_name16a(mob_browser):
    name_a_test16a(mob_browser)


@given('I name mobile funnel')
def give_name16ab(mob_browser):
    name_a_test16ab(mob_browser)


@given('I name a test planner on mobile phase web')
def give_name16ac_web(browser):
    name_a_test16ac_web(browser)


@given('I name a test planner on mobile phase mobile')
def give_name16ac_mob(mob_browser):
    name_a_test16ac_mob(mob_browser)


@given('Test Completed')
def give_name16c(browser):
    name_a_test16c(browser)


@given('I name a test incorrect password change')
def give_name17(browser):
    name_a_test17(browser)


@given('I name a test mobile')
def give_name18(mob_browser):
    name_a_test18(mob_browser)


@given('I name a test purchase a plan')
def give_name19(browser):
    name_a_test19(browser)


@given('I name test template page without login')
def give_name20(browser):
    name_a_test20(browser)


@given('I name test image resizer page without login')
def give_name20_ir(browser):
    name_a_test20_ir(browser)


@given('I name test image resizer page after login')
def give_name20_ir_2(browser):
    name_a_test20_ir_2(browser)


@given('I name test mobile view of image resizer page after login')
def give_name20_ir_3(mob_browser):
    name_a_test20_ir_3(mob_browser)


@given('I name test mobile view of image resizer page without login')
def give_name20_ir_4(mob_browser):
    name_a_test20_ir_4(mob_browser)


@given('I name test template page after login')
def give_name21(browser):
    name_a_test21(browser)


@given('I name test deleted account login')
def give_name22(browser):
    name_a_test22(browser)


@given('I name a tools links')
def give_name23(browser):
    name_a_test23(browser)


@given('I name a logo links')
def give_name24(browser):
    name_a_test_24(browser)


@given('I name a test purchase a plan with 2FA')
def give_name25(browser):
    name_a_test25(browser)


@given('I name a test B1 to AB1 on publish page')
def give_name25e(browser):
    name_a_test25e(browser)


@given('I name a test Starter Annual purchases a plan and cancels it')
def give_name26(browser):
    name_a_test26(browser)


@given('I name a editorial test filters')
def give_name28(browser):
    name_a_test28(browser)


@given('I name a editorial test filters with subscribed user')
def give_name27(browser):
    name_a_test27(browser)


@given('I name a editorial test filters with starter plan user')
def give_name29(browser):
    name_a_test29(browser)


@given('I name a UTM check')
def give_name30(browser):
    name_a_test30(browser)


@given('I name a Promo Performance Tests')
def give_name31(browser):
    name_a_test31(browser)


@given('I name Animation Tests')
def give_name31a(browser):
    name_a_test31a(browser)


@given('I name Animation Tests second half set')
def give_name31b(browser):
    name_a_test31b(browser)


@given('I name a test create from photo uploaded')
def give_name32(browser):
    name_a_test32(browser)


@given('I name a test footer links on Promo-next')
def give_name33(browser):
    name_a_test33(browser)


@given('I name a test header links on Promo-next')
def give_name34(browser):
    name_a_test34(browser)


@given('I name a test edit video')
def give_name35(browser):
    name_a_test35(browser)


@given('I name a test aspect ratio functionalities')
def give_name35a(browser):
    name_a_test35a(browser)


@given('I name a test full preview')
def give_name36(browser):
    name_a_test36(browser)


@given('I name Publisher Tests')
def give_name37(browser):
    name_a_test_37(browser)


@given('I name Scheduler Happy Path Tests')
def give_name38(browser):
    name_a_test_38(browser)


@given('I name Scheduler with Issues Tests')
def give_name39(browser):
    name_a_test_39(browser)


@given('I name Scheduler edit and scheduler')
def give_name41(browser):
    name_a_test_41(browser)


@given('I name publish YT and LI')
def give_name42(browser):
    name_a_test_42(browser)


@given('I name reschedule YT and LI')
def give_name43(browser):
    name_a_test_43(browser)


@given('I name a new post button')
def give_name44(browser):
    name_a_test_44(browser)


@given('I name a post duplication')
def give_name45(browser):
    name_a_test_45(browser)


@given('I name a planner post duplication published')
def give_name46(browser):
    name_a_test_46(browser)


@given('I name a planner post duplication scheduled')
def give_name47(browser):
    name_a_test_47(browser)


@given('I name create another post from publish summary')
def give_name48(browser):
    name_a_test_48(browser)


@given('I name test verify predefined ratio')
def give_name49(browser):
    name_a_test_49(browser)


@given('I name a test create from video uploaded')
def give_name50(browser):
    name_a_test_50(browser)


@given('I name not logged on mobile')
def give_name51(mob_browser):
    name_a_test51(mob_browser)


@given('I name a test clean mobile user')
def give_name52(browser):
    name_a_test52(browser)


TYPES = {'d': str}


@given(parsers.cfparse('I name a "{env:d}" test generate video', extra_types=TYPES))
@given('I name a "<env>" test generate video')
def give_name40(browser, env):
    name_a_test_40(browser, env)


# JS script for naming Smoke tests
@given('I name a test smoke new user')
def give_name_s1(browser):
    name_a_smoke_test1(browser)


@given('I name a test smoke existing user')
def give_name_s2(browser):
    name_a_smoke_test2(browser)


# Photo to Video - PTV and Shopify

@given('I name PTV Test sanity')
def give_name_ptv1(browser):
    name_ptv_01(browser)


@given('I name Shopify Test sanity')
def give_name_shop1(browser):
    name_shop_01(browser)


# Steps for naming cancellation flow

@given('I name a test Starter Monthly Cancels the Offer Survey 1st')
def give_name_p1a(browser):
    name_a_test_pricing1a(browser)


@given('I name a test Starter Monthly Cancels the Offer Survey 2nd')
def give_name_p1b(browser):
    name_a_test_pricing1b(browser)


@given('I name a test Starter Monthly Accepts the Offer Survey 1st')
def give_name_p2a(browser):
    name_a_test_pricing2a(browser)


@given('I name a test Starter Monthly Accepts the Offer Survey 2nd')
def give_name_p2b(browser):
    name_a_test_pricing2b(browser)


@given('I name a test Starter Monthly Accepts second Offer Survey 2nd')
def give_name_p2b(browser):
    name_a_test_pricing2c(browser)


@given('I name a test Starter Monthly Closes the Offer Survey 1st')
def give_name_p3a(browser):
    name_a_test_pricing3a(browser)


@given('I name a test Starter Monthly Closes the Offer Survey 2nd')
def give_name_p3b(browser):
    name_a_test_pricing3b(browser)


@given('I name a test Business Monthly Cancels the Offer Survey 1st')
def give_name_p4a(browser):
    name_a_test_pricing4a(browser)


@given('I name a test Business Monthly Cancels the Offer Survey 2nd')
def give_name_p4b(browser):
    name_a_test_pricing4b(browser)


@given('I name a test Business Monthly Accepts 1st Offer Survey 1st')
def give_name_p5a(browser):
    name_a_test_pricing5a(browser)


@given('I name a test Business Monthly Accepts 1st Offer Survey 2nd')
def give_name_p5b(browser):
    name_a_test_pricing5b(browser)


@given('I name a test Business Monthly Accepts 2nd Offer Survey 1st')
def give_name_p6a(browser):
    name_a_test_pricing6a(browser)


@given('I name a test Business Monthly Accepts 2nd Offer Survey 2nd')
def give_name_p6b(browser):
    name_a_test_pricing6b(browser)


@given('I name a test Agency Monthly Cancels the Offer Survey 1st')
def give_name_p7a(browser):
    name_a_test_pricing7a(browser)


@given('I name a test Agency Monthly Cancels the Offer Survey 2nd')
def give_name_p7b(browser):
    name_a_test_pricing7b(browser)


@given('I name a test Agency Monthly Accepts 1st Offer A - Survey 1st')
def give_name_p8a(browser):
    name_a_test_pricing8a(browser)


@given('I name a test Agency Monthly Accepts 1st Offer A - Survey 2nd')
def give_name_p8b(browser):
    name_a_test_pricing8b(browser)


@given('I name a test Agency Monthly Accepts 1st Offer B - Survey 1st')
def give_name_p9a(browser):
    name_a_test_pricing9a(browser)


@given('I name a test Agency Monthly Accepts 1st Offer B - Survey 2nd')
def give_name_p9b(browser):
    name_a_test_pricing9b(browser)


@given('I name a test Agency Monthly Accepts 2nd Offer - Survey 1st')
def give_name_p10a(browser):
    name_a_test_pricing10a(browser)


@given('I name a test Agency Monthly Accepts 2nd Offer - Survey 2nd')
def give_name_p10b(browser):
    name_a_test_pricing10b(browser)


@given('I name a test Special Offer User Cancels the Offer - Survey 1st')
def give_name_p11a(browser):
    name_a_test_pricing11a(browser)


@given('I name a test Special Offer User Cancels the Offer - Survey 2nd')
def give_name_p11b(browser):
    name_a_test_pricing11b(browser)


@given('I name a test Special Offer User Accepts 1st Offer A - Survey 1st')
def give_name_p12a(browser):
    name_a_test_pricing12a(browser)


@given('I name a test Special Offer User Accepts 1st Offer A - Survey 2nd')
def give_name_p12b(browser):
    name_a_test_pricing12b(browser)


@given('I name a test Special Offer User Accepts 1st Offer B - Survey 1st')
def give_name_p13a(browser):
    name_a_test_pricing13a1(browser)


@given('I name a test Special Offer User Accepts 1st Offer B - Survey 2nd')
def give_name_p13b(browser):
    name_a_test_pricing13a2(browser)


@given('I name a test Special Offer User Accepts 2nd Offer - Survey 1st')
def give_name_p13a(browser):
    name_a_test_pricing13b1(browser)


@given('I name a test Special Offer User Accepts 2nd Offer - Survey 2nd')
def give_name_p13a(browser):
    name_a_test_pricing13b2(browser)


@given('I name a test Starter Annual Cancels the Offer - Survey 1st')
def give_name_p14a(browser):
    name_a_test_pricing14a(browser)


@given('I name a test Starter Annual Cancels the Offer - Survey 2nd')
def give_name_p14b(browser):
    name_a_test_pricing14b(browser)


@given('I name a test Starter Annual Accepts 1st Offer - Survey 1st')
def give_name_p15a(browser):
    name_a_test_pricing15a(browser)


@given('I name a test Starter Annual Accepts 1st Offer - Survey 2nd')
def give_name_p15b(browser):
    name_a_test_pricing15b(browser)


@given('I name a test Starter Annual Accepts 2nd Offer - Survey 1st')
def give_name_p16a(browser):
    name_a_test_pricing16a(browser)


@given('I name a test Starter Annual Accepts 2nd Offer - Survey 2nd')
def give_name_p16b(browser):
    name_a_test_pricing16b(browser)


@given('I name a test Business Annual Cancels the Offer - Survey 1st')
def give_name_p17a(browser):
    name_a_test_pricing17a(browser)


@given('I name a test Business Annual Cancels the Offer - Survey 2nd')
def give_name_p17b(browser):
    name_a_test_pricing17b(browser)


@given('I name a test Business Annual Accepts 1st Offer - Survey 1st')
def give_name_p18a(browser):
    name_a_test_pricing18a(browser)


@given('I name a test Business Annual Accepts 1st Offer - Survey 2nd')
def give_name_p18b(browser):
    name_a_test_pricing18b(browser)


@given('I name a test Business Annual Accepts 2nd Offer - Survey 1st')
def give_name_p19a(browser):
    name_a_test_pricing19a(browser)


@given('I name a test Business Annual Accepts 2nd Offer - Survey 2nd')
def give_name_p19b(browser):
    name_a_test_pricing19b(browser)


@given('I name a test Agency Annual Cancels the Offer - Survey 1st')
def give_name_p20a(browser):
    name_a_test_pricing20a(browser)


@given('I name a test Agency Annual Cancels the Offer - Survey 2nd')
def give_name_p20b(browser):
    name_a_test_pricing20b(browser)


@given('I name a test Agency Annual Accepts 1st Offer - Survey 1st')
def give_name_p21a(browser):
    name_a_test_pricing21a(browser)


@given('I name a test Agency Annual Accepts 1st Offer - Survey 2nd')
def give_name_p21b(browser):
    name_a_test_pricing21b(browser)


@given('I name a test Agency Annual Accepts 2nd Offer A - Survey 1st')
def give_name_p22a(browser):
    name_a_test_pricing22a(browser)


@given('I name a test Agency Annual Accepts 2nd Offer A - Survey 2nd')
def give_name_p22b(browser):
    name_a_test_pricing22b(browser)


@given('I name a test Agency Annual Accepts 2nd Offer B - Survey 1st')
def give_name_p23a(browser):
    name_a_test_pricing23a(browser)


@given('I name a test Agency Annual Accepts 2nd Offer B - Survey 2nd')
def give_name_p23b(browser):
    name_a_test_pricing23b(browser)


@given('I name a test Basic Monthly User Accepts First and Only Offer')
def give_name_b1a(browser):
    name_a_test_pricing24a(browser)


@given('I name a test Basic Monthly User Accepts Second Offer')
def give_name_b1b(browser):
    name_a_test_pricing24b(browser)


@given('I name a test Basic Monthly User Cancels the Offer')
def give_name_b1c(browser):
    name_a_test24c(browser)


@given('I name a test Basic Monthly User Closes the Offer')
def give_name_b1d(browser):
    name_a_test24d(browser)


@given('I name a test standard monthly accepts first offer and only offer')
def give_name_b2a(browser):
    name_a_test25a(browser)


@given('I name a test Standard Monthly User Accepts Second Offer')
def give_name_b2b(browser):
    name_a_test25b(browser)


@given('I name a test Standard Monthly User Cancels the offer')
def give_name_b2c(browser):
    name_a_test25c(browser)


@given('I name a test Standard Monthly User Closes the offer')
def give_name_b2d(browser):
    name_a_test25d(browser)


@given('I name a test Pro Monthly User Accepts First Offer Basic Monthly')
def give_name_b3a(browser):
    name_a_test26a(browser)


@given('I name a test Pro Monthly User Accepts First Offer Standard Monthly')
def give_name_b3b(browser):
    name_a_test26b(browser)


@given('I name a test Pro Monthly User Accepts special offer')
def give_name_b3c(browser):
    name_a_test26c(browser)


@given('I name a test Pro Monthly User Cancels the offer')
def give_name_b3d(browser):
    name_a_test26d(browser)


@given('I name a test Pro Monthly User Closes the offer')
def give_name_b3e(browser):
    name_a_test26e(browser)


@given('I name a test Basic Annual User Accepts First and Only Offer')
def give_name_b33a(browser):
    name_a_test27a(browser)


@given('I name a test Basic Annual User Accepts Second Offer')
def give_name_b33b(browser):
    name_a_test27b(browser)


@given('I name a test Basic Annual User Cancels the offer')
def give_name_b33c(browser):
    name_a_test27c(browser)


@given('I name a test Basic Annual User Closes the offer')
def give_name_b33d(browser):
    name_a_test27d(browser)


@given('I name a test standard Annual User Accepts First and only offer')
def give_name_b34a(browser):
    name_a_test28a(browser)


@given('I name a test standard Annual User Second offer')
def give_name_b34b(browser):
    name_a_test_28b(browser)


@given('I name a test standard Annual User Cancels the offer')
def give_name_b34c(browser):
    name_a_test_28c(browser)


@given('I name a test standard Annual User Closes the offer')
def give_name_b34d(browser):
    name_a_test_28d(browser)


@given('I name a test Pro Annual User Accepts First and Only Offer')
def give_name_b35a(browser):
    name_a_test_29a(browser)


@given('I name a test Pro Annual User Accepts Second Offer Basic Monthly')
def give_name_b35b(browser):
    name_a_test_29b(browser)


@given('I name a test Pro Annual User Accepts Second Offer Standard Monthly')
def give_name_b35c(browser):
    name_a_test_29c(browser)


@given('I name a test Pro Annual User Cancels the Offer')
def give_name_b35d(browser):
    name_a_test_29d(browser)


@given('I name a test Pro Annual User Closes the Offer')
def give_name_b35e(browser):
    name_a_test_29e(browser)


@given(parsers.cfparse('I name a test Verify first offer for C Plan monthly user "{email_pricing_format:d}"', extra_types=TYPES))
@given('I name a test Verify first offer for C Plan monthly user "<email_pricing_format>"')
def give_name_b36a(browser, email_pricing_format):
    name_a_test_41a(browser, email_pricing_format)


@given(parsers.cfparse('I name a test verify second offer for C Plan monthly user "{email_pricing_format:d}"', extra_types=TYPES))
@given('I name a test verify second offer for C Plan monthly user "<email_pricing_format>"')
def give_name_b36b(browser, email_pricing_format):
    name_a_test_41b(browser, email_pricing_format)


@given(parsers.cfparse('I name a test verify first offer for C Plan annual user "{email_pricing_format:d}"', extra_types=TYPES))
@given('I name a test verify first offer for C Plan annual user "<email_pricing_format>"')
def give_name_b36c(browser, email_pricing_format):
    name_a_test_41c(browser, email_pricing_format)


@given(parsers.cfparse('I name a test verify second offer for C Plan annual user "{email_pricing_format:d}"', extra_types=TYPES))
@given('I name a test verify second offer for C Plan annual user "<email_pricing_format>"')
def give_name_b36d(browser, email_pricing_format):
    name_a_test_41d(browser, email_pricing_format)


# Steps for naming assertion for cancellation flow


@then('I check assertion for cancellation flow')
def assert_cancellation_t1(browser):
    assertion_cancellation(browser)


@then('I check assertion for accepted offer')
def assert_cancellation_t2(browser):
    assertion_cancellation2(browser)


@then('I check assertion for closed offer')
def assert_cancellation_t3(browser):
    assertion_cancellation3(browser)


@then('I check assertion for downgrade flow')
def assert_cancellation_t4(browser):
    assertion_cancellation4(browser)


@then(parsers.cfparse('I check assertion for displayed offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('I check assertion for displayed offer "<email_pricing_format>"')
def assert_displayed_offer_u1(browser, email_pricing_format):
    assertion_monthly_plan_first_offer(browser, email_pricing_format)


@then(parsers.cfparse('I check assertion for displayed second offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('I check assertion for displayed second offer "<email_pricing_format>"')
def assert_displayed_offer_u2(browser, email_pricing_format):
    assertion_monthly_plan_second_offer(browser, email_pricing_format)


@then(parsers.cfparse('I check assertion for displayed first offer "{email_pricing_format:d}"', extra_types=TYPES))
@then('I check assertion for displayed first offer "<email_pricing_format>"')
def assert_displayed_offer_u3(browser, email_pricing_format):
    assertion_annual_plan_first_offer(browser, email_pricing_format)


@then(parsers.cfparse('I check assertion for displayed second offer for annual plan users "{email_pricing_format}"', extra_types=TYPES))
@then('I check assertion for displayed second offer for annual plan users "<email_pricing_format>"')
def assert_displayed_offer_u4(browser, email_pricing_format):
    assertion_annual_plan_second_offer(browser, email_pricing_format)


@then('I check Animation test completed')
def assert_animation_tests(browser):
    animation_test_completed(browser)

# @then('I check assertion for pending offer')
# def assert_cancellation_t5(browser):
#     assertion_cancellation5(browser)


# Social Calendar
@given(parsers.cfparse('I name a test verify social media calendar day: "{day:d}"', extra_types=TYPES))
@given('I name a test verify social media calendar day: "<day>"')
def give_name_cal1(browser, day):
    name_a_test_cal1(browser, day)


@then('I check assertion for rendering all the templates')
def assert_calendar_page(browser):
    assertion_calendar_page_displayed(browser)


# Onboarding names
@given('I name a test onboarding skip')
def give_name_ob1(browser):
    name_a_test_ob1(browser)


@given('I name a test onboarding filled')
def give_name_ob2(browser):
    name_a_test_ob2(browser)


@given('I name a test leaving onboarding form empty')
def give_name_ob3(browser):
    name_a_test_ob3(browser)


@given('I name a test FB user completes onboarding')
def give_name_ob4(browser):
    name_a_test_ob4(browser)


@given('I name a test reaching to onboarding from templates page')
def give_name_ob5(browser):
    name_a_test_ob5(browser)


@given('I name a test onboarding add logo')
def give_name_ob6(browser):
    name_a_test_ob6(browser)