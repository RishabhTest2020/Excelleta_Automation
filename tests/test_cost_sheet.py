import logging
from selenium.common import ElementClickInterceptedException
from helpers.common_helpers import *
from locators.rfq_tab_locators import save_btn
from pages.cost_sheet_page import *
from pytest_bdd import given, when, then, parsers
from locators.cost_sheet_locators import *
from tests.test_rfq_tab import drawing_data_steps, rfq_steps
from tests.test_te_tab import te_all_data_dicts, create_testeps

cost_sheet_steps = CostSheetPage()
approve_cs_steps = Approve_Cost_Sheet()


@then(parsers.parse('Generate Costing Data and Norms, Nav direct {direct}'))
def generate_costing_norms(browser, direct):
    if direct == "true":
        mte = get_element_text(browser, costing_mte_loc)
        cost_sheet_steps.__dict__['mte_name'] = mte
        do_click(browser, costing_mte_loc)
        sleep(2)
    else:
        browser.get(globalEnvs.main_url + '/marketing-technical-evaluation')
        sleep(2)
        mte_name = drawing_data_steps.te_link.split("-")[1]
        cost_sheet_steps.goto_created_mte(browser, mte_name)
    do_click(browser, generate_costing_bn_loc)
    sleep(2)
    do_click(browser, cs_actions_btn_loc)
    sleep(1)
    do_click(browser, cs_actions_norms_btn_loc)
    should_be_visible(browser, cs_actions_norms_header_loc, "cs_actions_norms_header_loc")
    cost_sheet_steps.rm_norms_fiscal_year_option(browser, index='6')
    cost_sheet_steps.rm_norms_date_range_option(browser, index='2')
    #cost_sheet_steps.bop_norms_date_range_option(browser, index=2) #Not getting Values in this drop down
    cost_sheet_steps.process_norms_date_range_selection(browser, index='2')
    cost_sheet_steps.other_norms_date_range_selection(browser, index='2')
    cost_sheet_steps.over_head_norms_selection(browser, index='1')
    do_click(browser, generate_costing_btn_loc)
    sleep(2)
    do_click(browser, cs_add_expense_btn_loc)
    should_be_visible(browser, cs_add_expense_header_loc, "cs_add_expense_header_loc")
    cost_sheet_steps.add_expense_flat_rate(browser)
    do_click(browser, add_update_btn_loc)
    sleep(2)
    try:
        do_click(browser, save_btn)
    except ElementClickInterceptedException:
        sleep(2)
        do_click(browser, save_btn)
    sleep(2)
    current_url = browser.current_url
    assert 'MTE' in current_url


@then('Goto MTE Cost Sheet')
def mte_cost_sheet(browser):
    try:
        mte_name = drawing_data_steps.te_link.split("-")[1]
    except:
        mte_name = cost_sheet_steps.__dict__['mte_name'].split("-")[1].split(" ")[0]
    cost_sheet_steps.goto_created_cost_sheet(browser, mte_name)


@then(parsers.parse('Verify Cost Raw Material data {section}'))
def verify_te_data(browser, section):
    create_te_class_data = get_class_global_variables_dict(cost_sheet_steps)
    create_te_class_data['te_all_data_dicts'] = te_all_data_dicts
    logging.info(create_te_class_data.values())
    cost_sheet_steps.verify_cost_sections_data(browser, create_te_class_data, section)


@then(parsers.parse('Approve CS all levels'))
def approve_cs_levels(browser):
    current_url = browser.current_url
    cs_no = current_url.split("/")[-1]
    approve_cs_steps.approve_cost_sheet(browser, cs_no, rfq_steps.business_dev_head, rfq_steps.cft_member,
                                        rfq_steps.business_dev_head)


@then(parsers.parse('Reject CS at level {level:d}, cs reason {reason}'))
def approve_cs_levels(browser, level, reason):
    current_url = browser.current_url
    cs_no = current_url.split("/")[-1]
    approve_cs_steps.reject_cost_sheet(browser, level, cs_no, reason, rfq_steps.business_dev_head, rfq_steps.cft_member,
                                       rfq_steps.business_dev_head)


@then('Revoke Cost sheet')
def revoke_cost_sheet_data(browser):
    approve_cs_steps.revoke_cost_sheet(browser)
