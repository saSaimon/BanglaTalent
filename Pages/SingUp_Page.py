import time

from selenium.webdriver.common.by import By

from Pages.Base_Page import Page
from Pages.Login_Page import LoginPage


class SingUpPage(Page):
    SignUpButton = (By.XPATH, '//div[@class="flex items-center md:ml-6 md:my-0 my-7 justify-center"]/a[2]')
    NextButton = (By.XPATH,
                  "//button[@class='inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary h-10 px-4 py-2 w-full']")
    SignUpButtonTab = (By.XPATH, "//button[text()='Sign Up']")
    CreateYourAccount = (By.XPATH,
                         "//div/h1[@class='lg:text-24 sm:text-22 text-20 text-secondary-foreground font-bold md:leading-[48px] leading-[43px]']")
    Google = (By.XPATH, "//button/img[@alt='google']")
    Microsoft = (By.XPATH, "//button/img[@alt='microsoft']")
    LinkedIn = (By.XPATH, "//button/img[@alt='linkedin']")
    FirstName = (By.XPATH, "//input[@id='firstName']")
    LastName = (By.XPATH, "//input[@id='lastName']")
    DatePicker = (By.XPATH, "//div/input[@placeholder='MM/DD/YYYY']")
    PhoneNumber = (By.XPATH, "//input[@id = 'phoneNumber']")
    Email = (By.XPATH, "//input[@id = 'email']")
    Password = (By.XPATH, "//input[@id = 'password']")
    isRemember = (By.XPATH, "//div/label[@for='remember']")
    SubmitButton = (By.XPATH, "//button[@type='submit']")

    SuccessOrFailedMessage = (By.XPATH, "//div[@class='text-sm opacity-90']")

    """"
    Enter OTP
    """
    EnterOTPText = (By.XPATH, "//div/h1[@class = 'font-bold lg:text-24 sm:text-22 text-20 text-secondary-foreground']")
    VerifyButton = (By.XPATH, "//button[@type= 'submit']")

    def click_Sing_up_Tab(self):
        self.click(*self.SignUpButtonTab)
        time.sleep(10)

    def verify_create_your_account_text(self, context):
        self.wait_for_element(*self.CreateYourAccount)
        self.find_element(*self.CreateYourAccount)
        self.verify_text('Create Your Account', *self.CreateYourAccount, context=context)

    def verify_google_icon(self):
        googleIcon = self.find_element(*self.Google)
        assert googleIcon.is_displayed(), f'Google icon is present and visible'

    def click_google_icon(self):
        self.click(*self.Google)
        time.sleep(5)
        self.previous_page()

    def verify_microsoft_icon(self):
        microsoftIcon = self.find_element(*self.Microsoft)
        assert microsoftIcon.is_displayed(), f'Microsoft icon is present and visible'

    def click_microsoft_icon(self):
        self.click(*self.Microsoft)
        time.sleep(5)
        self.previous_page()

    def verify_LinkedIn_icon(self):
        LinkedInIcon = self.find_element(*self.LinkedIn)
        assert LinkedInIcon.is_displayed(), f'LinkedInIcon icon is present and visible'

    def click_LinkedIn_icon(self):
        self.click(*self.LinkedIn)
        time.sleep(5)
        self.previous_page()

    def input_first_name(self, text):
        self.input_text(text, *self.FirstName)

    def input_last_name(self, text):
        self.input_text(text, *self.LastName)

    def input_dob(self, text):
        self.input_text(text, *self.DatePicker)
        time.sleep(5)

    def input_phone_number(self, text):
        self.input_text(text, *self.PhoneNumber)

    def input_email(self, text):
        self.input_text(text, *self.Email)

    def input_password(self, text):
        self.input_text(text, *self.Password)

    def click_keep_sing_in(self):
        self.click(*self.isRemember)

    def click_sing_up_button(self):
        self.click(*self.SubmitButton)
        time.sleep(10)

    def success_failed_message(self, context):
        self.find_element(*self.SuccessOrFailedMessage)
        self.verify_text('Job Seeker has been successfully registered', *self.SuccessOrFailedMessage, context=context)

    # def verify_enter_OTP_text(self, context):
    #     self.find_element(*self.EnterOTPText)
    #     self.verify_text('Enter OTP', *self.EnterOTPText, context=context)

