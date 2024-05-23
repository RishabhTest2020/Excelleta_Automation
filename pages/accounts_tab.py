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
