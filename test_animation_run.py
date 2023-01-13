from pytest_bdd import scenarios
from tests.test_animators import *
from tests.test_assertion import *
from web_driver.driver import *
scenarios('feature_files/test_animators_scenarios.feature')