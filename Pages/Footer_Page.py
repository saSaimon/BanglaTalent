import time
from typing import Tuple

import self as self
from selenium.webdriver.common.by import By

from Pages.Base_Page import Page


class FooterPage(Page):
    Company = (By.XPATH, "//p[normalize-space()='Company']")
    AboutUs = (By.XPATH, "//a[normalize-space()='About Us']")
    Jobs = (By.XPATH, "//a[normalize-space()='Jobs']")
    Help = (By.XPATH, "//a[normalize-space()='Help']")

    ContactHeading = (By.XPATH, "//p[normalize-space()='Contact']")
    contact = (By.XPATH, "//a[normalize-space()='Contact']")
    FAQ = (By.XPATH, "//a[normalize-space()='FAQ']")

    Legal = (By.XPATH, "//p[normalize-space()='Legal']")
    Privacy = (By.XPATH, "//a[normalize-space()='Privacy']")
    Disclaimer = (By.XPATH, "//a[normalize-space()='Disclaimer']")
    GDPR = (By.XPATH, "//a[normalize-space()='GDPR']")

    Copy_Rights = (By.XPATH, "//p[normalize-space()='© 2024 BanglaTalent All Rights Reserved.']")

    Facebook = (By.XPATH, "//span[normalize-space()='Facebook']")
    Tiktok = (By.XPATH, "//span[normalize-space()='Tiktok']")
    Instagram = (By.XPATH, "//span[normalize-space()='Instagram']")
    FooterLogo = (By.XPATH, "")

    def FooterLogo_present(self):
        self.find_element(*self.FooterLogo)

    def Company_present(self, context):
        time.sleep(5)
        self.find_element(*self.Company)
        self.verify_text('Company', *self.Company, context=context)

    def ContactHeading_present(self, context):
        self.find_element(*self.ContactHeading)
        self.verify_text('Contact', *self.ContactHeading, context=context)

    def Legal_present(self, context):
        self.find_element(*self.Legal)
        self.verify_text('Legal', *self.Legal, context=context)

    def Facebook_present(self):
        self.find_element(*self.Facebook)

    def Tiktok_present(self):
        self.find_element(*self.Tiktok)

    def Instagram_present(self):
        self.find_element(*self.Instagram)

    def Click_AboutUs(self):
        # self.verify_text('About Us', *self.AboutUs, context=context)
        self.click(*self.AboutUs)
        time.sleep(5)
        self.previous_page()
        time.sleep(2)

    def Click_Jobs(self):
        # self.find_element(*self.Jobs)
        # self.verify_text('Jobs', *self.Jobs, context=context)
        self.click(*self.Jobs)
        time.sleep(5)
        self.previous_page()

    def Click_Help(self):
        # self.find_element(*self.Help)
        # self.verify_text('Help', *self.Help, context=context)
        self.click(*self.Help)
        time.sleep(5)
        self.previous_page()

    def Click_contact(self):
        # self.find_element(*self.contact)
        # self.verify_text('contact', *self.contact, context=context)
        self.click(*self.contact)
        time.sleep(5)
        self.previous_page()

    def Click_FAQ(self):
        # self.find_element(*self.FAQ)
        # self.verify_text('FAQ', *self.FAQ, context=context)
        self.click(*self.FAQ)
        time.sleep(5)
        self.previous_page()

    def Click_Disclaimer(self):
        # self.find_element(*self.Disclaimer)
        # self.verify_text('Contact', *self.Disclaimer, context=context)
        self.click(*self.Disclaimer)
        time.sleep(5)
        self.previous_page()

    def Click_Privacy(self):
        # self.find_element(*self.Privacy)
        # self.verify_text('Privacy', *self.Privacy, context=context)
        self.click(*self.Privacy)
        time.sleep(5)
        self.previous_page()

    def Click_GDPR(self):
        # self.find_element(*self.GDPR)
        # self.verify_text('GDPR', *self.GDPR, context=context)
        self.click(*self.GDPR)
        time.sleep(5)
        self.previous_page()
