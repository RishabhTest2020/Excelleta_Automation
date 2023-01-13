from pytest_bdd import when, then, given, scenario, scenarios


def name_a_smoke_test1(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Smoke Scenario New User"}}')


def name_a_smoke_test2(browser):
    browser.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "Smoke Scenario Existing User"}}')