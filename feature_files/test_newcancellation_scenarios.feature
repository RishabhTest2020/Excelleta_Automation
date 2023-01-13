Feature: Cancellation Flow Test Env BrowserStack

	Scenario: Basic Monthly User Accepts First Offer Basic Monthly Half Price
		Given I name a test Basic Monthly User Accepts First and Only Offer
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		And User accepts half price b1 monthly offer
		And I check assertion for accepted offer

	Scenario: Basic Monthly User Accepts Second Offer Lite Plan Monthly
		Given I name a test Basic Monthly User Accepts Second Offer
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		Then User declines an offer
		Then User gets offer to switch to light plan monthly
		And User accepts lite plan offer
		And I check assertion for downgrade flow

	Scenario: Basic Monthly User Cancels the Offer
		Given I name a test Basic Monthly User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		Then User declines an offer
		Then User gets offer to switch to light plan monthly
		And User cancels anyway
		And I check assertion for cancellation flow

	Scenario: Basic Monthly User Closes the Offer
		Given I name a test Basic Monthly User Closes the Offer
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		Then User declines an offer
		Then User gets offer to switch to light plan monthly
		And User closes the offer
		And I check assertion for closed offer

	Scenario: Standard Monthly User Accepts First Offer Basic Monthly
		Given I name a test standard monthly accepts first offer and only offer
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade to Basic Monthly
		And User accepts the downgrade offer
		And I check assertion for downgrade flow

	Scenario: Standard Monthly User Accepts Second Offer Half Price Basic Annual
		Given I name a test Standard Monthly User Accepts Second Offer
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User accepts basic annual for half price offer
		And I check assertion for accepted offer

	Scenario: Standard Monthly User Cancels the Offer
		Given I name a test Standard Monthly User Cancels the offer
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User cancels anyway
		And I check assertion for cancellation flow

	Scenario: Standard Monthly User Closes the Offer
		Given I name a test Standard Monthly User Closes the offer
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User closes the offer
		And I check assertion for closed offer

	Scenario: Pro Monthly User Accepts First Offer Basic Monthly
		Given I name a test Pro Monthly User Accepts First Offer Basic Monthly
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Basic Offer
		And I check assertion for downgrade flow

	Scenario: Pro Monthly User Accepts First Offer Standard Monthly
		Given I name a test Pro Monthly User Accepts First Offer Standard Monthly
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Standard Offer
		And I check assertion for downgrade flow

	Scenario: Pro Monthly User Accepts Second Offer Semi Annual Offer
		Given I name a test Pro Monthly User Accepts special offer
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User declines an offer
		Then User gets Special Offer Unlimited 6 Months
		And User accepts special offer
		And I check assertion for downgrade flow

	Scenario: Pro Monthly User Cancels the Offer
		Given I name a test Pro Monthly User Cancels the offer
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User declines an offer
		Then User gets Special Offer Unlimited 6 Months
		And User cancels anyway
		And I check assertion for cancellation flow

	Scenario: Pro Monthly User Closes the Offer
		Given I name a test Pro Monthly User Closes the offer
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User declines an offer
		Then User gets Special Offer Unlimited 6 Months
		And User closes the offer
		And I check assertion for closed offer


	Scenario: Basic Annual User Accepts First Offer Switch to Monthly
		Given I name a test Basic Annual User Accepts First and Only Offer
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade from Annual to Monthly
		Then User accepts basic monthly Offer
		And I check assertion for accepted offer

	Scenario: Basic Annual User Accepts Second Offer Half Price Basic Annual
		Given I name a test Basic Annual User Accepts Second Offer
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User accepts basic annual for half price offer
		And I check assertion for accepted offer

	Scenario: Basic Annual User Cancels the Offer
		Given I name a test Basic Annual User Cancels the offer
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User cancels anyway
		And I check assertion for cancellation flow

	Scenario: Basic Annual User Closes the Offer
		Given I name a test Basic Annual User Closes the offer
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User closes the offer
		And I check assertion for closed offer

	Scenario: Standard Annual User Accepts First Offer Switch to Monthly
		Given I name a test standard Annual User Accepts First and only offer
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade from Annual to Monthly
		And User accepts standard monthly Offer
		And I check assertion for accepted offer

	Scenario: Standard Annual User Accepts Second Offer Basic Monthly
		Given I name a test standard Annual User Second offer
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic Monthly
		And User accepts the downgrade offer
		And I check assertion for downgrade flow

	Scenario: Standard Annual User Cancels the Offer
		Given I name a test standard Annual User Cancels the offer
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic Monthly
		And User cancels anyway
		And I check assertion for cancellation flow

	Scenario: Standard Annual User Closes the Offer
		Given I name a test standard Annual User Closes the offer
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic Monthly
		And User closes the offer
		And I check assertion for closed offer

	Scenario: Pro Annual User Accepts First Offer Switch to Monthly
		Given I name a test Pro Annual User Accepts First and Only Offer
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade from Annual to Monthly
		And User accepts pro monthly Offer
		And I check assertion for accepted offer

	Scenario: Pro Annual User Accepts Second Offer Basic Monthly
		Given I name a test Pro Annual User Accepts Second Offer Basic Monthly
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Basic Offer
		And I check assertion for downgrade flow

	Scenario: Pro Annual User Accepts Second Offer Standard Monthly
		Given I name a test Pro Annual User Accepts Second Offer Standard Monthly
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Standard Offer
		And I check assertion for downgrade flow

	Scenario: Pro Annual User Cancels the offer
		Given I name a test Pro Annual User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		And User cancels anyway
		And I check assertion for cancellation flow

	Scenario: Pro Annual User Closes the offer
		Given I name a test Pro Annual User Closes the Offer
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		And User closes the offer
		And I check assertion for closed offer

