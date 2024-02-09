# Created by Hp at 2/7/2024

Feature: Footer Section Test
  In this feature, certain ui and functionality will be tested.
  Background:
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies

  Scenario: Check and click certain elements present in the footer section
#    Given FooterLogo is present
    Given Verify Company is present
    Then Click on AboutUs link
    Then Click on Jobs link
    Then Click on Help link

    Then Verify ContactHeading is present
    Then Click on Contact link
    Then Click on FAQ link
#
    Then Verify Legal is present
    Then Click on Privacy link
    Then Click on Disclaimer link
    Then Click on GDPR link

