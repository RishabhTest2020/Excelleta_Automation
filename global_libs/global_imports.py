from global_libs.config import *
globalEnvs = global_env_vars()
from global_libs.driver import *
# from helpers.common_helpers import *
from helpers.generator import *
from test_data.testdata import *
from test_data import *
from pytest_bdd import given, when, then, parsers
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from conftest import *


# Locators
from locators.common_locators_file import *
from locators.accounts_tab_locators import *
from locators.contact_tab_locators import *

#pages
from pages.new_login_page import *
from pages.accounts_tab import *
from pages.contacts_tab import *

#tests
from tests.test_login import *
from tests.test_accounts_tab import *
from tests.test_contacts_tab import *




