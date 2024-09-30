#noinspection CucumberPlusUndefinedStep
Feature: Automation Sanity Test Plan Execelleta

  
  @Sanity @Sanity_bony @Sanity_etdev #@TestCI
  Scenario: TC_03 Verify Accounts Tab and New Account creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    Then Verify account creation data
    When Navigate to Accounts tab 5
    Then Verify created account data
    Then Verify accounts table head column

  @Sanity @Sanity_bony @Sanity_etdev #@Test
  Scenario: TC_04 Verify Contacts Tab and New Contact creation
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    Then Verify created contact FE Info
    When Navigate to Contact tab 5
    Then Verify created contact data
    Then Verify contact table head column

  @Sanity @Sanity_bony @Sanity_etdev #@Test
  Scenario: TC_05 Verify Rfq Tab and New Rfq creation Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ single, location Bony Plant Gujarat, Bony Plant Gujarat
    When Navigate to RFQ tab 250
    Then Verify created Rfq data
    Then Verify Rfq table head column

  @Sanity @Sanity_bony @Sanity_etdev  #@Test
  Scenario: TC_06 Create and verify Drawing data and TE data Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ single, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data single, Polymer
    When Create TE data 1, Polymer
    Then Verify TE data
    Then Approve TE all levels, back true level 3 assert True

  @Sanity @Sanity_bony @Sanity_etdev #@Test
  Scenario: TC_07 Create Multi level BOM and approve flow Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ multi, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data multi, Polymer
    When Create TE data 1, Polymer
    When Add sub assembly and its data
    When Create TE data 2, Polymer
    When Add assembly part Compound 1 2
    When Create TE data 3, Polymer
    When Create TE BOP data 1
    When Create TE data 4, Polymer
    When Add assembly part Compound 2 3
    When Create TE data 3, Polymer
    When Create TE BOP data 2
    When Create TE data 4, Polymer
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 3 assert True

  @Sanity @Sanity_bony @Sanity_etdev @Test
  Scenario: TC_08 Create Multi level BOM, create norms and Generate cost approval flow Bony
    Given Login into Excelleta UI
