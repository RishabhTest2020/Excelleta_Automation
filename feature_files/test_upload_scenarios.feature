# Created by Rishabh Gupta at 10/6/2022
Feature: Upload tests

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
		When I use upload functionality with "wistia"
		When I use upload functionality with "hubspot"
		When I use upload functionality with "dropbox"
		Then I check assertion publish video