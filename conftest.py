import pdb
import sys
import time

import pytest
import os
import requests
from requests.exceptions import MissingSchema

from helpers.common_helpers import slack_message
from global_libs.config import *


class TestResult:
    failed: int
    passed: int
    skipped: int


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    This function takes information from BrowserStack or from GotLab worker and returns execution results on Slack
    Returns:
        Report sent to Slack (test_automation channel)
    """
    yield
    try:
        Browser = os.environ['browser']
        url = os.environ['url']
        if Browser == "headless_chrome":
            if hasattr(terminalreporter.config, 'workerinput'):
                return
            passed_report = []
            failed_report = []
            if int(exitstatus) == 0:
                color_bar = "#00FF00"
                for passed in terminalreporter.stats.get('passed', []):
                    passed_report.append('Passed!')
                    passed_report.append(str(passed.nodeid.split(':')[-1].split(' ')[0]))
                    passed_report.append('Duration: ' + str(passed.duration / 60) + 'mins')
                passed_report_str = ('\n'.join(passed_report))
                slack_message('Smoke Test Report', passed_report_str, color_bar, environment=url)
            else:
                color_bar = "#FF0000"
                for passed in terminalreporter.stats.get('passed', []):
                    failed_report.append('Passed!')
                    failed_report.append(str(passed.nodeid.split(':')[-1].split(' ')[0]))
                    failed_report.append('Duration: ' + str(passed.duration / 60) + 'mins')
                for failed in terminalreporter.stats.get('failed', []):
                    failed_report.append('Failed!')
                    failed_report.append(str(failed.nodeid.split(':')[-1].split(' ')[0]))
                    failed_report.append('Duration: ' + str(failed.duration / 60) + 'mins')
                    failed_report.append(str(failed.longreprtext))
                failed_report_str = ('\n'.join(failed_report))
                slack_message('Smoke Test Report', failed_report_str, color_bar, environment=url)
        else:
            executor_file = []
            for passed in terminalreporter.stats.get('passed', []):
                executor_file.append(str(passed.nodeid.split(':')[0]))
            for failed in terminalreporter.stats.get('failed', []):
                executor_file.append(str(failed.nodeid.split(':')[0]))
            for skipped in terminalreporter.stats.get('skipped', []):
                executor_file.append(str(skipped.nodeid.split(':')[0]))
            if executor_file[0] == 'test_links_run.py':
                if hasattr(terminalreporter.config, 'workerinput'):
                    return
                try:
                    browserstack_url_creds = os.environ.get("BROWSERSTACK").split('@')[0]
                    bs_resp = requests.get(
                        f'{browserstack_url_creds}@api.browserstack.com/automate/builds.json?limit=1')
                except MissingSchema:
                    browserstack_url_creds_def = os.environ.get("BROWSERSTACK_DEF").split('@')[0]
                    bs_resp = requests.get(
                        f'{browserstack_url_creds_def}@api.browserstack.com/automate/builds.json?limit=1')
                bs_resp_json = bs_resp.json()[0]
                hashed_id = bs_resp_json['automation_build']['hashed_id']
                bs_url = f'https://automate.browserstack.com/dashboard/v2/builds/{hashed_id}'
                test_duration = bs_resp_json['automation_build']['duration'] / 60
                test_result = TestResult()
                test_result.failed = len(terminalreporter.stats.get('failed', []))
                test_result.passed = len(terminalreporter.stats.get('passed', []))
                total_no_of_tests = int(test_result.passed) + int(test_result.failed)
                passed_report = []
                failed_report = []
                time.sleep(1)
                if True:
                    color_bar = "#FF0000"
                    failed_report.append(
                        f'Test Scenarios Passed:  {test_result.passed}' + f' Out of {total_no_of_tests}'
                        + ' :tada:')
                    failed_report.append('Duration of all Scenarios: ' + str(test_duration) + ' mins')
                    failed_report.append('Go to BS Build Dashboard: ' + f'<{bs_url}|BS Build Link>')
                    for failed in terminalreporter.stats.get('failed', []):
                        failed_report.append('Failed!')
                        failed_report.append(str(failed.nodeid.split(':')[-1].split(' ')[0]))
                        failed_report.append('Duration: ' + str(failed.duration / 60) + 'mins')
                    if 1 != 0:
                        links_no_titles = 'jnjn'
                    else:
                        links_no_titles = 'All links are asserted successfully'
                    failed_report_str = str('\n'.join(failed_report))
                    failed_report_str_final = str(failed_report_str + "\n" + "\n" +
                                                  "Links Titles:" + '\n' + links_no_titles)
                    slack_message(username=f'Promo Links Test Report', text=failed_report_str_final, color=color_bar,
                                  environment=url)
            elif Browser == "browserstack":
                if hasattr(terminalreporter.config, 'workerinput'):
                    return
                try:
                    browserstack_url_creds = os.environ.get("BROWSERSTACK").split('@')[0]
                    bs_resp = requests.get(
                        f'{browserstack_url_creds}@api.browserstack.com/automate/builds.json?limit=1')
                except MissingSchema:
                    browserstack_url_creds_def = os.environ.get("BROWSERSTACK_DEF").split('@')[0]
                    bs_resp = requests.get(
                        f'{browserstack_url_creds_def}@api.browserstack.com/automate/builds.json?limit=1')
                bs_resp_json = bs_resp.json()[0]
                hashed_id = bs_resp_json['automation_build']['hashed_id']
                bs_url = f'https://automate.browserstack.com/dashboard/v2/builds/{hashed_id}'
                # bs_build_name = bs_resp_json['automation_build']['name']
                # bs_name_split = bs_build_name.split(' ')[:3]
                # build_name = ' '.join(bs_name_split)
                ci_build_name = os.environ.get('CI_JOB_NAME')
                test_duration = bs_resp_json['automation_build']['duration'] / 60
                test_result = TestResult()
                test_result.failed = len(terminalreporter.stats.get('failed', []))
                test_result.passed = len(terminalreporter.stats.get('passed', []))
                test_result.skipped = len(terminalreporter.stats.get('skipped', []))
                total_no_of_tests = int(test_result.passed) + int(test_result.failed) + int(test_result.skipped)
                passed_report = []
                failed_report = []
                if int(exitstatus) == 0:
                    color_bar = "#00FF00"
                    passed_report.append(f'Test Scenarios Passed:  {test_result.passed}' + '  ' + f'skipped: '
                                                                                                  f'{test_result.skipped}' +
                                         f' Out of {total_no_of_tests}' + ' :tada:')
                    passed_report.append('Duration of all Scenarios: ' + str(test_duration) + ' mins')
                    passed_report.append('Go to BS Build Dashboard: ' + f'<{bs_url}|BS Build Link>')
                    passed_report_str = ('\n'.join(passed_report))
                    slack_message(ci_build_name, passed_report_str, color_bar, environment=url)
                else:
                    color_bar = "#FF0000"
                    failed_report.append('Go to BS Build Dashboard: ' + f'<{bs_url}|BS Build Link>')
                    failed_report.append('Duration of all Scenarios: ' + str(test_duration) + ' mins')
                    failed_report.append(
                        f'Test Scenarios Passed:  {test_result.passed}' + f' Out of {total_no_of_tests}'
                        + ' :tada:')
                    for failed in terminalreporter.stats.get('failed', []):
                        failed_report.append('Failed!')
                        failed_report.append(str(failed.nodeid.split(':')[-1].split(' ')[0]))
                        failed_report.append('Duration: ' + str(failed.duration / 60) + ' mins')
                    for skipped in terminalreporter.stats.get('skipped', []):
                        failed_report.append('Skipped!')
                        failed_report.append(str(skipped.nodeid.split(':')[-1].split(' ')[0]))
                        failed_report.append('Duration: ' + str(skipped.duration / 60) + ' mins')
                    failed_report_str = ('\n'.join(failed_report))
                    slack_message(ci_build_name, failed_report_str, color_bar, environment=url)
            else:
                pass
    except KeyError:

        pass


# pytest plugin hook
# def pytest_sessionfinish(session, exitstatus):
#     """executes after whole test run finishes."""
#     Browser = os.environ['browser']
#     if Browser == "headless_chrome":
#         session.config.pluginmanager.get_plugin('terminalreporter')
#     else:
#         pass


def pytest_sessionstart(session):
    get_env()


def pytest_configure(config):
    var1 = os.getenv('main_url')
    pytest.main_url = var1
    # vars_dict = {'main_url': var1}
    # return vars_dict
