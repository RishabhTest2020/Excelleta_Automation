Feature: Renderer Suite - short scenarios for video generation

	Scenario Outline: Generate video and publish
		Given I name a "<env>" test generate video
		Given I update headers through ModHeader
		Given User is logged in "<env>" with shorter new auth
		When I customize the video
		Then I verify navigation to editor page
		When I Publish the video
		Then I verify pricing/publish navigation
		And I check assertion publish video
		Examples:
			| env      |
			| prod     |
			| test01   |
			| test02   |
			| test03   |
			| test04   |
			| test05   |
			| poland01 |
			| staging |