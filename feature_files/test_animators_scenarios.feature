Feature: Automation test Animators


# TESTING ANIMATIONS

    Scenario: Verify Animations using Animation Playground Extension first half
          Given I name Animation Tests
          Given User enables animation playground google chrome extension
          When User opens a animation preview tab first half set
          Then I check Animation test completed

    Scenario: Verify Animations using Animation Playground Extension second half
          Given I name Animation Tests second half set
          Given User enables animation playground google chrome extension
          When User opens a animation preview tab second half set
          Then I check Animation test completed






