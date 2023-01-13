Feature: Automation Test Plan for Mobile View BrowserStack

# GENERAL

  	Scenario: Verify Magic Link Functionality
		Given I name mobile funnel
		Given I update headers through ModHeader mob
		Given Homepage has been opened
		Given User is logged in on mobile browser
		When I click on Start Now
		When I select video and use that
		Then I check assertion mobile path

	Scenario: Mobile view basics for not logged
		Given I name a test clean mobile user
		Given I update headers through ModHeader
		When I am logged in with a mobile user
		Given I name not logged on mobile
		Given I update headers through ModHeader mob
		Given Homepage has been opened
		When I click on Try for free
		When I open a hamburger menu
		When I open a social calendar on mobile
		When I open a hamburger menu
		When I open pricing page on mobile
		Then I sign up on mobile
		And I purchase a plan on mobile
		Then I check assertion pricing mobile

	Scenario: Verify shared video in mobile view
		Given I name get video share link
		Given I update headers through ModHeader
		Given User is logged in with shorter new auth
		Then I go to Dashboard Published Tab
		Then I republish the published video
		Then I verify pricing/publish navigation
		Then I copy video share link
		Given Test Completed
		Given I name mobile view shared video test
		Given I update headers through ModHeader mob
		Then I verify open shared link is playing in mobile view
		Then I check assertion video in mobile view

# IMAGE RESIZER

	Scenario: Verify mobile view of image resizer after login
		 Given I name test mobile view of image resizer page after login
		 Given I update headers through ModHeader mob
		 Given User is logged in on mobile browser
		 When I go to image resizer on mobile
		 And I upload the image on mobile image resizer
		 And I select social images on mobile and download
		 Then I log out on mobile
		 And I check assertion logged out on mobile

	Scenario: Verify mobile view of image resizer without login
		 Given I name test mobile view of image resizer page without login
		 Given I update headers through ModHeader mob
		 When I go to image resizer on mobile
		 And I upload the image on mobile image resizer
		 And I select social images on mobile and download
		 Then I verify redirection to the mobile signup page
		 And I check assertion signup on mobile

# PLANNER

# to_improve: uncomment this scenario when BOOST-2268 is fixed
#	Scenario: Verify planner functionalities on mobile
#		Given I name a test planner on mobile phase web
#		Given I update headers through ModHeader
#		Given User is logged in with shorter new auth socials
#		Then User cleaned all scheduled posts
#		Then I go to Dashboard Published Tab
#		Then I republish the published video
#		Then I verify pricing/publish navigation
#		Then I add draft LI
#		Then I schedule a LI post
#		Given Test Completed
#		Given I name a test planner on mobile phase mobile
#		Given I update headers through ModHeader mob
#		Given Homepage has been opened
#		Given Linkedin user is logged in on mobile browser
#		Then I go to Planner on mobile
#		Then I preview and delete a scheduled LI post
#		Then I check assertion of Planner in mobile view