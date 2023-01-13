from selenium.webdriver.common.by import By
from test_data.testdata import *

FB_EMAIL_INPUT = (By.ID, "email")
FB_PASS_INPUT = (By.ID, "pass")
FB_PASS_INPUT2 = (By.XPATH, '//INPUT[@name="pass"]')
FB_CONTINUE_BTN = (By.XPATH, '//*[@data-testid="sec_ac_button"]')
FB_CONTINUE_BTN_ON_APP_REQUEST = (By.XPATH, "//DIV[@aria-label='Continue']")
FB_CONTINUE_AS_VICTORIA = (By.XPATH, '//DIV[@aria-label="Continue as Victoria Promoautom"]')
FB_CONTINUE_AS_VICTORIA_SHORT = (By.XPATH, '//DIV[@aria-label="Continue as Victoria"]')
FB_CONTINUE_AS_KASIA = (By.XPATH, '//DIV[@aria-label="Continue as Kasia Promote"]')
LOGIN_ANOTHER_ACCOUNT = (By.XPATH, '//*[text()="Log in to another account."]')
FB_LOGIN_BTN = (By.ID, "loginbutton")
FB_OK_BTN = (By.XPATH, "//BUTTON[@name='__CONFIRM__']")
FB_ACCEPT_COOKIES = (By.XPATH, "//BUTTON[@data-testid='cookie-policy-banner-accept']")
FB_ACCEPT_ALL_COOKIES = (By.XPATH, "//BUTTON[@data-testid='cookie-policy-manage-dialog-accept-button']")
COOKIES_ALLOW = (By.XPATH, '//*[text()="Allow All Cookies"]')
IG_BUSINESS_POPUP_ALL_ASSETS = (By.XPATH, '//div[@class="_8ci9"]')
IG_BUSINESS_POPUP_NEXT_BTN = (By.XPATH, '(//div[@aria-label="Next"])[1]')
IG_BUSINESS_POPUP_DONE_BTN = (By.XPATH, '(//div[@aria-label="Done"])[1]')
IG_BUSINESS_POPUP_OK_BTN = (By.XPATH, '(//div[@aria-label="OK"])[1]')

#  Twitter locators

TWIT_EMAIL_TXT = (By.XPATH, '//INPUT[@id="username_or_email"]')
TWIT_PASS_TXT = (By.XPATH, '//INPUT[@id="password"]')
TWIT_AUTHIRIZE_BTN = (By.XPATH, '//INPUT[@class="submit button selected"]')
TWIT_CHALLENGE = (By.XPATH, '//INPUT[@id="challenge_response"]')
TWIT_CHALLENGE_SUBMIT = (By.XPATH, '//INPUT[@id="email_challenge_submit"]')
TWIT_AUTHIRIZE_APP = (By.XPATH, '//INPUT[@value="Authorize app"]')
TWIT_NEW_POPUP_LOGIN_INPUT = (By.XPATH, '//INPUT[@name="text"]')
TWIT_NEXT_BTN = (By.XPATH, '//SPAN[contains(text(),"Next")]')
TWIT_NEW_POPUP_PASS_INPUT = (By.XPATH, '//INPUT[@name="password"]')
TWIT_NEW_LOGIN_BTN = (By.XPATH, '//SPAN[contains(text(),"Log in")]')

# LinkedIn locators

LI_EMAIL_TXT = (By.XPATH, '//INPUT[@id="username"]')
LI_PASS_TXT = (By.XPATH, '//INPUT[@id="password"]')
LI_SIGN_IN_BTN = (By.XPATH, '//BUTTON[@data-litms-control-urn="login-submit"])')
LI_ALLOW_BTN = (By.XPATH, '//BUTTON[@id="oauth__auth-form__submit-btn"]')


# Shopify locators
SHOPIFY_EMAIL_INPUT = (By.XPATH, '//input[@id="account_email"]')
SHOPIFY_CONTINUE_WITH_EMAIL = (By.XPATH, '//button[@data-bind-disabled="captchaDisabled"]')
SHOPIFY_CONTINUE_WITH_FB = (By.XPATH, '//span[normalize-space()="Continue with Facebook"]')
SHOPIFY_PASS_INPUT = (By.XPATH, '//input[@id="account_password"]')
SHOPIFY_ADMIN_APPS = (By.XPATH, '//span[normalize-space()="Apps"]')
SHOPIFY_ADMIN_APP_TEST01 = (By.XPATH, '//div[contains(text(),"Promo.com (test01)")]')
SHOPIFY_ADMIN_APP_TEST02 = (By.XPATH, '//div[contains(text(),"Promo.com (test02)")]')
SHOPIFY_ADMIN_APP_TEST03 = (By.XPATH, '//div[contains(text(),"Promo.com (test03)")]')
SHOPIFY_ADMIN_APP_TEST04 = (By.XPATH, '//div[contains(text(),"Promo.com (test04)")]')
SHOPIFY_ADMIN_APP_TEST05 = (By.XPATH, '//div[contains(text(),"Promo.com (test05) Test")]')
SHOPIFY_ADMIN_APP_POLAND01 = (By.XPATH, '//div[contains(text(),"Promo.com (poland01) Test")]')
SHOPIFY_ADMIN_APP_STAGING = (By.XPATH, '//div[contains(text(),"Promo.com (staging)")]')
SHOPIFY_ADMIN_APP_PROD = (By.XPATH, '//div[contains(text(),"Promo.com - Promo Video Maker")]')
SHOPIFY_MYVIDEO_HEADER = (By.XPATH, '//a[normalize-space()="My videos"]')
SHOPIFY_CREATE_NEW_BTN = (By.XPATH, '//button[normalize-space()="Create new"]')
SHOPIFY_WIZARD_MAIN_TITLE = (By.XPATH, '//div[@class="step-details__title"]')
SHOPIFY_LOGO_IN_SHOP = (By.XPATH, '(//img[@alt="Shopify"])[1]')
SHOPIFY_WIZARD_SEARCH_PRODUCT = (By.XPATH, '//input[@placeholder="Search product"]')
SHOPIFY_USERNAME = (By.XPATH, '//div[@class="publish-list-item__username"]')
SHOPIFY_REVIEW_BTN = (By.XPATH, '//button[@class="btn app-button review-button dashboard-tabs__review-btn"]')
SHOPIFY_NO_VIDEOS_TITLE = (By.XPATH, '(//span[@class="no-videos-found__title"])[1]')
SHOPIFY_MAKE_A_VIDEO = (By.XPATH, '//button[normalize-space()="Make a video"]')
SHOPIFY_SAVE_BTN = (By.XPATH, '//div[@class="nav-button editor-page-header__save-btn"]')
SHOPIFY_SAVE_BTN_SAVED_STATE = (By.XPATH, '//div[@class="nav-button editor-page-header__save-btn nav-button--disabled"]')


