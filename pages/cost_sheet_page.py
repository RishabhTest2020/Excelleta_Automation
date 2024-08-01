import logging
import os
from selenium.webdriver import Keys
from helpers.common_helpers import *
from locators.contact_tab_locators import *
from test_data.testdata import *
from time import sleep
from locators.cost_sheet_locators import *


class CostSheetPage:
    def __init__(self):
        self.cosy_expense_type_selection = None
        self.cost_over_head_norms = None
        self.cost_other_norms_date_range = None
        self.cost_process_norm_date_range = None
        self.cost_rm_norm_date_range = None
        self.cost_rm_fiscal_year = None


    def goto_created_mte(self, browser, mte_name):
        te_loc = (By.XPATH, f'//a[contains(text(), "MTE-{mte_name}")]')
        logging.info(te_loc)
        try:
            do_click(browser, te_loc, 15)
        except TimeoutException:
            do_click(browser, te_loc)
        loader_should_be_invisile(browser, 3)

    def rm_norms_fiscal_year_option(self, browser, index):
        do_click(browser, norms_fiscal_year_loc)
        values = get_list_of_elems_text(browser, norms_fiscal_year_options[0], norms_fiscal_year_options[1])
        #assert values == fiscal_year_dd_data
        select_option = norms_fiscal_year_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(norms_fiscal_year_options, 1, select_option)
        self.cost_rm_fiscal_year = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)

    def rm_norms_date_range_option(self, browser, index):
        do_click(browser, cs_rm_norms_date_range)
        values = get_list_of_elems_text(browser, cs_rm_norms_date_range_options[0], cs_rm_norms_date_range_options[1])
        assert values == rm_norms_date_range_data
        select_option = cs_rm_norms_date_range_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(cs_rm_norms_date_range_options, 1, select_option)
        self.cost_rm_norm_date_range = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)

    def bop_norms_date_range_option(self, browser, index):
        do_click(browser, cs_bop_norms_date_range)
        values = get_list_of_elems_text(browser, cs_bop_norms_date_range_options[0], cs_bop_norms_date_range_options[1])
        # assert values == fiscal_year_dd_data  have to write data
        select_option = cs_bop_norms_date_range_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(cs_bop_norms_date_range_options, 1, select_option)
        option = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)
        return option

    def process_norms_date_range_selection(self, browser, index):
        do_click(browser, cs_process_norms_date_range)
        select_option = cs_process_norms_date_range_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(cs_process_norms_date_range_options, 1, select_option)
        self.cost_process_norm_date_range = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)

    def other_norms_date_range_selection(self, browser, index):
        do_click(browser, cs_other_norms_date_range)
        select_option = cs_other_norms_date_range_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(cs_other_norms_date_range_options, 1, select_option)
        self.cost_other_norms_date_range = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)

    def over_head_norms_selection(self, browser, index):
        do_click(browser, cs_over_heads_select_loc)
        select_option = cs_over_heads_options_loc[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(cs_over_heads_options_loc, 1, select_option)
        self.cost_over_head_norms = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)

    def expense_type_selection(self, browser, index='6'):
        do_click(browser, expense_type_input_loc)
        select_option = transport_expense_type_loc[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(transport_expense_type_loc, 1, select_option)
        self.cosy_expense_type_selection = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)

    def enter_flat_rate_discount(self, browser, rate='100', discount='10'):
        do_click(browser, flat_rate_input_loc)
        do_send_keys(browser, flat_rate_input_loc, rate)
        do_send_keys(browser, discount_rate_input_loc, discount)

    def add_expense_flat_rate(self, browser, rate_type_ind='2'):
        do_click(browser, cs_ae_rate_type_dropdown_loc)
        select_option = cs_ae_rate_type_dropdown_options_loc[1] + f'[{rate_type_ind}]'
        select_option_loc = replace_in_tuple(cs_ae_rate_type_dropdown_options_loc, 1, select_option)
        option = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)
        should_be_visible(browser, flat_expense_header_loc, "flat_expense_header_loc")
        self.expense_type_selection(browser)
        self.enter_flat_rate_discount(browser)
        return option

    def verify_cost_sections_data(self, browser, all_data_dict, section):
        cost_section_loc = cost_section_rows_loc[1].replace('section_name', f'{section}')
        values = get_list_of_elems_text(browser, cost_section_rows_loc[0], cost_section_loc)
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
