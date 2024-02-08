# Created by macbookpro at 8/2/24
Feature: Different Login Test Cases
  In this feature, different login test cases will be implemented.

  Scenario: User can log in with valid email and valid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Click next button
    Then Enter valid email for employer
    Then Enter valid password for employer
    Then Click Sign in Button to login
    Then Verify Job Listing element is present
