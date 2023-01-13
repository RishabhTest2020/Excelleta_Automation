import json
import os
import requests
import stripe
import datetime
import calendar
import time
from helpers.common_helpers import do_hover, get_element_text
from locators.locators_file import USERNAME_MENU
from test_data.testdata import *
from pages.newcancellation_page import *


try:
    geo_id = os.environ['COUNTRY']
except KeyError:
    geo_id = None


def epoch_date(update_hours):
    """
    returns formatted datetime according to provided hours (to be advanced in stripe)
    """
    import datetime
    dht = datetime.datetime.now()
    day = dht.day
    month = dht.month
    year = dht.year
    hours = dht.hour
    minutes = dht.minute
    seconds = dht.second
    udht = dht + datetime.timedelta(hours=update_hours)
    uday = udht.day
    umonth = udht.month
    uyear = udht.year
    uhours = udht.hour
    uminutes = udht.minute
    useconds = udht.second
    t = datetime.datetime(year, month, day, hours, minutes, seconds)
    ut = datetime.datetime(uyear, umonth, uday, uhours, uminutes, useconds)
    epoch_formatted_date = calendar.timegm(t.timetuple())
    next_day_epoch_formatted_date = calendar.timegm(ut.timetuple())
    print(str(epoch_formatted_date) + "  " + str(next_day_epoch_formatted_date))
    return epoch_formatted_date, next_day_epoch_formatted_date


def login_user(email, domain, password, geo_ip):
    """
    This function fetch authorization token using /services/auth/v1/token API
    """
    cf_headers = {'CF-Access-Client-Id': '352a2f064e280d15bf045a6c9740638c.access',
                  'CF-Access-Client-Secret': '6cd0992b7b60282508def9d038f51f2371c4cf2b1a2ed6d6392868b5e4bfbd4c',
                                             'X-Forwarded-For': f'{geo_ip}'}
    login_api_url = f'{domain}/services/auth/v1/token'
    login = requests.post(login_api_url, headers=cf_headers, json={'email': email,
                                                                   'password': password})
    login_json = login.json()
    # print('Login Cookies:', login.cookies)
    print('Login JSON:', login_json)
    login_cookies = login.cookies
    global login_token
    login_token = login_json['token']
    refresh_token = login_json['refresh_token']
    reporting_token = login_json['reporting_token']
    # print(email, ' logged in with success', today_date())
    return login_token, refresh_token, login_cookies, reporting_token


def stripe_create_customer(customerId):
    """
    advances time for the provided customerId
    """
    global stripe_clock_simulated
    # Stripe api authentication
    stripe_key = os.environ['STRIPE_KEY']
    stripe.api_key = stripe_key
    for i in range(2):
        if i == 0:
            hours = 25
        else:
            hours = 26
        epoch_formatted_date, next_day_epoch_formatted_date = epoch_date(hours)
        # Fetch stripe customer details and get test_clock id
        stripe_customer = stripe.Customer.retrieve(f"{customerId}")
        clock_id = stripe_customer['test_clock']
        # Advance the simulated time
        stripe.test_helpers.TestClock.advance(clock_id, frozen_time=next_day_epoch_formatted_date)
        # Monitor and handle changes
        start_time = time.time()
        while time.time() <= start_time + 50:
            stripe_clock_simulated = stripe.test_helpers.TestClock.retrieve(clock_id)
            stripe_clock_simulated_status = stripe_clock_simulated['status']
            if stripe_clock_simulated_status == 'ready':
                break
        else:
            print(f'Stripe clock simulation error: {stripe_clock_simulated}')
        time.sleep(4)


def get_plan(domain, login_token, auth_cookies):
    """
    this function returns customerId (to be consumed by stripe_create_customer() fx
    """
    get_plans_api = f'{domain}/data/billing/get-plans'
    headers = {
        'CF-Access-Client-Id': '352a2f064e280d15bf045a6c9740638c.access',
        'CF-Access-Client-Secret': '6cd0992b7b60282508def9d038f51f2371c4cf2b1a2ed6d6392868b5e4bfbd4c',
        'accept': '*/*',
        'origin': f'{domain}',
        'authorization': f'Bearer {login_token}',
        'referer': f'{domain}/pricing'
    }
    get_plans_resp = requests.get(get_plans_api, headers=headers, cookies=auth_cookies)
    get_plans_resp_js = get_plans_resp.json()
    customerId = get_plans_resp_js['customerId']
    return customerId


def set_token_auth(domain, email, password):
    geo_ip = os.environ.get("CURRENCY_IP")
    login_token, refresh_token, login_cookies, reporting_token = login_user(f'{email}', domain, password, geo_ip)
    headers = {
        'CF-Access-Client-Id': '352a2f064e280d15bf045a6c9740638c.access',
        'CF-Access-Client-Secret': '6cd0992b7b60282508def9d038f51f2371c4cf2b1a2ed6d6392868b5e4bfbd4c',
        'accept': '*/*',
        'origin': f'{domain}',
        'authorization': f'Bearer {login_token}',
        'X-Forwarded-For': f'{geo_ip}'
    }

    data = {
        'token': f'{login_token}',
        'email': f'{email}'
    }

    cookies = {
        'PromoRefreshToken': f'{refresh_token}',
    }

    set_tokens_response = requests.post(f'{domain}/api/auth/set-tokens', headers=headers, cookies=cookies,
                                        data=data)
    auth_token_cookies = set_tokens_response.cookies
    return login_token, auth_token_cookies


def advance_time_from_stripe_clock(browser):
    """
    this function gets and sets args to stripe_create_customer() fx and advances time from the stripe clock
    """
    domain = os.environ['url']
    do_hover(browser, USERNAME_MENU)
    name = (By.XPATH, '//DIV[@class="email"]')
    email = get_element_text(browser, name)
    fomatted_email = email.strip("\'")
    password = random_password
    login_token, auth_cookies = set_token_auth(domain, fomatted_email, password)
    customerId = get_plan(domain, login_token, auth_cookies)
    stripe_create_customer(customerId)
