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
        do_click(browser, te_loc)
        loader_should_be_invisile(browser, 3)
        tool_txt = get_element_text(browser, assembly_node_label)
        assert tool_txt == tool

    def add_operation(self, browser):
        do_click(browser, assembly_list_add_btn)
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
        self.formatted_time_app = None

    def approve_te(self, browser, *args):
        range_mod = range(0, 4)
        for i in range_mod:
            text = random_correct_name(5, 5, 'first_name')
            self.comments.append(text)
            do_click(browser, approve_request)
            do_send_keys(browser, add_comment, text)
            current_date_time = datetime.now()
            self.formatted_time.append(current_date_time.strftime("%d-%b-%Y, %I:%M %p"))
            do_click(browser, save_btn)
            current_date_time2 = datetime.now()
            self.formatted_time.append(current_date_time2.strftime("%d-%b-%Y, %I:%M %p"))
            sleep(1)
            if i > 0:
                sleep(4)
                do_click(browser, te_approval_history)
                ah_headers = get_list_of_elems_text(browser, approval_pop_header[0], approval_pop_header[1])
                assert ah_headers == approval_history_headers
                if i == range_mod[-1]:
                    approval_pop_values1 = approval_pop_values[1].replace("[2]",  "[1]")
                    ah_row_vals = get_list_of_elems_text(browser, approval_pop_values[0], approval_pop_values1)
                else:
                    ah_row_vals = get_list_of_elems_text(browser, approval_pop_values[0], approval_pop_values[1])
                actual_vals = [f'TE Approval Level - {i}', args[i - 1], 'Saurabh Shrivastava', 'Approved',
                               self.formatted_time[2:][i - 1], self.formatted_time[2:][i], self.comments[i]]
                logging.info(ah_row_vals)
                logging.info(actual_vals)
                assert ah_row_vals == actual_vals
                do_click(browser, slide_back_btn)


class Edit_TE:

    def __init__(self):
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
