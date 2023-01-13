Feature: Cancellation Flow Test Plan - Local

	Scenario: Basic Monthly User Accepts First Offer Basic Monthly Half Price
		Given I update headers through ModHeader
		And User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		And User accepts half price b1 monthly offer

	Scenario: Basic Monthly User Accepts Second Offer Lite Plan Monthly
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		Then User declines an offer
		Then User gets offer to switch to light plan monthly
		And User accepts lite plan offer

	Scenario: Basic Monthly User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		Then User declines an offer
		Then User gets offer to switch to light plan monthly
		And User cancels anyway

	Scenario: Basic Monthly User Closes the Offer
		Given I update headers through ModHeader
		Given User with Basic Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer basic monthly half a price
		Then User declines an offer
		Then User gets offer to switch to light plan monthly
		And User closes the offer

	Scenario: Standard Monthly User Accepts First Offer Basic Monthly
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade to Basic Monthly
		And User accepts the downgrade offer

	Scenario: Standard Monthly User Accepts Second Offer Half Price Basic Annual
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User accepts basic annual for half price offer

	Scenario: Standard Monthly User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User cancels anyway

	Scenario: Standard Monthly User Closes the Offer
		Given I update headers through ModHeader
		Given User with Standard Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User closes the offer

	Scenario: Pro Monthly User Accepts First Offer Basic Monthly
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Basic Offer

	Scenario: Pro Monthly User Accepts First Offer Standard Monthly
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Standard Offer


	Scenario: Pro Monthly User Accepts Second Offer Semi Annual Offer
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User declines an offer
		Then User gets Special Offer Unlimited 6 Months
		And User accepts special offer

	Scenario: Pro Monthly User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User declines an offer
		Then User gets Special Offer Unlimited 6 Months
		And User cancels anyway


	Scenario: Pro Monthly User Closes the Offer
		Given I update headers through ModHeader
		Given User with Pro Monthly is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User declines an offer
		Then User gets Special Offer Unlimited 6 Months
		And User closes the offer

	Scenario: Basic Annual User Accepts First Offer Switch to Monthly
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade from Annual to Monthly
		Then User accepts basic monthly Offer

	Scenario: Basic Annual User Accepts Second Offer Half Price Basic Annual
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User accepts basic annual for half price offer

	Scenario: Basic Annual User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User cancels anyway

	Scenario: Basic Annual User Closes the Offer
		Given I update headers through ModHeader
		Given User with Basic Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer half price basic annual
		And User closes the offer

	Scenario: Standard Annual User Accepts First Offer Switch to Monthly
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade from Annual to Monthly
		Then User accepts standard monthly Offer

	Scenario: Standard Annual User Accepts Second Offer Basic Monthly
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic Monthly
		And User accepts the downgrade offer

	Scenario: Standard Annual User Cancels the Offer
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic Monthly
		And User cancels anyway

	Scenario: Standard Annual User Closes the Offer
		Given I update headers through ModHeader
		Given User with Standard Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic Monthly
		And User closes the offer

	Scenario: Pro Annual User Accepts First Offer Switch to Monthly
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User chooses plan survey from 1st group
		Then User gets offer Downgrade from Annual to Monthly
		And User accepts pro monthly Offer

	Scenario: Pro Annual User Accepts Second Offer Basic Monthly
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Basic Offer

	Scenario: Pro Annual User Accepts Second Offer Standard Monthly
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		Then User accepts Standard Offer

	Scenario: Pro Annual User Cancels the offer
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		And User cancels anyway

	Scenario: Pro Annual User Closes the offer
		Given I update headers through ModHeader
		Given User with Pro Annual is logged in
		When User cancels a plan survey 2nd group
		Then User gets offer Downgrade from Annual to Monthly
		Then User declines an offer
		Then User gets offer Downgrade to Basic or Standard Monthly
		And User closes the offer

#	Scenario Outline: Verify first offer for C Plan monthly user
#		Given I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Monthly User gets first offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstartermonthly+test01 |
#			| cplanbusinessmonthly+test01 |
#			| cplanagencymonthly+test01 |
#
#	Scenario Outline: Verify second offer for C plan monthly user
#		Given I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Monthly User gets first offer "<email_pricing_format>"
#		Then User declines an offer
#		Then Monthly user gets second offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstartermonthly+test01 |
#			| cplanbusinessmonthly+test01 |
#			| cplanagencymonthly+test01 |
#
#	Scenario Outline: Verify first offer for C Plan annual user
#		Given I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Annual User gets first offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstarterannual+test01 |
#			| cplanbusinessannual+test01 |
#			| cplanagencyannual+test01 |
#
#	Scenario Outline: Verify second offer for C Plan annual user
#		Given I update headers through ModHeader
#		And User with C plan is logged in "<email_pricing_format>"
#		When User cancels a plan survey 2nd group
#		Then Annual User gets first offer "<email_pricing_format>"
#		Then User declines an offer
#		Then Annual user gets second offer "<email_pricing_format>"
#		Examples:
#			| email_pricing_format |
#			| cplanstarterannual+test01 |
#			| cplanbusinessannual+test01 |
#			| cplanagencyannual+test01 |


# C PLANS
# STARTER MONTHLY

#  	Scenario: Starter Monthly Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Half a Price
#		And User cancels anyway
#
#    Scenario: Starter Monthly Accepts First Offer
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User chooses plan survey from 1st group
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts downgraded offer
#
#	Scenario: Starter Monthly Accepts Second Offer
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Half a Price
#		And User accepts the offer
#
#    Scenario: Starter Monthly Closes the Offer
#		Given I update headers through ModHeader
#		Given User with Starter Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Half a Price
#		And User closes the offer

