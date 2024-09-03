#noinspection CucumberPlusUndefinedStep
Feature: Automation Sanity Test Plan Execelleta


  @Sanity @Sanity_metalman @Sanity_bony @TestCI
  Scenario: TC_01 Verify Successful login
    Given Login into Excelleta UI


  @Sanity @Sanity_metalman @Sanity_bony @TestCI
  Scenario: TC_02 Verify login with invalid creds
    Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

  @Sanity @Sanity_metalman @Sanity_bony #@TestCI
  Scenario: TC_03 Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    Then Verify account creation data
    When Navigate to Accounts tab 5
    Then Verify created account data
    Then Verify accounts table head column

  @Sanity @Sanity_metalman @Sanity_bony #@Test
  Scenario: TC_04 Verify Contacts Tab and New Contact creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    Then Verify created contact FE Info
    When Navigate to Contact tab 5
    Then Verify created contact data
    Then Verify contact table head column

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_05 Verify Rfq Tab and New Rfq creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 20
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    When Navigate to RFQ tab 30
    Then Verify created Rfq data
    Then Verify Rfq table head column

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_06 Create and verify Drawing data and TE data
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 25
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data single, Fabrication
    When Create TE data 1, Fabrication
    Then Verify TE data
    Then Approve TE all levels, back true level 3 assert True

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_07 Create Multi level BOM and approve flow B31
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location B-31, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_08 Create Multi level BOM, create norms and Generate cost approval flow
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Approve CS all levels
#  Then Verify Cost Raw Material data Raw Material

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_09 Create Multi level BOM and reject approval all levels
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
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

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_10 Verify Norms Manufacturing locations navs
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 25
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    When Navigate to RFQ tab 25
    Then Verify Manufacturing Location of Norms

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_11 Create Multi level BOM, Generate cost and all level reject flow
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
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

  @Sanity @Sanity_metalman
  Scenario: TC_12 Verify Reject And Revoke Functionality of ROI
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 30
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    Then Reject ROI data
    Then Revoke ROI data

  @Sanity @Sanity_metalman
  Scenario: TC_13 Verify Reject And Revoke Functionality OF TF
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    Then Reject technical feasibility
    Then Revoke technical feasibility

  @Sanity @Sanity_metalman
  Scenario: TC_14 Verify Technical Feasibility As No
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    Then Technical feasibility as No

  # @Sanity @Sanity_metalman @Test
  Scenario: TC_15 Verify Managers data in Edit RFQ
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 25
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    Then Verify Edit Managers Information in RFQ

  @Sanity @Sanity_metalman
  Scenario: TC_16 Revoke TE and verify Approval History
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ single, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data single, Fabrication
    When Create TE data 1, Fabrication
    Then Revoke TE and Verify History

  @Sanity @Sanity_metalman
  Scenario: TC_17 Create Multi level BOM, Generate cost and revoke flow
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Revoke Cost sheet


  @Sanity @Sanity_metalman #@Test
  Scenario: TC_18 Create Multi level BOM and approve flow Dharhuhera
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Dharuhera, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_19 Create Multi level BOM and approve flow Hosur
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Hosur, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 15
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True

  @Sanity @Sanity_metalman #@Test
  Scenario: TC_20 Create Multi level BOM and approve flow Pantnagar3
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Fabrication
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 35
    Then Create a RFQ multi, location Pantnagar -III, Delhi Corp
    Then Add Drawing Data Fabrication
    When Navigate to Technical Evaluation tab 10
    When Edit TE Assembly and fill raw material data multi, Fabrication
    When Create TE data 1, Fabrication
    When Add sub assembly and its data
    When Create TE data 2, Fabrication
    When Add assembly part Rod/Bar 1 2
    When Create TE data 3, Fabrication
    When Create TE BOP data 1
    When Create TE data 4, Fabrication
    When Add assembly part Rod/Bar 2 3
    When Create TE data 3, Fabrication
    When Create TE BOP data 2
    When Create TE data 4, Fabrication
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert True