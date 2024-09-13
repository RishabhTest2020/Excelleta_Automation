import logging
import os

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys

from helpers.common_helpers import *
from locators.accounts_tab_locators import accounts_table_row_loc, accounts_head_col
from locators.contact_tab_locators import *
from locators.rfq_tab_locators import *
from test_data.testdata import *
from time import sleep
from datetime import datetime, timedelta


class Rfq:

    def __init__(self):
        self.business_dev_head = None
        self.rfq_text_boxes_data = None
        self.cft_member = None
        self.surface_treatment_head = None
        self.plant_head = None
        self.development_lead = None
        self.marketing_lead = None
        self.pm_lead = None
        self.rfq_shipping_address = None
        self.incoterms = None
        self.packaging_cost = None
        self.rfq_currency = None
        self.costing_format = None
        self.offer_validity = None
        self.costing_completion = None
        self.cft_completion = None
        self.finalizing_date = None
        self.project_life_num = None
        self.project_life_unit = None
        self.day_volume_unit = None
        self.day_volume = None
        self.annum_volume_unit = None
        self.annum_volume = None
        self.estimates_sop = None
        self.quotation_type = None
        self.company_priority = None
        self.manufacturing_location = None
        self.dev_lead_location = None
        self.customer_target_date = None
        self.rfq_received_date = None
        self.confidentiality = None
        self.business_value = None
        self.business_nature = None
        self.business_evaluation = None
        self.contact_person = None
        self.rfq_id = None

    def verify_rfq_head_col(self, browser):
        elems = browser.find_elements(accounts_head_col[0], accounts_head_col[1])
        elems_len = len(elems)
        col_names_lst = []
        for i in range(1, elems_len - 1):
            col_loc = accounts_head_col[1] + f'[{i}]'
            scroll_into_the_view(browser, accounts_head_col[0], col_loc)
            col_name = get_text_by_js_xpath(browser, col_loc)
            col_names_lst.append(col_name)
        logging.info(col_names_lst)
        assert rfq_header_table_col.sort() == col_names_lst.sort()

    def select_account_and_key_person(self, browser, acc_name: str):
        do_clear(browser, rfq_acc_name)
        do_send_keys(browser, rfq_acc_name, Keys.ENTER)
        do_send_keys(browser, rfq_acc_name, acc_name)
        do_send_keys(browser, rfq_acc_name, Keys.ENTER)
        try:
            highlighted_name = get_element_text(browser, contact_acc_name_highlight)
        except TimeoutException:
            do_clear(browser, rfq_acc_name)
            do_send_keys(browser, rfq_acc_name, Keys.ENTER)
            do_send_keys(browser, rfq_acc_name, acc_name)
            do_send_keys(browser, rfq_acc_name, Keys.ENTER)
            highlighted_name = get_element_text(browser, contact_acc_name_highlight)
        assert highlighted_name.lower() == acc_name.lower()
        do_click(browser, contact_acc_name_highlight)
        loader_should_be_invisile(browser, 4)
        do_click(browser, rfq_key_contact_person)
        self.contact_person = get_element_text(browser, select_key_contact_peroson)
        do_click(browser, select_key_contact_peroson)
        loader_should_be_invisile(browser, 4)

    def select_business_evaluation(self, browser, dep_index=2):
        do_click(browser, rfq_business_evaluation)
        values = get_list_of_elems_text(browser, rfq_business_evaluation_options[0], rfq_business_evaluation_options[1])
        assert values == rfq_business_evaluation_data
        select_name = rfq_business_evaluation_options[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(rfq_business_evaluation_options, 1, select_name)
        self.business_evaluation = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def verify_domain(self, browser, domain):
        txt = get_element_text(browser, rfq_business_domain)
        assert txt == domain

    def select_business_nature(self, browser):
        do_click(browser, rfq_business_nature)
        self.business_nature = get_element_text(browser, rfq_business_nature_select)
        do_click(browser, rfq_business_nature_select)

    def select_business_segment(self, browser):
        do_click(browser, rfq_business_segment)
        self.business_nature = get_element_text(browser, rfq_business_segment_select)
        do_click(browser, rfq_business_segment_select)

    def select_business_value(self, browser, dep_index=2):
        do_click(browser, rfq_business_value)
        values = get_list_of_elems_text(browser, rfq_business_value_select[0], rfq_business_value_select[1])
        assert values == rfq_business_values_data
        select_name = rfq_business_value_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(rfq_business_value_select, 1, select_name)
        self.business_value = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_confidentiality(self, browser, dep_index=2):
        do_click(browser, rfq_confidentiality)
        values = get_list_of_elems_text(browser, rfq_confidentiality_select[0], rfq_confidentiality_select[1])
        assert values == rfq_confidentiality_dropdown
        select_name = rfq_confidentiality_select[1] + f'[{dep_index}]'
        select_dep_loc = replace_in_tuple(rfq_confidentiality_select, 1, select_name)
        self.confidentiality = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_rfq_received_date(self, browser):
        todayDate = datetime.today()
        yesterday = todayDate - timedelta(days=1)
        yesterday_formatted_date = yesterday.strftime('%m/%d/%Y')
        self.rfq_received_date = yesterday_formatted_date
        do_send_keys(browser, rfq_received_date_loc, yesterday_formatted_date)

    def select_customer_target_date(self, browser):
        todayDate = datetime.today()
        yesterday = todayDate + timedelta(days=6)
        yesterday_formatted_date = yesterday.strftime('%m/%d/%Y')
        self.customer_target_date = yesterday_formatted_date
        do_send_keys(browser, rfq_target_date_loc, yesterday_formatted_date)

    def select_dev_lead_location(self, browser, index=2):
        do_click(browser, rfq_dev_lead_loc)
        values = get_list_of_elems_text(browser, rfq_dev_lead_loc_select_opts[0], rfq_dev_lead_loc_select_opts[1])
        rfq_dev_lead_location_data = get_env_var_from_globals('rfq_dev_lead_location_data_')
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(rfq_dev_lead_location_data, values)
        assert val is True
        # select_name = rfq_dev_lead_loc_select[1] + f'[{index}]'
        select_name = rfq_dev_lead_loc_select[1].replace('devleadlocaton', index)
        select_dep_loc = replace_in_tuple(rfq_dev_lead_loc_select, 1, select_name)
        self.dev_lead_location = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_manufacturing_location(self, browser, index):
        do_click(browser, rfq_manufacturing_loc)
        values = get_list_of_elems_text(browser, rfq_manufacturing_loc_select_opts[0], rfq_manufacturing_loc_select_opts[1])
        rfq_manufacturing_location_data = get_env_var_from_globals('rfq_manufacturing_location_data_')
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(rfq_manufacturing_location_data, values)
        assert val is True
        # select_name = rfq_manufacturing_loc_select[1] + f'[{index}]'
        select_name = rfq_manufacturing_loc_select[1].replace('manulocation', index)
        select_dep_loc = replace_in_tuple(rfq_manufacturing_loc_select, 1, select_name)
        self.manufacturing_location = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_company_priority(self, browser, index=2):
        do_click(browser, rfq_company_priority_loc)
        values = get_list_of_elems_text(browser, rfq_company_priority_loc_select[0], rfq_company_priority_loc_select[1])
        assert values == rfq_company_priority_dropdown
        select_name = rfq_company_priority_loc_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(rfq_company_priority_loc_select, 1, select_name)
        self.company_priority = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_quotation_type(self, browser):
        do_click(browser, rfq_generate_quote_loc)
        self.quotation_type = get_element_text(browser, rfq_generate_quote_loc_select)
        do_click(browser, rfq_generate_quote_loc_select)

    def select_estimates_sop(self, browser):
        todayDate = datetime.today()
        yesterday = todayDate + timedelta(days=8)
        yesterday_formatted_date = yesterday.strftime('%m/%d/%Y')
        self.estimates_sop = yesterday_formatted_date
        do_send_keys(browser, rfq_estimates_sop_loc, yesterday_formatted_date)

    def select_per_annum_volume(self, browser, index=2):
        self.annum_volume = 100
        do_send_keys(browser, annum_vol_txtbox, self.annum_volume)
        do_click(browser, rfq_annum_vol_loc)
        values = get_list_of_elems_text(browser, rfq_annum_vol_loc_select[0], rfq_annum_vol_loc_select[1])
        assert values == rfq_units_dropdown
        select_name = rfq_annum_vol_loc_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(rfq_annum_vol_loc_select, 1, select_name)
        self.annum_volume_unit = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_per_day_volume(self, browser):
        self.day_volume = 10
        do_clear(browser, day_vol_txtbox)
        do_send_keys(browser, day_vol_txtbox, self.day_volume)
        self.day_volume_unit = get_element_text(browser, rfq_day_vol_loc)

    def select_project_life(self, browser, index=3):
        self.project_life_num = 3
        do_send_keys(browser, project_life_txtbox, self.project_life_num)
        do_click(browser, rfq_project_life_loc)
        values = get_list_of_elems_text(browser, rfq_project_life_select[0], rfq_project_life_select[1])
        assert values == rfq_project_life_data
        select_name = rfq_project_life_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(rfq_project_life_select, 1, select_name)
        self.project_life_unit = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_finalizing_date(self, browser):
        todayDate = datetime.today()
        yesterday = todayDate + timedelta(days=4)
        yesterday_formatted_date = yesterday.strftime('%m/%d/%Y')
        self.finalizing_date = yesterday_formatted_date
        do_send_keys(browser, finalize_date_loc, yesterday_formatted_date)

    def select_cft_completion_date(self, browser):
        todayDate = datetime.today()
        yesterday = todayDate + timedelta(days=5)
        yesterday_formatted_date = yesterday.strftime('%m/%d/%Y')
        self.cft_completion = yesterday_formatted_date
        do_send_keys(browser, cft_review_loc, yesterday_formatted_date)

    def select_costing_completion_date(self, browser):
        todayDate = datetime.today()
        yesterday = todayDate + timedelta(days=7)
        yesterday_formatted_date = yesterday.strftime('%m/%d/%Y')
        self.costing_completion = yesterday_formatted_date
        do_send_keys(browser, costing_completed_loc, yesterday_formatted_date)

    def select_offer_validity(self, browser, index=2):
        do_click(browser, rfq_offer_validity_loc)
        values = get_list_of_elems_text(browser, rfq_offer_validity_select[0], rfq_offer_validity_select[1])
        assert values == rfq_offer_validity_data
        select_name = rfq_offer_validity_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(rfq_offer_validity_select, 1, select_name)
        self.offer_validity = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_costing_format(self, browser, index=2):
        do_click(browser, costing_format_loc)
        values = get_list_of_elems_text(browser, costing_format_select[0], costing_format_select[1])
        assert values == rfq_costing_format_data
        select_name = costing_format_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(costing_format_select, 1, select_name)
        self.costing_format = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_currency(self, browser, index=6):
        do_click(browser, currency_loc)
        values = get_list_of_elems_text(browser, currency_select[0], currency_select[1])
        check_common_elements = lambda list1, list2: all(i in list2 for i in list1)
        val = check_common_elements(rfq_currency_data, values)
        assert val is True
        select_name = currency_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(currency_select, 1, select_name)
        self.rfq_currency = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_packaging_cost(self, browser, index=2):
        do_click(browser, packing_cost_loc)
        values = get_list_of_elems_text(browser, packing_cost_select[0], packing_cost_select[1])
        assert values == rfq_cost_packaging_dropdown
        select_name = packing_cost_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(packing_cost_select, 1, select_name)
        self.packaging_cost = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_incoterms(self, browser, index=2):
        do_click(browser, incoterms_loc)
        values = get_list_of_elems_text(browser, incoterms_select[0], incoterms_select[1])
        assert values == rfq_incoterms_data
        select_name = incoterms_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(incoterms_select, 1, select_name)
        self.incoterms = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)

    def select_rfq_shipping_address(self, browser):
        do_click(browser, rfq_shipping)
        self.rfq_shipping_address = get_element_text(browser, rfq_shipping_select)
        do_click(browser, rfq_shipping_select)

    def select_other_info_checkbox(self, browser):
        checkboxes = [roi_chkbox, tect_feas_chkbox, satc_chkbox]
        if os.environ['ENV'] == 'bony':
            checkboxes[0] = compound_feas_chkbox
        for chkbox in checkboxes:
            do_click(browser, chkbox)

    def select_pm_lead(self, browser):
        do_click(browser, pm_lead_loc)
        self.pm_lead = get_element_text(browser, pm_lead_select)
        do_click(browser, pm_lead_select)

    def select_marketing_lead(self, browser):
        do_click(browser, mk_lead_loc)
        self.marketing_lead = get_element_text(browser, mk_lead_select)
        do_click(browser, mk_lead_select)

    def select_development_lead(self, browser):
        do_click(browser, dev_lead_loc)
        self.development_lead = get_element_text(browser, dev_lead_select)
        do_click(browser, dev_lead_select)

    def select_plant_head(self, browser):
        do_click(browser, plant_head_loc)
        self.plant_head = get_element_text(browser, plant_head_select)
        do_click(browser, plant_head_select)

    def select_surface_treatment_head(self, browser):
        do_click(browser, surface_treat_loc)
        self.surface_treatment_head = get_element_text(browser, surface_treat_select)
        do_click(browser, surface_treat_select)

    def select_cft_member(self, browser):
        do_click(browser, cft_member_loc)
        self.cft_member = get_element_text(browser, cft_member_select)
        do_click(browser, cft_member_select)

    def select_business_dev_head(self, browser):
        scroll_into_the_view(browser, dev_head_loc[0], dev_head_loc[1])
        do_click(browser, dev_head_loc)
        self.business_dev_head = get_element_text(browser, dev_head_select)
        do_click(browser, dev_head_select)        

    def verify_heading(self, browser):
        headings = ['Customer Information', 'Business Information', 'Project Details', 'Sample Quantity', 'Timeline',
                    'Costing', 'Logistics', 'Other Information', 'Manager Details']
        for head in headings:
            heading = rfq_heading[1].replace('heading', head)
            heading_loc = replace_in_tuple(rfq_heading, 1, heading)
            scroll_into_the_view(browser, heading_loc[0], heading_loc[1])
            should_be_visible(browser, heading_loc, head)

    def fill_rfq_txt_box(self, browser):
        self.rfq_text_boxes_data = rfq_txtboxes_data
        for txtbox, data in zip(text_boxes.values(), self.rfq_text_boxes_data):
            scroll_into_the_view(browser, txtbox[0], txtbox[1])
            do_send_keys(browser, txtbox, data)

    def select_rfq_toggles(self, browser, assem_type):
        for key, path in rfq_toggles_loc.items():
            scroll_into_the_view(browser, path[0], path[1])
            js_click_by_xpath(browser, path[1])
        if assem_type == 'single':
            st_type = rfq_surface_treatment_loc[1].replace('[1]', '[2]')
            assembly_type_loc = assembly_type_tog_loc[1].replace('[2]', '[1]')
            js_click_by_xpath(browser, assembly_type_loc)
            js_click_by_xpath(browser, st_type)
        else:
            js_click_by_xpath(browser, assembly_type_tog_loc[1])
            js_click_by_xpath(browser, rfq_surface_treatment_loc[1])

    def verify_created_dict(self, browser, all_data_dict: dict, acc_name):
        sleep(2)
        rfq_tabl_loc = rfq_table_row_loc[1].replace("acc_name", acc_name)
        values = get_list_of_elems_text(browser, rfq_table_row_loc[0], rfq_tabl_loc)
        logging.info(values)
        assert len(values) > 0
        all_data = list(all_data_dict.values())
        acc_data_list1 = all_data[0]
        acc_data_list = [acc_data_list1]
        for i in all_data[1:]:
            i_type = type(i)
            if i_type == list:
                acc_data_list.extend(i)
            else:
                acc_data_list.append(str(i))
        logging.info(acc_data_list)
        values = [x for x in values if x != "-"]
        non_present_data = []
        for i in values[1:]:
            for j in acc_data_list:
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
        assert len(non_present_data) <= 9
        self.rfq_id = values[0]


    def verify_selected_managers_data(self, browser):
        do_click(browser, rfq_more_details_btn_loc)
        sleep(2)
        do_click(browser, rfq_details_edit_btn_loc)
        loader_should_be_invisile(browser, 5)
        should_be_visible(browser, manager_details_header_loc, "manager_details_header_loc")
        pm_lead_name = get_element_text(browser, pm_lead_loc)
        assert pm_lead_name == self.pm_lead
        mk_lead_name = get_element_text(browser, mk_lead_loc)
        assert mk_lead_name == self.marketing_lead
        dev_lead_name = get_element_text(browser, dev_lead_loc)
        assert dev_lead_name == self.development_lead
        plant_lead_name = get_element_text(browser, plant_head_loc)
        assert plant_lead_name == self.plant_head
        surface_head_name = get_element_text(browser, surface_treat_loc)
        assert surface_head_name == self.surface_treatment_head
        cft_mem_name = get_element_text(browser, cft_member_loc)
        assert cft_mem_name == self.cft_member
        dev_head_name = get_element_text(browser, dev_head_loc)
        assert dev_head_name == self.business_dev_head


