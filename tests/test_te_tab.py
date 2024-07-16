import logging

from helpers.common_helpers import *
from locators.accounts_tab_locators import save_btn
from pages.rfq_tab import Drawing_data
from pages.technical_evaluation_tab import *
from pytest_bdd import given, when, then
from tests.test_rfq_tab import drawing_data_steps, rfq_steps


create_testeps = Create_TE()
approve_te_steps = Approve_TE()
edit_te_steps = Edit_TE()
bop_data_steps = CreateBopDetails()

@when('Create TE data')
def create_te_data(browser):
    create_testeps.add_operation(browser)
    create_testeps.select_machine(browser)
    create_testeps.select_te_process(browser)
    create_testeps.select_te_process_unit(browser)
    create_testeps.select_operation_source(browser)
    create_testeps.fill_te_txtbox_data(browser)
    create_testeps.select_inspection_instrument(browser)
    create_testeps.verify_te_heading(browser)
    do_click(browser, save_btn)


@when('Edit TE Assembly and fill raw material data')
def edit_te_raw_material(browser):
    create_testeps.goto_te_verify_part_add_assembly(browser, drawing_data_steps.te_link, rfq_txtboxes_data[3])
    edit_te_steps.edit_assembly(browser)
    edit_te_steps.select_drawing_name(browser)
    edit_te_steps.select_surface_area_unit(browser)
    edit_te_steps.select_manufacturing_source(browser)
    edit_te_steps.select_rm_type(browser)
    edit_te_steps.select_raw_material(browser)
    edit_te_steps.select_add_rod_size(browser)
    do_click(browser, update_btn)
    sleep(2)
    try:
        do_click(browser, update_btn)
    except TimeoutException:
        pass


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

@when('Create TE BOP data')
def create_te_bop_info(browser):
    bop_data_steps.enter_component_number(browser)
    bop_data_steps.bop_raw_material_data(browser)
    bop_data_steps.select_bop_name_field(browser)
    bop_data_steps.select_bop_type_field(browser)
    do_click(browser, save_btn)
