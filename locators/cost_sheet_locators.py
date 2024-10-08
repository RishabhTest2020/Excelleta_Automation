from selenium.webdriver.common.by import By

cost_section_headers_loc = (By.XPATH, '//h2[contains(text(), "section_name")]/..//div[@ref="gridHeader"]')
cost_section_rows_loc = (By.XPATH, '//h2[contains(text(), "section_name")]/..//div[@role="gridcell"]')
cost_send_for_approval_loc = (By.XPATH, '//span[contains(text(), "Send For Approval")]')
cost_approval_history_loc = (By.XPATH, '(//span[contains(text(), "Approval History")])')
cost_approve_btn_loc = (By.XPATH, '//span[contains(text(), "Approve")]')
cost_send_customer_for_approval = (By.XPATH, '//span[contains(text(), "Send Customer")]')
select_cost_sheet_loc = (By.XPATH, '(//a[contains(text(), "mte_name")]/../../..//a)[1]')

#Cost_Sheet_Actions
generate_costing_bn_loc = (By.XPATH, '//*[contains(@class,"main-row")]//*[contains(text(),"Generate Costing")]')
costing_mte_loc = (By.XPATH, '//button[contains(@title, "MTE")]')
cs_actions_btn_loc = (By.XPATH, '//*[contains(@class,"floating-label") and normalize-space(text())="Actions"]')
cs_actions_norms_btn_loc = (By.XPATH, '//*[contains(@class,"norms-btn") and normalize-space(text())="Norms"]')
cs_actions_norms_header_loc = (By.XPATH, '//*[contains(@class,"floating_modal")]//*[normalize-space(text())="Norms Section"]')
norms_fiscal_year_loc = (By.XPATH, '(//*[contains(@name, "normsFiscalYear")])')
norms_fiscal_year_options = (By.XPATH, '(//*[contains(@name, "normsFiscalYear")]/option)')
cs_rm_norms_date_range = (By.XPATH, '(//*[contains(@name, "rmNormsDateRange")])')
cs_rm_norms_date_range_options = (By.XPATH, '(//*[contains(@name, "rmNormsDateRange")]/option)')
cs_bop_norms_date_range = (By.XPATH, '(//*[contains(@name, "bopNormsDateRange")])')
cs_bop_norms_date_range_options = (By.XPATH, '(//*[contains(@name, "bopNormsDateRange")]/option)')
cs_process_norms_date_range = (By.XPATH, '(//*[contains(@name, "processNormsDateRange")])')
cs_process_norms_date_range_options = (By.XPATH, '(//*[contains(@name, "processNormsDateRange")]/option)')
cs_other_norms_date_range = (By.XPATH, '(//*[contains(@name, "otherNormsDateRange")])')
cs_other_norms_date_range_options = (By.XPATH, '(//*[contains(@name, "otherNormsDateRange")]/option)')
cs_over_heads_select_loc = (By.XPATH, '//*[contains(text(),"Over Heads")]/following::ng-multiselect-dropdown')
cs_over_heads_options_loc = (By.XPATH, '(//*[contains(text(),"Over Heads")]/following::ng-multiselect-dropdown//li)')
generate_costing_btn_loc = (By.XPATH, '//*[contains(@value, "Generate Costing ")]')
cs_add_expense_btn_loc = (By.XPATH, '//*[contains(@class, "expense-btn") and normalize-space(text()) = "Add Expenses"]')
cs_add_expense_header_loc = (By.XPATH, '//*[contains(@class, "floating_modal")]//*[normalize-space(text()) = "Add Expenses"]')
cs_ae_rate_type_dropdown_loc = (By.XPATH, '//*[contains(@name,"aeRateType")]')
cs_ae_rate_type_dropdown_options_loc = (By.XPATH, '(//*[contains(@name,"aeRateType")]/option)')
flat_expense_header_loc = (By.XPATH, '//*[contains(@class,"ng-star-inserted")]//*[contains(text(),"Flat Expenses")]')
expense_type_input_loc = (By.XPATH, '//*[contains(@class,"mat-mdc-form-field-infix")]//input')
transport_expense_type_loc = (By.XPATH, '(//mat-option[@role="option"]//span)')
flat_rate_input_loc = (By.XPATH, '//*[contains(text(),"Flat Rate")]/ancestor::div[contains(@class,"applicableFlatRate")]//input')
discount_rate_input_loc = (By.XPATH, '//*[contains(text(),"Discount")]/ancestor::div[contains(@class,"discountPercentage")]//input')
add_update_btn_loc = (By.XPATH, '//*[contains(@class,"addEditAdminExpenses ")]//*[contains(@value,"Add/Update")]')
send_for_approval_btn_loc = (By.XPATH, '//*[contains(@class,"custom-header-btns")]//*[contains(text(), "Send For Approval")]')
cmt_submit_btn_loc = (By.XPATH, '//*[contains(text(), "Submit")]')
send_for_cust_approval_btn_loc = (By.XPATH, '//*[contains(@class,"custom-header-btns")]//*[contains(text(), "Send Customer For Approval")]')
cs_approval_histry_btn_loc = (By.XPATH, '//*[contains(text(), "Approval History")]')
cs_revoke_btn_loc = (By.XPATH, '//*[contains(@class,"custom-header-btns")]//span[contains(text(), "Revoke")]')