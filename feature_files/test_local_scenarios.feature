Feature: Automation Test Plan Prod for Local

# GENERAL

	Scenario: Verify clicking main logo
		When I open pricing page
		Then I click on main logo as not logged in
		Given User is logged in with new auth
		Then I go to my account
		Then I click on main logo as logged in
		When I go to Brand Manager page
		Then I click on main logo as logged in

	Scenario: Check menu and footer links
		When I go to Promo site
		Then I close ModHeader tab
		Then I check main menu links
		And I check footer links

	Scenario: Fully preview a video
		Given User is logged in with shorter new auth
		When I search the video
		When I fully preview a video

# LOGIN

	Scenario: Successful new Login to the Promo
		Given I have an email
		And I have a password
		When I go to Promo site new
		And I click on login button
		And I enter my email new
		And I enter my password new
		And I press the login button new
		Then I check logged username
		And I should navigated to "Create Page"
#
	Scenario: Empty Login fields error
		Given I have an email
		When I go to Promo site new
		And I click on login button
		And I enter my email new
		And I press the login button new
		Then I should get error "This field can’t be empty"

	Scenario: Wrong ID and password in login
		Given I have an email
		And I have a wrong password
		When I go to Promo site
		And I click on login button
		And I enter my email new
		And I enter a wrong password new
		And I press the login button new
		Then I should get error "Your email or password is incorrect"

	Scenario: Try to login with deleted account
		Given I sign up and log in with deleted credentials


# EDITOR

	Scenario: Customize video and publish it
		Given User is logged in with shorter new auth
		When I verify sorting
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
		And I verify play pause buttons and timeline options
		And I add 2nd Caption and change font color
		And I add characters in text animation
		And I am changing font color
		And I am changing text alignment
		And I am changing the font
		And I am changing capitalization style
		And I change text positions
		And I change text style once
		And I am changing ratio
		And I am changing outro background
		And I am going to media tab
#		And I am uploading a video
#		And I select an audio
		When I Publish the video
		Then I go back to editor and discard the changes
		Then I verify pricing/publish navigation

	Scenario: Add media to video and publish it
		Given User is logged in with shorter new auth
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
		And I upload font and add it
		And I upload a watermark and add it
		And I upload a logo and add it
		And I upload an audio and select it
		Then I am adding a new clip
		And I am going to media tab
		And I select a photo and add it
		And I am previewing a photo
		And I am adding a new clip
		Then I am uploading a photo and replacing
		Then I am changing transitions
		And I verify added favourites media
		When I Publish the video
		Then I verify pricing/publish navigation

	Scenario: Create video from uploaded and verify functionalities of publish page
		Given User is logged in with shorter new auth
		When I am uploading a photo on create page
		Then I verify navigation to editor page
		When I Publish the video
		Then I verify pricing/publish navigation
		When I am using download video functionality
		Then verify download functionality for ".mp4"
		When I am using download JPEG image functionality
		Then verify download functionality for ".jpg"
		When I am using download GIF image functionality
		Then verify download functionality for ".gif"
		Then I verify embed functionality
		When I use upload functionality with "wistia"
		When I use upload functionality with "hubspot"
		When I use upload functionality with "dropbox"

	Scenario: Verify Publisher functionalities
		Given User is logged in with shorter new auth
		Then I go to Dashboard Published Tab
		Then I republish the published video
		Then I verify pricing/publish navigation
		Then I verify FB publisher
		Then I verify IG publisher
		Then I verify TWIT publisher

# ONBOARDING

		Scenario:  Verify onboarding basics skip
		When I create a new account new auth shorter
		Then I reach to onboarding first screen
		And I click on no website option
		And I reach to onboarding second screen
		And I click to skip onboarding flow
		And I go to my account
		And I delete my account new

	Scenario:  Verify onboarding basics filled brandfetch
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

# SIGN UP  / NEW USER

	Scenario: Verify the new signup process
		When I create a new account new auth
		And I select video preference
		Then I verify Special Offer button
		And I go to my account
		And I delete my account new

	Scenario: Verify the new fb signup process
		When I create a new account new auth with Facebook
		Then I go to my account
		And I disconnect Facebook
		And I delete my account new

	Scenario: Signup verify premium tags and see pricing
		When I create a new account new auth
		When I select video preference
		When I search the video
		And I am filtering premium videos on create page
		And I customize the video
		Then I verify navigation to editor page new user
		And I am filtering premium videos
#		And I select an audio
		When I Publish the video
		Then I verify pricing/publish navigation new user
		Then I close pricing page
		Then I go to my account
		And I delete my account new

#	Scenario: Verify the new google signup process
#		When I create a new account new auth with Google
#		Then I go to my account
#		And I disconnect Google
#		And I delete my account new

	Scenario: Signup verify editorial tags and see pricing
		When I create a new account new auth
		When I select video preference
		And I am filtering editorial videos and photos on create page
		And I customize the video
		Then I verify navigation to editor page new user
		And I am filtering editorial videos and photos
