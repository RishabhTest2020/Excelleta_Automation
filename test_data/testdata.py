from helpers.generator import *

accounts_table_header_col = ['Action', 'Account No', 'Account Name', 'Website', 'Email ID', 'Phone Number',
                             'Landline Number', 'Customer Code', 'Business Nature',
                             'Business Domain', 'Payment Method', 'Payment Term', 'Business Segment', 'Address',
                             'Postal Code', 'GSTIN', 'Country', 'State', 'City', 'Created On', 'Last Modified On']

accounts_create_fields_gen = ['accountName', 'accountEmail', 'website', 'mobileNumber',
                              'landlineNumber', 'panNo', 'customerCode', 'noOfWorkingDays']

accounts_general_details = [random_correct_name(1, 6), f'{random_email_generator()}', 'www.testwesite.com',
                            '9090909090', '12345678', 'QWERT1234Y', f'{generate_random_five_digit_number()}', 7]


start_months_data = ['Select Month', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

rm_type_list = ['Select Norms Rate Type', 'Base Rate', 'Landed Rate']