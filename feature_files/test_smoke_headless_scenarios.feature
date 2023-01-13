Feature: Automation Smoke Test Plan Prod BrowserStack


  Scenario: Smoke Scenario New User
	  When I create a new account new auth
	  And I select video preference
	  And I search the video
	  And I customize the video
	  Then I verify navigation to editor page new user
	  When I Publish the video
	  Then I verify pricing/publish navigation new user
	  Then I close pricing page
	  Then I go to my account
	  And I delete my account new

  Scenario: Smoke Scenario Existing User
	  Given User is logged in with shorter new auth
	  When I search the video
	  And I customize the video
	  Then I verify navigation to editor page
	  And I am changing font color
	  And I am changing text alignment
	  And I am changing the font
	  And I am changing capitalization style
	  And I change text positions
	  And I change text style once
	  And I am changing ratio
	  And I am adding a new clip
	  And I am uploading a photo and replacing
	  And I am going to editor tab
	  And I upload a logo and add it
	  When I Publish the video
	  Then I verify pricing/publish navigation
	  Then I change video name
	  When I goto Drafts page
	  Then I verify drafted video
	  And  I verify draft share buttons
	  And I publish drafted video
	  And I sign out
