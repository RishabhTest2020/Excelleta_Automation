import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd()+"/assets/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("SEO Pages Performance Data").worksheet('Report')
data_sheet = client.open("SEO Pages Performance Data").worksheet('Data')
data = sheet.get_all_records()
events_sheet = client.open("Promo Analytics data").worksheet('Data')
# sheet.delete_rows(3, 103)
# sheet.add_rows(103)
b_plan_pricing = client.open("Copy of Localized Pricing May 2021").worksheet('Pricing 2020')
c_plan_pricing = client.open("Copy of Localized Pricing May 2021").worksheet('Pricing 2021')


def urls_data(row):
    urls = data_sheet.cell(row, 1).value
    return urls


def iterations_data():
    iterations = data_sheet.cell(2, 2).value
    return iterations


def insert_rows(num):
    sheet.insert_rows(row=num, values='NA')


def insert_row():
    sheet.insert_row(index=1, values='NA')


def update_cell(row, col, value):
    sheet.update_cell(row, col, value)


def format_cells(ranges, bg_color, percent, bold_bool):
    sheet.format(ranges, {
                    "backgroundColor": {
                        bg_color: int(percent)
                    },
                    "horizontalAlignment": "CENTER",
                    "textFormat": {
                        "fontSize": 10,
                        "bold": bool(bold_bool)
                    }
                })


def new_insert_rows(num, workbook):
    workbook.insert_rows(row=num, values='NA')


def new_insert_row(workbook):
    workbook.insert_row(index=1, values='NA')


def new_update_cell(workbook, row, col, value):
    workbook.update_cell(row, col, value)


def new_format_cells(workbook, ranges, bg_color, percent, bold_bool):
    workbook.format(ranges, {
                    "backgroundColor": {
                        bg_color: int(percent)
                    },
                    "horizontalAlignment": "CENTER",
                    "textFormat": {
                        "fontSize": 10,
                        "bold": bool(bold_bool)
                    }
                })
