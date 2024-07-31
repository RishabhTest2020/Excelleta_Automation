import logging

from helpers.common_helpers import *
from locators.accounts_tab_locators import save_btn
from pages.rfq_tab import Drawing_data
from pages.technical_evaluation_tab import *
from pytest_bdd import given, when, then, parsers
from tests.test_rfq_tab import drawing_data_steps, rfq_steps

create_testeps = Create_TE()
approve_te_steps = Approve_TE()
edit_te_steps = Edit_TE()
edit_te_steps_sub_assembly = Edit_TE()
edit_te_steps_parts = Edit_TE()
edit_te_steps_bop = Edit_TE()
bop_data_steps = CreateBopDetails()
te_all_data_dicts = {}
add_st_opts_steps = AddSTOperations()


@when(parsers.parse('Create TE data {index:d}'))
def create_te_data(browser, index):
    create_testeps.add_operation(browser, index=index)
    create_testeps.select_machine(browser)
    create_testeps.select_te_process(browser)
    create_testeps.select_te_process_unit(browser)
    create_testeps.select_operation_source(browser)
    create_testeps.fill_te_txtbox_data(browser)
    create_testeps.select_inspection_instrument(browser)
    create_testeps.verify_te_heading(browser)
    do_click(browser, save_btn)
    sleep(2)
    te_all_data_dicts[f'created_te_data{index}'] = create_testeps.__dict__


@when(parsers.parse('Edit TE Assembly and fill raw material data {ass_type}'))
def edit_te_raw_material(browser, ass_type):
    create_testeps.goto_te_verify_part_add_assembly(browser, drawing_data_steps.te_link, rfq_txtboxes_data[3])
    edit_te_steps.edit_assembly(browser)
    edit_te_steps.select_drawing_name(browser)
    edit_te_steps.select_surface_area_unit(browser)
    edit_te_steps.select_manufacturing_source(browser)
    if ass_type == 'single':
        edit_te_steps.select_rm_type(browser)
        edit_te_steps.select_raw_material(browser)
        edit_te_steps.select_add_rod_size(browser)
    else:
        surface_area_val = 100
        do_send_keys(browser, net_weight_part_loc, edit_te_steps.net_weigh_part)
        do_send_keys(browser, surface_area_val_loc, surface_area_val)
        edit_te_steps.__dict__['surface_area_val'] = surface_area_val
    do_click(browser, update_btn)
    sleep(2)
    try:
        do_click(browser, update_btn)
        sleep(2)
    except TimeoutException:
        pass


@when('Add sub assembly and its data')
def add_sub_assembly(browser):
    create_testeps.add_operation(browser, ops=False)
    do_click(browser, sub_assemply_btn)
    sleep(1)
    sub_assembly_name = "Autom Sub Assembly"
    do_send_keys(browser, sub_assembly_name_loc, sub_assembly_name)
    sub_assembly_component_number = generate_random_five_digit_number()
    do_send_keys(browser, sub_assembly_component_number_loc, sub_assembly_component_number)
    edit_te_steps_sub_assembly.select_drawing_name(browser)
    edit_te_steps_sub_assembly.select_surface_area_unit(browser)
    edit_te_steps_sub_assembly.select_manufacturing_source(browser)
    surface_area_val = 100
    do_send_keys(browser, net_weight_part_loc, edit_te_steps.net_weigh_part)
    do_send_keys(browser, surface_area_val_loc, surface_area_val)
    edit_te_steps_sub_assembly.__dict__['subA_surface_area_val'] = surface_area_val
    edit_te_steps_sub_assembly.__dict__['sub_assembly_name'] = sub_assembly_name
    edit_te_steps_sub_assembly.__dict__['sub_assembly_component_number'] = sub_assembly_component_number
    try:
        do_click(browser, save_btn)
        sleep(2)
    except TimeoutException:
        sleep(1)
        do_click(browser, save_btn)
        sleep(2)


