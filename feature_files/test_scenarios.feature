Feature: Automation Smoke Test Plan Prod BrowserStack


  @Sanity
  Scenario: Verify Successful login
    Given Login into Excelleta UI


  @Sanity
  Scenario: Verify login with invalid creds
    Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

  @Sanity
  Scenario: Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab
    Then Create an account
    When Navigate to Accounts tab
    Then Verify created account data
    Then Verify accounts table head column

  @Sanity
  Scenario: Verify Contacts Tab and New Contact creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab
    Then Create an account
    When Navigate to Contact tab
    When Create an Contact
    When Navigate to Contact tab
    Then Verify created contact data
    Then Verify contact table head column

  @Sanity
  Scenario: Verify Rfq Tab and New Rfq creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab
    Then Create an account
    When Navigate to Contact tab
    When Create an Contact
    When Navigate to RFQ tab
    Then Create a RFQ
    When Navigate to RFQ tab
    Then Verify created Rfq data
    Then Verify Rfq table head column