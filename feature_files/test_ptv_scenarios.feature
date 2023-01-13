Feature: Automation Test Plan Photo to Video

  Scenario: Verify PTV functionalities
    Given I name PTV Test sanity
    Given I update headers through ModHeader
    Given User is logged in with shorter new auth
    When I go to PTV landing page
    Then I click create a new video
    Then I choose a PTV template
    Then I choose uploaded image
    Then I publish a PTV or Shopify video
    Then I verify socials PTV
    Then I publish PTV post on FB
    Then I go to PTV or Shopify My published videos
    Then I delete last published video
    When I go back from PTV to Promo
    Then I check assertion create page