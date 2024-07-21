from selenium.webdriver.common.by import By

cost_section_headers_loc = (By.XPATH, '//h2[contains(text(), "section_name")]/..//div[@ref="gridHeader"]')
cost_section_rows_loc = (By.XPATH, '//h2[contains(text(), "section_name")]/..//div[@role="gridcell"]')
cost_send_for_approval_loc = (By.XPATH, '//span[contains(text(), "Send For Approval")]')
cost_approval_history_loc = (By.XPATH, '(//span[contains(text(), "Approval History")])')
cost_approve_btn_loc = (By.XPATH, '//span[contains(text(), "Approve")]')
cost_send_customer_for_approval = By.XPATH, '//span[contains(text(), "Send Customer")]'