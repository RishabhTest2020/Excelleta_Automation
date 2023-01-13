from web_driver.driver import browser
from pytest_bdd import scenarios
from tests.test_templates_page import *
from tests.test_assertion import *
from tests.test_mod_header import *
from tests.test_signup_page import *
from tests.test_onboarding import *
from tests.test_my_account_page import *
from tests.test_brand_manager import *
import pytest


scenarios('feature_files/test_onboarding_scenarios.feature')
