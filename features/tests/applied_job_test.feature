# Created by nabia at 2/28/2024
Feature: Different test cases for Applied Job will be implemented here
   Enter feature description here

Scenario: Test Apply Job feature with Bangla Talent Resume
    Given User can enter to the https://dev.banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click Looking For Job
    Then Enter valid email for employer nsharli8256+4@gmail.com
    Then Enter valid password for employer Sitakund1#
    Then Click Sign in Button to login
    Then User will click search button
    Then User will find job by name PHP2
    When User will click apply job button
    Then User will enter a new email nsharli@gmail.com
    Then User will enter a new Phone number 0712485654
    Then User will select BT Resume
    Then User will click Submit Application button
    Then User will be navigates to the congratulations page


Scenario: Test Apply Job feature with a valid Resume
    Given User can enter to the https://dev.banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click Looking For Job
    Then Enter valid email for employer nsharli8256+4@gmail.com
    Then Enter valid password for employer Sitakund1#
    Then Click Sign in Button to login
    Then User will click search button
    Then User will find job by name PHP
    When User will click apply job button
    Then User will enter a new email nsharli@gmail.com
    Then User will enter a new Phone number 0712485654
    Then User will Upload Resume
    Then User will Click Upload Resume checkbox
    Then User will select file nsharli.pdf
    Then User will Upload a cover Letter
    Then User will click cover letter checkbox
    Then user will select cover letter
    Then User will click Submit Application button
     Then User will be navigates to the congratulations page

Scenario: Test Apply Job feature with Uploaded Resume
    Given User can enter to the https://dev.banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click Looking For Job
    Then Enter valid email for employer nsharli8256+4@gmail.com
    Then Enter valid password for employer Sitakund1#
    Then Click Sign in Button to login
    Then User will click search button
    Then User will find job by name Web Developer
    When User will click apply job button
    Then User will enter a new email nsharli@gmail.com
    Then User will enter a new Phone number 0712485654
    Then User will upload Video Instruction
    Then User will click Video Introduction checkbox
    Then User will select file nsharli.mp4
    Then User will click Submit Application button
     Then User will be navigates to the congratulations page



#Scenario: Test Apply Job feature with a Resume larger than max size
#    Given User can enter to the https://dev.banglatalent.com/
#    Then Accept All Cookies
#    Then Click on Sign in button
#    Then Click Looking For Job
#    Then Enter valid email for employer nsharli8256+4@gmail.com
#    Then Enter valid password for employer Sitakund1#
#    Then Click Sign in Button to login
#    Then User will click search button
#    Then User will find job by name PHP
#    When User will click apply job button
#    Then User will enter a new email nsharli@gmail.com
#    Then User will enter a new Phone number 0712485654
#    Then User will Upload Resume
#    Then User will see an error message File size should be less than 10MB