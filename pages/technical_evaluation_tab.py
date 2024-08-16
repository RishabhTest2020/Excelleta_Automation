import logging

from helpers.common_helpers import *
from locators.rfq_tab_locators import *
from locators.technical_evaluation_tab_locators import *
from test_data.testdata import *
from time import sleep


class Create_TE:
    def __init__(self):
        self.te_txt_data = None
        self.inspection_instrument = None
        self.operation_source = None
        self.te_process_unit = None
        self.te_process = None
        self.te_machine = None

    def goto_te_verify_part_add_assembly(self, browser, te_name, tool):
        te_loc = (By.XPATH, f'//a[contains(text(), "{te_name}")]')
        logging.info(te_loc)
        try:
            do_click(browser, te_loc, 15)
        except TimeoutException:
            do_click(browser, te_loc)
        loader_should_be_invisile(browser, 3)
        tool_txt = get_element_text(browser, assembly_node_label)
        assert tool_txt == tool

    def add_operation(self, browser, index=1, ops=True):
        assembly_list_add_btn_loc = assembly_list_add_btn[1] + f'[{index}]'
        assembly_list_add_btn_loc_tup = replace_in_tuple(assembly_list_add_btn, 1, assembly_list_add_btn_loc)
        do_click(browser, assembly_list_add_btn_loc_tup)
        if ops is True:
            do_click(browser, add_view_operation)
            sleep(2)

    def verify_te_heading(self, browser):
        headings = ['Operation Details Fabrication', 'Tooling Details Fabrication', 'Other Information Fabrication']
        for head in headings:
            heading = te_headings[1].replace('heading', head)
            heading_loc = replace_in_tuple(te_headings, 1, heading)
            scroll_into_the_view(browser, heading_loc[0], heading_loc[1])
            should_be_visible(browser, heading_loc, head)

    def select_machine(self, browser, dep_index=3):
        do_click(browser, machine_loc)
        values = get_list_of_elems_text(browser, machine_loc_select[0], machine_loc_select[1])
        assert values == te_machine_dd_data
        select_name = machine_loc_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(machine_loc_select, 1, select_name)
        self.te_machine = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(1.5)

    def select_te_process(self, browser, dep_index=2):
        do_click(browser, process_loc)
        values = get_list_of_elems_text(browser, process_loc_select[0], process_loc_select[1])
        assert values == te_process_dd_data
        select_name = process_loc_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(process_loc_select, 1, select_name)
        self.te_process = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_te_process_unit(self, browser, dep_index=2):
        do_click(browser, process_unit_loc)
        values = get_list_of_elems_text(browser, process_unit_loc_select[0], process_unit_loc_select[1])
        assert values == te_process_unit_dd_data
        select_name = process_unit_loc_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(process_unit_loc_select, 1, select_name)
        self.te_process_unit = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_operation_source(self, browser, dep_index=3):
        scroll_into_the_view(browser, ops_source_loc[0], ops_source_loc[1])
        do_click(browser, ops_source_loc)
        values = get_list_of_elems_text(browser, ops_source_loc_select[0], ops_source_loc_select[1])
        assert values == te_ops_source_dd_data
        select_name = ops_source_loc_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(ops_source_loc_select, 1, select_name)
        self.operation_source = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)
        return self.operation_source

    def select_inspection_instrument(self, browser, dep_index=3):
        do_click(browser, ins_instrument_loc)
        values = get_list_of_elems_text(browser, ins_instrument_loc_select[0], ins_instrument_loc_select[1])
        assert values == te_inspection_instrument_dd_data
        select_name = ins_instrument_loc_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(ins_instrument_loc_select, 1, select_name)
        self.inspection_instrument = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def fill_te_txtbox_data(self, browser):
        ids_list = ['Cycle Time', 'Unit Value', 'Name of Tool/Fixture', 'Length', 'Width', 'Height', 'Density',
                    'Factor',
                    'Criticality Value', 'Judgment Based Tooling Cost', 'Skilled Man Power', 'Unskilled Man Power',
                    'Material Handling', 'Total Investment Cost', 'Machine Investment Details', 'Remarks']
        self.te_txt_data = [100, 18, 'Driller', 10, 11, 12, 14, 15, 50, 1000, 16, 17, 'Test Material Handling', 100000,
                            'Test Machine Investment', 'This is for automation testing']
        for b_id, data in zip(ids_list[:-2], self.te_txt_data[:-2]):
            bill_loc_str = assembly_txt_boxes[1].replace("field_name", b_id)
            bill_loc = replace_in_tuple(assembly_txt_boxes, 1, bill_loc_str)
            logging.info(bill_loc)
            do_send_keys(browser, bill_loc, data)

        bill_loc_str_txt = assembly_txt_boxes_txt[1].replace("field_name", ids_list[-2])
        bill_loc_txt = replace_in_tuple(assembly_txt_boxes_txt, 1, bill_loc_str_txt)
        do_send_keys(browser, bill_loc_txt, self.te_txt_data[-2])
        bill_loc_str_txt = assembly_txt_boxes_txt[1].replace("field_name", ids_list[-1])
        bill_loc_txt = replace_in_tuple(assembly_txt_boxes_txt, 1, bill_loc_str_txt)
        do_send_keys(browser, bill_loc_txt, self.te_txt_data[-1])

    def verify_data_te(self, browser, all_data_dict):
        loader_should_be_invisile(browser, 5)
        do_click(browser, te_operations_section)
        sleep(2)
        values = get_list_of_elems_text(browser, operations_row_value[0], operations_row_value[1])
        logging.info(values)
        assert len(values) > 0
        all_data = list(all_data_dict.values())
        acc_data_list1 = all_data[0]
        acc_data_list = list(acc_data_list1)
        for i in all_data[1:]:
            i_type = type(i)
            if i_type == list:
                acc_data_list.extend(i)
            else:
                acc_data_list.append(str(i))
        logging.info(acc_data_list)
        values = [x for x in values if x != "-"]
        non_present_data = []
        for i in values:
            for j in acc_data_list:
                if isinstance(j, int):
                    k = str(j)
                else:
                    k = j
                if i == k:
                    break
                else:
                    if acc_data_list.index(j) == len(acc_data_list) - 1:
                        non_present_data.append(i)
                        break
        logging.info(non_present_data)
        assert len(non_present_data) <= 3


