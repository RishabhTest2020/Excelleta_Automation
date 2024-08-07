from selenium.webdriver.common.by import By

# General
excelleta_logo = (By.XPATH, '//img[contains(@class, "insightLogo") and contains(@src, "org_login_logo.svg")]')
email_text_box = (By.XPATH, '//input[@id="email"]')
password_text_box = (By.XPATH, '//input[@id="password"]')
login_btn = (By.XPATH, '//button[text()="Log In"]')
dashboard_txt = (By.XPATH, '//h2[contains(text(), "Dashboard")]')
loader_loc = (By.XPATH, '//*[contains(@alt, "builder")]')
invalid_creds_message = (By.XPATH, '//*[contains(text(), "Login failed. Please check your credentials")]')
menu_tab_loc = '//*[@class= "menuTxt" and contains(text(), "tab_name")]'
pages_name_loc = '//*[contains(@class, "pageName") and contains(text(), "tab_name")]'
default_view_loc = (By.XPATH, '//*[contains(text(), "Default View")]')
rectangle_icon = (By.XPATH, '//*[@class="searchIco icon-rectangleIco"]')
sidebar_button = (By.XPATH, '//nav[@class="sidebar"]//button')
sidebar_hov = (By.XPATH, '//img[@alt="dashboard"]')