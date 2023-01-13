from web_driver.driver import browser, mob_browser
from pytest_bdd import scenarios
from tests.test_login import *
from tests.test_create_page import *
from tests.test_editor_page import *
from tests.test_signup_page import *
from tests.test_links_page import *
from tests.test_pricing_plan import *
from tests.test_my_account_page import *
from tests.test_brand_manager import *
from tests.test_dashboard import *
from tests.test_mobile_view import *
from tests.test_assertion import *
from tests.test_templates_page import *
from tests.test_mod_header import *
from tests.test_mod_header_mobile import *
from tests.test_publisher_page import *
from tests.test_planner_page import *
from tests.test_onboarding import *
import pytest


scenarios('feature_files/test_scenarios.feature')






