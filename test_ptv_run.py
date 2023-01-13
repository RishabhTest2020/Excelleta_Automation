from web_driver.driver import browser
from pytest_bdd import scenarios
from tests.test_login import *
from tests.test_create_page import *
from tests.test_editor_page import *
from tests.test_signup_page import *
from tests.test_pricing_plan import *
from tests.test_my_account_page import *
from tests.test_dashboard import *
from tests.test_assertion import *
from tests.test_templates_page import *
from tests.test_mod_header import *
from tests.test_ptv import *
import pytest


scenarios('feature_files/test_ptv_scenarios.feature')
