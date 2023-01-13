Feature: Automation Test Plan Publisher and Scheduler BrowserStack (test and prod) - regression tests

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

 Scenario: Verify Scheduler functionalities with issues
   Given I name Scheduler with Issues Tests
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth
   Then User cleaned all scheduled posts
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I publish empty post
   Then I go back to Publish Page
   Then I publish and schedule two posts
   Then I go to My Calendar
   Then I verify My Calendar issue path
   And I check assertion My Calendar

 Scenario: Verify Scheduler edit and reschedule
   Given I name Scheduler edit and scheduler
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth
   Then User cleaned all scheduled posts
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I schedule a post and edit it
   Then I reschedule a post
   Then I go to My Calendar
   Then I verify My Calendar reschedule path
   And I check assertion My Calendar

 Scenario: Verify publish and schedule for YT and LI
   Given I name publish YT and LI
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth socials
   Then User cleaned all scheduled posts
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I add drafts YT and LI
   Then I publish and schedule YT and LI posts
   Then I go to My Calendar
   Then I verify My Calendar YT and LI
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

 Scenario: Verify a new post button
   Given I name a new post button
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth
   Then I open Planner
   Then I add a new post for today
   Then I go to My Calendar
   Then I add a new post for next day
   And I check assertion My Calendar

 Scenario: Verify post duplication and deletion
   Given I name a post duplication
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth
   Then User cleaned all scheduled posts
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I create fb draft
   Then I duplicate first post and delete second
   Then I publish duplicated post
   Then I go to My Calendar
   Then I verify My Calendar duplication
   And I check assertion My Calendar

Scenario: Verify duplication a published post from planner
   Given I name a planner post duplication published
   Given I update headers through ModHeader
   Given User is logged in with shorter new auth
   Then User cleaned all scheduled posts
   Then I go to Dashboard Published Tab
   Then I republish the published video
   Then I verify pricing/publish navigation
   Then I verify FB publisher
   Then I duplicate a post from Planner
   Then I publish a post duplicated from Planner
   Then I go to My Calendar
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

Scenario: Verify create another post from publish summary
  Given I name create another post from publish summary
  Given I update headers through ModHeader
  Given User is logged in with shorter new auth
  Then I open Planner
  Then I add a new post for today and create another post
  And I check assertion Publisher

# to_improve: uncomment this scenario when BOOST-2268 is fixed
#Scenario: Verify planner functionalities on mobile
#  Given I name a test planner on mobile phase web
#  Given I update headers through ModHeader
#  Given User is logged in with shorter new auth socials
#  Then User cleaned all scheduled posts
#  Then I go to Dashboard Published Tab
#  Then I republish the published video
#  Then I verify pricing/publish navigation
#  Then I add draft LI
#  Then I schedule a LI post
#  Given Test Completed
#  Given I name a test planner on mobile phase mobile
#  Given I update headers through ModHeader mob
#  Given Homepage has been opened
#  Given Linkedin user is logged in on mobile browser
#  Then I go to Planner on mobile
#  Then I preview and delete a scheduled LI post
#  Then I check assertion of Planner in mobile view

