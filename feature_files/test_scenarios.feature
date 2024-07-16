Feature: Automation Smoke Test Plan Prod BrowserStack


  @Sanity @TestCI
  Scenario: TC_01 Verify Successful login
    Given Login into Excelleta UI


  @Sanity
  Scenario: TC_02 Verify login with invalid creds
    Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

  @Sanity
  Scenario: TC_03 Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Accounts tab 5
    Then Verify created account data
    Then Verify accounts table head column

  @Sanity
  Scenario: TC_04 Verify Contacts Tab and New Contact creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to Contact tab 5
    Then Verify created contact data
    Then Verify contact table head column

  @Sanity
  Scenario: TC_05 Verify Rfq Tab and New Rfq creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 5
    Then Create a RFQ single
    When Navigate to RFQ tab 30
    Then Verify created Rfq data
    Then Verify Rfq table head column

  @Sanity
  Scenario: TC_06 Create and verify Drawing data and TE data
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 5
    Then Create a RFQ single
    When Navigate to RFQ tab 30
    Then Add Drawing Data
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data single
    When Create TE data
    Then Verify TE data
    Then Approve TE all levels

#  @Test
  Scenario: Add Norms
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5

  @Test
  Scenario: TC_06 Create and verify Drawing data and TE data
    Given Login into Excelleta UI
    When Navigate to Technical Evaluation tab 10
#    When Edit TE Assembly and fill raw material data multi
    When Add sub assembly and its data
    When Add assembly part
