import time

from behave import given, then


@then('Click on Sign Up button')
def sing_up_button(context):
    context.app.landing_page.click_Sing_up_button()


@then('Click on Sing Up Tab')
def click_Sing_Up_Tab(context):
    context.app.singUp_page.click_Sing_up_Tab()


@then('Verify the Create Your Account Text')
def create_your_account(context):
    context.app.singUp_page.verify_create_your_account_text(context)


@then('Verify the google icon is present')
def verify_google_icon(context):
    context.app.singUp_page.verify_google_icon()


@then('Click Google icon')
def click_google(context):
    context.app.singUp_page.click_google_icon()


@then('Verify the microsoft icon is present')
def verify_microsoft_icon(context):
    context.app.singUp_page.verify_microsoft_icon()


@then('Click Microsoft icon')
def click_microsoft(context):
    context.app.singUp_page.click_microsoft_icon()


@then('Click LinkedIn icon')
def click_LinkedIn(context):
    context.app.singUp_page.click_microsoft_icon()


@then("Verify the LinkedIn icon is present")
def Verify_LinkedIn_icon(context):
    context.app.singUp_page.verify_LinkedIn_icon()


@then("Enter valid first name {first_name}")
def input_first_name(context, first_name):
    context.app.singUp_page.input_first_name(first_name)


@then("Enter valid last name {last_name}")
def input_last_name(context, last_name):
    context.app.singUp_page.input_last_name(last_name)


@then("Enter valid DOB {DOB}")
def input_dob(context, DOB):
    context.app.singUp_page.input_dob(DOB)


@then("Enter valid phone number {phone_number}")
def input_phoneNumber(context, phone_number):
    context.app.singUp_page.input_phone_number(phone_number)


@then("Enter a valid email {email}")
def input_email(context, email):
    context.app.singUp_page.input_email(email)


@then("Enter an exist email {email}")
def input_exist_email(context, email):
    context.app.singUp_page.input_email(email)


@then("Enter an invalid email {email}")
def input_invalid_email(context, email):
    context.app.singUp_page.input_email(email)


@then("Enter a valid password {password}")
def input_password(context, password):
    context.app.singUp_page.input_password(password)


@then("click on the keep me sing in")
def keep_me_sing_in(context):
    context.app.singUp_page.click_keep_sing_in()
    time.sleep(5)


@then("click on the submit button and Verify the Sign up successful")
def submitButton(context):
    context.app.singUp_page.click_sing_up_button()
    # context.app.singUp_page.success_failed_message(context)


@then("user will navigates to  the Enter OTP page")
def enter_OTP_text(context):
    context.app.singUp_page.verify_enter_OTP_text(context)


# @then("Enter the OTP and click on the Verify button")
# def click_verify_button(context):
