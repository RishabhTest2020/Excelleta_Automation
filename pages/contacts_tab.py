import logging
import os

from selenium.webdriver import Keys

from helpers.common_helpers import *
from locators.contact_tab_locators import *
from test_data.testdata import *
from time import sleep
from locators.accounts_tab_locators import *


class Contacts:
    def __init__(self):
        self.anniversary_date = None
        self.marital = None
        self.contact_city = None
        self.contact_state = None
        self.contact_country = None
        self.contact_billing_data = None
        self.dob_data = None
        self.gender = None
        self.report_to = None
        self.designation = None
        self.department = None
        self.name_title = None
        self.contact_details = None

    def verify_contacts_head_col(self, browser):
        elems = browser.find_elements(accounts_head_col[0], accounts_head_col[1])
        elems_len = len(elems)
        col_names_lst = []
        for i in range(1, elems_len+1):
            col_loc = accounts_head_col[1] + f'[{i}]'
            scroll_into_the_view(browser, accounts_head_col[0], col_loc)
            col_name = get_text_by_js_xpath(browser, col_loc)
            col_names_lst.append(col_name)
        logging.info(col_names_lst)
        assert contact_table_header_col.sort() == col_names_lst.sort()

    def select_account(self, browser, acc_name: str):
        do_send_keys(browser, contact_acc_name, acc_name)
        highlighted_name = get_element_text(browser, contact_acc_name_highlight)
        assert highlighted_name.lower() == acc_name.lower()
        do_click(browser, contact_acc_name_highlight)

    def add_contacts_data_in_txt_box(self, browser):
        self.contact_details = [random_correct_name(5, 4, 'first_name'), random_correct_name(5, 4, 'last_name'),
                                f'{random_email_generator()}', '9090909090']
        for field_name, data in zip(contacts_create_fields_gen, self.contact_details):
            acco_field = contact_field_txtbox[1].replace('field_name', field_name)
            acc_field_loc = replace_in_tuple(contact_field_txtbox, 1, acco_field)
            do_send_keys(browser, acc_field_loc, data)
        do_send_keys(browser, mobile_field_txtbox, self.contact_details[-1])
        upload_elem = browser.find_element(contact_logo[0], contact_logo[1])
        upload_elem.send_keys(os.getcwd() + '/files/watermark.png')
        do_click(browser, accept_uploaded_image)
        sleep(3)
        should_be_visible(browser, uploaded_img, 'uploaded_img')
        self.dob_data = '05/07/1996'
        do_send_keys(browser, select_date, self.dob_data)
        do_click(browser, check_email_option)
        do_click(browser, send_greetings_yes)
        do_click(browser, send_acknowledgement_yes)

    def select_title_field(self, browser, title_index=2):
        do_click(browser, select_title)
        values = get_list_of_elems_text(browser, select_title_options[0], select_title_options[1])
        assert values == titles_data
        select_name_tite = select_title_options[1] + f'[{title_index}]'
        select_title_loc = replace_in_tuple(select_title_options, 1, select_name_tite)
        self.name_title = get_element_text(browser, select_title_loc)
        do_click(browser, select_title_loc)
        time.sleep(0.5)

    def select_department_field(self, browser, dep_index=2):
        do_click(browser, select_department)
        values = get_list_of_elems_text(browser, select_department_options[0], select_department_options[1])
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(department_data, values)
        assert val is True
        select_department_name = select_department_options[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(select_department_options, 1, select_department_name)
        self.department = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_designation_field(self, browser, dep_index=2):
        do_click(browser, select_department)
        values = get_list_of_elems_text(browser, select_designation_options[0], select_designation_options[1])
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(designation_data, values)
        assert val is True
        select_designation_name = select_designation_options[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(select_designation_options, 1, select_designation_name)
        self.designation = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_report_to_field(self, browser):
        do_click(browser, select_report_to)
        values = get_list_of_elems_text(browser, select_report_to_options[0], select_report_to_options[1])
        assert values == report_to_data
        # select_designation_name = select_report_to_options[1] + f'[{rep_index}]'
        # select_rep_loc = replace_in_tuple(select_report_to_options, 1, select_designation_name)
        # self.report_to = get_element_text(browser, select_rep_loc)
        # do_click(browser, select_rep_loc)
        # sleep(0.5)

    def select_gender_field(self, browser, gen_index=2):
        do_click(browser, select_gender)
        values = get_list_of_elems_text(browser, select_gender_options[0], select_gender_options[1])
        assert values == gender_data
        select_gender_name = select_gender_options[1] + f'[{gen_index}]'
        select_gen_loc = replace_in_tuple(select_gender_options, 1, select_gender_name)
        self.gender = get_element_text(browser, select_gen_loc)
        do_click(browser, select_gen_loc)
        sleep(0.5)

    def select_marital_field(self, browser, mar_index=2):
        do_click(browser, select_marital_status)
        values = get_list_of_elems_text(browser, select_marital_options[0], select_marital_options[1])
        assert values == marital_data
        select_marital_name = select_marital_options[1] + f'[{mar_index}]'
        select_mar_loc = replace_in_tuple(select_marital_options, 1, select_marital_name)
        self.marital = get_element_text(browser, select_mar_loc)
        do_click(browser, select_mar_loc)
        sleep(0.5)
        if mar_index == 2:
            self.anniversary_date = '05/07/2024'
            anni_date = select_date[1] + '[2]'
            date_loc = replace_in_tuple(select_date, 1, anni_date)
            do_send_keys(browser, date_loc, self.anniversary_date)

    def fill_contact_billing_txtbox_data(self, browser):
        should_be_visible(browser, official_address_txt, 'official_address_txt2')
        should_be_visible(browser, residential_address_txt, 'residential_address_txt')

        ids_list = ['address', 'postalCode', 'address', 'postalCode']
        self.contact_billing_data = [f'{random_correct_name(5, 4, 'first_name')}, Gurgaon',
                                     generate_random_five_digit_number(10),
                                     f'{random_correct_name(5, 4, 'first_name')}, Gurgaon',
                                     generate_random_five_digit_number(10)]
        for b_id, data, index in zip(ids_list, self.contact_billing_data, comprehension_range(1, len(ids_list))):
            bill_loc_str = billing_txt_box[1].replace("billingTxtBox", b_id) + f'[{index}]'
            bill_loc = replace_in_tuple(billing_txt_box, 1, bill_loc_str)
            do_send_keys(browser, bill_loc, data)

    def select_contact_country_fields(self, browser, country='India'):
        for index in range(1, 3):
            billing_country_path = contact_billing_country[1] + f'[{index}]'
            billing_country_loc = replace_in_tuple(contact_billing_country, 1, billing_country_path)
            do_click(browser, billing_country_loc)
            country_options = contact_billing_country_options[1].replace('index', str(index))
            values = get_list_of_elems_text(browser, contact_billing_country_options[0], country_options)
            assert values == billing_countries_list
            select_cou = contact_billing_country_select[1].replace('country_name', country).replace('index', str(index))
            select_cou_loc = replace_in_tuple(contact_billing_country_select, 1, select_cou)
            scroll_into_the_view(browser, select_cou_loc[0], select_cou_loc[1])
            self.contact_country = get_element_text(browser, select_cou_loc)
            do_click(browser, select_cou_loc)
            do_click(browser, official_address_txt)
            sleep(0.5)

    def select_contact_state_fields(self, browser, state='Uttar Pradesh'):
        for index in range(1, 3):
            billing_state_path = contact_billing_state[1] + f'[{index}]'
            billing_state_loc = replace_in_tuple(contact_billing_state, 1, billing_state_path)
            do_click(browser, billing_state_loc)
            state_options = contact_billing_state_options[1].replace('index', str(index))
            values = get_list_of_elems_text(browser, contact_billing_state_options[0], state_options)
            assert values == billing_india_states_list
            select_cou = contact_billing_state_select[1].replace('state_name', state).replace('index', str(index))
            select_cou_loc = replace_in_tuple(contact_billing_state_select, 1, select_cou)
            scroll_into_the_view(browser, select_cou_loc[0], select_cou_loc[1])
            self.contact_state = get_element_text(browser, select_cou_loc)
            do_click(browser, select_cou_loc)
            do_click(browser, official_address_txt)
            sleep(0.5)

    def select_contact_city_fields(self, browser, city='Ghaziabad'):
        for index in range(1, 3):
            billing_city_path = contact_billing_city[1] + f'[{index}]'
            billing_city_loc = replace_in_tuple(contact_billing_city, 1, billing_city_path)
            do_click(browser, billing_city_loc)
            city_options = contact_billing_city_options[1].replace('index', str(index))
            values = get_list_of_elems_text(browser, contact_billing_city_options[0], city_options)
            assert values == billing_uttar_pradesh_cities_list
            select_cou = contact_billing_city_select[1].replace('city_name', city).replace('index', str(index))
            select_cou_loc = replace_in_tuple(contact_billing_city_select, 1, select_cou)
            scroll_into_the_view(browser, select_cou_loc[0], select_cou_loc[1])
            self.contact_city = get_element_text(browser, select_cou_loc)
            do_click(browser, select_cou_loc)
            do_click(browser, official_address_txt)
            sleep(0.5)

    def verify_created_contact(self, browser, all_data_dict: dict):
        sleep(2)
        loader_should_be_invisile(browser, 10)
        values = get_list_of_elems_text(browser, accounts_table_row_loc[0], accounts_table_row_loc[1])

        all_data = list(all_data_dict.values())
        acc_data_list = []
        for i in all_data:
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
                if '9090909090' in i:
                    i = str(i).replace("+91-", '')
                if i == j:
                    break
                else:
                    if acc_data_list.index(j) == len(acc_data_list) - 1:
                        non_present_data.append(i)
                        break
        logging.info(non_present_data)
        assert len(non_present_data) == 0

