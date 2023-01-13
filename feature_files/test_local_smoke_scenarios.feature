Feature: Automation Smoke Test Plan Prod Local


  Scenario: Smoke Scenario New User
	  Given I update headers through ModHeader
	  When I go to Promo site
	  And I create a new account new auth
	  And I select video preference
	  And I search the video
	  And I customize the video
	  Then I verify navigation to editor page
	  And I upload an audio and select it
	  When I Publish the video
	  Then I verify pricing/publish navigation new user
	  Then I close pricing page
	  Then I go to my account
	  And I delete my account new
	  When I create a new account new auth with Facebook
	  Then I go to my account
	  And I disconnect Facebook
	  And I delete my account new


  Scenario: Smoke Scenario Existing User
	  Given I update headers through ModHeader
	  Given User is logged in with new auth
	  When I search the video
	  And I customize the video
	  Then I verify navigation to editor page
	  And I upload a watermark and add it
	  And I upload a logo and add it
	  And I am adding a new clip
	  And I am uploading a photo and replacing
	  And I am going to editor tab
	  And I am changing font color
	  And I am changing text alignment
	  And I am changing the font
	  And I am changing capitalization style
	  And I change text positions
	  And I change text style once
	  And I am changing ratio
	  When I Publish the video
	  Then I verify pricing/publish navigation
	  When I goto Drafts page
	  Then I verify drafted video
	  And  I verify draft share buttons
	  And I publish drafted video
	  And I sign out