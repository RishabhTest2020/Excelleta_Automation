Feature: Automation Test Plan Shopify BrowserStack


Scenario: Verify fb Shopify functionalities
    Given I name Shopify Test sanity
    Given I update headers through ModHeader
    Given User is fb logged in to Shopify QA Poland Shop
    When User chooses an environment
    Then User is redirected to the Shop
    Then User cleans all drafts
    Then I click create a new Shopify video
    Then I choose a Shopify template
    Then I choose uploaded image
    Then I publish a PTV or Shopify video
    Then I verify socials Shopify
    Then I go to PTV or Shopify My published videos
    Then I delete last published video
    Then I check assertion Shopify