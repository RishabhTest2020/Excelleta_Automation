#noinspection CucumberPlusUndefinedStep
Feature: Automation Sanity Test Plan Execelleta


  @Sanity @TestCI
  Scenario: TC_01 Verify Successful login
    Given Login into Excelleta UI


  @Sanity @TestCI
  Scenario: TC_02 Verify login with invalid creds
    Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

  @Sanity @TestCI
  Scenario: TC_03 Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    Then Verify account creation data
    When Navigate to Accounts tab 5
    Then Verify created account data
    Then Verify accounts table head column

  @Sanity #@Test
  Scenario: TC_04 Verify Contacts Tab and New Contact creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    Then Verify created contact FE Info
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
    When Navigate to RFQ tab 20
    Then Create a RFQ single, location 3
    When Navigate to RFQ tab 30
    Then Verify created Rfq data
    Then Verify Rfq table head column

  @Sanity  #@Test
  Scenario: TC_06 Create and verify Drawing data and TE data
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 25
    Then Create a RFQ single, location 3
    Then Add Drawing Data
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data single
    When Create TE data 1
    Then Verify TE data
    Then Approve TE all levels, back true level 3 assert True

  @Sanity #@Test
  Scenario: TC_07 Create Multi level BOM and approve flow B31
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 6
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True

@Sanity #@Test
  Scenario: TC_08 Create Multi level BOM, create norms and Generate cost approval flow
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 3
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Approve CS all levels
#  Then Verify Cost Raw Material data Raw Material

  @Sanity #@Test
  Scenario: TC_09 Create Multi level BOM and reject approval all levels
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 3
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Reject TE, back false level 1 assert True
    Then Clone TE
    Then Reject TE, back false level 2 assert True
    Then Clone TE
    Then Reject TE, back false level 3 assert True
    Then Clone TE
    Then Reject TE, back false level 4 assert True
    Then Clone TE
    Then Approve TE all levels, back false level 4 assert True

  @Sanity #@Test
  Scenario: TC_10 Verify Norms Manufacturing locations navs
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 25
    Then Create a RFQ single, location 3
    When Navigate to RFQ tab 25
    Then Verify Manufacturing Location of Norms

  @Sanity #@Test
  Scenario: TC_11 Create Multi level BOM, Generate cost and all level reject flow
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 3
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Reject CS at level 1, cs reason NA
    Then Generate Costing Data and Norms, Nav direct true
    When Navigate to Costing Sheet tab 5
    Then Goto MTE Cost Sheet
    Then Reject CS at level 2, cs reason NA
    Then Generate Costing Data and Norms, Nav direct true
    When Navigate to Costing Sheet tab 5
    Then Goto MTE Cost Sheet
    Then Reject CS at level 4, cs reason revision
    Then Generate Costing Data and Norms, Nav direct true
    When Navigate to Costing Sheet tab 5
    Then Goto MTE Cost Sheet
    Then Reject CS at level 4, cs reason lost

  @Sanity
  Scenario: TC_12 Verify Reject And Revoke Functionality of ROI
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 30
    Then Create a RFQ single, location 3
    Then Reject ROI data
    Then Revoke ROI data

  @Sanity
  Scenario: TC_13 Verify Reject And Revoke Functionality OF TF
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ single, location 3
    Then Reject technical feasibility
    Then Revoke technical feasibility

  @Sanity
  Scenario: TC_14 Verify Technical Feasibility As No
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ single, location 3
    Then Technical feasibility as No

  # @Sanity @Test
  Scenario: TC_15 Verify Managers data in Edit RFQ
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 25
    Then Create a RFQ single, location 3
    Then Add Drawing Data
    Then Verify Edit Managers Information in RFQ

  @Sanity
  Scenario: TC_16 Revoke TE and verify Approval History
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ single, location 3
    Then Add Drawing Data
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data single
    When Create TE data 1
    Then Revoke TE and Verify History

  @Sanity
  Scenario: TC_17 Create Multi level BOM, Generate cost and revoke flow
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 3
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Revoke Cost sheet


  @Sanity @Test
  Scenario: TC_18 Create Multi level BOM and approve flow Dharhuhera
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 9
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True

  @Sanity #@Test
  Scenario: TC_19 Create Multi level BOM and approve flow Hosur
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 7
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True

  @Sanity #@Test
  Scenario: TC_18 Create Multi level BOM and approve flow Pantnagar3
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location 11
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
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True