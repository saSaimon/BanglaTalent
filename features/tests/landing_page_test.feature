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