from global_libs.global_imports import *


@then('Verify accounts table head column')
def acc_head_colm(browser):
    verify_accounts_head_col(browser)


@then('Create an account')
def account_creation(browser):
    create_an_account(browser)

