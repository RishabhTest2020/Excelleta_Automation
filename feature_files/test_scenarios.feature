Feature: Automation Test Plan Prod BrowserStack


# GENERAL

	Scenario: Verify UTM on Promo URL
		Given I name a UTM check
		When I open Promo URL and check UTM
		Then I check assertion URL UTM

	Scenario: Verify clicking main logo
		Given I name a test main logo
		When I open pricing page
		Then I click on main logo as not logged in
		Given User is logged in with new auth
		Then I go to my account
		Then I click on main logo as logged in
		When I go to Brand Manager page
		Then I click on main logo as logged in
		And I check assertion main logo as logged

	Scenario: Fully preview a video
		Given I name a test full preview
		Given User is logged in with shorter new auth
		When I search the video
		When I fully preview a video
		Then I check assertion full preview

# LOGIN

	Scenario: Successful new Login to the Promo
		Given I name a test new login
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
		Given I have an email
		When I go to Promo site
		And I click on login button
		And I enter my email new
		And I press the login button new
		Then I should get error "This field can’t be empty"
		And I check assertion empty textbox error

	Scenario: Wrong ID and password in login
		Given I name a test wrong login
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
		Given I sign up and log in with deleted credentials
		Then I check assertion wrong login

# EDITOR

	Scenario: Customize video and publish it
		Given I name a test publish video
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
#		And I select an audio
		And I am changing outro background
		When I Publish the video
		Then I go back to editor and discard the changes
		Then I verify pricing/publish navigation
		And I check assertion publish video

	Scenario: Add media to video and publish it
		Given I name a test add media
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
		And I check assertion publish video

	Scenario: Create video from uploaded photo and verify functionalities of publish page
		Given I name a test create from photo uploaded
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
#		When I use upload functionality with "wistia"
#		When I use upload functionality with "hubspot"
#		When I use upload functionality with "dropbox"
		Then I check assertion publish video

	Scenario: Create video from uploaded video
		Given I name a test create from video uploaded
		Given User is logged in with shorter new auth
		When I create a video from uploaded video
		Then I verify navigation to editor page
		When I Publish the video
		Then I verify pricing/publish navigation
		Then I check assertion publish video

# ONBOARDING

		Scenario:  Verify onboarding basics skip
		Given I name a test onboarding skip
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

# SIGN UP  / NEW USER

	Scenario: Verify the new signup process
		Given I name a test signup
		When I create a new account new auth
		And I select video preference
		Then I verify Special Offer button
		And I go to my account
		And I delete my account new
		And I check assertion deleted/logged out account

	Scenario: Verify the new fb signup process
		Given I name a test fb signup
		When I create a new account new auth with Facebook
		Then I go to my account
		And I disconnect Facebook
		And I delete my account new
		And I check assertion deleted/logged out account

	Scenario: Signup verify premium tags and see pricing
		Given I name a test filters
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
		And I check assertion deleted/logged out account

	Scenario: Signup verify editorial tags and see pricing
		Given I name a editorial test filters
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
		And I check assertion deleted/logged out account

	Scenario: New user purchases plan after uploading a watermark
		Given I name a test purchase a plan for watermark
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
		And I check assertion deleted/logged out account

# to_improve should be uncommented when Google part is done
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
		Given User is logged in with new auth
		Then I sign out
		And I check assertion deleted/logged out account

# DASHBOARD AND DRAFTS

	Scenario: Verify Drafted video and delete
		Given I name a test draft delete
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
		And I check assertion draft deleted

	Scenario: Verify Drafted video and publish
		Given I name a test draft publish
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
		And I check assertion publish video

	Scenario: Edit published video starting from Dashboard
		Given I name a test edit video
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
		Then I check assertion publish video

	Scenario: Verify aspect ratio functionalities
		Given I name a test aspect ratio functionalities
		Given User is logged in with shorter new auth
		Then I go to Dashboard Published Tab
		Then I republish the published video
		Then I verify pricing/publish navigation
		When I check the aspect ratio functionalities
		Then I check assertion publish video

# BRAND MANAGER

	Scenario: Verify Brand Manager Functionalities Basic
		Given I name a test brand manager basic
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
		And I check assertion brand deleted

	Scenario: Verify Brand Manager Functionalities through Wizard
		Given I name a test brand manager wizard
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
		Then I check assertion logo and watermark sync


# TEMPLATES

	Scenario: Verify template page without login
		Given I name test template page without login
		When I go to Promo site
		Then I go to Templates page
		And I change ratios and verify
		And I search templates with valid and invalid keys
		And I customize video and verify redirection to signup page
		And I check assertion signup redirection

	Scenario: Verify template page after login
		Given I name test template page after login
		Given User is logged in with shorter new auth
		Then I go to Templates page
		And I preview template and verify share buttons
		And I go to Templates page
		And I change ratios and verify
		And I search templates with valid and invalid keys
		And I browse templates category and verify breadcrumbs
		And I customize template
		Then I verify navigation to editor page
		And I verify play pause buttons and timeline options
		And I add 2nd Caption and change font color
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
		And I check assertion publish video

# MY ACCOUNT

	Scenario: Verify incorrect change of password
		Given I name a test incorrect password change
		Given User is logged in with shorter new auth
		Then I go to my account
		Then I change my password incorrectly
		And I check assertion changes in my account

	Scenario: Verify password changes
		Given I name a test change password
		Given User is logged in with new auth - change pass separate account
		Then I go to my account
		And I change my password
		And I sign out
		And I login with changed password
		And I go to my account
		And I rechange my password
		And I sign out
		And I login with old password
		And I check assertion wrong login

# MOBILE

	Scenario: Verify Magic Link Functionality
		Given I name mobile funnel
		Given Homepage has been opened
		Given User is logged in on mobile browser
		When I click on Start Now
		When I select video and use that
		Then I check assertion mobile path

	Scenario: Verify shared video in mobile view
		Given I name get video share link
		Given User is logged in with shorter new auth
		Then I go to Dashboard Published Tab
		Then I republish the published video
		Then I verify pricing/publish navigation
		Then I copy video share link
		Given Test Completed
		Given I name mobile view shared video test
		Then I verify open shared link is playing in mobile view
		Then I check assertion video in mobile view

# OTHER

		Scenario: Promo Performance Tests
		Given I name a Promo Performance Tests
		Given I open Promo Pages