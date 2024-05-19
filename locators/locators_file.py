from selenium.webdriver.common.by import By

# General
excelleta_logo = (By.XPATH, '//img[contains(@class, "insightLogo") and contains(@src, "org_login_logo.svg")]')
email_text_box = (By.XPATH, '//input[@id="email"]')
password_text_box = (By.XPATH, '//input[@id="password"]')
login_btn = (By.XPATH, '//button[text()="Log In"]')
dashboard_txt = (By.XPATH, '//h2[contains(text(), "Dashboard")]')
loader_loc = (By.XPATH, '//*[contains(@alt, "builder")]')