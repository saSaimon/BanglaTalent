# Created by DELL at 2/11/2024
Feature: Different test cases for employer home page
  In this feature different test cases for Post A Job section will be implemented

  Scenario: Check certain elements present in employer home page
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of Post A Job button
    Then Click on the Post A Job button
    Then Verify the present of search icon
    Then Click on the search icon
    Then Verify the present of messenger icon
    Then click on the messenger icon
    Then Verify the present of calender icon
    Then Click on the Calender icon
    Then Verify the present of Notification icon
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Back to the home Page
    Then Verify Search Candidate Here element is present
    Then Verify Job Listing element is present
#    Then Verify View All link for job listing is present
#    Then click on View link For job listing
#    Then Verify Inbox text is present
#    Then Verify View all link for inbox is present
#    Then Click on the View All link for inbox
    Then Verify Calender text is present



