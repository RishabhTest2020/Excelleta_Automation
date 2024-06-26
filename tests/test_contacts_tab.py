import logging

from helpers.common_helpers import *
from pages.contacts_tab import *
from pytest_bdd import given, when, then
from tests.test_accounts_tab import accounts_steps

contacts_steps = Contacts()


@then('Verify contact table head column')
def acc_head_colm(browser):
    wait_for_ajax(browser)
    contacts_steps.verify_contacts_head_col(browser)


@when('Create an Contact')
def create_an_contact(browser):
    do_click(browser, add_contact_btn)
    contacts_steps.select_account(browser, accounts_steps.account_details[0])
    contacts_steps.add_contacts_data_in_txt_box(browser)
    contacts_steps.select_title_field(browser)
    contacts_steps.select_department_field(browser)
    contacts_steps.select_designation_field(browser)
    contacts_steps.select_report_to_field(browser)
    contacts_steps.select_gender_field(browser)
    contacts_steps.select_marital_field(browser)
    contacts_steps.select_contact_country_fields(browser)
    contacts_steps.select_contact_state_fields(browser)
    contacts_steps.select_contact_city_fields(browser)
    contacts_steps.fill_contact_billing_txtbox_data(browser)
    do_click(browser, save_btn)


@then('Verify created contact data')
def verify_account(browser):
    contact_class_data = get_class_global_variables_dict(contacts_steps)
    logging.info(contact_class_data.values())
    contacts_steps.verify_created_contact(browser, contact_class_data)