#	Scenario Outline: Verify first offer for C Plan monthly user
#		Given I name a test Verify first offer for C Plan monthly user "<email_pricing_format>"
#		And I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Monthly User gets first offer "<email_pricing_format>"
#		And I check assertion for displayed offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstartermonthly+test01 |
#			| cplanbusinessmonthly+test01 |
#			| cplanagencymonthly+test01 |
#
#	Scenario Outline: Verify second offer for C plan monthly user
#		Given I name a test verify second offer for C Plan monthly user "<email_pricing_format>"
#		And I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Monthly User gets first offer "<email_pricing_format>"
#		Then User declines an offer
#		Then Monthly user gets second offer "<email_pricing_format>"
#		And I check assertion for displayed second offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstartermonthly+test01 |
#			| cplanbusinessmonthly+test01 |
#			| cplanagencymonthly+test01 |
#
#	Scenario Outline: Verify first offer for C Plan annual user
#		Given I name a test verify first offer for C Plan annual user "<email_pricing_format>"
#		And I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Annual User gets first offer "<email_pricing_format>"
#		And I check assertion for displayed first offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstarterannual+test01 |
#			| cplanbusinessannual+test01 |
#			| cplanagencyannual+test01 |
#
#	Scenario Outline: Verify second offer for C Plan annual user
#		Given I name a test verify second offer for C Plan annual user "<email_pricing_format>"
#		And I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Annual User gets first offer "<email_pricing_format>"
#		Then User declines an offer
#		Then Annual user gets second offer "<email_pricing_format>"
#		And I check assertion for displayed second offer for annual plan users "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstarterannual+test01 |
#			| cplanbusinessannual+test01 |
#			| cplanagencyannual+test01 |



# STARTER MONTHLY SURVEY 1st GROUP - CHAT AND 1 OFFER

#  	Scenario: Starter Monthly Cancels the Offer (chat and offer)
#		Given I name a test Starter Monthly Cancels the Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Starter Monthly Accepts the Offer (chat and offer)
#		Given I name a test Starter Monthly Accepts the Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts the offer
#		And I check assertion for accepted offer
#
#    Scenario: Starter Monthly Closes the Offer (chat and offer)
#		Given I name a test Starter Monthly Closes the Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User closes the offer
#		And I check assertion for closed offer

