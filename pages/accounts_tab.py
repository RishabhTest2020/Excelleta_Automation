import logging

from global_libs.global_imports import *


def verify_accounts_head_col(browser):
    elems = browser.find_elements(accounts_head_col[0], accounts_head_col[1])
    elems_len = len(elems)
    col_names_lst = []
    for i in range(1, elems_len):
        col_name = get_text_by_js_xpath(browser, accounts_head_col[1] + f'[{i}]')
        col_names_lst.append(col_name)
    print(col_names_lst)
    assert accounts_table_header_col == col_names_lst


def add_accounts_data_in_txt_box(browser):
    account_details = accounts_general_details
    for field_name, data in zip(accounts_create_fields_gen, account_details):
        acco_field = acc_field_txtbox[1].replace('field_name', field_name)
        acc_field_loc = replace_in_tuple(acc_field_txtbox, 1, acco_field)
        do_send_keys(browser, acc_field_loc, data)


def select_start_month_field(browser):
    do_click(browser, start_month)
    values = get_list_of_elems_text(browser, start_month_list[0], start_month_list[1])
    assert values == start_months_data
    current_month = datetime.now().month + 1
    select_month = start_month_list[1] + f'[{current_month}]'
    select_month_loc = replace_in_tuple(start_month_list, 1, select_month)
    do_click(browser, select_month_loc)


def select_rm_norms_field(browser, rm_type=1):
    do_click(browser, rm_norms)
    values = get_list_of_elems_text(browser, rm_norms_options[0], rm_norms_options[1])
    assert values == rm_type_list
    select_month = start_month_list[1] + f'[{rm_type}]'
    select_month_loc = replace_in_tuple(start_month_list, 1, select_month)
    do_click(browser, select_month_loc)



def create_an_account(browser):
    do_click(browser, add_accounts_btn)
    should_be_visible(browser, acc_basic_info_txt, 'acc_basic_info_txt')
    add_accounts_data_in_txt_box(browser)
    select_start_month_field(browser)
    select_rm_norms_field(browser)
    do_send_keys(browser, tnc_loc, 'TNC Automation')





