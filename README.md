# Sanity Automation Scripts for Promo.com Web

This a project for web automation of Promo.com and test environments.

Project includes sanity testing paths.

Technology stack: [Python](https://www.python.org/), [Selenium](https://www.selenium.dev/), 
[PyTest](https://docs.pytest.org/en/stable/), [PyTest BDD](https://pypi.org/project/pytest-bdd/).

Page Object Model was used as design pattern with function-based programming. Classes are not implemented in this project.

### Table of contents

1. [Directory structure](#paragraph1)
2. [Local environment setup](#paragraph2)
3. [Access to test environments via Cloudflare](#paragraph3)
4. [Promo Users](#paragraph4)
5. [to_delete and to_improve patterns](#paragraph5)
6. [Run from local device on BrowserStack](#paragraph6)
7. [Run on local device](#paragraph7)
8. [Credentials access](#paragraph8)
9. [BrowserStack credentials - local execution](#paragraph9)
   1. [Solution 1 - environmental variable](#subparagraph9a)
   2. [Solution 2 - add BS credentials in ad hoc way](#subparagraph9b)
   3. [BrowserStack - GitLab execution](#subparagraph9c)
10. [SSL issues](#paragraph10)
11. [GitLab configuration](#paragraph11)
12. [Locators](#paragraph12)
13. [TID parameter](#paragraph13)
14. [Allure Reports](#paragraph14)
15. [Parallel running](#paragraph15)
16. [Different currency](#paragraph16)
17. [Reports on Slack](#paragraph17)
    1. [Sanity reports on Slack](#subparagraph17a)
    2. [Pages performance report on Slack](#subparagraph17b)
18. [Social Calendar](#paragraph18)
19. [How to generate new gmail token](#paragraph19) 
20. [Promo Animation Tests](paragraph20)
21. [List of the available sanity scenarios](#paragraph21)

### Directory structure <a name="paragraph1"></a>

```
.
├── allureport                                          # local folder contained Allure reports
├── assets                                              # local folder contained credentials
├── feature_files                                       # folder contains Gherkin scenarios 
                                                        (different for sanity, smoke, pvg, next, production, test envs etc.)
├── files                                               # assets like logos, plugins, photos
├── helpers                                             # folder contains supporting functions and data generator
├── locators                                            # folder contains locators                                  
├── pages                                               # folder contains page objects and suitable test cases
├── test_data                                           # folder contains test data urls, titles, message and error texts
├── tests                                               # folder contains Gherkin steps for scenarios
├── web_driver                                          # folder contains webdriver and BrowserStack configs
├── conftest.py                                         # the file contains code related to Slack reports
├── requirements.txt                                    # pip requirements file
├── requirements.in                                     # using pip-compile to be compiled to reqirements.txt
├── gitlab-ci.yml                                       # GitLab integration, jobs
├── test_auth_run.py [BS][prod]                         # auth scenarios runner for production - BrowserStack
├── test_cancellation_run.py [BS][test]                 # cancellation scenarios runner for test envs - BrowserStack
├── test_cookies_run.py [prod]                          # cookies scenarios runner for production - Europe only
├── test_editorial_local_run.py [local][prod]           # editorial scenarios runner for production - local
├── test_editorial_run.py [BS][prod]                    # editorial scenarios runner for production - BrowserStack
├── test_env_auth_run.py [BS][test]                     # auth scenarios runner for test environments - BrowserStack
├── test_env_run.py [BS][test]                          # main scenarios runner for test environments - BrowserStack
├── test_links_run.py [BS][prod][test]                  # links scenarios runner for production - BrowserStack
├── test_local_run.py [local][prod]                     # main scenarios runner for production - local
├── test_local_env_run.py [local][test]                 # main scenarios runner for test environments - local
├── test_local_smoke_run.py [local][prod]               # main scenarios runner for smoke tests - local
├── test_onboarding_run.py [test][prod]                 # scenario runner for onboarding suite - only BrowserStack
├── test_performance_run.py [local][prod]               # performance SEO scenarios runner for production - local
├── test_ptv_run.py [BS][prod][test                     # PTV scenarios runner for production and test envs - BrowserStack
├── test_run.py [BS][prod]                              # main scenarios runner for production - BrowserStack
├── test_shopify_local_run.py [local][test][prod]       # runner for Shopify - local environment
├── test_shopify_run.py [BS][test][prod]                # runner for Shopify - BrowserStack
├── test_rendering_run.py [BS][test][prod]              # runner for video generation short scenario - all envs - BrowserStack
├── test_scheduler_run.py [BS][test][prod]              # scenarios runner for publisher/scheduler - BrowserStack
├── test_social_calendar_run.py [BS][prod]              # only prod: social media calendar tests for every day - BrowserStack
├── test_smoke_run.py [BS][prod]                        # main scenarios runner for smoke tests - BrowserStack
├── test_templates_run.py [BS][test]                    # templates scenarios runner for prod and test environments - BrowserStack
└── README.md
```

### Local environment setup <a name="paragraph2"></a>

To use this project Python 3.10. is required.

MacOS
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install pip-tools
pip install -r requirements.txt
```

Windows
```bash
python3.10 -m venv venv
\path\to\env\Scripts\activate
example: C:\Users\Username\venv\Scripts\activate.bat
pip install pip-tools
pip install -r requirements.txt
```

The convention for managing Python dependency is as follows:
- we add the dependency into requirements.in
- we call ```pip-compile``` or ```python3.8 -m piptools compile``` to create requirements.txt
- we commit both files to repository.

To run tests locally Selenium Webdriver is required. 
In this project Selenium Webdriver is managed automatically by 
[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager) and optionally via 
[BrowserStack](https://browserstack.com).
Be sure that you have updated version of [Chrome Browser](https://www.google.com/chrome/) or [Firefox Browser](https://www.mozilla.org/en-US/firefox/browsers/) on your device.


### Access to test environments via Cloudflare <a name="paragraph3"></a>

We are using Cloudflare to hide test environments from the external traffic.
Custom headers with access tokens have been added using Chrome Plugin [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en)
List of test envs: test01, test02, test03, test04, test05, poland01, yellow-php [+ promo.com]
Due to a different domain structure, test06 is not compatible with this code.

### Promo Users <a name="paragraph4"></a>

Promo user and Facebook user is needed to run the scripts.
Default account is: promo.test.automation@gmail.com (both Promo and Facebook).
Password should be added separate, local text file (see "Credentials access" section below).

You can use your own accounts. Be sure that Promo account has plan purchased and brand manager, 
watermark, full HD functionality turned on.


### to_delete and to_improve patterns [PyCharm] <a name="paragraph5"></a>
Two special comment's patterns are used in this repository:
- to_delete: this comment informs that specific part of code should be deleted in future
- to_improve: this comment informs how the specific part of code should be improved 

How to use them for the first time? 
- open the Project Preferences
- open Editor --> TODO
- remove all default patterns
- add two patterns: \bto_delete\b.* and \bto_improve\b.*
- to see all comments with these patterns use TODO tab in PyCharm (at the bottom, next to Terminal tab)

![Patterns TODO](files/patterns_todo.png "Patterns TODO")

### Run from local device on BrowserStack <a name="paragraph6"></a>

Run tests in main project folder

Test Plans:
- **test_auth_run.py** [BS][prod]                         # auth scenarios runner for production - BrowserStack
- **test_cancellation_run.py** [BS][test]                 # cancellation scenarios runner for test envs - BrowserStack
- **test_cookies_run.py** [BS][prod]                    # cookies scenarios runner for prod Europe only - BrowserStack
- **test_editorial_run.py** [BS][prod][test]              # editorial scenarios runner for production and test envs - BrowserStack
- **test_env_auth_run.py** [BS][test]                     # auth scenarios runner for test environments - BrowserStack
- **test_env_run.py** [BS][test]                          # main scenarios runner for test environments - BrowserStack
- **test_links_run.py** [BS][prod][test]                  # links scenarios runner for production - BrowserStack
- **test_onboarding_run.py** [BS][test][prod]             # runner for onboarding suite - BrowserStack
- **test_rendering_run.py** [BS][test][prod]              # runner for video generation short scenario - all envs - BrowserStack
- **test_run.py** [BS][prod]                              # main scenarios runner for production - BrowserStack
- **test_smoke_run.py** [BS][prod]                        # main scenarios runner for smoke tests - BrowserStack
- **test_scheduler_run.py** [BS][test][prod]              # scenarios runner for publisher/scheduler - BrowserStack
- **test_templates_run.py** [BS][test]                    # templates scenarios runner for prod and test environments - BrowserStack
- **test_image_resizer_run.py** [BS][prod][test]          # image resizer scenarios runner for prod and test envs - BrowserStack

[prod] - production scenario
[test] - test env scenario


For all test inside the chosen Test Plan:

```
browser=browserstack BS_BUILD_NAME=[chosen name] url=[chosen url] pytest [test plan name]
```

example:

```
browser=browserstack BS_BUILD_NAME=AUTOM-234 url=https://promo.com/ pytest test_run.py 
```

One chosen test:

```
browser=browserstack BS_BUILD_NAME=[chosen name] url=[chosen url] pytest [test plan name] -k [name of invidual scenario]
```

Multiple chosen test:

```
eg. browser=browserstack BS_BUILD_NAME=[chosen name] url=[chosen url] pytest [test plan name] -k "test_verify_the_new_fb_signup_process or test_verify_template_page_after_login"
```

Multiple chosen test from Gitlab CI:

```
eg. Key: SCENARIO, Value: test_verify_the_new_fb_signup_process or test_verify_template_page_after_login
```

example:

```
browser=browserstack BS_BUILD_NAME=MY-TEST url=https://test03.promo.com/ pytest test_run.py -k test_empty_login_fields_error
```


### Run on local device <a name="paragraph7"></a>

Run tests in main project folder

Test Plans: 
- **test_editorial_local_run.py** [local][prod]            # editorial scenarios runner for production - local
- **test_local_run.py** [local][prod]                      # main scenarios runner for production - local
- **test_local_env_run.py** [local][test]                  # main scenarios runner for test environments - local
- **test_local_smoke_run.py** [local][prod][test]          # main scenarios runner for smoke tests - local
- **test_performance_run.py** [local][prod]                # performance SEO scenarios runner for production - local
- **test_image_resizer_local_run.py** [local][prod][test]  # image resizer scenarios runner for prod and test envs - local
 
For all test inside the Test Plan:

```
browser=[chosen browser] url=[chosen url] pytest [test plan name]
```

example:

```
browser=chrome url=https://promo.com/ pytest test_local_run.py
```

One chosen test:

```
browser=[chosen browser] url=[chosen url] pytest [test plan name] -k [name of invidual scenario]
```

example:

```
browser=firefox url=https://test03.promo.com/ pytest test_local_env_run.py -k test_empty_login_fields_error
```

### Credentials access <a name="paragraph8"></a>

Project uses text files to store credentials - passwords and credit card details.

read_creds function is used to read file line by line and it uses index to read a particular line 

Example:

```
do_send_keys(browser, USER_PASSWORD_TEXTBOX, read_creds(password, 0), 10)
```

Before first use of the code, please create assets folder and add text file with your credentials. 
Add the file path in testdata.py file using global variable (if differs from the default).


Example:

```
password = '/assets/promopass.txt'
```

For now, in the code there are three types of hidden credentials:
Promo account password: /assets/promopass.txt - 1st line
Promo account password (separate account for password changes): /assets/promopass.txt - 2nd line
Facebook password: /assets/promopass.txt - 3rd line
Credit Card data: /assets/card_details.txt


### BrowserStack credentials - local execution <a name="paragraph9"></a>

Browser Stack key is a sensitive data, so should be kept in environmental variable or should be added "ad hoc" inside the command.

#### Solution 1 - environmental variable <a name="subparagraph9a"></a>

To set environmental variables, open:

Bash
```
nano .bash_profile
```
ZSH
```
nano .zshrc
```
and add variable with BrowserStack credentials = so-called hub url.

Example of hub url:

```
https://[your_username]:[your_access_key]@hub-cloud.browserstack.com/wd/hub
```

Variables are case-sensitive and should be added in separate line each.
Assign to a variable using an equals sign = with no blanks around it.
Use quotes when your variable consists of special characters or blanks.

Example:
```
export BROWSERSTACK='https://[your_username]:[your_access_key]@hub-cloud.browserstack.com/wd/hub'
```

BrowserStack key can be obtained on: https://www.browserstack.com/accounts/settings
/under Automate section/.


#### Solution 2 - add BS credentials in ad hoc way <a name="subparagraph9b"></a>

Use regular command with BROWSERSTACK env variable
Example:

```
browser=browserstack BROWSERSTACK=<your hub url> url=https://promo.com BS_BUILD_NAME=Test pytest test_links_run.py -k test_check_menu_and_footer_links
```

#### BrowserStack - GitLab execution <a name="subparagraph9c"></a>

Credentials are set automatically when running tests from GitLab.

How to run only one chosen test from GitLab?

- open CI/CD --> Pipelines
- find the latest develop branch and open it
- open chosen suite (by clicking on the job name, example: sanity_suite_test02)
- fill out variable fields: 
```
key: SCENARIO
value: [name of the test]
```
example:
```
value: test_generate_video_and_publish
```
- click Trigger this manual action

### SSL issues <a name="paragraph10"></a>

If you have a problem with SSL, update Python certificates using:

```
pip install certifi
```

or change https to http


### GitLab configuration <a name="paragraph11"></a>

GitLab configuration is added to gitlab-ci.yml file. 
Test envs and prod executions can be triggered manually from the CI/CD --> Pipelines (develop branch).
Executions are also triggered automatically after web changes.


### Locators <a name="paragraph12"></a>

[Naming convention](https://easyhi.atlassian.net/l/c/PmGXTRce) of locators on front-end can be found in Confluence.

Locators are stored in shared files inside /locators folder.


### TID parameter <a name="paragraph13"></a>

TID is an identifier which we can open some features for a given % of users.

Example: `https://promo.com?tid=100820201` [in general it is a date + 1 or 0]

How to run tests with TID?

- from GitLab: click on chosen job and provide a variable: key = TID, value = ?tid=220320221
- locally: add `TID=?tid=220320221` before pytest command

example: 
```
browser=browserstack url=https://promo.com BS_BUILD_NAME=example_name TID=?tid=220320221 pytest test_run.py
```


### Allure Reports (optional) <a name="paragraph14"></a>
For more detailed reports you can use [Allure Framework](https://docs.qameta.io/allure/)

- install Allure on your computer (see documentation above)
- create directory where test will be stored
- run the test with command

```
[regular command / examples above] --alluredir="[path to the directory]"
```

- verify test reports after running Allure local server 
(reports will be opened in your browser)


```
allure serve [path to the directory]
```


### Parallel running <a name="paragraph15"></a>

For running tests in parallel use [PyTest XDist](https://pypi.org/project/pytest-xdist/)
To send tests to multiple CPUs, use the -n option.
It is allowed to use it locally and on BrowserStack.

Example:

```
browser=chrome url=https://promo.com/ pytest test_local_run.py -n 3
```

### Different currencies <a name="paragraph16"></a>
If you want to run a test with specific currency, add CURRENCY_IP variable

Example:
```
 browser=browserstack url=https://test03.promo.com BS_BUILD_NAME=AUTOM-337 CURRENCY_IP=146.59.14.96 pytest test_env_run.py -k test_signup_verify_editorial_tags_and_see_pricing
```
- US = '135.148.4.33' 
- EU = '5.135.110.142' 
- DE = '51.75.70.34' 
- UK = '198.244.148.214' 
- PL = '146.59.14.96' 
- Singapur = '51.79.254.182' 
- Canada = '192.99.54.60' 
- Australia = '139.99.236.163'

### Merge develop into master job [GitLab] 

- Click on merge-to-master 
- A new pipeline will be created of master
- If new pipeline will not be created of master check logs of execution

### Reports on Slack <a name="paragraph17"></a>

#### Sanity reports on Slack <a name="subparagraph17a"></a>

Reports on Slack are coded in conftest.py 
pytest_terminal_summary covers:
- headless Chrome and BrowserStack executions
- Smoke Test Report, Regular Sanity Report, Links Test Report
- when tests failed, the color is red (#FF0000), when all tests passed, the color is green (#00FF00)
- duration in minutes and number of tests (X of X)
- report contains a direct BrowserStack link to the chosen execution
- data from BrowserStack are fetched from API (api.browserstack.com/automate/builds.json)
- when Links Test fails, the report shows all not-found links 


#### Pages performance report on Slack <a name="subparagraph17b"></a>

Available only for production environment.
The script will open listed URLs 5 times with ajax wait
and fetch DOM complete, response start and navigation start time from DEV tool.
This report will show: 
- BPC (Frontend Performance Calculation: (responseStart - navigationStart)/1000) and 
- FPC (Frontend Performance Calculation: (domComplete - responseStart)/1000).

We will get all the calculations mean value on report and if the value is greater than 1 then it will show red vertical line and if not then green vertical line in Slack notification.


SEO performance report (coming soon)

### Social Calendar <a name="paragraph18"></a>

Social Calendar can be run from GitLab (set for 5 threads) or on local using this command

```
browser=browserstack url=https://promo.com BS_BUILD_NAME=social_cal pytest test_social_calendar_run.py -n 4
```

Social Calendar accepts MONTH variable
- default is a current month
- MONTH - should be value: ```next``` (for a next month) or ```next_to_next``` (for a month +2)

When month is shorter than 31 days, the script will return "This day doesn't exist in current month" result.

Calendar suite user is:
- name: Social Calendar Automate 
- email: promo.test.automation+calendar@gmail.com

### How to generate new gmail token <a name="paragraph19"></a>

It is required for email checking script

Locally: 

- Delete /assets/token.json file
- open get_emails.py and uncomment last lines of the code
- Now run the command ```python helpers/get_emails.py```
- A new window will open, login and click on continue
- If script is running - kill it
- Open get_emails.py and comment last lines of the code
- Now add the new token in git by ```git add assets/* -f```
- Push it to the repo
- Create merge request and merge to develop and master

credentials:
sampletestuser08@gmail.com / pass: promotestuser@08

### Promo Animations Test <a name="paragraph20"></a>

We have a job for that in the "others" stage "promo_animations_test".
As of now, we have 144 animation folders and the script will test all of them.
Since we have so many animations so the test will take less than 2 hours to be completed.

Right now every folder contains 1/3/6/9 JSON files and selecting no. of files path is static, not dynamic, but it will work fine until n unless we will add more animation folders with different files length apart from 1/3/6/9.

We will get two different Slack notifications one is for completion and another is a report which will show whether the animation worked or not and in the notification non-working animation folder's name will be printed.


### List of the available sanity scenarios - production <a name="paragraph21"></a>

test_run.py (test_scenarios.feature)

Scenarios (Sanity):
- test_verify_clicking_main_logo
- test_successful_new_login_to_the_promo 
- test_empty_login_fields_error
- test_wrong_id_and_password_in_login
- test_try_to_login_with_deleted_account
- test_customize_video_and_publish_it
- test_add_media_to_video_and_publish_it 
- test_create_video_from_uploaded_and_publish_it
- test_verify_the_new_signup_process
- test_verify_the_new_fb_signup_process
- test_signup_verify_premium_tags_and_see_pricing
- test_signup_verify_editorial_tags_and_see_pricing 
- test_verify_the_sign_out_process
- test_verify_drafted_video_and_delete 
- test_verify_drafted_video_and_publish
- test_verify_publisher_functionalities
- test_verify_scheduler_functionalities_happy_path
- test_edit_published_video_starting_from_dashboard
- test_verify_brand_manager_functionalities_basic
- test_verify_brand_manager_functionalities_through_wizard
- test_new_user_purchases_plan_after_uploading_a_watermark
- test_new_user_purchases_plan_after_adding_a_brand
- test_verify_template_page_without_login
- test_verify_template_page_after_login
- test_verify_incorrect_change_of_password
- test_verify_password_changes
- test_verify_magic_link_functionality [mobile]
- test_verify_shared_video_in_mobile_view [mobile]
- test_promo_performance_tests
- test_verify_predefined_ratios_on_category_page [only test envs]

Uploads Tests (Wistia, Hubspot...) - requires a refreshed token
- test_create_video_from_uploaded_and_verify_functionalities_of_publish_page

Publisher Suite:
- test_verify_publisher_functionalities
- test_verify_scheduler_functionalities_happy_path
- test_verify_scheduler_functionalities_with_issues
- test_verify_scheduler_edit_and_reschedule
- test_verify_publish_and_schedule_for_YT_and_LI (user: promo.test.automation+socials@gmail.com)
- test_verify_reschedule_YT_and_LI (user: promo.test.automation+socials@gmail.com)
- test_verify_a_new_post_button
- test_verify_post_duplication_and_deletion
- test_verify_duplication_a_published_post_from_planner
- test_verify_duplication_a_scheduled_post_from_planner
- test_verify_create_another_post_from_publish_summary
- test_verify_planner_functionalities_on_mobile [mobile] (user: promo.test.automation+socials@gmail.com)

Cookies Suite:
- test_verify_cookies_bar

Mobile View Suite [mobile]:
- test_verify_magic_link_functionality
- test_verify_shared_video_in_mobile_view
- test_verify_mobile_view_of_image_resizer_after_login
- test_verify_mobile_view_of_image_resizer_without_login
- test_verify_planner_functionalities_on_mobile

Image Resizer Suite:
- test_verify_image_resizer_without_login
- test_verify_image_resizer_after_login
- test_verify_mobile_view_of_image_resizer_after_login [mobile]
- test_verify_mobile_view_of_image_resizer_without_login [mobile]

Onboarding Suite:
- test_verify_onboarding_basics_skip
- test_verify_onboarding_basics_filled_brandfetch
- test_verify_onboarding_without_providing_information
- test_verify_onboarding_with_FB_user 
- test_verify_reaching_to_onboarding_from_templates_page

PTV Suite:
- test_verify_PTV_functionalities

Shopify Suite:
- test_verify_fb_shopify_functionalities (login with a Facebook account to avoid Captcha)