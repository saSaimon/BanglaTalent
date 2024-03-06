import time
from typing import Tuple

from selenium.webdriver.common.by import By

from Pages.Base_Page import Page


class AppliedJob(Page):
    SearchButton = (By.XPATH, "//button[normalize-space()='Search']")
    JObTitles = (By.XPATH, "//div[@class='text-xl font-medium text-secondary-foreground']")
    ViewDetailsButton = (By.XPATH, "//button[@type='button'][normalize-space()='View Details']")

    EmailField = (By.XPATH, "//input[@id='email']")
    CountryField = (By.XPATH, "button[role='combobox']")
    Countries = (By.XPATH, "(//div[@role='option'])")
    PhoneNumber = (By.XPATH, "//input[@id='phone']")
    # ResumePath = 'F:/nsharli.pdf'
    ResumePath = 'F:/nsharli2.pdf'
    VideoPath = 'F:/nabia.MP4'
    UploadResumeButton = (By.XPATH, "(//input[@type='file'])[1]")
    UploadVideoButton = (By.XPATH, "(//input[@type='file'])[2]")
    UploadCoverLetterButton = (By.XPATH, "(//input[@type='file'])[3]")
    BanglaTalentCheckbox = (By.XPATH, "//label[normalize-space()='BanglaTalent Resume']")
    UploadedResumeCheckbox = (By.XPATH, "//label[normalize-space()='Uploaded Resume']")
    UploadedResumeRadio = (By.XPATH, "(//button[@role='radio'])[2]")
    RadioButtons = By.XPATH, "(//button[@role='radio'])"
    FilesName = (By.XPATH, "//div[@class='text-[#D71E2A] text-sm not-italic font-normal leading-[150%]']")
    VideoIntroductionCheckBox = (By.XPATH, "//label[normalize-space()='Video Introduction']")
    VideoIntroductionRadio = (By.XPATH, "(//button[@role='radio'])[3]")
    CoverLetterCheckbox = (By.XPATH, "//label[normalize-space()='Cover Letter']")
    CoverLetterRadio = (By.XPATH, "(//button[@role='radio'])[4]")
    SubmitApplicationButton = (By.XPATH, "//button[normalize-space()='Submit Application']")
    ErrorMessage = (By.XPATH, "//div[@class='mb-1 mr-3 font-bold text-md']")
    CongratulationsMessage = (By.XPATH, "//h1[normalize-space()='Congratulations!']")
    ProfileIcon = (By.XPATH, "(//div[@class='mr-2 overflow-hidden border flex items-center justify-center border-gray-100 rounded-full shadow-sm w-9 h-9 md:w-11 md:h-11'])[2]")
    Profile = (By.XPATH, "//p[normalize-space()='Profile']")

    def click_search_button(self):
        time.sleep(2)
        self.click(*self.SearchButton)
        time.sleep(5)

    def find_job_by_name(self, text):
        jobs = self.find_elements(*self.JObTitles)
        ViewDetailsButtons = self.find_elements(*self.ViewDetailsButton)
        for i in range(len(jobs)):
            if text in jobs[i].text:
                ViewDetailsButtons[i].click()
                break
        time.sleep(5)

    def enter_a_new_email(self, text):
        self.find_element(*self.EmailField).clear()
        self.input_text(text, *self.EmailField)

    def enter_phone_number(self, text):
        self.find_element(*self.PhoneNumber).clear()
        self.input_text(text, *self.PhoneNumber)

    def upload_resume(self):
        self.find_element(*self.UploadResumeButton).send_keys(*self.ResumePath)
        time.sleep(6)

    def upload_video(self):
        self.find_element(*self.UploadVideoButton).send_keys(*self.VideoPath)
        time.sleep(10)

    def upload_cover_letter(self):
        self.find_element(*self.UploadCoverLetterButton).send_keys(*self.ResumePath)
        time.sleep(5)

    def select_BT_resume(self):
        self.click(*self.BanglaTalentCheckbox)


    def click_uploaded_resume_checkbox(self):
        self.click(*self.UploadedResumeCheckbox)
        time.sleep(5)

    def select_uploaded_resume(self):
        self.click(*self.UploadedResumeRadio)

    def select_uploaded_resume2(self, text):
        filesName = self.find_elements(*self.FilesName)
        radioButtons = self.find_elements(*self.RadioButtons)
        for i in range(len(filesName)):
            if text in filesName[i].text:
                radioButtons[i-1].click()
                break
        time.sleep(5)


    def click_video_introduction_checkbox(self):
        self.click(*self.VideoIntroductionCheckBox)

    def select_video_introduction(self):
        self.click(*self.VideoIntroductionRadio)

    def click_cover_letter_checkbox(self):
        self.click(*self.CoverLetterCheckbox)

    def select_cover_letter(self):
        self.click(*self.CoverLetterRadio)
        time.sleep(3)

    def click_submit_application_button(self):
        self.click(*self.SubmitApplicationButton)
        time.sleep(3)

    def verify_congratulations_message(self, context):
        self.verify_text('CONGRATULATIONS!', *self.CongratulationsMessage, context=context)



    def check_error_message(self, context, text):
        self.verify_text(text, *self.ErrorMessage, context=context)

    def click_on_profile_icon(self):
        self.click(*self.ProfileIcon)


    def click_profile_name(self):
        self.click(*self.Profile)
        time.sleep(20)


        
