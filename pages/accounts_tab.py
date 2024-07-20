import logging
import time
from datetime import timedelta

from selenium.webdriver import Keys

from helpers.common_helpers import *
import pytest
from locators.accounts_tab_locators import *
from test_data.testdata import *
from time import sleep


@pytest.mark.usefixtures("browser")
class Accounts:

    def __init__(self):
        self.account_details = None
        self.billing_data = None
        self.country = None
        self.state = None
        self.payment_term = None
        self.payment_method = None
        self.business_segment = None
        self.business_domain = None
        self.business_nature = None
        self.rm_norms = None
        self.start_month = None
        self.city = None

    def verify_accounts_head_col(self, browser):
        elems = browser.find_elements(accounts_head_col[0], accounts_head_col[1])
        elems_len = len(elems)
        col_names_lst = []
        for i in range(1, elems_len - 1):
            col_loc = accounts_head_col[1] + f'[{i}]'
            scroll_into_the_view(browser, accounts_head_col[0], col_loc)
            col_name = get_text_by_js_xpath(browser, col_loc)
            col_names_lst.append(col_name)
        logging.info(col_names_lst)
        assert accounts_table_header_col.sort() == col_names_lst.sort()

    def add_accounts_data_in_txt_box(self, browser):
        if sys.platform == 'win32':
            number = '99090909090'
        else:
            number = '99090909090'
        self.account_details = [random_correct_name(8, 4, 'first_name'), f'{random_email_generator()}',
                                'www.testwesite.com', number, '12345678', generate_random_pan(),
                                f'{generate_random_five_digit_number()}', 7]
        logging.info(self.account_details)
        for field_name, data in zip(accounts_create_fields_gen, self.account_details):
            acco_field = acc_field_txtbox[1].replace('field_name', field_name)
            acc_field_loc = replace_in_tuple(acc_field_txtbox, 1, acco_field)
            do_clear(browser, acc_field_loc)
            do_send_keys(browser, acc_field_loc, data)

    def select_start_month_field(self, browser):
        loader_should_be_invisile(browser, 4)
        do_click(browser, start_month)
        values = get_list_of_elems_text(browser, start_month_list[0], start_month_list[1])
        assert values == start_months_data
        current_month = datetime.now().month + 1
        select_month = start_month_list[1] + f'[{current_month}]'
        select_month_loc = replace_in_tuple(start_month_list, 1, select_month)
        self.start_month = get_element_text(browser, select_month_loc)
        do_click(browser, select_month_loc)
        sleep(0.5)

    def select_rm_norms_field(self, browser, rm_type=2):
        do_click(browser, rm_norms)
        values = get_list_of_elems_text(browser, rm_norms_options[0], rm_norms_options[1])
        assert values == rm_type_list
        select_rm = rm_norms_options[1] + f'[{rm_type}]'
        select_rm_loc = replace_in_tuple(rm_norms_options, 1, select_rm)
        self.rm_norms = get_element_text(browser, select_rm_loc)
        do_click(browser, select_rm_loc)
        sleep(0.5)

    def select_business_nature_field(self, browser, bn_type=2):
        should_be_visible(browser, business_info_h3, 'business_info_h3')
        do_click(browser, business_nature)
        values = get_list_of_elems_text(browser, business_nature_option_txt[0], business_nature_option_txt[1])
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(business_nature_list, values)
        assert val is True
        select_bn = business_nature_option[1] + f'[{bn_type}]'
        select_bn_loc = replace_in_tuple(business_nature_option, 1, select_bn)
        do_click(browser, select_bn_loc)
        do_click(browser, business_info_h3)
        self.business_nature = get_element_text(browser, business_nature_selected).rstrip(" x ")
        assert self.business_nature == business_nature_list[bn_type - 1]

    def select_business_domain_field(self, browser, bd_type=2):
        do_click(browser, business_domain)
        values = get_list_of_elems_text(browser, business_domain_option_txt[0], business_domain_option_txt[1])
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(business_domain_list, values)
        assert val is True
        select_bd = business_domain_option[1] + f'[{bd_type}]'
        select_bn_loc = replace_in_tuple(business_domain_option, 1, select_bd)
        do_click(browser, select_bn_loc)
        do_click(browser, business_info_h3)
        self.business_domain = get_element_text(browser, business_domain_selected).rstrip(" x ")
        assert self.business_domain == business_domain_list[bd_type - 1]

    def select_business_segment_field(self, browser, bs_type=2):
        do_click(browser, business_segment)
        values = get_list_of_elems_text(browser, business_segment_option_txt[0], business_segment_option_txt[1])
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(business_segment_list, values)
        assert val is True
        select_bs = business_segment_option[1] + f'[{bs_type}]'
        select_bs_loc = replace_in_tuple(business_segment_option, 1, select_bs)
        do_click(browser, select_bs_loc)
        do_click(browser, business_info_h3)
        self.business_segment = get_element_text(browser, business_segment_selected).rstrip(" x ")
        assert self.business_segment == business_segment_list[bs_type - 1]

    def select_payment_method_field(self, browser, pm_type=2):
        scroll_into_the_view(browser, payment_details_h3[0], payment_details_h3[1])
        should_be_visible(browser, payment_details_h3, 'payment_details_h3')
        do_click(browser, payment_method)
        values = get_list_of_elems_text(browser, payment_method_options[0], payment_method_options[1])
        assert values == payment_method_list
        select_pm = payment_method_options[1] + f'[{pm_type}]'
        select_pm_loc = replace_in_tuple(payment_method_options, 1, select_pm)
        self.payment_method = get_element_text(browser, select_pm_loc)
        do_click(browser, select_pm_loc)
        do_click(browser, payment_details_h3)
        sleep(0.5)

    def select_payment_term_field(self, browser, pt_type=3):
        do_click(browser, payment_term)
        values = get_list_of_elems_text(browser, payment_term_options[0], payment_term_options[1])
        assert values == payment_term_list
        select_pt = payment_term_options[1] + f'[{pt_type}]'
        select_pt_loc = replace_in_tuple(payment_term_options, 1, select_pt)
        self.payment_term = get_element_text(browser, select_pt_loc)
        do_click(browser, select_pt_loc)
        do_click(browser, payment_details_h3)
        sleep(0.5)

    def fill_billing_txtbox_data(self, browser):
        should_be_visible(browser, Billing_Address1_h3, 'Billing_Address1_h3')
        ids_list = ['billingAddress', 'billingPostalCode', 'gstin']
        self.billing_data = ['Test Address, Gurgaon', generate_random_number(6), generate_random_gst()]
        for b_id, data in zip(ids_list, self.billing_data):
            bill_loc_str = billing_txt_box[1].replace("billingTxtBox", b_id)
            bill_loc = replace_in_tuple(billing_txt_box, 1, bill_loc_str)
            do_send_keys(browser, bill_loc, data)

    def select_country_field(self, browser, country='India'):
        do_click(browser, billing_country)
        values = get_list_of_elems_text(browser, billing_country_options[0], billing_country_options[1])
        assert values == billing_countries_list
        select_cou = billing_country_select[1].replace('country_name', country)
        select_cou_loc = replace_in_tuple(billing_country_select, 1, select_cou)
        scroll_into_the_view(browser, select_cou_loc[0], select_cou_loc[1])
        self.country = get_element_text(browser, select_cou_loc)
        do_click(browser, select_cou_loc)
        loader_should_be_invisile(browser, 2)
        do_click(browser, Billing_Address1_h3)
        sleep(0.5)

    def select_state_field(self, browser, state='Uttar Pradesh'):
        do_click(browser, billing_state)
        values = get_list_of_elems_text(browser, billing_state_options[0], billing_state_options[1])
        assert values == billing_india_states_list
        select_cou = billing_state_select[1].replace('state_name', state)
        select_cou_loc = replace_in_tuple(billing_state_select, 1, select_cou)
        scroll_into_the_view(browser, select_cou_loc[0], select_cou_loc[1])
        self.state = get_element_text(browser, select_cou_loc)
        do_click(browser, select_cou_loc)
        time.sleep(1)
        do_click(browser, Billing_Address1_h3)
        sleep(0.5)

    def select_city_field(self, browser, city='Ghaziabad'):
        do_click(browser, billing_city)
        values = get_list_of_elems_text(browser, billing_city_options[0], billing_city_options[1])
        assert values == billing_uttar_pradesh_cities_list
        select_cou = billing_city_select[1].replace('city_name', city)
        select_cou_loc = replace_in_tuple(billing_city_select, 1, select_cou)
        scroll_into_the_view(browser, select_cou_loc[0], select_cou_loc[1])
        self.city = get_element_text(browser, select_cou_loc)
        do_click(browser, select_cou_loc)
        do_click(browser, Billing_Address1_h3)
        sleep(0.5)

    def verify_created_account(self, browser, all_data_dict: dict):
        sleep(2)
        loader_should_be_invisile(browser, 10)
        acc_name_loc = accounts_name_row_loc[1].replace("name", self.account_details[0])
        row_num = get_list_of_elems_attributes_value(browser, accounts_name_row_loc[0], acc_name_loc, 'row-id')
        accounts_table_row_loc_new = accounts_table_row_loc[1].replace("0", row_num[0])
        values = get_list_of_elems_text(browser, accounts_table_row_loc[0], accounts_table_row_loc_new)
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
        for i in values[1:-3]:
            for j in acc_data_list:
                if ('9090909090' in i or '99090909090' in i) is True:
                    i = str(i).replace("+91-", '')
                if i == j:
                    break
                else:
                    if acc_data_list.index(j) == len(acc_data_list) - 1:
                        non_present_data.append(i)
                        break
        logging.info(non_present_data)
        assert len(non_present_data) == 0

    def verify_created_account_details(self, browser):
        should_be_visible(browser, accnt_details_header_loc, "accnt_details_header_loc")
        for col_name in account_details_data:
            acct_details_cols = account_details_cols_locs[1].replace("field", col_name)
            r_acct_details_cols = replace_in_tuple(account_details_cols_locs, 1, acct_details_cols)
            should_be_visible(browser, r_acct_details_cols, "r_acct_details_cols")
        basic_acct_details_fields = ['Account Name', 'Email ID', 'Website', 'Phone Number', 'Landline Number',
                                     'PAN Number', 'Customer Code', 'Number of Working Days(In year)']
        actual_item_list = []
        for field_name in basic_acct_details_fields:
            basic_acct_details_loc = accnt_details_values_locs[1].replace("feild", field_name)
            basic_acct_details_value_loc = replace_in_tuple(accnt_details_values_locs, 1, basic_acct_details_loc)
            actual_values_txt = get_element_text(browser, basic_acct_details_value_loc)
            if actual_values_txt == "+91-9090909090":
                actual_values_txt = "99090909090"
            if actual_values_txt == "7":
                actual_values_txt = 7
            actual_item_list.append(actual_values_txt)
        logging.info(self.account_details)
        logging.info(actual_item_list)
        assert actual_item_list == self.account_details
        logging.info("Initial values validated")
        business_type_list = ["FY Start Month", "RM Norms Rate Type", "Business Nature", "Business Domain ",
                              "Business Segment", "Payment Method", "Payment Term"]
        actual_business_type_list = []
        for field_name in business_type_list:
            acct_details_loc = accnt_details_values_locs[1].replace("feild", field_name)
            acct_business_type_val_loc = replace_in_tuple(accnt_details_values_locs, 1, acct_details_loc)
            acct_business_type_val_txt = get_element_text(browser, acct_business_type_val_loc)
            if acct_business_type_val_txt == "07 Days":
                acct_business_type_val_txt = acct_business_type_val_txt.lower()
            actual_business_type_list.append(acct_business_type_val_txt)
        logging.info(actual_business_type_list)
        exptd_business_type_list = [self.start_month, self.rm_norms, self.business_nature, self.business_domain,
                                    self.business_segment, self.payment_method, self.payment_term]
        logging.info(exptd_business_type_list)
        assert actual_business_type_list == exptd_business_type_list

    def verify_address_details(self, browser):
        address_city_txt = self.billing_data[0].split(',')
        sp_address_city_txt = [address.strip() for address in address_city_txt]
        expected_address_list = [sp_address_city_txt[0], sp_address_city_txt[1], self.city, self.state, self.country,
                                 self.billing_data[1]]
        logging.info(expected_address_list)
        should_be_visible(browser, address_details_header_loc, "address_details_header_loc")
        should_be_visible(browser, primary_billing_address_loc, "primary_billing_address_loc")
        actual_billing_address_txt = get_element_text(browser, billing_address_txt_loc)
        split_billing_address_list = actual_billing_address_txt.split(',')
        cleaned_billing_addresses = [address.strip() for address in split_billing_address_list]
        cleaned_billing_addresses[-1] = cleaned_billing_addresses[-1].rstrip('.')
        logging.info(cleaned_billing_addresses)
        assert cleaned_billing_addresses == expected_address_list
        actual_shipping_address_txt = get_element_text(browser, primary_shipping_address_txt_loc)
        split_shipping_address_list = actual_shipping_address_txt.split(',')
        cleaned_shipping_addresses = [address.strip() for address in split_shipping_address_list]
        cleaned_shipping_addresses[-1] = cleaned_shipping_addresses[-1].rstrip('.')
        logging.info(cleaned_shipping_addresses)
        assert cleaned_shipping_addresses == expected_address_list


