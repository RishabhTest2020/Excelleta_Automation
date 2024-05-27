from helpers.common_helpers import *
from global_libs.global_imports import *


def add_contacts_data_in_txt_box(browser):
    contact_details = contacts_general_details
    for field_name, data in zip(contacts_create_fields_gen, contact_details):
        acco_field = contact_field_txtbox[1].replace('field_name', field_name)
        acc_field_loc = replace_in_tuple(contact_field_txtbox, 1, acco_field)
        do_send_keys(browser, acc_field_loc, data)
