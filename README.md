# Sanity Automation Scripts for Excelleta Web

This a project for web automation of Excelleta and test environments.

Project includes sanity testing paths.

Technology stack: [Python](https://www.python.org/), [Selenium](https://www.selenium.dev/), 
[PyTest](https://docs.pytest.org/en/stable/), [PyTest BDD](https://pypi.org/project/pytest-bdd/).

Page Object Model was used as design pattern with function-based programming. Classes are not implemented in this project.

### Table of contents

1. [Directory structure](#paragraph1)
2. [Local environment setup](#paragraph2)
3. [to_delete and to_improve patterns](#paragraph5)
4. [Run from local device on BrowserStack](#paragraph6)
5. [Run on local device](#paragraph7)
6. [Credentials access](#paragraph8)
7. [SSL issues](#paragraph10)
8. [Locators](#paragraph12)
9. [Allure Reports](#paragraph14)
10. [Parallel running](#paragraph15)
11. [List of the available sanity scenarios](#paragraph21)

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
├── gitlab-ci.yml                                       # GitLab integration, jobs                    # PTV scenarios runner for production and test envs - BrowserStack
├── test_run.py                              # main scenarios runner for production - BrowserStack
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
[Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager).
Be sure that you have updated version of [Chrome Browser](https://www.google.com/chrome/) or [Firefox Browser](https://www.mozilla.org/en-US/firefox/browsers/) on your device.


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

[Patterns TODO](files/patterns_todo.png "Patterns TODO")

### Run on local device <a name="paragraph7"></a>

Run tests in main project folder


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


### Command to run tests using Tag and Threads <a name="paragraph15"></a>

For running tests in parallel use [PyTest XDist](https://pypi.org/project/pytest-xdist/)
To send tests to multiple CPUs, use the -n option.
It is allowed to use it locally.
-m should be passed with Tag

Example:

```
pytest test_run.py -m Smoke -n 3
```