class Drawing_data:

    def __init__(self):
        self.te_link = None
        self.roi_years = None
        self.threed_received_date = None
        self.threed_copy = None
        self.twod_received_date = None
        self.twod_copy = None
        self.drawing_txt_data = None

    def goto_rfq_verify_chart_blink(self, browser, rfq_name):
        rfq_loc = (By.XPATH, f'//a[contains(text(), "{rfq_name}")]')
        logging.info(rfq_name)
        do_click(browser, rfq_loc)
        loader_should_be_invisile(browser, 3)
        diagram_highlight_blink_loc = diagram_highlight_blink[1].replace("Stage", "Drawing")
        diagram_highlight_blink_loc1 = replace_in_tuple(diagram_highlight_blink, 1, diagram_highlight_blink_loc)
        should_be_visible(browser, diagram_highlight_blink_loc1, 'diagram_highlight_blink_loc')

    def add_drawing_data(self, browser):
        do_click(browser, add_drawing_diagram)
        self.drawing_txt_data = [random_correct_name(6, 6,'first_name'), generate_random_five_digit_number(),
                                 generate_random_five_digit_number(), "Automation Testing"]
        for loc, entry in zip(drawing_fields_locs, self.drawing_txt_data):
            do_send_keys(browser, loc, entry)

    def select_2d_soft_copy(self, browser, index=2):
        do_click(browser, twod_soft_copy)
        values = get_list_of_elems_text(browser, twod_soft_copy_select[0], twod_soft_copy_select[1])
        assert values == twod_options
        select_name = twod_soft_copy_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(twod_soft_copy_select, 1, select_name)
        self.twod_copy = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)
        upload_file = upload_soft_copy[1] + '[1]'
        upload_file_loc = replace_in_tuple(upload_soft_copy, 1, upload_file)
        elem = browser.find_element(By.XPATH, upload_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/automation-report.zip')
        copy_received = copy_received_date[1] + '[1]'
        copy_received_loc = replace_in_tuple(copy_received_date, 1, copy_received)
        todayDate = datetime.today()
        yesterday = todayDate - timedelta(days=1)
        self.twod_received_date = yesterday.strftime('%m/%d/%Y')
        do_send_keys(browser, copy_received_loc, self.twod_received_date)

    def select_3d_soft_copy(self, browser, index=2):
        do_click(browser, threed_soft_copy)
        values = get_list_of_elems_text(browser, threed_soft_copy_select[0], threed_soft_copy_select[1])
        assert values == threed_options
        select_name = threed_soft_copy_select[1] + f'[{index}]'
        select_dep_loc = replace_in_tuple(twod_soft_copy_select, 1, select_name)
        self.threed_copy = get_element_text(browser, select_dep_loc)
        do_click(browser, select_dep_loc)
        sleep(0.5)
        upload_file = upload_soft_copy[1] + '[2]'
        upload_file_loc = replace_in_tuple(upload_soft_copy, 1, upload_file)
        elem = browser.find_element(By.XPATH, upload_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/automation-report.zip')
        copy_received = copy_received_date[1] + '[2]'
        copy_received_loc = replace_in_tuple(copy_received_date, 1, copy_received)
        todayDate = datetime.today()
        yesterday = todayDate - timedelta(days=1)
        self.threed_received_date = yesterday.strftime('%m/%d/%Y')
        do_send_keys(browser, copy_received_loc, self.threed_received_date)
        do_click(browser, save_btn)
        sleep(2)

    def add_roi_and_approve(self, browser):
        do_click(browser, add_roi_btn)
        self.roi_years = '5'
        do_send_keys(browser, roi_field_loc, self.roi_years)
        elem = browser.find_element(By.XPATH, roi_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        wait_for_ajax(browser)
        scroll_into_the_view(browser, roi_menu_btn[0], roi_menu_btn[1])
        sleep(0.5)
        try:
            do_click(browser, roi_menu_btn)
            do_click(browser, approve_roi_te)
        except (TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
            sleep(0.5)
            do_click(browser, roi_menu_btn)
            do_click(browser, approve_roi_te)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)

    def add_roi_and_reject(self, browser):
        do_click(browser, add_roi_btn)
        self.roi_years = '5'
        do_send_keys(browser, roi_field_loc, self.roi_years)
        elem = browser.find_element(By.XPATH, roi_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_invisible(browser, add_roi_btn, "add_roi_btn")
        wait_for_ajax(browser)
        scroll_into_the_view(browser, roi_menu_btn[0], roi_menu_btn[1])
        sleep(0.5)
        try:
            do_click(browser, roi_menu_btn)
            do_click(browser, reject_roi_te)
        except (TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
            sleep(0.5)
            do_click(browser, roi_menu_btn)
            do_click(browser, reject_roi_te)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_visible(browser, add_roi_btn, "add_roi_btn")
        should_be_invisible(browser, add_technical_feasibility, "add_technical_feasibility")

    def add_roi_and_revoke(self, browser):
        do_click(browser, add_roi_btn)
        self.roi_years = '5'
        do_send_keys(browser, roi_field_loc, self.roi_years)
        elem = browser.find_element(By.XPATH, roi_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_invisible(browser, add_roi_btn, "add_roi_btn")
        wait_for_ajax(browser)
        scroll_into_the_view(browser, roi_menu_btn[0], roi_menu_btn[1])
        sleep(0.5)
        try:
            do_click(browser, roi_menu_btn)
            do_click(browser, revoke_roi_te)
        except (TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
            sleep(0.5)
            do_click(browser, roi_menu_btn)
            do_click(browser, revoke_roi_te)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_visible(browser, add_roi_btn, "add_roi_btn")
        should_be_invisible(browser, add_technical_feasibility, "add_technical_feasibility")

    def add_technical_feasibility(self, browser):
        do_click(browser, add_technical_feasibility)
        elem = browser.find_element(By.XPATH, tf_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        wait_for_ajax(browser)
        scroll_into_the_view(browser, te_menu_btn[0], te_menu_btn[1])
        sleep(1)
        do_click(browser, te_menu_btn)
        try:
            do_click(browser, approve_roi_te)
        except (TimeoutException, ElementClickInterceptedException):
            do_click(browser, te_menu_btn)
            do_click(browser, approve_roi_te)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        loader_should_be_invisile(browser, 5)
        self.te_link = get_element_text(browser, te_name_link)
        logging.info(self.te_link)
        diagram_highlight_blink_loc = diagram_highlight_blink[1].replace("Stage", "Technical Evaluation")
        scroll_into_the_view(browser, diagram_highlight_blink[0], diagram_highlight_blink_loc)
        diagram_highlight_blink_loc1 = replace_in_tuple(diagram_highlight_blink, 1, diagram_highlight_blink_loc)
        should_be_visible(browser, diagram_highlight_blink_loc1, 'diagram_highlight_blink_loc')

    def add_technical_feasibility_reject(self, browser):
        do_click(browser, add_technical_feasibility)
        elem = browser.find_element(By.XPATH, tf_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_invisible(browser, add_technical_feasibility, "add_technical_feasibility")
        wait_for_ajax(browser)
        scroll_into_the_view(browser, te_menu_btn[0], te_menu_btn[1])
        sleep(1)
        do_click(browser, te_menu_btn)
        try:
            do_click(browser, reject_roi_te)
        except (TimeoutException, ElementClickInterceptedException):
            do_click(browser, te_menu_btn)
            do_click(browser, reject_roi_te)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_visible(browser, add_technical_feasibility, "add_technical_feasibility")
        sleep(5)


    def add_technical_feasibility_revoke(self, browser):
        do_click(browser, add_technical_feasibility)
        elem = browser.find_element(By.XPATH, tf_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        should_be_invisible(browser, add_technical_feasibility, "add_technical_feasibility")
        sleep(2)
        wait_for_ajax(browser)
        scroll_into_the_view(browser, te_menu_btn[0], te_menu_btn[1])
        sleep(1)
        do_click(browser, te_menu_btn)
        try:
            do_click(browser, revoke_roi_te)
        except (TimeoutException, ElementClickInterceptedException):
            do_click(browser, te_menu_btn)
            do_click(browser, revoke_roi_te)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        sleep(2)
        should_be_visible(browser, add_technical_feasibility, "add_technical_feasibility")

    def add_technical_feasibility_as_no(self, browser):
        do_click(browser, add_technical_feasibility)
        elem = browser.find_element(By.XPATH, tf_file_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_click(browser, tech_feasi_is_no_loc, 20)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)
        should_be_visible(browser, add_technical_feasibility, "add_technical_feasibility")
        should_be_invisible(browser, te_menu_btn, "tf_menu_btn")

    def add_compound_feasibility(self, browser):
        do_click(browser, add_compound_feasibility_loc)
        elem = browser.find_element(By.XPATH, compound_cf_sheet_input_loc[1])
        elem.send_keys(os.getcwd() + '/files/Account_List.xlsx')
        sleep(0.4)
        do_click(browser, compound_feas_as_yes_loc, 20)
        do_send_keys(browser, add_comment, 'Test')
        do_click(browser, save_btn)