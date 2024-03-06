import time

from selenium.webdriver.common.by import By

from Pages.Base_Page import Page


class SettingsAndPreferences(Page):
    PasswordAndSecurity = (By.XPATH, "//button[normalize-space()='Password & Security']")
    LanguagePreferences = (By.XPATH, "//button[normalize-space()='Language Preferences']")
    AccountDeletion = (By.XPATH, "//button[normalize-space()='Account Deletion']")
    TwoFactorAuthenticationIcon = (By.XPATH, "//div/button[@role='switch']")
    ChangePasswordButton = (By.XPATH, "//button[normalize-space()='Change Password']")
    OldPassword = (By.XPATH, "//input[@id='oldPassword']")
    NewPassword = (By.XPATH, "//input[@id='newPassword']")
    SubmitButton = (By.XPATH, "//button[@type='submit']")
    SuccessOrFailedMessage = (By.XPATH, "//div[@class = 'font-bold mb-1 text-md']")
    BT_logo = (By.XPATH, "//a[@href = '/employer']")
    ValidationErrorMessage = (By.XPATH, "//div[@class='text-[12px] mt-1 select-none leading-none text-destructive']")
    CloseIcon = (By.XPATH, "(//*[name()='svg'][@class='hover:cursor-pointer'])[1]")
    BanglaLanguage = (By.XPATH, "//button[@value='bangla']")
    EnglishLanguage = (By.XPATH, "//button[@value='english']")
    SaveUpdateButton = (By.XPATH, "(//button[normalize-space()='Save Update'])[1]")
    SingOutButton = (By.XPATH, "// button[normalize-space() = 'Sign Out']")
    YesButton = (By.XPATH, "//button[normalize-space()='Yes, Do it!']")
    NoButton = (By.XPATH, "//button[normalize-space()='No']")
    SingOutSuccess = (By.XPATH, "//h1[normalize-space()='Welcome Back.']")
    DeleteButton = (By.XPATH, "//button[normalize-space()='Delete']")



    def verify_password_and_security_text_present(self, context):
        self.verify_text('Password & Security', *self.PasswordAndSecurity, context=context)

    def verify_language_preferences_text_present(self, context):
        self.verify_text('Language Preferences', *self.LanguagePreferences, context=context)

    def click_language_and_preferences(self):
        self.click(*self.LanguagePreferences)
        time.sleep(5)

    def Verify_account_deletion(self, context):
        self.verify_text('Account Deletion', *self.AccountDeletion, context=context)

    def click_account_deletion(self):
        self.click(*self.AccountDeletion)

    def turn_on_authentication_icon(self):
        self.click(*self.TwoFactorAuthenticationIcon)
        time.sleep(5)

    def turn_off_authentication_icon(self):
        self.click(*self.TwoFactorAuthenticationIcon)
        time.sleep(5)

    def click_change_password_button(self):
        self.click(*self.ChangePasswordButton)
        time.sleep(5)

    def enter_old_password(self, text):
        self.input_text(text, *self.OldPassword)

    def enter_new_password(self, text):
        self.input_text(text, *self.NewPassword)

    def click_on_submit_button(self):
        self.click(*self.SubmitButton)
        time.sleep(3)

    def verify_success_message(self, context):
        self.verify_text('Change Password Success!', *self.SuccessOrFailedMessage, context=context)

    def verify_failed_message(self, context):
        self.verify_text('Change Password Failed', *self.SuccessOrFailedMessage, context=context)

    def verify_validation_error_message(self, context):
        self.verify_text("New password can't be the same as the old password", *self.ValidationErrorMessage,
                         context=context)

    def click_POPUP(self):
        self.click(*self.CloseIcon)

    def click_bangla(self):
        self.click(*self.BanglaLanguage)

    def click_english(self):
        self.click(*self.EnglishLanguage)

    def click_save_update_button(self):
        self.click(*self.SaveUpdateButton)
        time.sleep(5)

    def click_sing_out_button(self):
        self.click(*self.SingOutButton)
        time.sleep(2)

    def click_yes_button(self):
        self.click(*self.YesButton)
        time.sleep(3)

    def verify_sing_out_success(self, context):
        self.verify_text('Welcome Back.', *self.SingOutSuccess, context=context)

    def click_on_delete_button(self):
        self.click(*self.DeleteButton)
        time.sleep(5)




