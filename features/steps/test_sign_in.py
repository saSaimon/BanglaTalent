import time

from behave import given, then
from dotenv import load_dotenv
import os

load_dotenv()
username = os.environ.get('BT_USER')
password = os.environ.get('BT_PASS')


@given('User can enter to the {website}')
def enter_into_website(context, website):
    try:
        context.app.login_page.enter_to_website(url=website)
    except Exception as e:
        context.logger.error(f"Error entering website {website}: {e}")
        raise


@then('Accept all cookies')
def accept_cookies(context):
    context.app.login_page.accept_cookies()


@then('Reject All Cookies')
def reject_cookies(context):
    context.app.login_page.reject_cookies()


@then('Click on Sign in button')
def click_sign_in_button(context):
    context.app.login_page.click_sign_in_button()


@then('Click Looking For Job')
def click_next_button(context):
    context.app.login_page.click_looking_for_job()


@then('Enter valid email')
def enter_valid_email(context):
    context.app.login_page.input_email(username)


@then('Enter valid password')
def enter_valid_password(context):
    context.app.login_page.input_password(password)


@then('Click Sign in Button to login')
def click_sign_ing_button(context):
    context.app.login_page.click_sign_in_to_login()
    time.sleep(5)


@then('Enter invalid email')
def enter_valid_email(context):
    context.app.login_page.input_email(username + 'abc')


@then('Enter invalid password')
def enter_valid_password(context):
    context.app.login_page.input_password(password + 'abc')


@then('Verify Sign in is Successful')
def sign_in_successful(context):
    context.app.login_page.verify_bt_logo()


@then('Verify Sign in is Successful for employer')
def sing_in_successful_for_employer(context):
    context.app.login_page.verify_bt_logo_for_employer()


@then('Verify Login Failed')
def login_failed(context):
    context.app.login_page.verify_login_failed(context)


@then('Check Keep me sign in')
def click_checkbox(context):
    context.app.login_page.check_keep_me_sign_ing(context)


@then('Verify Email Validation is present')
def check_email_validation(context):
    context.app.login_page.check_email_validation(context)


@then('Verify Password Validation is present')
def check_email_validation(context):
    context.app.login_page.check_password_validation(context)


@then('Enter valid email for employer {email}')
def enter_valid_email(context, email):
    context.app.login_page.input_email(email)


@then('Enter valid password for employer {password}')
def enter_valid_password(context, password):
    context.app.login_page.input_password(password)
    time.sleep(45)


@then('Click on Looking to hire')
def click_looking_to_hire(context):
    context.app.login_page.click_hire()


@then('Enter invalid email for employer {email}')
def enter_valid_email(context, email):
    context.app.login_page.input_email(email)


@then('Enter invalid password for employer {password}')
def enter_valid_password(context, password):
    context.app.login_page.input_password(password)
    time.sleep(20)





