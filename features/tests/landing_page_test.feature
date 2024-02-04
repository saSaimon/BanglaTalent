# Created by macbookpro at 2/2/24
Feature: Landing Page Test
  In this feature, certain ui and functionality will be tested.
  Background:
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
  
  Scenario: Check certain elements present in Landing Page
    Given Logo is present
    Then Verify Find a job is present
    Then Verify Post a job is present
    Then Verify About us job present
    Then Verify Find a job is present in lower
    Then Verify Post a job lower present
    Then Verify Search Bar is present
    Then Verify Job Carts are present
    Then Verify Top pick Carts are present
    Then Verify Success Stories slides are present

  Scenario Outline: Check Find a job section
    Given Logo is present
    When User click Find a job first option
    Then Verify there are available some vacancies
    When User will input keywords: <keywords>
    When User will input location: <input_location>
    When User will select by location: <select_location>
    When Input Salary range: <salary_range>
    When User will click search button
    Then Verify there are job carts with this search
   Examples:
    |keywords      |input_location   |select_location|salary_range |
    |qa            |Bangladesh       |Bangladesh     |1000         |
    |dev           |India            |India          |10000        |
    |content writer|UK               |UK             |100000       |
    |dev           |USA              |USA            |10           |

  Scenario: Test Job Details
    Given Logo is present
    When User click Find a job first option
    Then Verify there are available some vacancies
    When User will click search button
    When Select job cart by name: Manager
    Then Verify Apply Job button is present
    When User will click apply job button
    When User will click yes button
    Then Verify pop up sign in window


