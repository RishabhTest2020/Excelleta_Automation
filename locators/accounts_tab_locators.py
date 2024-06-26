from selenium.webdriver.common.by import By


accounts_headers_cta = (By.XPATH, '//*[contains(@class, "addAccountCTA")]/button[contains(@class, "settingBtn")][index]')
accounts_head_col = (By.XPATH, '(//span[contains(@class, "ag-header-cell-text")])')
add_accounts_btn = (By.XPATH, '//*[contains(@class, "addAccountCTA")]/button[contains(text(), "Add New Account")]')
acc_basic_info_txt = (By.XPATH, '//h3[contains(text(), "Account Basic Information")]')
cancel_btn = (By.XPATH, '//button[contains(text(), "Cancel")]')
save_btn = (By.XPATH, '//button[contains(text(), "Save")]')
paste_image_loc = (By.XPATH, '//div[contains(@class, "paste-img")]')
acc_field_txtbox = (By.XPATH, '//input[@name="field_name"]')       #accountName
country_dd_loc = (By.XPATH, '//div[contains(@class, "countryFlagCode")]')
country_search_txtbox = (By.XPATH, '//input[contains(@placeholder, "Search Country")]')
start_month = (By.XPATH, '//select[@id= "startMonth"]')
start_month_list = (By.XPATH, '(//select[@id= "startMonth"]/option)')
rm_norms = (By.XPATH, '//select[@id="rmNormsRateTypeId"]')
rm_norms_options = (By.XPATH, '(//select[@id="rmNormsRateTypeId"]/option)')
tnc_loc = (By.XPATH, '//*[@id="terms"]')
# pan = panNo, start month is * startMonth, RM norms = rmNormsRateTypeId, customer code = customerCode,
# working days = noOfWorkingDays, t&c = terms, business nature = businessNatureIds, domain id = businessDomainIds,
# segment = segmentIds, paymnt = paymentMethodId, payment term = paymentTermId,

business_info_h3 = (By.XPATH, '//h3[contains(text(), "Business Information")]')
business_nature = (By.XPATH, '//*[contains(text(), "Select Business Nature")]')
business_nature_option = (By.XPATH, '(//*[contains(@name, "businessNatureIds")]//input/..)')
business_nature_option_txt = (By.XPATH, '(//*[contains(@name, "businessNatureIds")]//div)')
business_nature_selected = (By.XPATH, '(//*[text()= "Business Nature"]/parent::*//span[@class="selected-item"])')
business_domain = (By.XPATH, '//*[contains(text(), "Select Business Domain")]')
business_domain_option = (By.XPATH, '(//*[contains(@name, "businessDomainIds")]//input/..)')
business_domain_option_txt = (By.XPATH, '(//*[contains(@name, "businessDomainIds")]//div)')
business_domain_selected = (By.XPATH, '(//*[text()= "Business Domain"]/parent::*//span[@class="selected-item"])')
business_segment = (By.XPATH, '//*[contains(text(), "Select Business Segment")]')
business_segment_option = (By.XPATH, '(//*[contains(@name, "segmentIds")]//input/..)')
business_segment_option_txt = (By.XPATH, '(//*[contains(@name, "segmentIds")]//div)')
business_segment_selected = (By.XPATH, '(//*[text()= "Business Segment"]/parent::*//span[@class="selected-item"])')


payment_details_h3 = (By.XPATH, '//h3[contains(text(), "Payment Details")]')
payment_method = (By.XPATH, '//select[@id="paymentMethodId"]')
payment_method_options = (By.XPATH, '(//select[@id="paymentMethodId"]/option)')
payment_term = (By.XPATH, '//select[@id="paymentTermId"]')
payment_term_options = (By.XPATH, '(//select[@id="paymentTermId"]/option)')

Billing_Address1_h3 = (By.XPATH, '//h3[contains(text(), "Billing Address 1")]')
billing_country = (By.XPATH, '(//*[contains(@id, "billingCountry")])')
billing_country_options = (By.XPATH, '(//*[contains(@id, "billingCountry")]/option)')
billing_country_select = (By.XPATH, '//*[contains(@id, "billingCountry")]/option[contains(text(),"country_name")]')
billing_state = (By.XPATH, '(//*[contains(@id, "billingState")])')
billing_state_options = (By.XPATH, '(//*[contains(@id, "billingState")]/option)')
billing_state_select = (By.XPATH, '//*[contains(@id, "billingState")]/option[contains(text(),"state_name")]')
billing_city = (By.XPATH, '(//*[contains(@id, "billingCity0")])')
billing_city_options = (By.XPATH, '(//*[contains(@id, "billingCity0")]/option)')
billing_city_select = (By.XPATH, '//*[contains(@id, "billingCity0")]/option[contains(text(),"city_name")]')
billing_txt_box = (By.XPATH, '(//*[contains(@id, "billingTxtBox")])')

#  state //*[contains(@id, "billingState")], city = billingCity, address = billingAddress, postal = billingPostalCode
# gst = gstin


shipping_add_yes = (By.XPATH, '//*[contains(text(), "Shipping Address")]/following-sibling::div[contains(@class, "question")]//span[text()= "Yes"]')
primary_add_yes = (By.XPATH, '//*[contains(text(), "Primary Billing")]/following-sibling::div[contains(@class, "question")]//span[text()= "Yes"]')
add_new_billing_btn = (By.XPATH, '//*[contains(text(), " Add New Billing Address ")]')

accounts_table_row_loc_a = (By.XPATH, '(//div[@row-index="0"]//*[contains(@class, "ag-cell-value")]//a)')
accounts_table_row_loc = (By.XPATH, '(//div[@row-index="0"]//*[contains(@class, "ag-cell-value")]/span)')

accounts_details_sidebar_rfq = (By.XPATH, '//*[@class="main-content"]//li[contains(text(), "RFQ")]')
accounts_details_rfq_cta = (By.XPATH, '//a[contains(text(), "RFQ")]')

accounts_norms = (By.XPATH, '//button[contains(text(), "Norms")]')
norms_type = (By.XPATH, '(//*[contains(@name, "normsType")])')
norms_type_options = (By.XPATH, '(//*[contains(@name, "normsType"")]/option)')
fiscal_year = (By.XPATH, '(//*[contains(@name, "fiscalYear")])')
fiscal_year_options = (By.XPATH, '(//*[contains(@name, "fiscalYear"")]/option)')
norms_filter = (By.XPATH, '(//*[contains(@name, "normsFilter")])')
norms_filter_options = (By.XPATH, '(//*[contains(@name, "normsFilter"")]/option)')
effective_from = (By.XPATH, '(//*[contains(@for, "effectiveFrom")]/..//input)')
effective_till = (By.XPATH, '(//*[contains(@for, "effectiveTill")]/..//input)')
manuf_location = (By.XPATH, '(//*[contains(@name, "mfgLocation")])')
manuf_location_options = (By.XPATH, '(//*[contains(@name, "mfgLocation"")]/option)')
acc_business_nature = (By.XPATH, '(//*[contains(@name, "accountBusinessNature")])')
acc_business_nature_options = (By.XPATH, '(//*[contains(@name, "accountBusinessNature")]/option)')