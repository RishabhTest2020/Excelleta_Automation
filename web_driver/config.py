import os
import uuid
from datetime import date, datetime
from pytz import reference
from setuptools._distutils.command.build import build

browserstack_url = os.environ.get("BROWSERSTACK")
default_browserstack_url = os.environ.get("BROWSERSTACK_DEF")
global env_url, env, tid
try:
    env = os.environ['url']
    try:
        env_url = env.split("?")[0].split("/")[2]
    except IndexError:
        env_url = env.split("?")[0]
except KeyError:
    pass
global currency_ip
try:
    currency_ip = os.environ.get("CURRENCY_IP")
except KeyError:
    pass

if currency_ip is not None:
    pass
else:
    currency_ip = '135.148.4.33'


def currency_ip_name():
    if currency_ip == '135.148.4.33':
        currency_name = 'USA'
    elif currency_ip == '5.135.110.142':
        currency_name = 'Europe'
    elif currency_ip == '51.75.70.34':
        currency_name = 'Denmark'
    elif currency_ip == '198.244.148.214':
        currency_name = 'UK'
    elif currency_ip == '146.59.14.96':
        currency_name = 'Poland'
    elif currency_ip == '51.79.254.182':
        currency_name = 'Singapore'
    elif currency_ip == '192.99.54.60':
        currency_name = 'Canada'
    elif currency_ip == '139.99.236.163':
        currency_name = 'Australia'
    else:
        currency_name = 'Def Currency'
    return currency_name


global build_name
try:
    build_name_raw = os.getenv("BS_BUILD_NAME")
    build_name = build_name_raw.replace("_", " ").title()
except (NameError, AttributeError) as e:
    pass
try:
    tid = os.environ['TID']
except (NameError, KeyError):
    pass


def today_date():
    """
    Returns current date and time
    """
    dt = date.today()
    ht = datetime.now()
    tz = reference.LocalTimezone()
    time_zone = tz.tzname(ht)
    sanity_date = dt.strftime("%d/%m/%Y") + " " + ht.strftime("%H:%M") + " " + time_zone
    return sanity_date


def short_date():
    """
    Returns current short date
    """
    dt = str(date.today())
    creation_date = 'created' + dt
    return creation_date


# More about capabilities: https://www.browserstack.com/automate/capabilities
try:
    desired_cap = {
        'browserName': 'Chrome',
        'browserVersion': 'latest',
        'bstack:options': {
            "os": "OS X",
            "osVersion": "Monterey",
            'debug': 'True',
            'idleTimeout': '1000',
            'resolution': '1600x1200',
            'projectName': 'Sanity Web',
            'buildName': f'Promo {build_name} {today_date()}' + " " + env + tid + ' ' + currency_ip_name(),
            'seleniumVersion': '4.1.2',
            'maskCommands': 'setValues, getValues, setCookies, getCookies',
            'maskBasicAuth': 'true',
            'seleniumLogs': 'false',
            "consoleLogs": "verbose",
            'hosts': f'{currency_ip} {env_url}'
        }
    }
except NameError:
    try:
        desired_cap = {
            'browserName': 'Chrome',
            'browserVersion': 'latest',
            'bstack:options': {
                "os": "OS X",
                "osVersion": "Monterey",
                'debug': 'True',
                'idleTimeout': '1000',
                'resolution': '1600x1200',
                'projectName': 'Sanity Web',
                'buildName': f'Promo {build_name} {today_date()}' + " " + env + ' ' + currency_ip_name(),
                'seleniumVersion': "4.1.2",
                'maskCommands': 'setValues, getValues, setCookies, getCookies',
                'maskBasicAuth': 'true',
                'seleniumLogs': 'false',
                "consoleLogs": "verbose",
                'hosts': f'{currency_ip} {env_url}',
            }
        }
    except:
        pass

try:
    mob_desired_cap = {
            'browserName': 'Chrome',
            'browserVersion': 'latest',
            'bstack:options': {
                "os": "OS X",
                "osVersion": "Monterey",
                'debug': 'True',
                'idleTimeout': '1000',
                'resolution': '1600x1200',
                'projectName': 'Sanity Web',
                'buildName': f'Promo {build_name} {today_date()}' + " " + env + tid + ' ' + currency_ip_name(),
                'seleniumVersion': "4.1.2",
                'maskCommands': 'setValues, getValues, setCookies, getCookies',
                'maskBasicAuth': 'true',
                'seleniumLogs': 'false',
                "consoleLogs": "verbose",
                'hosts': f'{currency_ip} {env_url}',
            }
        }

except NameError:
    try:
        mob_desired_cap = {
            'browserName': 'Chrome',
            'browserVersion': 'latest',
            'bstack:options': {
                "os": "OS X",
                "osVersion": "Monterey",
                'debug': 'True',
                'idleTimeout': '1000',
                'resolution': '1600x1200',
                'projectName': 'Sanity Web',
                'buildName': f'Promo {build_name} {today_date()}' + " " + env + ' ' + currency_ip_name(),
                'seleniumVersion': "4.1.2",
                'maskCommands': 'setValues, getValues, setCookies, getCookies',
                'maskBasicAuth': 'true',
                'seleniumLogs': 'false',
                "consoleLogs": "verbose",
                'hosts': f'{currency_ip} {env_url}',
            }
        }
    except NameError:
        pass

