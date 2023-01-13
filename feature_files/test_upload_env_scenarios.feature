# Created by Rishabh Gupta at 10/6/2022
Feature: BS env upload scenarios

	Scenario: Create video from uploaded photo and verify functionalities of publish page
		Given I name a test create from photo uploaded
		Given I update headers through ModHeader
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
		Then I check assertion publish video

    Scenario: New user purchases a plan and verify download functionality in publish page
		Given I name a test purchase a plan
		Given I update headers through ModHeader
		When I create a new account new auth
		When I select video preference
		When I go to pricing page
		Then I choose business plan and goto Create page
		When I search the video
		And I customize the video
		Then I verify navigation to editor page
#		And I select an audio
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
		Then I go to my account
		And I delete my account new
		And I check assertion deleted/logged out account