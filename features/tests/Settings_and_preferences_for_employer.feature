# Created by DELL at 2/13/2024
Feature: Different test cases for Settings and preference will be implemented here
  # Enter feature description here

Scenario: User will be able to activate or deactivate Two Factor Authentication
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Turn On Two Factor Authentication Icon
    Then Turn off Two Factor Authentication Icon



Scenario: User will be able to Change Password
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Password and Security
    Then Click Change password button
    Then Enter Old Password Bangladesh1#
    Then Enter New Password Sitakund1#
    Then Click on Submit Button
    Then Check the successful message
    Then Close the Change Password POPUP


Scenario: User attempts to change password with an incorrect old password
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Password and Security
    Then Click Change password button
    Then Enter Incorrect Old Password Bangladesh1#
    Then Enter New Password Sitakund1#
    Then Click on Submit Button
    Then Check the failed message
    Then Close the Change Password POPUP


Scenario: User attempts to change password to the same password
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Password and Security
    Then Click Change password button
    Then Enter Old Password Bangladesh1#
    Then Enter the Old Password as New Password Bangladesh1#
    Then Check validation error message for attempts to change password
    Then Close the Change Password POPUP

Scenario: User will be able to select language as Bangla
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Language Preference
    Then Click Language Preference
    Then click on Bangla
    Then Click on Save Update button

Scenario: User will be able to select language as English
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Language Preference
    Then Click Language Preference
    Then Click on English
    Then Click on Save Update button


Scenario: User will be able to sing out from all device
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Account Deletion
    Then Click Account Deletion
    Then Click Sing Out button
    Then Then Click on Yes, do it button
    Then Verify sing out success

Scenario: User will be able to delete the account
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign in button
    Then Click on Looking to hire
    Then Enter valid email for employer employer@mail.com
    Then Enter valid password for employer Employer@12345
    Then Click Sign in Button to login
    Then Verify the present of setting icon
    Then Click on the setting icon
    Then Verify the present of Account Deletion
    Then Click Account Deletion
    Then Click Delete button
    Then Verify sing out success


