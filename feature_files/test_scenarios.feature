Feature: Automation Smoke Test Plan Prod BrowserStack


  @Smoke
  Scenario: Verify Successful login
    Given Login into Excelleta UI


  @Smoke
  Scenario: Verify login with invalid creds
    Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

  @New
  Scenario: Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab
#    Then Verify accounts table head column
    Then Create an account