from web_driver.driver import browser
from pytest_bdd import scenarios
from tests.test_assertion import *
from tests.test_mod_header import *
from tests.test_ptv import *
from tests.test_shopify import *
import pytest


scenarios('feature_files/test_shopify_scenarios.feature')