# STARTER MONTHLY SURVEY 2nd GROUP - 2 OFFERS

#  	Scenario: Starter Monthly Cancels the Offer
#		Given I name a test Starter Monthly Cancels the Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Half a Price
#		And User cancels anyway
#		And I check assertion for cancellation flow
##
#    Scenario: Starter Monthly Accepts first Offer
#		Given I name a test Starter Monthly Accepts the Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts downgraded offer
#		And I check assertion for downgrade flow
#
#	Scenario: Starter Monthly Accepts Second Offer
#		Given I name a test Starter Monthly Accepts second Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Half a Price
#		And User accepts the offer
#		And I check assertion for accepted offer
#
#    Scenario: Starter Monthly Closes the Offer
#		Given I name a test Starter Monthly Closes the Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Half a Price
#		And User closes the offer
#		And I check assertion for closed offer

# BUSINESS MONTHLY SURVEY 1st GROUP - CHAT AND 1 OFFER

#  	Scenario: Business Monthly Cancels the Offer (chat and offer)
#		Given I name a test Business Monthly Cancels the Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#  	Scenario: Business Monthly Accepts an Offer (chat and offer)
#		Given I name a test Business Monthly Accepts 1st Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts offer
#		And I check assertion for accepted offer
#
#
## BUSINESS MONTHLY SURVEY 2nd GROUP - 2 OFFERS
#
#  	Scenario: Business Monthly Cancels the Offer
#		Given I name a test Business Monthly Cancels the Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#	Scenario: Business Monthly Accepts First and Only Offer
#		Given I name a test Business Monthly Accepts 1st Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts offer
#		And I check assertion for accepted offer
#
#  	Scenario: Business Monthly Accepts first offer
#		Given I name a test Business Monthly Accepts 1st Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts offer
#		And I check assertion for accepted offer
#
#  	Scenario: Business Monthly Accepts second Offer
#		Given I name a test Business Monthly Accepts 2nd Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User accepts the downgrade offer
#		And I check assertion for downgrade flow
#
## AGENCY MONTHLY SURVEY 1st GROUP - CHAT AND 1 OFFER
#
#	Scenario: Agency Monthly Cancels the Offer Survey First Group (chat and offer)
#		Given I name a test Agency Monthly Cancels the Offer Survey 1st
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#	Scenario: Agency Monthly Accepts 1st Offer A (chat and offer)
#		Given I name a test Agency Monthly Accepts 1st Offer A - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Starter offer
#		And I check assertion for downgrade flow
#
#	Scenario: Agency Monthly Accepts 1st Offer B (chat and offer)
#		Given I name a test Agency Monthly Accepts 1st Offer B - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Business offer
#		And I check assertion for downgrade flow
#
#
## AGENCY MONTHLY SURVEY 2nd GROUP - 2 OFFERS
#
#	Scenario: Agency Monthly Cancels the Offer Survey Second Group
#		Given I name a test Agency Monthly Cancels the Offer Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Unlimited 6 Months
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#	Scenario: Agency Monthly Accepts First Offer Starter Monthly
#		Given I name a test Agency Monthly Accepts 1st Offer A - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Starter offer
#		And I check assertion for downgrade flow
#
#	Scenario: Agency Monthly Accepts First Offer Business Monthly
#		Given I name a test Agency Monthly Accepts 1st Offer B - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Business offer
#		And I check assertion for downgrade flow
#
#	Scenario: Agency Monthly Accepts Second Offer
#		Given I name a test Agency Monthly Accepts 2nd Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Unlimited 6 Months
#		And User accepts offer
#		And I check assertion for accepted offer

# STARTER ANNUAL SURVEY 1st GROUP - CHAT AND 1 OFFER

#  	Scenario: Starter Annual Cancels an Offer (chat and offer)
#		Given I name a test Starter Annual Cancels the Offer - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Starter Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Starter Annual Accepts an Offer (chat and offer)
#		Given I name a test Starter Annual Accepts 1st Offer - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Starter Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts the offer
#		And I check assertion for accepted offer