@when(parsers.parse('Add assembly part {index:d} {rm_index:d}'))
def edit_te_raw_material(browser, index, rm_index):
    create_testeps.add_operation(browser, ops=False, index=index)
    do_click(browser, add_part_btn)
    sleep(1)
    part_name = f"Automation Part {index}"
    do_send_keys(browser, add_part_name_loc, part_name)
    part_component_number = generate_random_five_digit_number()
    do_send_keys(browser, sub_assembly_component_number_loc, part_component_number)
    edit_te_steps_parts.select_drawing_name(browser)
    surface_area_val = 100
    do_send_keys(browser, surface_area_val_loc, surface_area_val)
    edit_te_steps_sub_assembly.__dict__['part_surface_area_val'] = surface_area_val
    edit_te_steps_parts.select_surface_area_unit(browser)
    edit_te_steps_parts.select_manufacturing_source(browser)
    edit_te_steps_parts.select_surface_treatment(browser)
    edit_te_steps_parts.select_rm_type(browser)
    edit_te_steps_parts.select_raw_material(browser, index=rm_index)
    edit_te_steps_parts.select_add_rod_size(browser)
    edit_te_steps_parts.__dict__['part_name'] = part_name
    edit_te_steps_parts.__dict__['part_component_number'] = part_component_number
    try:
        do_click(browser, save_btn)
        sleep(2)
    except TimeoutException:
        sleep(1)
        do_click(browser, save_btn)
        sleep(2)
    te_all_data_dicts[f'created_te_parts{index}'] = edit_te_steps_parts.__dict__


@then('Verify TE data')
def verify_te_data(browser):
    create_te_class_data = get_class_global_variables_dict(create_testeps)
    logging.info(create_te_class_data.values())
    create_te_class_data['type'] = 'Assembly'
    create_te_class_data['part'] = rfq_txtboxes_data[3]
    create_te_class_data['comp_num'] = rfq_txtboxes_data[4]
    create_te_class_data['order'] = 1
    create_testeps.verify_data_te(browser, create_te_class_data)


@then(parsers.parse('Approve TE all levels, back {back} level {level}'))
def approve_te_levels(browser, back, level):
    if back == 'true':
        do_click(browser, operations_tab_back_btn)
    current_url = browser.current_url
    te_no = current_url.split("/")[-2]
    if level == '3':
        approve_te_steps.approve_te(browser, rfq_steps.development_lead, rfq_steps.plant_head,
                                    rfq_steps.business_dev_head)
    else:
        approve_te_steps.approve_te(browser, rfq_steps.development_lead, rfq_steps.plant_head,
                                    rfq_steps.surface_treatment_head, rfq_steps.business_dev_head)


@when(parsers.parse('Create TE BOP data {index:d}'))
def create_te_bop_info(browser, index):
    create_testeps.add_operation(browser, ops=False, index=index)
    do_click(browser, te_add_bop_btn_loc)
    should_be_visible(browser, bop_details_header_loc, "bop_details_header_loc")
    bop_data_steps.enter_component_number(browser)
    edit_te_steps_bop.select_drawing_name(browser)
    bop_data_steps.bop_raw_material_data(browser)
    bop_data_steps.select_bop_name_field(browser)
    bop_data_steps.select_bop_type_field(browser)
    sleep(1)
    do_click(browser, save_btn)
    sleep(2)
    te_all_data_dicts[f'bop_data{index}'] = bop_data_steps.__dict__


@when(parsers.parse('Create ST Ops data {index:d}'))
def create_st_operations_info(browser, index):
    add_st_opts_steps.add_st_operation(browser, ops=True, index=index)
    should_be_visible(browser, st_operation_header_loc, "st_operation_header_loc")
    add_st_opts_steps.select_st_process(browser)
    add_st_opts_steps.select_critical_non_critical(browser)
    create_testeps.select_operation_source(browser)
    add_st_opts_steps.select_subtract_type_drop_down(browser)
    add_st_opts_steps.select_subtract_drop_down(browser)
    add_st_opts_steps.select_drain_hole_reqd(browser)
    add_st_opts_steps.select_masking_drop(browser)
    add_st_opts_steps.st_operations_mandtry_fields(browser)
    add_st_opts_steps.st_operations_un_mandtry_fields(browser)
    sleep(1)
    do_click(browser, save_btn)
    sleep(2)
