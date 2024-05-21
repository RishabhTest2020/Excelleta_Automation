Feature: Automation Smoke Test Plan Prod BrowserStack


  @Smoke
  Scenario: Verify Successful login
	  Given Login into Excelleta UI

  Scenario: Verify login with invalid creds
      Given Login with invalid creds test@yopmail.com 123test into Excelleta UI