class Approve_TE:

    def __init__(self):
        self.formatted_time = []
        self.comments = []
        self.formatted_time_app = []

    def approve_te(self, browser, te_id=None, asserts=True, *args):
        args_len = len(args)
        range_mod = range(0, args_len + 1)
        for i in range_mod:
            text = random_correct_name(5, 5, 'first_name')
            self.comments.append(text)
            if (args_len == 3) or (args_len >= 4 and i == 0):
                do_click(browser, approve_request)
                do_send_keys(browser, add_comment, text)
                current_date_time = datetime.now()
                self.formatted_time.append(current_date_time.strftime("%d-%b-%Y, %I:%M %p"))
                do_click(browser, save_btn)
                current_date_time2 = datetime.now()
                self.formatted_time_app.append(current_date_time2.strftime("%d-%b-%Y, %I:%M %p"))
            else:
                te_calls = TE_API_calls()
                approver_email = [x for x in globalEnvs.__dict__ if args[i - 1].split(" ")[0] in x]
                te_calls.api_login(email=os.getenv(approver_email[0]), password=globalEnvs.approver_password)
                current_date_time = datetime.now()
                self.formatted_time.append(current_date_time.strftime("%d-%b-%Y, %I:%M %p"))
                te_calls.approve_te(token=te_calls.token, te_id=te_id, userid=te_calls.user_id, comment=text)
                current_date_time2 = datetime.now()
                self.formatted_time_app.append(current_date_time2.strftime("%d-%b-%Y, %I:%M %p"))
            sleep(1)
            if asserts is True or asserts == 'True':
                if i > 0:
                    sleep(4)
                    if args_len >= 4:
                        browser.refresh()
                        sleep(2)
                    do_click(browser, te_approval_history)
                    ah_headers = get_list_of_elems_text(browser, approval_pop_header[0], approval_pop_header[1])
                    assert ah_headers == approval_history_headers
                    if i == range_mod[-1]:
                        approval_pop_values1 = approval_pop_values[1].replace("[2]", "[1]")
                    elif i == range_mod[1] and args_len >= 4:
                        approval_pop_values1 = approval_pop_values[1].replace("[2]", f"[{args_len - i}]")
                    else:
                        approval_pop_values1 = approval_pop_values[1]
                    ah_row_vals = get_list_of_elems_text(browser, approval_pop_values[0], approval_pop_values1)
                    time1 = ah_row_vals[-2]
                    time2 = ah_row_vals[-3]
                    if args_len >= 4 and range_mod.index(i) >= 3:
                        j = i - 1
                    else:
                        j = i
                    if args_len >= 4:
                        actual_vals = [f'TE Approval Level - {j}', args[i - 1], args[i - 1], 'Approved',
                                       time2, time1, self.comments[-1]]
                    else:
                        actual_vals = [f'TE Approval Level - {j}', args[i - 1], 'Saurabh Shrivastava', 'Approved',
                                       time2, time1, self.comments[-1]]
                    logging.info(ah_row_vals)
                    logging.info(actual_vals)
                    assert ah_row_vals == actual_vals
                    do_click(browser, slide_back_btn)

    def reject_te(self, browser, te_id, level, asserts=True, *args):
        args_len = len(args)
        range_mod = range(0, args_len + 1)
        for i in range_mod:
            text = random_correct_name(5, 5, 'first_name')
            self.comments.append(text)
            if i == 0 and int(level) >= 1:
                do_click(browser, approve_request)
                do_send_keys(browser, add_comment, text)
                do_click(browser, save_btn)
            else:
                te_calls = TE_API_calls()
                approver_email = [x for x in globalEnvs.__dict__ if args[i - 1].split(" ")[0] in x]
                te_calls.api_login(email=os.getenv(approver_email[0]), password=globalEnvs.approver_password)
                if i == int(level):
                    te_calls.approve_te(token=te_calls.token, te_id=te_id, userid=te_calls.user_id, comment=text,
                                        status="REJECTED")
                else:
                    te_calls.approve_te(token=te_calls.token, te_id=te_id, userid=te_calls.user_id, comment=text)
            sleep(1)
            if (asserts is True or asserts == 'True') and i == int(level):
                if i > 0:
                    browser.refresh()
                    sleep(2)
                    do_click(browser, te_approval_history)
                    ah_headers = get_list_of_elems_text(browser, approval_pop_header[0], approval_pop_header[1])
                    assert ah_headers == approval_history_headers
                    approval_pop_values1 = approval_pop_values[1].replace("[2]", "[1]")
                    ah_row_vals = get_list_of_elems_text(browser, approval_pop_values[0], approval_pop_values1)
                    time1 = ah_row_vals[-2]
                    time2 = ah_row_vals[-3]
                    if int(level) == 2:
                        actual_vals = [f'TE Approval Level - 2', args[i], args[i - 1], 'Rejected',
                                       time2, time1, self.comments[-1]]
                        ah_row_vals2 = get_list_of_elems_text(browser, approval_pop_values[0], approval_pop_values[1])
                        time3 = ah_row_vals2[-2]
                        time4 = ah_row_vals2[-3]
                        actual_vals2 = [f'TE Approval Level - 2', args[i - 1], args[i - 1], 'Rejected',
                                        time4, time3, self.comments[-1]]
                        logging.info(ah_row_vals2)
                        logging.info(actual_vals2)
                        assert ah_row_vals2 == actual_vals2

                    else:
                        if int(level) >= 3:
                            j = i - 1
                        else:
                            j = i
                        actual_vals = [f'TE Approval Level - {j}', args[i - 1], args[i - 1], 'Rejected',
                                       time2, time1, self.comments[-1]]
                    logging.info(ah_row_vals)
                    logging.info(actual_vals)
                    assert ah_row_vals == actual_vals
                    do_click(browser, slide_back_btn)
                    break


