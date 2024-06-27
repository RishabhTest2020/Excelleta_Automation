import logging

from helpers.common_helpers import *
from locators.accounts_tab_locators import save_btn
from pages.rfq_tab import Drawing_data
from pages.technical_evaluation_tab import *
from pytest_bdd import given, when, then


create_testeps = Create_TE()
drawing_data_steps = Drawing_data()


@when('Create TE data')
def create_te_data(browser):
    create_testeps.goto_te_verify_part_add_assembly(browser, 'TE-363', 'Carburetor')#drawing_data_steps.te_link, rfq_txtboxes_data[3])
    create_testeps.select_machine(browser)
    create_testeps.select_te_process(browser)
    create_testeps.select_te_process_unit(browser)
    create_testeps.select_operation_source(browser)
    create_testeps.fill_te_txtbox_data(browser)
    create_testeps.select_inspection_instrument(browser)
    create_testeps.verify_te_heading(browser)
    do_click(browser, save_btn)
