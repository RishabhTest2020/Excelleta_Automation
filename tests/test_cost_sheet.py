import logging
from helpers.common_helpers import *
from locators.rfq_tab_locators import save_btn
from pages.cost_sheet_page import *
from pytest_bdd import given, when, then, parsers
from locators.cost_sheet_locators import *
from tests.test_rfq_tab import drawing_data_steps
from tests.test_te_tab import te_all_data_dicts, create_testeps

cost_sheet_steps = CostSheetPage()


@then('Generate Costing Data and Norms')
def generate_costing_norms(browser):
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
    do_click(browser, save_btn)
    sleep(2)
    current_url = browser.current_url
    assert 'MTE' in current_url


@then(parsers.parse('Verify Cost Raw Material data {section}'))
def verify_te_data(browser, section):
    mte_name = drawing_data_steps.te_link.split("-")[1]
    cost_sheet_steps.goto_created_cost_sheet(browser, mte_name)
    create_te_class_data = get_class_global_variables_dict(cost_sheet_steps)
    create_te_class_data['te_all_data_dicts'] = te_all_data_dicts
    logging.info(create_te_class_data.values())
    cost_sheet_steps.verify_cost_sections_data(browser, create_te_class_data, section)