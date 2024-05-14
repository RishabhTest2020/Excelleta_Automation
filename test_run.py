from global_libs.driver import browser
from pytest_bdd import scenarios
from tests.test_login import *
import pytest


scenarios('feature_files/test_scenarios.feature')