class Edit_TE:

    def __init__(self):
        self.ecn_type = None
        self.surface_treatment = None
        self.net_weigh_part = 0.2
        self.rod_length = 100
        self.raw_material = None
        self.rm_type = None
        self.manufacturing_source = None
        self.surface_area_unit = None
        self.drawing_name = None

    def edit_assembly(self, browser):
        do_click(browser, assembly_list_add_btn)
        do_click(browser, edit_operation)
        sleep(2)

    def select_drawing_name(self, browser, index=2):
        do_click(browser, drawing_name_loc)
        select_name = drawing_name_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(drawing_name_loc_select, 1, select_name)
        self.drawing_name = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(0.5)

    def select_surface_area_unit(self, browser, index=2):
        scroll_into_the_view(browser, surface_area_unit_loc[0], surface_area_unit_loc[1])
        do_click(browser, surface_area_unit_loc)
        values = get_list_of_elems_text(browser, surface_area_unit_loc_select[0], surface_area_unit_loc_select[1])
        assert values == surface_area_unit_dd_data
        select_name = surface_area_unit_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(surface_area_unit_loc_select, 1, select_name)
        self.surface_area_unit = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(0.5)

    def select_manufacturing_source(self, browser, index=2):
        do_click(browser, manu_source_loc)
        values = get_list_of_elems_text(browser, manu_source_loc_select[0], manu_source_loc_select[1])
        assert values == manufacturing_source_dd_data
        select_name = manu_source_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(manu_source_loc_select, 1, select_name)
        self.manufacturing_source = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(0.5)

    def select_rm_type(self, browser, index=2):
        scroll_into_the_view(browser, rm_type_loc[0], rm_type_loc[1])
        do_click(browser, rm_type_loc)
        values = get_list_of_elems_text(browser, rm_type_loc_select[0], rm_type_loc_select[1])
        assert values == rm_type_dd_data
        select_name = rm_type_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(rm_type_loc_select, 1, select_name)
        self.rm_type = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(0.5)

    def select_raw_material(self, browser, index=2):
        scroll_into_the_view(browser, rm_type_loc[0], rm_type_loc[1])
        do_click(browser, raw_mat_loc)
        values = get_list_of_elems_text(browser, raw_mat_loc_select[0], raw_mat_loc_select[1])
        assert values == rod_bar_dd_data
        select_name = raw_mat_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(raw_mat_loc_select, 1, select_name)
        self.raw_material = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(0.5)

    def select_add_rod_size(self, browser, index=2):
        scroll_into_the_view(browser, rod_length_loc[0], rod_length_loc[1])
        do_send_keys(browser, rod_length_loc, self.rod_length)
        scroll_into_the_view(browser, override_rod_size_loc[0], override_rod_size_loc[1])
        do_click(browser, override_rod_size_loc)
        select_name = override_rod_size_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(raw_mat_loc_select, 1, select_name)
        self.raw_material = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(1)
        scroll_into_the_view(browser, net_weight_part_loc[0], net_weight_part_loc[1])
        do_send_keys(browser, net_weight_part_loc, self.net_weigh_part)

    def select_surface_treatment(self, browser, index=3):
        do_click(browser, surface_treatment_loc)
        select_name = surface_treatment_loc_select[1] + f'[{index}]'
        select_loc = replace_in_tuple(surface_treatment_loc_select, 1, select_name)
        self.surface_treatment = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        sleep(0.5)
        
    def clone_te(self, browser, index=2):
        do_click(browser, te_clone_loc)
        do_click(browser, ecn_type_drop_down_loc)
        values = get_list_of_elems_text(browser, ecn_type_options_loc[0], ecn_type_options_loc[1])
        assert values == ecn_dd_data
        select_name = ecn_type_options_loc[1] + f'[{index}]'
        select_loc = replace_in_tuple(ecn_type_options_loc, 1, select_name)
        self.ecn_type = get_element_text(browser, select_loc)
        do_click(browser, select_loc)
        do_send_keys(browser, add_comment, "test")
        do_click(browser, save_btn)
        sleep(0.5)
        


