from selenium.webdriver.common.by import By


add_contact_btn = (By.XPATH, '//*[contains(@class, "addAccountCTA")]/button[contains(text(), "Add New Contacts")]')
contact_info_txt = (By.XPATH, '//h3[contains(text(), "Contact Information")]')
contact_acc_name = (By.XPATH, '//*[@for="accountName"]/..//input')
contact_acc_name_highlight = (By.XPATH, '//span[@class="highlight-text"]')
name_title = (By.XPATH, '//*[@name="title" ]')
contact_field_txtbox = (By.XPATH, '//*[@id="field_name"]')
# txtbox ids    firstName, lastName, email, mobileNumber, phoneNumber,

select_department = (By.XPATH, '//*[@id="departmentId"]')
select_designation = (By.XPATH, '//*[@id="designationId"]')
select_report_to = (By.XPATH, '//*[@id="reportTo"]')
select_gender = (By.XPATH, '//*[@id="gender"]')
select_date = (By.XPATH, '//input[@placeholder="select Date"]')
select_marital_status = (By.XPATH, '//*[@id="maritalStatus"]')
