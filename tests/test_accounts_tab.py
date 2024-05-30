from global_libs.global_imports import *
from helpers.common_helpers import *

accounts_steps = Accounts()


@then('Verify accounts table head column')
def acc_head_colm(browser):
    wait_for_ajax(browser)
    accounts_steps.verify_accounts_head_col(browser)


@then('Create an account')
def account_creation(browser):
    do_click(browser, add_accounts_btn)
    should_be_visible(browser, acc_basic_info_txt, 'acc_basic_info_txt')
    accounts_steps.add_accounts_data_in_txt_box(browser)
    accounts_steps.select_start_month_field(browser)
    accounts_steps.select_rm_norms_field(browser)
    do_send_keys(browser, tnc_loc, 'TNC Automation')
    accounts_steps.select_business_nature_field(browser)
    accounts_steps.select_business_domain_field(browser)
    accounts_steps.select_business_segment_field(browser)
    accounts_steps.select_payment_method_field(browser)
    accounts_steps.select_payment_term_field(browser)
    accounts_steps.fill_billing_txtbox_data(browser)
    accounts_steps.select_country_field(browser)
    accounts_steps.select_state_field(browser)
    accounts_steps.select_city_field(browser)
    do_click(browser, save_btn)


@then('Verify created account data')
def verify_account(browser):
    acc_class_data = get_class_global_variables_dict(accounts_steps)
    accounts_steps.verify_created_account(browser, acc_class_data)