class CreateBopDetails:
    def __init__(self):
        self.bop_basic_details_values = None
        self.bop_raw_mate_data = None
        self.bop_name_value = None
        self.bop_type_value = None
        self.bop_remarks = "Nothing for Now"

    def enter_component_number(self, browser):
        self.bop_basic_details_values = [generate_random_number(9), generate_random_five_digit_number(), 2]
        logging.info(self.bop_basic_details_values)
        for field_name, data in zip(bop_basic_details, self.bop_basic_details_values):
            bop_field = bop_basic_details_common_loc[1].replace('field', field_name)
            bop_field_loc = replace_in_tuple(bop_basic_details_common_loc, 1, bop_field)
            do_clear(browser, bop_field_loc)
            scroll_into_the_view(browser, bop_field_loc[0], bop_field_loc[1])
            do_send_keys(browser, bop_field_loc, data)
        upload_elem = browser.find_element(te_bop_logo[0], te_bop_logo[1])
        upload_elem.send_keys(os.getcwd() + '/files/watermark.png')
        do_click(browser, upload_img_accept_btn_loc)
        scroll_into_the_view(browser, te_bop_remarks_input_loc[0], te_bop_remarks_input_loc[1])
        do_send_keys(browser, te_bop_remarks_input_loc, self.bop_remarks)

    def bop_raw_material_data(self, browser, mgr_mm=50, thk_mm=10, weight=1000):
        self.bop_raw_mate_data = [random_correct_name(8, 4, 'first_name'), mgr_mm, thk_mm, weight]
        for field_name, data in zip(bop_raw_material_data, self.bop_raw_mate_data):
            bop_material_field = bop_basic_details_common_loc[1].replace('field', field_name)
            bop_material_field_loc = replace_in_tuple(bop_basic_details_common_loc, 1, bop_material_field)
            do_clear(browser, bop_material_field_loc)
            do_send_keys(browser, bop_material_field_loc, data)

    def select_bop_name_field(self, browser, index=3):
        bop_name_dropdown = bop_basic_details_common_loc[1].replace('field', "componentName")
        bop_material_field_loc = replace_in_tuple(bop_basic_details_common_loc, 1, bop_name_dropdown)
        scroll_into_the_view(browser, bop_material_field_loc[0], bop_material_field_loc[1])
        do_click(browser, bop_material_field_loc)
        bop_name_value = bop_name_values_loc[1] + f'[{index}]'
        bop_name_value_loc = replace_in_tuple(bop_name_values_loc, 1, bop_name_value)
        self.bop_name_value = get_element_text(browser, bop_name_value_loc)
        scroll_into_the_view(browser, bop_name_value_loc[0], bop_name_value_loc[1])
        do_click(browser, bop_name_value_loc)
        sleep(5)

    def select_bop_type_field(self, browser, index=2):
        do_click(browser, bop_type_dropdown_loc)
        bop_type_value = bop_type_options_loc[1] + f'[{index}]'
        bop_type_value_loc = replace_in_tuple(bop_name_values_loc, 1, bop_type_value)
        self.bop_type_value = get_element_text(browser, bop_type_value_loc)
        do_click(browser, bop_type_value_loc)


