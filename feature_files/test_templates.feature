Feature: Automation Test Plan Templates BrowserStack

# TEMPLATES

	Scenario: Verify template page without login
      Given I name test template page without login
      Given I update headers through ModHeader
      When I go to Promo site
      Then I go to Templates page
      And I change ratios and verify
      And I search templates with valid and invalid keys
      And I customize video and verify redirection to signup page
      And I check assertion signup redirection

	Scenario: Verify template page after login
      Given I name test template page after login
      Given I update headers through ModHeader
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
      And I add characters in text animation
      And I am changing font color
      And I am changing text alignment
      And I am changing the font
      And I am changing capitalization style
      And I change text positions
      And I change text style once
      And I am changing ratio
      # And I select an audio
      When I Publish the video
      Then I verify pricing/publish navigation
      And I check assertion publish video