import logging

from selenium.webdriver import Keys

from helpers.common_helpers import *
from pages.accounts_tab import *
from pytest_bdd import given, when, then
from pages.rfq_tab import Rfq


accounts_steps = Accounts()
norms_steps = Norms()
rfq_steps = Rfq()


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
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    do_click(browser, save_btn)
    nav_path = accounts_nav_name_loc[1].replace('acc_name', accounts_steps.account_details[0])
    nav_loc = replace_in_tuple(accounts_nav_name_loc, 1, nav_path)
    should_be_visible(browser, nav_loc, 'acc_nav_check')


@then('Verify created account data')
def verify_account(browser):
    acc_class_data = get_class_global_variables_dict(accounts_steps)
    logging.info(acc_class_data.values())
    accounts_steps.verify_created_account(browser, acc_class_data)


@then('Create norms data')
def create_norms(browser):
    pdb_apply()
    do_click(browser, accounts_norms)
    sleep(2)
    # norms_steps.select_bop_norms(browser)
    norms_steps.select_raw_material_norm(browser)
    norms_steps.select_process_norms(browser, 'MAPL B-12 Waluj') #rfq_steps.manufacturing_location)
    norms_steps.select_over_head_norms(browser, 'MAPL B-12 Waluj') #rfq_steps.manufacturing_location)

    # norms_steps.select_currency_norms(browser)
    # norms_steps.select_mhr_norms(browser, 'MAPL B-12 Waluj') #rfq_steps.manufacturing_location)
    pdb_apply()
