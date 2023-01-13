from selenium.webdriver.common.by import By

HOME_HAMBURGER_ICON = (By.XPATH, '//SPAN[@class="sidebar__icon"]')
HOME_LOGIN_BTN = (By.XPATH, '//LI[@class="sidebar__item login-btn"]')
HOME_SIGN_OUT_BTN = (By.XPATH, '//span[@class="sidebar__link logout"]')
SIGNUP_BTN = (By.XPATH, '//SPAN[@class="sidebar__link signup"]')
USERNAME_TXT = (By.XPATH, '//INPUT[@type="email"][@placeholder="Email Address"]')
PASSWORD_TXT = (By.XPATH, '//INPUT[@type="password"][@placeholder="Password"]')
LOGIN_BUTTON = (By.XPATH, '//Button[@type="submit"][@class="btn-main section-title"]')
START_NOW_BTN = (By.XPATH, '//BUTTON[@data-qaid="landing_try-for-free_button"]')
SELECT_HEALTH_BTN = (By.XPATH, '//A[text()="Health & Fitness"]')
SELECT_VID_BTN = (By.XPATH, '//DIV[@class="video-result result-collection"][1]')
USE_THIS_VID_BTN = (By.XPATH, '//BUTTON[@class="btn-main sub-title use-video-btn btn-pink"]')
OPEN_PROMO_EMAIL_PATH = (By.XPATH, '//P[@class="open-from-pc"]')
ACCEPT_MOB_COOKIES = (By.XPATH, '//BUTTON[@data-qaid="cookies_popup_button_agree"]')
SEARCH_BOX_DUMMY = (By.XPATH, '//DIV[@class="input-title-search-btn-container dummy"]/input')
SEARCH_BOX = (By.XPATH, '//H3[@class="medium-title"]/following::div[@class="input-title-search-btn-container"]/input')
SEARCH_SUBMIT_BTN = (By.XPATH, '//BUTTON[@class="btn-main search-overlay-button"][text()="Search"]')
SEARCH_ICON_SUBMIT_BTN = (By.XPATH, '//DIV[@class="input-title-search-btn-container dummy"]/button')
THANK_YOU_GIF = (By.XPATH, '//DIV[@class="wrapper-thank-you-gif"]')
SHARED_VIDEO = (By.XPATH, '//VIDEO[@id="video"]')
SIGNUP_MOB_BTN = (By.XPATH, '//button[@data-qaid="signup_new_btn"]')
SIGNUP_MOB_ON_POPUP = (By.XPATH, '//a[normalize-space()="Sign up"]')
SOCIAL_CALENDAR_FROM_MENU = (By.XPATH, '//a[@class="sidebar__link"][normalize-space()="Calendar"]')
PRICING_FROM_MENU = (By.XPATH, '//a[contains(@class,"sidebar__link")][normalize-space()="Pricing"]')
SOCIAL_CALENDAR_HEADER = (By.XPATH, '//span[@class="calendar-header__nav-date"]')
PRICING_HEADER = (By.XPATH, '//div[contains(@class,"PricingPagePrices")]')

# Pricing on mobile
CHOOSE_BASIC_BTN_MOB = (By.XPATH, '(//div[@class="subscribe"][normalize-space()="Choose Basic"])[2]')
PAYMENT_CARD_IFRAME_MOB_CARD = (By.XPATH, '//iframe[@title="Secure card number input frame"]')
PAYMENT_CARD_IFRAME_MOB_EXP = (By.XPATH, '//iframe[@title="Secure expiration date input frame"]')
PAYMENT_CARD_IFRAME_MOB_CVC = (By.XPATH, '//iframe[@title="Secure CVC input frame"]')
CARD_FIELD_MOB = (By.XPATH, '//INPUT[@name="cardnumber"]')
DATE_EXP_MOB = (By.XPATH, '//INPUT[@name="exp-date"]')
CVC_MOB = (By.XPATH, '//INPUT[@name="cvc"]')
PURCHASE_NOW_MOB = (By.XPATH, '(//button[normalize-space()="Purchase Now"])[1]')
PURCHASED_CURRENT_PLAN = (By.XPATH, '//div[@class="current"]')

# Mobile menu - Image resizer
IR_MOB_FACEBOOK_IMG = (By.XPATH, '(//button[@type="button"])[10]')
IR_MOB_INSTA_IMG = (By.XPATH, '(//button[@type="button"])[71]')
IR_SIGN_OUT_BTN = (By.XPATH, '//a[@class="mobile-header-menu__link"][normalize-space()="Sign Out"]')
IR_HAMBURGER_ICON = (By.XPATH, '//SPAN[@data-qaid="header_mobile_button"]')

# Mobile view of Planner
POST_DESCRIPTION_MOB = (By.XPATH, '//div[@class="post-menu-item-body__text text-body-micro"]')

