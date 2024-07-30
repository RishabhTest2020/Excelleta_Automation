Feature: Automation Sanity Test Plan Execelleta


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
    Then Verify account creation data
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
    #Then Verify created contact FE Info
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
    When Navigate to RFQ tab 10
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
    When Navigate to RFQ tab 10
    Then Create a RFQ single
    When Navigate to RFQ tab 30
    Then Add Drawing Data
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data single
    When Create TE data 1
    Then Verify TE data
    Then Approve TE all levels true


  @Sanity
  Scenario: TC_07 Create Multi level BOM
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 15
    Then Create a RFQ multi
    When Navigate to RFQ tab 30
    Then Add Drawing Data
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi
    When Create TE data 1
    When Add sub assembly and its data
    When Create TE data 2
    When Add assembly part 1 2
    When Create TE data 3
    When Create TE BOP data 1
    When Create TE data 4
    When Add assembly part 2 3
    When Create TE data 3
    When Create TE BOP data 2
    When Create TE data 4
    Then Approve TE all levels false
    Then Create norms data


  @Test
Scenario: TC_08 Generate costing data
  Given Login into Excelleta UI
  When Navigate to Accounts tab 5
  Then Create ST Ops data 3