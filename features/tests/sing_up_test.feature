# Created by DELL at 2/6/2024
Feature: Sing in Test Cases
  In this feature, Sing in test cases will be implemented.

  Scenario: User can Sing in with valid information
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign Up button
    Then Click next button
    Then Click on Sing Up Tab
    Then Verify the Create Your Account Text
    Then Verify the google icon is present
    Then Verify the microsoft icon is present
    Then Verify the LinkedIn icon is present
    Then Enter valid first name Nabia
    Then Enter valid last name Sharli
    Then Enter valid DOB 06/06/2006
    Then Enter valid phone number 017546856552
    Then Enter a valid email mapadek938@flexvio.com
    Then Enter a valid password Nabia@8256
    Then click on the keep me sing in
    Then click on the submit button and Verify the Sign up successful
    Then user will navigates to  the Enter OTP page
#    Then verifies the presence of the Resend Link
#    Then Enter the OTP and click on the Verify button
#    Then the OTP should be successfully verified



  Scenario: User can not Sing in with existing email
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign Up button
    Then Click next button
    Then Click on Sing Up Tab
    Then Verify the Create Your Account Text
    Then Verify the google icon is present
    Then Verify the microsoft icon is present
    Then Verify the LinkedIn icon is present
    Then Enter valid first name Nabia
    Then Enter valid last name Sharli
    Then Enter valid DOB 06/06/2006
    Then Enter valid phone number 017546856552
    Then Enter an exist email nsharli8256@gmail.com
    Then Enter a valid password Nabia@8256
    Then click on the keep me sing in
    Then click on the submit button and Verify the Sign up successful


  Scenario: User can not  Sing in with an invalid email
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign Up button
    Then Click next button
    Then Click on Sing Up Tab
    Then Verify the Create Your Account Text
    Then Verify the google icon is present
    Then Verify the microsoft icon is present
    Then Verify the LinkedIn icon is present
    Then Enter valid first name Nabia
    Then Enter valid last name Sharli
    Then Enter valid DOB 06/06/2006
    Then Enter valid phone number 017546856552
    Then Enter an invalid email nsharli8256@gmail
    Then Enter a valid password Nabia@8256
    Then click on the keep me sing in
    Then click on the submit button and Verify the Sign up successful


  Scenario: User can click all the Social media icon
    Given User can enter to the https://banglatalent.com/
    Then Accept All Cookies
    Then Click on Sign Up button
    Then Click next button
    Then Click on Sing Up Tab
    Then Verify the Create Your Account Text
    Then Verify the google icon is present
    Then Verify the microsoft icon is present
    Then Verify the LinkedIn icon is present
    Then Click Google icon
    Then Click Microsoft icon
    Then Click LinkedIn icon


