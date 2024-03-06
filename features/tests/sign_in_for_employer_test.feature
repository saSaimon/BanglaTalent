# Created by macbookpro at 8/2/24
Feature: Different Login Test Cases for Employer Sections
  In this feature, different login test cases of employer sections will be implemented.

  Scenario: User can log in with valid email and valid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify Sign in is Successful for employer


  Scenario: User can not log in with valid email and invalid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter invalid password for employer Bangladesh1#
    Then Click Sign in Button to login
    Then Verify Login Failed


  Scenario: User can not log in with invalid email and valid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter invalid email for employer nsharli8256@gmail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
   Then Verify Login Failed

  Scenario: User can not log in with invalid email and invalid pass
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter invalid email for employer nsharli8256@gmail.com
    Then Enter invalid password for employer Bangladesh1#
    Then Click Sign in Button to login
    Then Verify Login Failed