#    When Navigate to Accounts tab 5
#    Then Create an account Polymer
#    When Navigate to Contact tab 5
#    When Create an Contact
#    When Navigate to RFQ tab 250
#    Then Create a RFQ multi, location Bony Plant Gujarat,  Bony Plant Gujarat
#    Then Add Drawing Data Polymer
#    When Edit TE Assembly and fill raw material data multi, Polymer
#    When Create TE data 1, Polymer
#    When Add sub assembly and its data
#    When Create TE data 2, Polymer
#    When Add assembly part Compound 1 2
#    When Create TE data 3, Polymer
#    When Create TE BOP data 1
#    When Create TE data 4, Polymer
#    When Add assembly part Compound 2 3
#    When Create TE data 3, Polymer
#    When Create TE BOP data 2
#    When Create TE data 4, Polymer
#    When Create ST Ops data 3
#    When Create ST Ops data 5
#    Then Approve TE all levels, back false level 4 assert False
#    Then Create norms data
#    Then Generate Costing Data and Norms, Nav direct false
#    When Navigate to Costing Sheet tab 10
#    Then Goto MTE Cost Sheet
#    Then Approve CS all levels
#  Then Verify Cost Raw Material data Raw Material

  @Sanity @Sanity_bony @Sanity_etdev #@Test
  Scenario: TC_09 Create Multi level BOM and reject approval all levels Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ multi, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data multi, Polymer
    When Create TE data 1, Polymer
    When Add sub assembly and its data
    When Create TE data 2, Polymer
    When Add assembly part Compound 1 2
    When Create TE data 3, Polymer
    When Create TE BOP data 1
    When Create TE data 4, Polymer
    When Add assembly part Compound 2 3
    When Create TE data 3, Polymer
    When Create TE BOP data 2
    When Create TE data 4, Polymer
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
    

  @Sanity @Sanity_bony @Sanity_etdev #@Test
  Scenario: TC_11 Create Multi level BOM, Generate cost and all level reject flow Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ multi, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data multi, Polymer
    When Create TE data 1, Polymer
    When Add sub assembly and its data
    When Create TE data 2, Polymer
    When Add assembly part Compound 1 2
    When Create TE data 3, Polymer
    When Create TE BOP data 1
    When Create TE data 4, Polymer
    When Add assembly part Compound 2 3
    When Create TE data 3, Polymer
    When Create TE BOP data 2
    When Create TE data 4, Polymer
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

  @Sanity @Sanity_bony @Sanity_etdev
  Scenario: TC_12 Verify Reject And Revoke Functionality of ROI Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ single, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Reject ROI data
    Then Revoke ROI data

  @Sanity @Sanity_bony @Sanity_etdev
  Scenario: TC_13 Verify Reject And Revoke Functionality OF TF Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ single, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Reject technical feasibility
    Then Revoke technical feasibility

  @Sanity @Sanity_bony @Sanity_etdev
  Scenario: TC_14 Verify Technical Feasibility As No Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ single, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Technical feasibility as No
    

  @Sanity @Sanity_bony @Sanity_etdev
  Scenario: TC_16 Revoke TE and verify Approval History Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ single, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data single, Polymer
    When Create TE data 1, Polymer
    Then Revoke TE and Verify History

  @Sanity @Sanity_bony @Sanity_etdev
  Scenario: TC_17 Create Multi level BOM, Generate cost and revoke flow Bony
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ multi, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data multi, Polymer
    When Create TE data 1, Polymer
    When Add sub assembly and its data
    When Create TE data 2, Polymer
    When Add assembly part Compound 1 2
    When Create TE data 3, Polymer
    When Create TE BOP data 1
    When Create TE data 4, Polymer
    When Add assembly part Compound 2 3
    When Create TE data 3, Polymer
    When Create TE BOP data 2
    When Create TE data 4, Polymer
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Revoke Cost sheet

#  @Test
  Scenario: TC_18 Verify Add Part For Fabric Raw Material type
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ multi, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data multi, Polymer
    When Create TE data 1, Polymer
    When Add sub assembly and its data
    When Create TE data 2, Polymer
    When Add assembly part Fabric 1 2
    When Create TE data 3, Polymer
    When Create TE BOP data 1
    When Create TE data 4, Polymer
    When Add assembly part Fabric 2 3
    When Create TE data 3, Polymer
    When Create TE BOP data 2
    When Create TE data 4, Polymer
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Revoke Cost sheet

  Scenario: TC_19 Verify Add Part For Yarn Raw Material type
    Given Login into Excelleta UI
    When Navigate to Accounts tab 5
    Then Create an account Polymer
    When Navigate to Contact tab 5
    When Create an Contact
    When Navigate to RFQ tab 250
    Then Create a RFQ multi, location Bony Plant Gujarat, Bony Plant Gujarat
    Then Add Drawing Data Polymer
    When Edit TE Assembly and fill raw material data multi, Polymer
    When Create TE data 1, Polymer
    When Add sub assembly and its data
    When Create TE data 2, Polymer
    When Add assembly part Yarn 1 2
    When Create TE data 3, Polymer
    When Create TE BOP data 1
    When Create TE data 4, Polymer
    When Add assembly part Yarn 2 3
    When Create TE data 3, Polymer
    When Create TE BOP data 2
    When Create TE data 4, Polymer
    When Create ST Ops data 3
    When Create ST Ops data 5
    Then Approve TE all levels, back false level 4 assert False
    Then Create norms data
    Then Generate Costing Data and Norms, Nav direct false
    When Navigate to Costing Sheet tab 10
    Then Goto MTE Cost Sheet
    Then Revoke Cost sheet