# STARTER ANNUAL SURVEY 2nd GROUP - 2 OFFERS

#  	Scenario: Starter Annual Cancels the Offer
#		Given I name a test Starter Annual Cancels the Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User declines an offer
#		Then User gets offer Switch to Business Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Starter Annual Accepts first Offer
#		Given I name a test Starter Annual Accepts 1st Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts the offer
#		And I check assertion for accepted offer
#
#    Scenario: Starter Annual Accepts second Offer
#		Given I name a test Starter Annual Accepts 2nd Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Starter Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Switch to Business Monthly
#		And User accepts downgraded offer
#		And I check assertion for downgrade flow

# BUSINESS ANNUAL SURVEY 1st GROUP - CHAT AND 1 OFFER

#  	Scenario: Business Annual Cancels the Offer (chat and offer)
#		Given I name a test Business Annual Cancels the Offer - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Business Annual Accepts 1st Offer (chat and offer)
#		Given I name a test Business Annual Accepts 1st Offer - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts offer
#		And I check assertion for accepted offer

# BUSINESS ANNUAL SURVEY 2nd GROUP - 2 OFFERS

#  	Scenario: Business Annual Cancels the Offer Survey Second Group
#		Given I name a test Business Annual Cancels the Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Business Annual Accepts first Offer
#		Given I name a test Business Annual Accepts 1st Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts offer
#		And I check assertion for accepted offer
#
#    Scenario: Business Annual Accepts second Offer
#		Given I name a test Business Annual Accepts 2nd Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User accepts the downgrade offer
#		And I check assertion for downgrade flow
#
## AGENCY ANNUAL SURVEY 1st GROUP - CHAT AND 1 OFFER
#
#  	Scenario: Agency Annual Cancels the Offer (chat and offer)
#		Given I name a test Agency Annual Cancels the Offer - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Agency Annual Accepts 1st Offer (chat and offer)
#		Given I name a test Agency Annual Accepts 1st Offer - Survey 1st
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts offer
#		And I check assertion for accepted offer
#
## AGENCY ANNUAL SURVEY 2nd GROUP - 2 OFFERS
#
#  	Scenario: Agency Annual Cancels the Offer
#		Given I name a test Agency Annual Cancels the Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User declines an offer
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#    Scenario: Agency Annual Accepts first Offer
#		Given I name a test Agency Annual Accepts 1st Offer - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts offer
#		And I check assertion for accepted offer
#
#    Scenario: Agency Annual Accepts second Offer starter monthly
#		Given I name a test Agency Annual Accepts 2nd Offer A - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User accepts Starter offer
#		And I check assertion for downgrade flow
#
#    Scenario: Agency Annual Accepts second Offer business monthly
#		Given I name a test Agency Annual Accepts 2nd Offer B - Survey 2nd
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User accepts Business offer
#		And I check assertion for downgrade flow

# SPECIAL OFFER - BLOCKED
#
#	Scenario: Special Offer User Cancels the Offer
#		Given I name a test Special Offer User Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Special Offer is logged in
#		When User cancels a plan
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Half a Price 1 Month
#		And User cancels anyway
#		And I check assertion for cancellation flow
#
#
#	Scenario: Special Offer User Accepts 1st Offer A
#		Given I name a test Special Offer User Accepts 1st Offer A
#		Given I update headers through ModHeader
#		Given User with Special Offer is logged in
#		When User cancels a plan
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Starter offer
#		And I check assertion for downgrade flow
#
#	Scenario: Special Offer User Accepts 1st Offer B
#		Given I name a test Special Offer User Accepts 1st Offer B
#		Given I update headers through ModHeader
#		Given User with Special Offer is logged in
#		When User cancels a plan
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Business offer
#		And I check assertion for downgrade flow
#
#	Scenario: Special Offer User Accepts 2nd Offer
#		Given I name a test Special Offer User Accepts 2nd Offer
#		Given I update headers through ModHeader
#		Given User with Special Offer is logged in
#		When User cancels a plan
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Half a Price 1 Month
#		And User accepts the offer
#		And I check assertion for cancellation flow


