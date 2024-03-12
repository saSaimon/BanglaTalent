# Created by Nabia at 3/12/2024
Feature: Different test cases for Edit Profile
   Enter feature description here

Scenario Outline: Edit profile feature will be implemented
    Given User can enter to the https://dev.banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click Looking For Job
    Then Enter valid email for employer nsharli8256+4@gmail.com
    Then Enter valid password for employer Sitakund1#
    Then Click Sign in Button to login
    Then User will click Profile icon
    Then User will Navigate to the Profile section
    Then User will click profile edit icon
    Then User will edit FirstName <FirstName>
    Then User will edit LastName <LastName>
    Then User will edit Designation <Designation>
    Then User will edit phone Number <Phone>
    Then User will edit country <Country>
    Then User will Edit City <City>
    Then User will edit Zip code <ZipCode>
    Then User will edit linkedIn link <Link>
    Then User will Change Profile Picture
    Then User will Click Save Changes Button
    Examples:
        |FirstName  |LastName   |Designation    |Phone       |Country       |City       |ZipCode    |Link               |
        |Nabia      |Sharli     |SQA            |01756255558 |Bangladesh    |Dhaka      |1100       |www.facebook.com   |
        |Nabila     |Ibnath     |PHP            |017565565555|India         |Ahmedabad  |2200       |www.facebook.com   |
        |Ishika     |Mantaha    |Web Developer  |017565565555|Iran          |Abhar      |3300       |www.google.com     |
