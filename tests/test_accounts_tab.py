from global_libs.global_imports import *
from helpers.common_helpers import *


@then('Verify accounts table head column')
def acc_head_colm(browser):
    verify_accounts_head_col(browser)


@then('Create an account')
def account_creation(browser):
    do_click(browser, add_accounts_btn)
    should_be_visible(browser, acc_basic_info_txt, 'acc_basic_info_txt')
    add_accounts_data_in_txt_box(browser)
    select_start_month_field(browser)
    select_rm_norms_field(browser)
    do_send_keys(browser, tnc_loc, 'TNC Automation')
    select_business_nature_field(browser)
    select_business_domain_field(browser)
    select_business_segment_field(browser)
    select_payment_method_field(browser)
    select_payment_term_field(browser)
    fill_billing_txtbox_data(browser)
    select_country_field(browser)
    select_state_field(browser)
    select_city_field(browser)
    do_click(browser, save_btn)
    pdb_apply()


