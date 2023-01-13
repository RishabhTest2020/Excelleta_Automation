# Created by Rishabh Gupta at 5/10/2022
# Updated by Katarzyna Javaheri-Szpak on 7/12/2022
Feature: Automation Test Plan Prod BrowserStack

	Scenario: Verify image resizer without login
		Given I name test image resizer page without login
		Given I update headers through ModHeader
		When I go to Promo site
		Then I go to image resizer page
		And I upload the image on image resizer
		And I change IR Image Ratio
		And I download IR Image and verify redirection to signup page
		And I check assertion signup redirection

	 Scenario: Verify image resizer after login
		 Given I name test image resizer page after login
		 Given I update headers through ModHeader
		 Given User is logged in with shorter new auth
		 Then I go to image resizer page
		 And I upload the image on image resizer
		 And I change IR Image Ratio
		 And I select Social Image Ratios and download
		 And I convert IR Image to video
		 Then I verify navigation to editor page
		 When I Publish the video
		 Then I verify pricing/publish navigation
		 And I check assertion publish video

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
