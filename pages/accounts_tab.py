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
        for i in range(1, elems_len-1):
            col_loc = accounts_head_col[1] + f'[{i}]'
            scroll_into_the_view(browser, accounts_head_col[0], col_loc)
            col_name = get_text_by_js_xpath(browser, col_loc)
            col_names_lst.append(col_name)
        print(col_names_lst)
        assert accounts_table_header_col.sort() == col_names_lst

    def add_accounts_data_in_txt_box(self, browser):
        self.account_details = accounts_general_details
        for field_name, data in zip(accounts_create_fields_gen, self.account_details):
            acco_field = acc_field_txtbox[1].replace('field_name', field_name)
            acc_field_loc = replace_in_tuple(acc_field_txtbox, 1, acco_field)
            do_send_keys(browser, acc_field_loc, data)

    def select_start_month_field(self, browser):
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
        assert values[3:] == business_nature_list
        select_bn = business_nature_option[1] + f'[{bn_type}]'
        select_bn_loc = replace_in_tuple(business_nature_option, 1, select_bn)
        do_click(browser, select_bn_loc)
        do_click(browser, business_info_h3)
        self.business_nature = get_element_text(browser, business_nature_selected).rstrip(" x ")
        assert self.business_nature == business_nature_list[bn_type - 1]

    def select_business_domain_field(self, browser, bd_type=2):
        do_click(browser, business_domain)
        values = get_list_of_elems_text(browser, business_domain_option_txt[0], business_domain_option_txt[1])
        assert values[3:] == business_domain_list
        select_bd = business_domain_option[1] + f'[{bd_type}]'
        select_bn_loc = replace_in_tuple(business_domain_option, 1, select_bd)
        do_click(browser, select_bn_loc)
        do_click(browser, business_info_h3)
        self.business_domain = get_element_text(browser, business_domain_selected).rstrip(" x ")
        assert self.business_domain == business_domain_list[bd_type - 1]

    def select_business_segment_field(self, browser, bs_type=2):
        do_click(browser, business_segment)
        values = get_list_of_elems_text(browser, business_segment_option_txt[0], business_segment_option_txt[1])
        assert values[3:] == business_segment_list
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
        self.billing_data = billing_add_gst_pc_list
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
        values = get_list_of_elems_text(browser, accounts_table_row_loc[0], accounts_table_row_loc[1])
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
                if j == '9090909090':
                    i = str(i).replace("+91-", '')
                if i == j:
                    break
                else:
                    if acc_data_list.index(j) == -1:
                        non_present_data.append(i)
                        break
        print(non_present_data)
        assert len(non_present_data) == 0

