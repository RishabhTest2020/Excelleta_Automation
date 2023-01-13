Feature: Automation Cookies Test Plan Production - Europe Only


  Scenario: Verify cookies bar
    Given I name a test cookies
    When I go to Promo site
    And I click on agree and continue
    Then I check assertion cookies