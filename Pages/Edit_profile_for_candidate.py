import time
from typing import Tuple

from selenium.webdriver.common.by import By

from Pages.Base_Page import Page


class EditProfileForCandidate(Page):
    EditIConForProfile = (By.XPATH,
                          "(//*[name()='svg'][@class='absolute cursor-pointer top-4 right-4 text-secondary-foreground hover:text-gray-500'])[1]")
    FirstName = (By.XPATH, "//input[@id='firstName']")
    LastName = (By.XPATH, "//input[@id='lastName']")
    Designation = (By.XPATH, "//input[@id='designation']")
    Phone = (By.XPATH, "//input[@id='phoneNumber']")
    CountryFiled = (By.XPATH, "(//div[@class=' css-hlgwow'])[1]")
    Countries = (By.XPATH, "//div[@class=' css-10wo9uf-option']")
    City = (By.XPATH, "(//div[@class=' css-hlgwow'])[2]")
    Cities = (By.XPATH, "//div[@role='option']")
    ZipCode = (By.XPATH, "//input[@id='zipCode']")
    LinkedIn = (By.XPATH, "//input[@id='linkedin']")
    ProfilePicturePath = 'F:/ProfilePicture.png'
    UploadProfile = (By.XPATH, "(//input[@type='file'])[1]")
    SaveChangesButton = (By.XPATH, "//button[@type='submit']")

    def click_edit_profile(self):
        self.click(*self.EditIConForProfile)
        time.sleep(5)

    def edit_first_name(self, text):
        self.find_element(*self.FirstName).clear()
        self.input_text(text, *self.FirstName)

    def edit_last_name(self, text):
        self.find_element(*self.LastName).clear()
        self.input_text(text, *self.LastName)

    def edit_designation(self, text):
        self.find_element(*self.Designation).clear()
        self.input_text(text, *self.Designation)

    def edit_phone_number(self, text):
        self.find_element(*self.Phone).clear()
        self.input_text(text, *self.Phone)

    def edit_country(self, text):
        self.click(*self.CountryFiled)
        time.sleep(3)
        countries = self.find_elements(*self.Countries)

        for i in range(len(countries)):
            if text == countries[i].text:
                countries[i].click()
                break
        time.sleep(3)

    def edit_city(self, text):
        self.click(*self.City)
        cities = self.find_elements(*self.Cities)
        for i in range(len(cities)):
            if text == cities[i].text:
                cities[i].click()
                break
        time.sleep(3)

    def edit_zip_code(self, text):
        self.find_element(*self.ZipCode).clear()
        self.input_text(text, *self.ZipCode)

    def edit_link(self, text):
        self.find_element(*self.LinkedIn).clear()
        self.input_text(text, *self.LinkedIn)

    def edit_profile_picture(self):
        self.find_element(*self.UploadProfile).send_keys('F:/ProfilePicture.png')
        time.sleep(10)

    def click_submit_button(self):
        self.click(*self.SaveChangesButton)
        time.sleep(5)