class AddSTOperations:
    def __init__(self):
        self.st_process_val_txt = None
        self.st_critical_non_critical_options_val_txt = None
        self.st_subtract_type_option_val_txt = None
        self.st_subtract_option_val_txt = None
        self.st_drain_hole_reqd_option_val_txt = None
        self.st_masking_options_val_txt = None
        self.st_madatary_input_fields_data = []
        self.st_un_madatary_input_fields_data = []

    def select_st_process(self, browser, index=3):
        do_click(browser, st_operation_drop_down_loc)
        st_process_options_val = st_process_options_loc[1] + f'[{index}]'
        st_process_options_val_loc = replace_in_tuple(st_process_options_loc, 1, st_process_options_val)
        self.st_process_val_txt = get_element_text(browser, st_process_options_val_loc)
        do_click(browser, st_process_options_val_loc)

    def select_critical_non_critical(self, browser, index=2):
        do_click(browser, st_critical_non_critical_drop_loc)
        st_critical_non_critical_options_val = st_critical_non_critical_options_loc[1] + f'[{index}]'
        st_critical_non_critical_options_val_loc = replace_in_tuple(st_critical_non_critical_options_loc, 1,
                                                                    st_critical_non_critical_options_val)
        self.st_critical_non_critical_options_val_txt = get_element_text(browser,
                                                                         st_critical_non_critical_options_val_loc)
        do_click(browser, st_critical_non_critical_options_val_loc)

    def select_subtract_type_drop_down(self, browser, index=2):
        do_click(browser, st_subtract_type_drop_loc)
        st_subtract_type_option_val = st_subtract_type_option_loc[1] + f'[{index}]'
        st_subtract_type_option_val_loc = replace_in_tuple(st_subtract_type_option_loc, 1, st_subtract_type_option_val)
        self.st_subtract_type_option_val_txt = get_element_text(browser, st_subtract_type_option_val_loc)
        do_click(browser, st_subtract_type_option_val_loc)

    def select_subtract_drop_down(self, browser, index=2):
        do_click(browser, st_subtract_drop_loc)
        st_subtract_option_val = st_subtract_option_loc[1] + f'[{index}]'
        st_subtract_option_val_loc = replace_in_tuple(st_subtract_option_loc, 1, st_subtract_option_val)
        self.st_subtract_option_val_txt = get_element_text(browser, st_subtract_option_val_loc)
        do_click(browser, st_subtract_option_val_loc)

    def select_drain_hole_reqd(self, browser, index=3):
        do_click(browser, st_drain_hole_reqd_drop_loc)
        st_drain_hole_reqd_option_val = st_drain_hole_reqd_option_loc[1] + f'[{index}]'
        st_drain_hole_reqd_option_val_loc = replace_in_tuple(st_drain_hole_reqd_option_loc, 1,
                                                             st_drain_hole_reqd_option_val)
        self.st_drain_hole_reqd_option_val_txt = get_element_text(browser, st_drain_hole_reqd_option_val_loc)
        do_click(browser, st_drain_hole_reqd_option_val_loc)

    def select_masking_drop(self, browser, index=2):
        do_click(browser, st_masking_drop_down_loc)
        st_masking_options_val = st_masking_options_loc[1] + f'[{index}]'
        st_masking_options_val_loc = replace_in_tuple(st_masking_options_loc, 1, st_masking_options_val)
        self.st_masking_options_val_txt = get_element_text(browser, st_masking_options_val_loc)
        do_click(browser, st_masking_options_val_loc)

    def st_operations_mandtry_fields(self, browser):
        self.st_madatary_input_fields_data = [generate_random_number(3), 60, 100]
        for field_name, data in zip(st_ops_mandary_fields, self.st_madatary_input_fields_data):
            st_ops_field = st_ops_mndtry_details_common_loc[1].replace('field', field_name)
            st_ops_field_loc = replace_in_tuple(st_ops_mndtry_details_common_loc, 1, st_ops_field)
            do_clear(browser, st_ops_field_loc)
            scroll_into_the_view(browser, st_ops_field_loc[0], st_ops_field_loc[1])
            do_send_keys(browser, st_ops_field_loc, data)

    def st_operations_un_mandtry_fields(self, browser):
        self.st_un_madatary_input_fields_data = [generate_random_five_digit_number(), generate_random_number(6),
                                                 generate_random_number(9), 5, 'green', 20, generate_random_number(6),
                                                 generate_random_five_digit_number(), generate_random_number(4), 5000,
                                                 'NA', 'NA']
        for field_name, data in zip(st_ops_un_mndtry_fields, self.st_un_madatary_input_fields_data):
            st_ops_field = st_ops_mndtry_details_common_loc[1].replace('field', field_name)
            st_ops_field_loc = replace_in_tuple(st_ops_mndtry_details_common_loc, 1, st_ops_field)
            do_clear(browser, st_ops_field_loc)
            scroll_into_the_view(browser, st_ops_field_loc[0], st_ops_field_loc[1])
            do_send_keys(browser, st_ops_field_loc, data)
        upload_elem = browser.find_element(te_bop_logo[0], te_bop_logo[1])
        upload_elem.send_keys(os.getcwd() + '/files/watermark.png')
        do_click(browser, upload_img_accept_btn_loc)

    def add_st_operation(self, browser, index=1, ops=True):
        assembly_list_add_btn_loc = assembly_list_add_btn[1] + f'[{index}]'
        assembly_list_add_btn_loc_tup = replace_in_tuple(assembly_list_add_btn, 1, assembly_list_add_btn_loc)
        do_click(browser, assembly_list_add_btn_loc_tup)
        if ops is True:
            do_click(browser, st_operation_btn_loc)
            sleep(2)