# BUSINESS MONTHLY

#  	Scenario: Business Monthly Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User cancels anyway
#
#	Scenario: Business Monthly Accepts First and Only Offer
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts offer
#
#  	Scenario: Business Monthly Accepts first Offer
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		And User accepts offer
#
#  	Scenario: Business Monthly Accepts Second Offer
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User accepts the downgrade offer
#
#    Scenario: Business Monthly Closes the Offer
#		Given I update headers through ModHeader
#		Given User with Business Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer c2 monthly 20 percent off
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User closes the offer
#
## AGENCY MONTHLY
#
#	Scenario: Agency Monthly Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Unlimited 6 Months
#		And User cancels anyway
#
#	Scenario: Agency Monthly Accepts First Offer Starter Monthly
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Starter offer
#
#	Scenario: Agency Monthly Accepts First Offer Business Monthly
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User accepts Business offer
#
#	Scenario: Agency Monthly Accepts Second Offer
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Unlimited 6 Months
#		And User accepts offer
#
#    Scenario: Agency Monthly Closes the Offer
#		Given I update headers through ModHeader
#		Given User with Agency Monthly is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade to Starter or Business Monthly
#		Then User declines an offer
#		And User gets Special Offer Unlimited 6 Months
#		And User closes the offer
#
## STARTER ANNUAL
#
##  	Scenario: Starter Annual Cancels the Offer
##		Given I update headers through ModHeader
##		Given User with Starter Annual is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade from Annual to Monthly
##		And User declines an offer
##		Then User gets offer Switch to Business Monthly
##		And User cancels anyway
##
##    Scenario: Starter Annual Accepts an Offer
##		Given I update headers through ModHeader
##		Given User with Starter Annual is logged in
##		When User chooses plan survey from 1st group
##		Then User gets offer Downgrade from Annual to Monthly
##		And User accepts the offer
##
##    Scenario: Starter Annual Accepts first Offer
##		Given I update headers through ModHeader
##		Given User with Starter Annual is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade from Annual to Monthly
##		And User accepts the offer
##
##    Scenario: Starter Annual Accepts second Offer
##		Given I update headers through ModHeader
##		Given User with Starter Annual is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade from Annual to Monthly
##		Then User declines an offer
##		Then User gets offer Switch to Business Monthly
##		And User accepts downgraded offer
#
## BUSINESS ANNUAL SURVEY 1st GROUP - CHAT AND 1 OFFER
#
#  	Scenario: Business Annual Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User cancels anyway
#
#    Scenario: Business Annual Accepts first Offer
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User chooses plan survey from 1st group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts the offer
#
## BUSINESS ANNUAL SURVEY 2nd GROUP - 2 OFFERS
#
#  	Scenario: Business Annual Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User cancels anyway
#
#    Scenario: Business Annual Accepts first Offer
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts the offer
#
#    Scenario: Business Annual Accepts second Offer
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User accepts the downgrade offer
#
#    Scenario: Business Annual closes the Offer
#		Given I update headers through ModHeader
#		Given User with Business Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter Monthly
#		And User closes the offer
#
## AGENCY ANNUAL SURVEY 1st GROUP - CHAT AND 1 OFFER
#
#  	Scenario: Agency Annual Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User cancels anyway
#
#    Scenario: Agency Annual Accepts 1st Offer
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts the offer
#
## AGENCY ANNUAL SURVEY 2nd GROUP - 2 OFFERS
#
#  	Scenario: Agency Annual Cancels the Offer
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User declines an offer
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User cancels anyway
#
#    Scenario: Agency Annual Accepts first Offer
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		And User accepts the offer
#
#    Scenario: Agency Annual Accepts second Offer starter monthly
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User accepts Starter offer
#
#    Scenario: Agency Annual Accepts second Offer business monthly
#		Given I update headers through ModHeader
#		Given User with Agency Annual is logged in
#		When User cancels a plan survey 2nd group
#		Then User gets offer Downgrade from Annual to Monthly
#		Then User declines an offer
#		Then User gets offer Downgrade to Starter or Business Monthly
#		And User accepts Business offer
#
## SPECIAL OFFER
##
##	Scenario: Special Offer User Cancels the Offer
##		Given I update headers through ModHeader
##		Given User with Special Offer is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade to Starter or Business Monthly
##		Then User declines an offer
##		And User gets Offer Half Price C1 Monthly
##		And User cancels anyway
##
##
##	Scenario: Special Offer User Accepts first Offer starter monthly
##		Given I update headers through ModHeader
##		Given User with Special Offer is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade to Starter or Business Monthly
##		Then User accepts Starter offer
##
##	Scenario: Special Offer User Accepts first Offer business monthly
##		Given I update headers through ModHeader
##		Given User with Special Offer is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade to Starter or Business Monthly
##		Then User accepts Business offer
##
##	Scenario: Special Offer User Accepts second Offer
##		Given I update headers through ModHeader
##		Given User with Special Offer is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade to Starter or Business Monthly
##		Then User declines an offer
##		And User gets Offer Half Price C1 Monthly
##		And User accepts the offer
##
##	Scenario: Special Offer user closes the Offer
##		Given I update headers through ModHeader
##		Given User with Special Offer is logged in
##		When User cancels a plan survey 2nd group
##		Then User gets offer Downgrade to Starter or Business Monthly
##		Then User declines an offer
##		And User gets Offer Half Price C1 Monthly
##		And User closes the offer
##
