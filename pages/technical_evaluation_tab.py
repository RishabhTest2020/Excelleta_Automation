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

        non_present_data = []
        for i in values[1:-3]:
            for j in acc_data_list:
                if i == j:
                    break
                else:
                    if acc_data_list.index(j) == -1:
                        non_present_data.append(i)
                        break
        logging.info(non_present_data)
        assert len(non_present_data) == 0


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