class TE_API_calls:

    def __init__(self):
        self.user_id = None
        self.token = None

    def api_login(self, email=globalEnvs.user_email, password=globalEnvs.user_password):
        url = f'{globalEnvs.api_url}/users/auth'
        headers = {'Accept': 'application/json, text/plain, */*', 'content-type': 'application/json'}
        payload = {
            "email": email,
            "password": password
        }
        resp = requests.post(f"{url}", headers=headers, json=payload, verify=False)
        resp_js = resp.json()
        logging.info(resp_js)
        self.token = resp_js['token']
        self.user_id = resp_js['userDto']['id']

    def approve_te(self, token, te_id, userid, comment, status="APPROVED"):
        #REJECTED
        url = f'{globalEnvs.api_url}/approval/updateApprovalStatus'
        headers = {'Accept': 'application/json, text/plain, */*', 'content-type': 'application/json',
                   'Authorization': f'Bearer {token}'}
        payload = {
            "entityId": int(te_id),
            "entityType": "TE",
            "adminUser": False,
            "status": status,
            "approvedBy": int(userid),
            "comment": comment,
            "version": "Version-1"
        }
        resp = requests.post(url, headers=headers, json=payload, verify=False)
        assert resp.status_code == 200
        logging.info(resp.json())

    def approve_cost_sheet(self, token, te_id, userid, comment, status="APPROVED"):
        url = f'{globalEnvs.api_url}/approval/updateApprovalStatus'
        headers = {'Accept': 'application/json, text/plain, */*', 'content-type': 'application/json',
                   'Authorization': f'Bearer {token}'}
        payload = {
            "entityId": int(te_id),
            "entityType": "COSTSHEET",
            "adminUser": False,
            "status": status,
            "approvedBy": int(userid),
            "comment": comment,
        }
        resp = requests.post(url, headers=headers, json=payload, verify=False)
        assert resp.status_code == 200
        logging.info(resp.json())
