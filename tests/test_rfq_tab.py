import logging

from helpers.common_helpers import *
from locators.accounts_tab_locators import save_btn
from pages.rfq_tab import *
from pytest_bdd import given, when, then
from tests.test_accounts_tab import accounts_steps

rfq_steps = Rfq()
drawing_data_steps = Drawing_data()


@then('Verify Rfq table head column')
def acc_head_colm(browser):
    wait_for_ajax(browser)
    rfq_steps.verify_rfq_head_col(browser)


@then('Create a RFQ')
def create_rfq(browser):
    do_click(browser, add_rfq_btn)
    rfq_steps.select_account_and_key_person(browser, accounts_steps.account_details[0])
    rfq_steps.select_business_evaluation(browser)
    rfq_steps.verify_domain(browser, 'Domestic')
    rfq_steps.select_business_nature(browser)
    rfq_steps.select_business_segment(browser)
    rfq_steps.select_business_value(browser)
    rfq_steps.fill_rfq_txt_box(browser)
    rfq_steps.select_rfq_received_date(browser)
    rfq_steps.select_confidentiality(browser)
    rfq_steps.select_customer_target_date(browser)
    rfq_steps.select_dev_lead_location(browser)
    rfq_steps.select_manufacturing_location(browser)
    rfq_steps.select_company_priority(browser)
    rfq_steps.select_finalizing_date(browser)
    rfq_steps.select_cft_completion_date(browser)
    rfq_steps.select_cft_member(browser)
    rfq_steps.select_costing_completion_date(browser)
    rfq_steps.select_costing_format(browser)
    rfq_steps.select_currency(browser)
    rfq_steps.select_surface_treatment_head(browser)
    rfq_steps.select_estimates_sop(browser)
    rfq_steps.select_incoterms(browser)
    rfq_steps.select_offer_validity(browser)
    rfq_steps.select_other_info_checkbox(browser)
    rfq_steps.select_packaging_cost(browser)
    rfq_steps.select_per_annum_volume(browser)
    rfq_steps.select_per_day_volume(browser)
    rfq_steps.select_plant_head(browser)
    rfq_steps.select_project_life(browser)
    rfq_steps.select_quotation_type(browser)
    rfq_steps.select_rfq_shipping_address(browser)
    rfq_steps.select_rfq_toggles(browser)
    rfq_steps.select_development_lead(browser)
    rfq_steps.select_marketing_lead(browser)
    rfq_steps.select_pm_lead(browser)
    rfq_steps.select_marketing_lead(browser)
    rfq_steps.verify_heading(browser)
    do_click(browser, save_btn)


@then('Verify created Rfq data')
def verify_account(browser):
    pdb_apply()
    rfq_class_data = get_class_global_variables_dict(rfq_steps)
    logging.info(rfq_class_data.values())
    rfq_steps.verify_created_dict(browser, rfq_class_data)


@then('Add Drawing Data')
def create_drawing_data(browser):
    drawing_data_steps.goto_rfq_verify_chart_blink(browser, rfq_steps.rfq_id)
    drawing_data_steps.add_drawing_data(browser)
    drawing_data_steps.select_2d_soft_copy(browser)
    drawing_data_steps.select_3d_soft_copy(browser)
    drawing_data_steps.add_roi_and_approve(browser)
    drawing_data_steps.add_technical_feasibility(browser)