class Norms:

    def __init__(self):
        self.rm_norms_filter = None
        self.rm_norm_fiscal_year = None
        self.over_head_norm_effective_till = None
        self.over_head_norm_effective_from = None
        self.process_norm_effective_till = None
        self.process_norm_effective_from = None
        self.mhr_norm_effective_till = None
        self.mhr_norm_effective_from = None
        self.currency_norm_effective_till = None
        self.currency_norm_effective_from = None
        self.bop_norms_filter = None
        self.bop_fiscal_year = None
        self.norm_vars = {}
        self.raw_material_col_data = None
        self.bop_norms_col_data = None
        self.expd_mhr_info_data = None
        self.machine_name = None
        self.mhr_info_place_txt = None
        self.oum_info_txt = None
        self.machine_variable_values = None
        self.space_rental_values = None
        self.finance_cost_values = None
        self.man_power_cost_values = None
        self.other_costs_values = None
        self.bop_col_headers = None
        self.raw_mate_col_headers = None
        self.process_norms_table_headers = None

    def select_norms(self, browser, index):
        do_click(browser, norms_type)
        values = get_list_of_elems_text(browser, norms_type_options[0], norms_type_options[1])
        assert values == norms_dd_data
        select_option = norms_type_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(norms_type_options, 1, select_option)
        norm = get_element_text(browser, select_option_loc)
        self.norm_vars[f'norm_{index}'] = norm
        do_click(browser, select_option_loc)
        sleep(1)

    def select_fiscal_year(self, browser, index):
        do_click(browser, fiscal_year)
        values = get_list_of_elems_text(browser, fiscal_year_options[0], fiscal_year_options[1])
        assert values == fiscal_year_dd_data
        select_option = fiscal_year_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(fiscal_year_options, 1, select_option)
        option = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)
        return option

    def select_norms_filter(self, browser, index):
        do_click(browser, norms_filter)
        values = get_list_of_elems_text(browser, norms_filter_options[0], norms_filter_options[1])
        assert values == norms_filter_dd_data
        select_option = norms_filter_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(norms_filter_options, 1, select_option)
        option = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)
        return option

    def select_norm_factoring_location(self, browser, index):
        do_click(browser, manuf_location)
        select_option = manuf_location_options[1] + f'[{index}]'
        select_option_loc = replace_in_tuple(manuf_location_options, 1, select_option)
        option = get_element_text(browser, select_option_loc)
        do_click(browser, select_option_loc)
        sleep(0.5)
        logging.info(option)
        return option

    def select_norm_business_nature(self, browser, index, dd_index=2):
        do_click(browser, acc_business_nature)
        values = get_list_of_elems_text(browser, acc_business_nature_options[0], acc_business_nature_options[1])
        assert values[1:] == business_nature_list[1:dd_index]
        select_bn = acc_business_nature_options[1] + f'[{index}]'
        select_bn_loc = replace_in_tuple(acc_business_nature_options, 1, select_bn)
        option = get_element_text(browser, select_bn_loc)
        do_click(browser, select_bn_loc)
        return option

    def select_bop_norms(self, browser, fis_index=6, nf_index=4):
        self.select_norms(browser, index=2)
        should_be_visible(browser, bop_norms_text, 'bop_norms_text')
        self.bop_fiscal_year = self.select_fiscal_year(browser, fis_index)
        self.bop_norms_filter = self.select_norms_filter(browser, nf_index)
        self.fill_bop_norms_cols_data(browser)
        sleep(2)
        do_click(browser, save_btn)

    def get_bop_norms_default_col_data(self, browser):
        self.bop_col_headers = ['BOP Name', 'Business Nature', 'Manufacturing Location', 'Fiscal Year']
        default_table_data = []
        table_cell_data ={}
        for num in range(1, 5):
            bop_table_cols_data = raw_material_cols[1] + f'[{num}]'
            bop_table_cols_data_loc = replace_in_tuple(raw_material_cols, 1, bop_table_cols_data)
            cell_data_txt = get_element_text(browser, bop_table_cols_data_loc)
            table_cell_data[self.bop_col_headers[num - 1]] = cell_data_txt
        default_table_data.append(table_cell_data)

    def fill_bop_norms_cols_data(self, browser):
        self.bop_norms_col_data = ['100', '75', '25', '80', '30', '70', '30']
        elems = browser.find_elements(raw_material_cols[0], raw_material_cols[1])
        elems_len = len(elems)
        count = 0
        for num in range(5, elems_len + 1):
            bop_norms_data = raw_material_cols[1] + f'[{num}]'
            bop_norms_data_loc = replace_in_tuple(raw_material_cols, 1, bop_norms_data)
            scroll_into_the_view(browser, bop_norms_data_loc[0], bop_norms_data_loc[1])
            do_double_click(browser, bop_norms_data_loc)
            sleep(1)
            input_bop_norms_data_loc = bop_norms_data_loc[1] + "//input"
            input_bop_norms_data_val_loc = replace_in_tuple(bop_norms_data_loc, 1, input_bop_norms_data_loc)
            try:
                do_send_keys(browser, input_bop_norms_data_val_loc, self.bop_norms_col_data[count])
            except Exception as e:
                logging.error(f"Error while sending keys: {e}")
            count += 1

    def fill_data_of_over_head_norms_table_data(self, browser, index_list: list, opt_index_list: list, txt: str):
        for index, opt_index in zip(index_list, opt_index_list):
            r_norms_flat_rate = norms_flat_rate_loc[1].replace('num', index)
            r_norms_flat_rate_loc = replace_in_tuple(norms_flat_rate_loc, 1, r_norms_flat_rate)
            do_double_click(browser, r_norms_flat_rate_loc)
            input_norms_flat_rate_loc = r_norms_flat_rate_loc[1] + "//input"
            r_input_norms_flat_rate_loc = replace_in_tuple(r_norms_flat_rate_loc, 1, input_norms_flat_rate_loc)
            do_send_keys(browser, r_input_norms_flat_rate_loc, txt)
            do_send_keys(browser, r_input_norms_flat_rate_loc, Keys.ENTER)
            norms_percentage_rate = norms_percentage_rate_loc[1].replace('num', index)
            r_norms_percentage_rate_loc = replace_in_tuple(norms_percentage_rate_loc, 1, norms_percentage_rate)
            do_double_click(browser, r_norms_percentage_rate_loc)
            input_norms_percentage_rate_loc = r_norms_percentage_rate_loc[1] + "//input"
            r_input_norms_percentage_rate_loc = replace_in_tuple(r_norms_percentage_rate_loc, 1, input_norms_percentage_rate_loc)
            do_send_keys(browser, r_input_norms_percentage_rate_loc, txt)
            do_send_keys(browser, r_input_norms_percentage_rate_loc, Keys.ENTER)
            r_norms_applicable_on = norms_applicable_on_loc[1].replace('num', index)
            r_norms_applicable_on_loc = replace_in_tuple(norms_applicable_on_loc, 1, r_norms_applicable_on)
            do_click(browser, r_norms_applicable_on_loc)
            rr_norms_applicable_options_loc = norms_applicable_options_loc[1].replace('num', index)
            r_norms_applicable_options = rr_norms_applicable_options_loc + f'[{opt_index}]'
            applicable_on_option_loc = replace_in_tuple(norms_applicable_options_loc, 1, r_norms_applicable_options)
            do_click(browser, applicable_on_option_loc)

    def select_currency_norms(self, browser):
        self.select_norms(browser, index=3)
        should_be_visible(browser, currency_norms_text, 'currency_norms_text')
        todayDate = datetime.today()
        self.currency_norm_effective_from = todayDate.strftime('%m/%d/%Y')
        yesterday = todayDate + timedelta(days=30)
        self.currency_norm_effective_till = yesterday.strftime('%m/%d/%Y')
        do_send_keys(browser, effective_from, str(self.currency_norm_effective_from))
        do_send_keys(browser, effective_till, str(self.currency_norm_effective_till))
        do_click(browser, save_btn)

    def select_mhr_norms(self, browser, location, ml_index=2, bn_index=2):
        self.select_norms(browser, index=4)
        should_be_visible(browser, mhr_norms_text, 'mhr_norms_text')
        manu_locate = self.select_norm_factoring_location(browser, ml_index)
        assert manu_locate == location
        self.select_norm_business_nature(browser, bn_index)
        todayDate = datetime.today()
        self.mhr_norm_effective_from = todayDate.strftime('%m/%d/%Y')
        yesterday = todayDate + timedelta(days=30)
        self.mhr_norm_effective_till = yesterday.strftime('%m/%d/%Y')
        do_send_keys(browser, effective_from, str(self.mhr_norm_effective_from))
        do_send_keys(browser, effective_till, str(self.mhr_norm_effective_till))
        self.all_data_of_mhr_cols(browser)
        do_click(browser, save_btn)

    def select_process_norms(self, browser, location, ml_index=2, bn_index=2):
        self.select_norms(browser, index=5)
        should_be_visible(browser, process_norms_text, 'process_norms_text')
        manu_locate = self.select_norm_factoring_location(browser, ml_index)
        # assert manu_locate == location
        self.select_norm_business_nature(browser, bn_index)
        todayDate = datetime.today()
        self.process_norm_effective_from = todayDate.strftime('%m/%d/%Y')
        yesterday = todayDate + timedelta(days=30)
        self.process_norm_effective_till = yesterday.strftime('%m/%d/%Y')
        do_send_keys(browser, effective_from, str(self.process_norm_effective_from))
        do_send_keys(browser, effective_till, str(self.process_norm_effective_till))
        self.get_process_norms_table_data(browser)
        do_click(browser, save_btn)

    def select_over_head_norms(self, browser, location, index_list: list, opt_index_list: list, txt: str, ml_index=2, bn_index=2, ):
        self.select_norms(browser, index=6)
        should_be_visible(browser, over_head_text, 'over_head_text')
        manu_locate = self.select_norm_factoring_location(browser, ml_index)
        # assert manu_locate == location
        self.select_norm_business_nature(browser, bn_index)
        todayDate = datetime.today()
        self.over_head_norm_effective_from = todayDate.strftime('%m/%d/%Y')
        yesterday = todayDate + timedelta(days=30)
        self.over_head_norm_effective_till = yesterday.strftime('%m/%d/%Y')
        do_send_keys(browser, effective_from, str(self.over_head_norm_effective_from))
        do_send_keys(browser, effective_till, str(self.over_head_norm_effective_till))
        self.fill_data_of_over_head_norms_table_data(browser, index_list, opt_index_list, txt)
        do_click(browser, save_btn)

    def select_raw_material_norm(self, browser, fis_index=6, nf_index=4):
        self.select_norms(browser, index=7)
        should_be_visible(browser, raw_material_norms_text, 'raw_material_norms_text')
        self.rm_norm_fiscal_year = self.select_fiscal_year(browser, fis_index)
        self.rm_norms_filter = self.select_norms_filter(browser, nf_index)
        self.get_raw_material_norms_table_data(browser)
        self.fill_raw_material_col_data(browser)
        sleep(2)
        do_click(browser, save_btn)

    def get_raw_material_norms_table_data(self, browser):
        self.raw_mate_col_headers = ['RM Name', 'RM Type', 'Business Nature', 'Manufacturing Location', 'Fiscal Year']
        default_raw_mate_table_data = []
        table_cell_data = {}
        for num in range(1, 6):
            raw_material_cols_data = raw_material_cols[1] + f'[{num}]'
            raw_material_cols_data_loc = replace_in_tuple(raw_material_cols, 1, raw_material_cols_data)
            cell_data_txt = get_element_text(browser, raw_material_cols_data_loc)
            table_cell_data[self.raw_mate_col_headers[num - 1]] = cell_data_txt
        default_raw_mate_table_data.append(table_cell_data)
        logging.info(default_raw_mate_table_data)

    def fill_raw_material_col_data(self, browser):
        self.raw_material_col_data = ['15', '20', '75', '25', '80', '30', '70', '30', '72', '34', '76', '31', '80', '44']
        elems = browser.find_elements(raw_material_cols[0], raw_material_cols[1])
        elems_len = len(elems)
        count = 0
        for num in range(6, elems_len + 1):
            raw_material_data = raw_material_cols[1] + f'[{num}]'
            raw_material_data_loc = replace_in_tuple(raw_material_cols, 1, raw_material_data)
            scroll_into_the_view(browser, raw_material_data_loc[0], raw_material_data_loc[1])
            do_double_click(browser, raw_material_data_loc)
            input_raw_material_data_loc = raw_material_data_loc[1] + "//input"
            sleep(1)
            input_bop_norms_data_val_loc = replace_in_tuple(raw_material_data_loc, 1, input_raw_material_data_loc)
            do_send_keys(browser, input_bop_norms_data_val_loc, self.raw_material_col_data[count])
            do_send_keys(browser, input_bop_norms_data_val_loc, Keys.ENTER)
            count += 1

    def all_data_of_mhr_cols(self, browser):
        self.provide_mhr_info(browser)
        self.select_machine_name(browser)
        self.select_mhr_info_process(browser)
        self.select_oum_info_col(browser)
        self.fill_machine_variable_cols(browser)
        self.fill_space_rental_cost_cols(browser)
        self.fill_finance_cost_cols(browser)
        self.fill_man_power_cost_cols(browser)
        self.fill_electric_cost_cols(browser)
        self.fill_other_costs_cols(browser)

    def provide_mhr_info(self, browser):
        self.expd_mhr_info_data = [random_correct_name(8, 4, 'first_name'), generate_random_number(5), "paramOne", "paramTwo", "paramThree", "paramFour"]
        for field_name, data in zip(mht_cols_valus, self.expd_mhr_info_data):
            mhr_info_field = mhr_data_cols_loc[1].replace('field', field_name)
            mhr_info_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, mhr_info_field)
            scroll_into_the_view(browser, mhr_info_field_loc[0], mhr_info_field_loc[1])
            do_clear(browser, mhr_info_field_loc)
            do_send_keys(browser, mhr_info_field_loc, data)
        self.select_machine_name(browser)
        self.select_mhr_info_process(browser)
        self.select_oum_info_col(browser)

    def select_machine_name(self, browser, index=6):
        scroll_into_the_view(browser, machine_name_selec_loc[0], machine_name_selec_loc[1])
        do_click(browser, machine_name_selec_loc)
        machine_name_place = machine_name_options_loc[1] + f'[{index}]'
        machine_name_place = replace_in_tuple(machine_name_options_loc, 1, machine_name_place)
        self.machine_name = get_element_text(browser, machine_name_place)
        scroll_into_the_view(browser, machine_name_place[0], machine_name_place[1])
        do_click(browser, machine_name_place)

    def select_mhr_info_process(self, browser, index=2):
        scroll_into_the_view(browser, mhr_info_process_selec_loc[0], mhr_info_process_selec_loc[1])
        do_click(browser, mhr_info_process_selec_loc)
        mhr_info_place = mhr_info_options_loc[1] + f'[{index}]'
        mhr_info_place = replace_in_tuple(mhr_info_options_loc, 1, mhr_info_place)
        self.mhr_info_place_txt = get_element_text(browser, mhr_info_place)
        scroll_into_the_view(browser, mhr_info_place[0], mhr_info_place[1])
        do_click(browser, mhr_info_place)

    def select_oum_info_col(self, browser, index=3):
        scroll_into_the_view(browser, oum_info_col_loc[0], oum_info_col_loc[1])
        do_click(browser, oum_info_col_loc)
        oum_info_place = mhr_info_options_loc[1] + f'[{index}]'
        oum_info_place = replace_in_tuple(mhr_info_options_loc, 1, oum_info_place)
        self.oum_info_txt = get_element_text(browser, oum_info_place)
        scroll_into_the_view(browser, oum_info_place[0], oum_info_place[1])
        do_click(browser, oum_info_place)

    def fill_machine_variable_cols(self, browser, no_of_work_days=7, no_of_hrs_inshift=10, no_of_days_for_prod=5, no_of_hrs_for_costing=12, cycle_time=25 ):
        self.machine_variable_values = [generate_random_number(5), no_of_work_days, no_of_hrs_inshift, no_of_days_for_prod, no_of_hrs_for_costing, cycle_time]
        should_be_visible(browser, machine_variable_header_loc, "machine_variable_header_loc")
        for field_name, data in zip(machine_variables, self.machine_variable_values):
            machine_vars_field = mhr_data_cols_loc[1].replace('field', field_name)
            machine_vars_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, machine_vars_field)
            do_clear(browser, machine_vars_field_loc)
            do_send_keys(browser, machine_vars_field_loc, data)

    def fill_space_rental_cost_cols(self, browser, length=500, width =55, height=400, feet=550):
        self.space_rental_values = [length, width, height, feet]
        should_be_visible(browser, space_rental_cost_header_loc, "space_rental_cost_header_loc")
        for field_name, data in zip(space_rental_cost_data, self.space_rental_values):
            space_rental_field = mhr_data_cols_loc[1].replace('field', field_name)
            space_rental_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, space_rental_field)
            do_clear(browser, space_rental_field_loc)
            do_send_keys(browser, space_rental_field_loc, data)

    def fill_finance_cost_cols(self, browser, depriciation_perce=10, interest=15):
        self.finance_cost_values = [depriciation_perce, interest]
        should_be_visible(browser, finance_cost_header_loc, "finance_cost_header_loc")
        for field_name, data in zip(finance_cost_data, self.finance_cost_values):
            finance_cost_field = mhr_data_cols_loc[1].replace('field', field_name)
            finance_cost_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, finance_cost_field)
            do_clear(browser, finance_cost_field_loc)
            do_send_keys(browser, finance_cost_field_loc, data)

    def fill_man_power_cost_cols(self, browser):
        self.man_power_cost_values = [20, 5000, 10, 3000, 2500]
        should_be_visible(browser, man_power_cost_header_loc, "man_power_cost_header_loc")
        for field_name, data in zip(man_power_cost_data, self.man_power_cost_values):
            man_power_cost_field = mhr_data_cols_loc[1].replace('field', field_name)
            man_power_cost_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, man_power_cost_field)
            do_clear(browser, man_power_cost_field_loc)
            do_send_keys(browser, man_power_cost_field_loc, data)

    def fill_electric_cost_cols(self, browser):
        self.electric_cost_values = [200, 500, 10, 14, 250]
        should_be_visible(browser, electricity_cost_header_loc, "electricity_cost_header_loc")
        for field_name, data in zip(electric_cost_data, self.electric_cost_values):
            electric_cost_field = mhr_data_cols_loc[1].replace('field', field_name)
            electric_cost_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, electric_cost_field)
            do_clear(browser, electric_cost_field_loc)
            do_send_keys(browser, electric_cost_field_loc, data)

    def fill_other_costs_cols(self, browser):
        self.other_costs_values = [20, 35, 100000, 200]
        should_be_visible(browser, electricity_cost_header_loc, "electricity_cost_header_loc")
        for field_name, data in zip(other_costs_data, self.other_costs_values):
            other_cost_field = mhr_data_cols_loc[1].replace('field', field_name)
            other_cost_field_loc = replace_in_tuple(mhr_data_cols_loc, 1, other_cost_field)
            do_clear(browser, other_cost_field_loc)
            do_send_keys(browser, other_cost_field_loc, data)

    def get_process_norms_table_data(self, browser):
        self.process_norms_table_headers = ['Machine', 'Process', 'Capacity', 'Process Unit', 'Rate(New)', 'Existing Rate']
        elems = browser.find_elements(process_norms_table_data_loc[0], process_norms_table_data_loc[1])
        elems_len = len(elems)
        col_names_lst = []
        for index in range(1, elems_len + 1):
            process_norms_cols_loc = process_norms_table_data_loc[1] + f'[{index}]//td'
            logging.info(process_norms_cols_loc)
            r_process_norms_cols_loc = replace_in_tuple(process_norms_table_data_loc, 1, process_norms_cols_loc)
            process_norms_cols_elems = browser.find_elements(r_process_norms_cols_loc[0], r_process_norms_cols_loc[1])
            elems_len = len(process_norms_cols_elems)
            table_cell_data = {}
            for i in range(1, elems_len + 1):
                process_norms_cell_value_loc = r_process_norms_cols_loc[1] + f'[{i}]'
                process_norms_cell_value_txt = replace_in_tuple(r_process_norms_cols_loc, 1, process_norms_cell_value_loc)
                cell_data_txt = get_element_text(browser, process_norms_cell_value_txt)
                table_cell_data[self.process_norms_table_headers[i - 1]] = cell_data_txt
            col_names_lst.append(table_cell_data)
            logging.info(col_names_lst)
        process_norms_table_new_rate_loc1 = process_norms_table_new_rate_loc[1] + '[1]'
        process_norms_table_new_rate_loc1 = replace_in_tuple(process_norms_table_new_rate_loc, 1, process_norms_table_new_rate_loc1)
        do_send_keys(browser, process_norms_table_new_rate_loc1, '100')

        process_norms_table_new_rate_loc2 = process_norms_table_new_rate_loc[1] + '[2]'
        process_norms_table_new_rate_loc2 = replace_in_tuple(process_norms_table_new_rate_loc, 1,
                                                             process_norms_table_new_rate_loc2)
        do_send_keys(browser, process_norms_table_new_rate_loc2, '100')



