from selenium.webdriver.common.by import By


accounts_headers_cta = (By.XPATH, '//*[contains(@class, "addAccountCTA")]/button[contains(@class, "settingBtn")][index]')
accounts_head_col = (By.XPATH, '(//span[contains(@class, "ag-header-cell-text")])')
add_accounts_btn = (By.XPATH, '//*[contains(@class, "addAccountCTA")]/button[contains(text(), "Add New Account")]')
acc_basic_info_txt = (By.XPATH, '//h3[contains(text(), "Account Basic Information")]')
cancel_btn = (By.XPATH, '//button[contains(text(), "Cancel")]')
save_btn = (By.XPATH, '//button[contains(text(), "Save")]')
paste_image_loc = (By.XPATH, '//div[contains(@class, "paste-img")]')
acc_name_txtbox = (By.XPATH, '//input[@name="accountName"]')
acc_email_txtbox = (By.XPATH, '//input[@name="accountEmail"]')
acc_website = (By.XPATH, '//input[@name="website"]')
acc_mob_num = (By.XPATH, '//input[@name="mobileNumber"]')
country_dd_loc = (By.XPATH, '//div[contains(@class, "countryFlagCode")]')
country_search_txtbox = (By.XPATH, '//input[contains(@placeholder, "Search Country")]')
acc_landline_txtbox = (By.XPATH, '//input[contains(@name, "mobileNumber")]')
# pan = panNo, start month is * startMonth, RM norms = rmNormsRateTypeId, customer code = customerCode,
# working days = noOfWorkingDays, t&c = terms, business nature = businessNatureIds, domain id = businessDomainIds,
# segment = segmentIds, paymnt = paymentMethodId, payment term = paymentTermId,


payment_details_h3 = (By.XPATH, '//h3[contains(text(), "Payment Details")')
Billing_Address1_h3 = (By.XPATH, '//h3[contains(text(), "Billing Address 1")')
billing_country = (By.XPATH, '(//*[contains(@id, "billingCountry")])')
#  state //*[contains(@id, "billingState")], city = billingCity, address = billingAddress, postal = billingPostalCode
# gst = gstin


shipping_add_yes = (By.XPATH, '//*[contains(text(), "Shipping Address")]/following-sibling::div[contains(@class, "question")]//span[text()= "Yes"]')
primary_add_yes = (By.XPATH, '//*[contains(text(), "Primary Billing")]/following-sibling::div[contains(@class, "question")]//span[text()= "Yes"]')
add_new_billing_btn = (By.XPATH, '//*[contains(text(), " Add New Billing Address ")]')

