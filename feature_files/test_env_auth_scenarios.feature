Feature: Automation Auth Test Plan Test Env BrowserStack


# LOGIN

    Scenario: Successful new Login to the Promo
          Given I name a test new login
          Given I update headers through ModHeader
          Given I have an email
          And I have a password
          When I go to Promo site new
          And I click on login button
          And I enter my email new
          And I enter my password new
          And I press the login button new
          Then I check logged username
          And I should navigated to "Create Page"
          And I check assertion create page

	Scenario: Empty Login fields error
		Given I name a test empty login
		Given I update headers through ModHeader
		Given I have an email
		When I go to Promo site
		And I click on login button
		And I enter my email new
		And I press the login button new
		Then I should get error "This field can’t be empty"
		And I check assertion empty textbox error

	Scenario: Wrong ID and password in login
		Given I name a test wrong login
		Given I update headers through ModHeader
		Given I have an email
		And I have a wrong password
		When I go to Promo site
		And I click on login button
		And I enter my email new
		And I enter a wrong password new
		And I press the login button new
		Then I should get error "Your email or password is incorrect"
		And I check assertion wrong login

	Scenario: Try to login with deleted account
		Given I name test deleted account login
		Given I update headers through ModHeader
		Given I sign up and log in with deleted credentials
		Then I check assertion wrong login



# SIGN UP  / NEW USER

  	Scenario: Verify the new signup process
		Given I name a test signup
		Given I update headers through ModHeader
		When I create a new account new auth
		And I select video preference
		Then I go to my account
		And I delete my account new
		And I check assertion deleted/logged out account

	Scenario: Verify the new fb signup process
		Given I name a test fb signup
		Given I update headers through ModHeader
		When I create a new account new auth with Facebook
		Then I go to my account
		And I disconnect Facebook
		And I delete my account new
		And I check assertion deleted/logged out account
#
#	Scenario: Verify the new google signup process
#		Given I name a test google signup
#		Given I update headers through ModHeader
#		When I create a new account new auth with Google
#		Then I go to my account
#		And I disconnect Google
#		And I delete my account new



# SIGN OUT

	Scenario: Verify the sign out process
		Given I name a test sign out
		Given I update headers through ModHeader
		Given User is logged in with new auth
		Then I sign out
		And I check assertion deleted/logged out account
