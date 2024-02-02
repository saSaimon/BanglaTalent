import time

from selenium.webdriver.common.by import By

from Pages.Base_Page import Page


class LoginPage(Page):
    AcceptCookies = (By.XPATH, "//button[contains(text(), 'Accept All')]")
    RejectCookies = (By.XPATH, "//button[contains(text(), 'Reject All')]")
    SignInButton = (By.XPATH, "//button[contains(text(), 'Sign In')]")
    NextButton = (By.XPATH, "//button[contains(text(), 'Next')]")
    EmailField = (By.XPATH, '//div[@class="relative w-full"]/input')
    PasswordField = (By.XPATH, '//*[@id="password"]')
    SubmitButton = (By.CSS_SELECTOR, "button[type='submit']")
    BtLogo = (By.CSS_SELECTOR, '[href="/candidate"]')
    LoginFailed = (By.CSS_SELECTOR, '[class="text-sm font-semibold [&+div]:text-xs"]')
    LoginFailedCart = (By.CSS_SELECTOR, '[class="grid gap-1"]')
    KeepMeSignCheckbox = (By.CSS_SELECTOR, '[class="flex space-x-2 items-top"] button')
    PasswordValidationMessage = (By.CSS_SELECTOR, '[class="text-[12px] mt-1 select-none leading-none text-destructive"]')
    EmailValidationMessage = (By.CSS_SELECTOR, '[class="text-[12px] mt-1 select-none leading-none text-destructive"]')

    def enter_to_website(self, url):
        self.open_url(url)

    def accept_cookies(self):
        self.click(*self.AcceptCookies)

    def reject_cookies(self):
        self.click(*self.RejectCookies)

    def click_sign_in_button(self):
        self.click(*self.SignInButton)

    def click_next_button(self):
        self.click(*self.NextButton)

    def input_email(self, text):
        self.wait_for_element(*self.EmailField)
        self.input_text(text, *self.EmailField)

    def input_password(self, text):
        self.input_text(text, *self.PasswordField)

    def click_sign_in_to_login(self):
        self.click(*self.SubmitButton)

    def verify_bt_logo(self):
        self.wait_for_element(*self.BtLogo)
        element = self.find_element(*self.BtLogo)
        assert element, f'Bt logo not found so login Unsuccessful'

    def verify_login_failed(self, context):
        self.wait_for_element(*self.LoginFailedCart)
        self.verify_text('Login Failed!', *self.LoginFailed, context=context)

    def check_keep_me_sign_ing(self, context):
        self.click(*self.KeepMeSignCheckbox)

    def check_password_validation(self, context):
        self.verify_text('Password must be at least 8 characters long', *self.PasswordValidationMessage, context=context)

    def check_email_validation(self, context):
        self.verify_text('Valid email is required!', *self.EmailValidationMessage, context=context)