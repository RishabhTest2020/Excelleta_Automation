Feature: Automation Test Plan Publisher and Scheduler BrowserStack (test and prod) - smoke tests

  Scenario: Verify Publisher functionalities
    Given I name Publisher Tests
    Given I update headers through ModHeader
    Given User is logged in with shorter new auth
    Then I go to Dashboard Published Tab
    Then I republish the published video
    Then I verify pricing/publish navigation
    Then I verify FB publisher
    Then I verify IG publisher
    Then I verify TWIT publisher
    And I check assertion My Calendar

  Scenario: Verify Scheduler functionalities happy path
    Given I name Scheduler Happy Path Tests
    Given I update headers through ModHeader
    Given User is logged in with shorter new auth
    Then User cleaned all scheduled posts
    Then I go to Dashboard Published Tab
    Then I republish the published video
    Then I verify pricing/publish navigation
    Then I schedule a FB post
    Then I schedule a IG post
    Then I schedule a TWIT post
    Then I go to My Calendar
    Then I verify My Calendar happy path
    And I check assertion My Calendar

 Scenario: Verify reschedule YT and LI
   Given I name reschedule YT and LI
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth socials
   Then User cleaned scheduled posts YT and LI
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I add drafts YT and LI
   Then I schedule YT and LI posts
   Then I go to My Calendar
   Then I reschedule YT or LI post
   Then I reschedule YT or LI post
   Then I verify My Calendar YT and LI rescheduled
   And I check assertion My Calendar

Scenario: Verify duplication a scheduled post from planner
   Given I name a planner post duplication scheduled
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth
   Then User cleaned all scheduled posts
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I connect and schedule TT publisher
   Then I duplicate a scheduled post from Planner
   Then I publish a scheduled post duplicated from Planner
   Then I go to My Calendar
   Then I verify My Calendar duplication from Planner
   And I check assertion My Calendar

