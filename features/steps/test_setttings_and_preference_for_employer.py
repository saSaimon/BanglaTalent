import time

from behave import given, then, when


@then("Turn On Two Factor Authentication Icon")
def turn_on_authentication_icon(context):
    context.app.settings_and_preferences.turn_on_authentication_icon()


@then("Turn off Two Factor Authentication Icon")
def turn_off_authentication_icon(context):
    context.app.settings_and_preferences.turn_off_authentication_icon()


@then("Click Change password button")
def click_change_password_button(context):
    context.app.settings_and_preferences.click_change_password_button()


@then("Enter Old Password {OldPassword}")
def step_impl(context, OldPassword):
    context.app.settings_and_preferences.enter_old_password(OldPassword)


@then("Enter New Password {NewPassword}")
def enter_new_password(context, NewPassword):
    context.app.settings_and_preferences.enter_new_password(NewPassword)


@then("Click on Submit Button")
def click_on_submit_button(context):
    context.app.settings_and_preferences.click_on_submit_button()


@then("Check the successful message")
def verify_success_message(context):
    context.app.settings_and_preferences.verify_success_message(context)


@then("Enter Incorrect Old Password {IncorrectPassword}")
def Enter_incorrect_old_password(context, IncorrectPassword):
    context.app.settings_and_preferences.enter_old_password(IncorrectPassword)


@then("Enter the Old Password as New Password {Password}")
def Enter_old_pass_as_new_pass(context, Password):
    context.app.settings_and_preferences.enter_new_password(Password)


@then("Verify the present of Password and Security")
def verify_password_and_security_text_present(context):
    context.app.settings_and_preferences.verify_password_and_security_text_present(context)


@then("Check the failed message")
def verify_failed_message(context):
    context.app.settings_and_preferences.verify_failed_message(context)
    time.sleep(5)


@then("Check validation error message for attempts to change password")
def verify_validation_error_message(context):
    context.app.settings_and_preferences.verify_validation_error_message(context)


@then("Close the Change Password POPUP")
def click_POPUP(context):
    context.app.settings_and_preferences.click_POPUP()
    time.sleep(2)


@then("Verify the present of Language Preference")
def verify_language_preferences_text_present(context):
    context.app.settings_and_preferences.verify_language_preferences_text_present(context)


@then("Click Language Preference")
def click_language_and_preferences(context):
    context.app.settings_and_preferences.click_language_and_preferences()


@then("click on Bangla")
def click_bangla(context):
    context.app.settings_and_preferences.click_bangla()


@then("Click on English")
def click_english(context):
    context.app.settings_and_preferences.click_english()


@then("Click on Save Update button")
def click_save_update_button(context):
    context.app.settings_and_preferences.click_save_update_button()


@then("Verify the present of Account Deletion")
def Verify_account_deletion(context):
    context.app.settings_and_preferences.Verify_account_deletion(context)


@then("Click Account Deletion")
def click_account_deletion(context):
    context.app.settings_and_preferences.click_account_deletion()
    time.sleep(5)


@then("Click Sing Out button")
def click_sing_out_button(context):
    context.app.settings_and_preferences.click_sing_out_button()


@then("Then Click on Yes, do it button")
def click_yes_button(context):
    context.app.settings_and_preferences.click_yes_button()


@then("Verify sing out success")
def verify_sing_out_success(context):
    context.app.settings_and_preferences.verify_sing_out_success(context)


@then("Click Delete button")
def click_on_delete_button(context):
    context.app.settings_and_preferences.click_on_delete_button()