#		And I select an audio
		When I Publish the video
		Then I verify pricing/publish navigation new user
		Then I close pricing page
		Then I go to my account
		And I delete my account new

	Scenario: New user purchases plan after uploading a watermark
		When I create a new account new auth
		When I select video preference
		When I search the video
		And I customize the video
		Then I verify navigation to editor page new user
		And I upload a watermark and add it
		When I Publish the video
		Then I verify pricing/publish navigation new user
		Then I go to my account
		And I delete my account new

	Scenario: New user purchases plan after adding a brand
		When I create a new account new auth
		When I select video preference
		When I go to Brand Manager page
		When I add first Brand Name
# to_improve: add a purchasing coverage, for now it verifies only the pricing widget
#		And I add Brand components
#		And I create a new project
#		And I search the video
#		And I customize the video
#		Then I verify navigation to editor page new user
#		When I Publish the video
#		Then I verify pricing/publish navigation
		Then I go to my account
		And I delete my account new

# SIGN OUT

	Scenario: Verify the sign out process
		Given User is logged in with shorter new auth
		Then I sign out

# DASHBOARD AND DRAFTS

	Scenario: Verify Drafted video and delete
		Given User is logged in with shorter new auth
		When I goto Drafts page
		Then Initially I delete the project
		And I go to create page
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
#		And I select an audio
		When I Publish the video
		Then I change video name
		When I goto Drafts page
		Then I verify drafted video
		And  I verify draft share buttons
#		And I delete the project

	Scenario: Verify Drafted video and publish
		Given User is logged in with shorter new auth
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
#		And I select an audio
		When I Publish the video
		Then I change video name
		When I goto Drafts page
		Then I verify drafted video
		And I publish drafted video

	Scenario: Edit published video starting from Dashboard
		Given User is logged in with shorter new auth
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
		When I Publish the video
		Then I verify pricing/publish navigation
		Then I make a draft as published on Publish Page
		Then I go to Dashboard Published Tab
		Then I edit published video from Dashboard
		Then I am adding a new clip
		When I Publish the video
		Then I verify pricing/publish navigation

	Scenario: Verify aspect ratio functionalities
		Given User is logged in with shorter new auth
		Then I go to Dashboard Published Tab
		Then I republish the published video
		Then I verify pricing/publish navigation
		When I check the aspect ratio functionalities

# BRAND MANAGER

	Scenario: Verify Brand Manager Functionalities Basic
		Given User is logged in with shorter new auth
		When I go to Brand Manager page
		Then I initially delete brands
		When I add Brand Name
		And I add Brand components
		And I create a new project
		And I search the video
		And I customize the video
		Then I verify navigation to editor page
		Then I select My Brand
#		And I select an audio
		When I Publish the video
		Then I verify pricing/publish navigation
		When I go to Brand Manager page
		Then I delete the brand

	Scenario: Verify Brand Manager Functionalities through Wizard
		Given User is logged in with shorter new auth
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
		And I upload a watermark and add it
		And I upload a logo and add it
		And Goto Brand Manager from Editor page
		Then I initially delete brands
		When I choose brand logo and watermark
		And I create a new project
		And I search the video
		And I customize the video
		Then I verify navigation to editor page
		Then I verify brand logo and watermark synced on editor


# TEMPLATES PAGE

	Scenario: Verify template page without login
      When I go to Promo site
      Then I go to Templates page
      And I change ratios and verify
      And I search templates with valid and invalid keys
      And I customize video and verify redirection to signup page

    Scenario: Verify template page after login
		Given User is logged in with shorter new auth
		Then I go to Templates page
		And I preview template and verify share buttons
		And I go to Templates page
		And I change ratios and verify
		And I search templates with valid and invalid keys
		And I browse templates category and verify breadcrumbs
		And I customize template
		Then I verify navigation to editor page
		And I am changing font color
		And I am changing text alignment
		And I am changing the font
		And I am changing capitalization style
		And I change text positions
		And I change text style once
		And I am changing ratio
#		And I select an audio
		When I Publish the video
		Then I verify pricing/publish navigation


# MY ACCOUNT

	Scenario: Verify password changes
		Given User is logged in with new auth - change pass separate account
		Then I go to my account
		And I change my password
		And I sign out
		And I login with changed password
		And I go to my account
		And I rechange my password
		And I sign out
		And I login with old password

	Scenario: Verify incorrect change of password
		Given User is logged in with shorter new auth
		Then I go to my account
		And I change my password incorrectly

# MOBILE

	Scenario: Verify Magic Link Functionality
		Given Homepage has been opened
		Given User is logged in on mobile browser
		When I click on Start Now
		When I select video and use that

	Scenario: Verify shared video in mobile view
		Given User is logged in with shorter new auth
		Then I go to Dashboard Published Tab
		Then I republish the published video
		Then I verify pricing/publish navigation
		Then I copy video share link
		Then I verify open shared link is playing in mobile view

	Scenario: Promo Performance Tests
		Given I open Promo Pages