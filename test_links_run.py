from web_driver.driver import browser
from pytest_bdd import scenarios
from tests.test_links_page import *
from tests.test_templates_page import *
from tests.test_assertion import *
from tests.test_login import *
from tests.test_mod_header import *
import pytest


scenarios('feature_files/test_links_scenarios.feature')