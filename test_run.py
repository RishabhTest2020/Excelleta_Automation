from global_libs.driver import browser
from pytest_bdd import scenarios
from tests.test_login import *
from tests.test_accounts_tab import *
from tests.test_contacts_tab import *

import pytest


scenarios('feature_files/test_scenarios.feature')


