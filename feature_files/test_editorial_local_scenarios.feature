Feature: Automation Test Plan - Local

  Scenario: Signup verify editorial tags and see pricing
	  Given I update headers through ModHeader
	  When I create a new account new auth
	  When I select video preference
	  And I am filtering editorial videos and photos on create page
	  And I customize the video
	  Then I verify navigation to editor page new user
	  And I am filtering editorial videos and photos
	  # And I select an audio
	  When I Publish the video
	  Then I verify pricing/publish navigation new user
	  Then I close pricing page
	  Then I go to my account
	  And I delete my account new


  Scenario: Signup purchase business plan and verify editorial tags and Publish pop up
	  Given I update headers through ModHeader
	  When I create a new account new auth
	  When I select video preference
	  When I go to pricing page
	  Then I choose business plan and goto Create page
	  When I am filtering editorial videos and photos on create page
	  And I customize the video
	  Then I verify navigation to editor page new user
	  And I am filtering editorial videos and photos
	  And I upload an audio and select it
	  When I Publish the video
	  Then I verify pricing/publish navigation for editorial video
	  Then I go to my account
	  And I delete my account new

  Scenario: User with starter plan see upgrade now pop while publishing the editorial
	  Given I update headers through ModHeader
	  When I create a new account new auth
	  When I select video preference
	  When I go to pricing page
	  Then I choose starter plan and goto Create page
	  When I am filtering editorial videos and photos on create page
	  And I customize the video
	  Then I verify navigation to editor page new user
	  And I am filtering editorial videos and photos
	  # And I select an audio
	  When I Publish the video
	  Then I verify pricing/publish navigation for editorial video
	  Then I go to my account
	  And I delete my account new