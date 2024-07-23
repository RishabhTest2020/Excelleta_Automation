import logging
from helpers.common_helpers import *
from pages.cost_sheet_page import *
from pytest_bdd import given, when, then
from locators.cost_sheet_locators import *


cost_sheet_steps = CostSheetPage()


@then('Generate Costing Data')
def generate_costing_norms(browser):
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
