Feature: Automation Test Plan Onboarding Popup Prod BrowserStack


	Scenario:  Verify onboarding basics skip
		Given I name a test onboarding skip
		Given I update headers through ModHeader
		When I create a new account new auth shorter
		Then I reach to onboarding first screen
		And I click on no website option
		And I reach to onboarding second screen
		And I click to skip onboarding flow
		And I go to my account
		And I delete my account new
		And I check assertion deleted/logged out account

	Scenario:  Verify onboarding basics filled brandfetch
		Given I name a test onboarding filled
		Given I update headers through ModHeader
		When I create a new account new auth shorter
		Then I reach to onboarding first screen
		And I fill out a website
		And I reach to onboarding second screen
		And I select business type
		And I set country and phone number
		And I mark checkbox
		And I click on start creating
		When I go to Brand Manager page
		Then No brand is added
		And I go to my account
		And I delete my account new
		And I check assertion deleted/logged out account

	Scenario:  Verify onboarding without providing information
		Given I name a test leaving onboarding form empty
		Given I update headers through ModHeader
		When I create a new account new auth shorter
		Then I reach to onboarding first screen
		And I click on no website option
		And I click on start creating
		Then I go to my account
		Then I delete my account new
		Then I check assertion deleted/logged out account

# to_improve currently blocked - upload logo
#	Scenario:  Verify onboarding add logo
#		Given I name a test onboarding add logo
#		Given I update headers through ModHeader
#		When I create a new account new auth shorter
#		Then I reach to onboarding first screen
#		And I click on no website option
#		And I reach to onboarding second screen
#		And I select business type
#		And I set country and phone number
#		And I add logo to onboarding
#		And I mark checkbox
#		And I click on start creating
#		When I go to Brand Manager page
#		Then No brand is added
#		And I go to my account
#		And I delete my account new
#		And I check assertion deleted/logged out account

	Scenario:  Verify onboarding with FB user
		Given I name a test FB user completes onboarding
		Given I update headers through ModHeader
		When I create a new account with Facebook onboarding
		Then I reach to onboarding first screen
		And I fill out a website
		Then I click to replace logo
		Then I delete logo
		Then I click on start creating
		Then I go to my account
		And I disconnect Facebook
		Then I delete my account new
		And I check assertion deleted/logged out account

	Scenario:  Verify reaching to onboarding from templates page
		Given I name a test reaching to onboarding from templates page
		Given I update headers through ModHeader
		When I go to Promo site
		Then I go to Templates page
		And I customize video and verify redirection to signup page
		When I create a new account new auth shorter
		Then I reach to onboarding first screen
		Then I click on no website option
		And I reach to onboarding second screen
		And I click to skip onboarding flow
		And I go to my account
		And I delete my account new
		And I check assertion deleted/logged out account
