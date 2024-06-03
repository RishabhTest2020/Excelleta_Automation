Feature: Automation Smoke Test Plan Prod BrowserStack


  @Smoke
  Scenario: Verify Successful login
    Given Login into Excelleta UI


  @Smoke1
  Scenario: Verify login with invalid creds
    Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

  @Smoke
  Scenario: Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab
    Then Create an account
    Then Verify created account data
    Then Verify accounts table head column

  @New
  Scenario: Verify Contacts Tab and New Contact creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab
    Then Create an account
    When Navigate to Contact tab
    When Create an Contact
    Then Verify created contact data
    Then Verify contact table head column

