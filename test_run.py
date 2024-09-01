from pytest_bdd import scenarios
from tests.test_login import *
from tests.test_accounts_tab import *
from tests.test_contacts_tab import *
from tests.test_rfq_tab import *
from tests.test_te_tab import *
from tests.test_cost_sheet import *

import pytest


scenarios('feature_files/test_scenarios.feature')

# scenarios('feature_files/test_scenarios_bony.feature')

