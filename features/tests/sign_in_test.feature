# Created by macbookpro at 1/2/24
Feature: Different Login Test Cases
  In this feature, different login test cases will be implemented.

  Scenario: User can log in with valid email and valid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click next button
    Then Enter valid email
    Then Enter valid password
    Then Click Sign in Button to login
    Then Verify Sign in is Successful

  Scenario: User can log in with invalid email and invalid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click next button
    Then Enter invalid email
    Then Enter invalid password
    Then Click Sign in Button to login
    Then Verify Login Failed

  Scenario: User can log in with valid email and invalid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click next button
    Then Enter valid email
    Then Enter invalid password
    Then Click Sign in Button to login
    Then Verify Login Failed

  Scenario: User can log in with invalid email and valid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click next button
    Then Enter invalid email
    Then Enter valid password
    Then Click Sign in Button to login
    Then Verify Login Failed

  Scenario: User can log in without Accepting Cookies
    Given User can enter to the https://banglatalent.com/
    Then Reject All Cookies
    Then Click on Sign in button
    Then Click next button
    Then Enter valid email
    Then Enter valid password
    Then Click Sign in Button to login
    Then Verify Sign in is Successful
