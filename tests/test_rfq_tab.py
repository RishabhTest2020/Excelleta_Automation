import logging

from helpers.common_helpers import *
from locators.accounts_tab_locators import save_btn
from pages.rfq_tab import *
from pytest_bdd import given, when, then, parsers
from tests.test_accounts_tab import accounts_steps

rfq_steps = Rfq()
drawing_data_steps = Drawing_data()


@then('Verify Rfq table head column')
def acc_head_colm(browser):
    wait_for_ajax(browser)
    rfq_steps.verify_rfq_head_col(browser)


@then(parsers.parse('Create a RFQ {types}'))
def create_rfq(browser, types):
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
    rfq_steps.select_costing_completion_date(browser)
    rfq_steps.select_costing_format(browser)
    rfq_steps.select_currency(browser)
    rfq_steps.select_estimates_sop(browser)
    rfq_steps.select_incoterms(browser)
    rfq_steps.select_offer_validity(browser)
    rfq_steps.select_other_info_checkbox(browser)
    rfq_steps.select_packaging_cost(browser)
    rfq_steps.select_per_annum_volume(browser)
    rfq_steps.select_per_day_volume(browser)
    rfq_steps.select_project_life(browser)
    rfq_steps.select_quotation_type(browser)
    rfq_steps.select_rfq_shipping_address(browser)
    rfq_steps.select_rfq_toggles(browser, types)
    rfq_steps.select_development_lead(browser)
    rfq_steps.select_marketing_lead(browser)
    rfq_steps.select_pm_lead(browser)
    rfq_steps.select_marketing_lead(browser)
    rfq_steps.select_plant_head(browser)
    rfq_steps.select_surface_treatment_head(browser)
    rfq_steps.select_cft_member(browser)
    rfq_steps.select_business_dev_head(browser)
    rfq_steps.verify_heading(browser)
    do_click(browser, save_btn)
    loader_should_be_invisile(browser, 5)
    current_url = browser.current_url
    assert 'editRFQ' in current_url
    rfq_no = current_url.split("/")[-2]
    rfq_steps.__dict__["rfq_url_id"] = f'RFQ-{rfq_no}'


@then('Verify created Rfq data')
def verify_account(browser):
    rfq_class_data = get_class_global_variables_dict(rfq_steps)
    date1 = rfq_class_data['costing_completion']
    date1_obj = datetime.strptime(date1, '%m/%d/%Y')
    date1_date = date1_obj.strftime('%d-%m-%Y')
    rfq_class_data['costing_completion'] = date1_date
    date2 = rfq_class_data['cft_completion']
    date2_obj = datetime.strptime(date2, '%m/%d/%Y')
    date2_date = date2_obj.strftime('%d-%m-%Y')
    rfq_class_data['cft_completion'] = date2_date
    date3 = rfq_class_data['finalizing_date']
    date3_obj = datetime.strptime(date3, '%m/%d/%Y')
    date3_date = date3_obj.strftime('%d-%m-%Y')
    rfq_class_data['finalizing_date'] = date3_date
    date4 = rfq_class_data['estimates_sop']
    date4_obj = datetime.strptime(date4, '%m/%d/%Y')
    date4_date = date4_obj.strftime('%d-%m-%Y')
    rfq_class_data['estimates_sop'] = date4_date
    date5 = rfq_class_data['customer_target_date']
    date5_obj = datetime.strptime(date5, '%m/%d/%Y')
    date5_date = date5_obj.strftime('%d-%m-%Y')
    rfq_class_data['customer_target_date'] = date5_date
    date6 = rfq_class_data['rfq_received_date']
    date6_obj = datetime.strptime(date6, '%m/%d/%Y')
    date6_date = date6_obj.strftime('%d-%m-%Y')
    rfq_class_data['rfq_received_date'] = date6_date
    rfq_class_data['acc_name'] = accounts_steps.account_details[0]
    rfq_class_data['own_name'] = 'Saurabh Shrivastava'
    rfq_class_data['domain'] = business_domain_list[1]
    rfq_class_data['nature'] = business_nature_list[1]
    address = rfq_class_data['rfq_shipping_address'].replace('(', "").replace(')', "")
    addrr = [x.lstrip(" ") for x in address.split(",")[1:]]
    address_str = address.split(",")[0] + ', ' + ",".join(addrr)
    rfq_class_data['rfq_shipping_address'] = address_str
    logging.info(rfq_class_data.values())
    rfq_steps.verify_created_dict(browser, rfq_class_data)


@then('Add Drawing Data')
def create_drawing_data(browser):
    drawing_data_steps.goto_rfq_verify_chart_blink(browser, rfq_steps.__dict__['rfq_url_id'])
    drawing_data_steps.add_drawing_data(browser)
    drawing_data_steps.select_2d_soft_copy(browser)
    drawing_data_steps.select_3d_soft_copy(browser)
    drawing_data_steps.add_roi_and_approve(browser)
    drawing_data_steps.add_technical_feasibility(browser)
    loader_should_be_invisile(browser, 10)
