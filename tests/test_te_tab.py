import logging

from helpers.common_helpers import *
from locators.accounts_tab_locators import save_btn
from pages.rfq_tab import Drawing_data
from pages.technical_evaluation_tab import *
from pytest_bdd import given, when, then
from tests.test_rfq_tab import drawing_data_steps, rfq_steps


create_testeps = Create_TE()
approve_te_steps = Approve_TE()


@when('Create TE data')
def create_te_data(browser):
    create_testeps.goto_te_verify_part_add_assembly(browser, drawing_data_steps.te_link, rfq_txtboxes_data[3])
    create_testeps.select_machine(browser)
    create_testeps.select_te_process(browser)
    create_testeps.select_te_process_unit(browser)
    create_testeps.select_operation_source(browser)
    create_testeps.fill_te_txtbox_data(browser)
    create_testeps.select_inspection_instrument(browser)
    create_testeps.verify_te_heading(browser)
    do_click(browser, save_btn)


@then('Verify TE data')
def verify_te_data(browser):
    create_te_class_data = get_class_global_variables_dict(create_testeps)
    logging.info(create_te_class_data.values())
    create_te_class_data['type'] = 'Assembly'
    create_te_class_data['part'] = rfq_txtboxes_data[3]
    create_te_class_data['comp_num'] = rfq_txtboxes_data[4]
    create_te_class_data['order'] = 1
    create_testeps.verify_data_te(browser, create_te_class_data)


@then('Approve TE all levels')
def approve_te_levels(browser):
    do_click(browser, operations_tab_back_btn)
    approve_te_steps.approve_te(browser, rfq_steps.development_lead, rfq_steps.plant_head
                                , 'Somvir Singh')
