Feature: Automation Test Plan Prod BrowserStack Check the Links


	Scenario: Check menu and footer links
		Given I name a test links
		Given I update headers through ModHeader
		When I go to Promo site
		Then I close ModHeader tab
		Then I check main menu links
		And I check footer links
		Then I check assertion links

	Scenario: Check tools links
		Given I name a tools links
		Given I update headers through ModHeader
		When I go to Promo site
		Then I close ModHeader tab
		Then I check tools links
		Then I check assertion tool links

	Scenario: Check partners logos and links
		Given I name a logo links
		Given I update headers through ModHeader
		Then I check logos links
		Then I check assertion logos links

	Scenario: Check footer links on Templates Page
		Given I name a test footer links on Promo-next
		Given I update headers through ModHeader
		When I go to Promo site
		Then I check templates footer links
		Then I check assertion templates Footer links

	Scenario: Check header links on Templates page
		Given I name a test header links on Promo-next
		Given I update headers through ModHeader
		When I go to Promo site
		Then I check templates header links
		Then I check assertion templates Header links