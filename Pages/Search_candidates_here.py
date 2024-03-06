from selenium.webdriver.common.by import By

from Pages.Base_Page import Page
import time


class SearchCandidatesHere(Page):
    KeyWords = (By.CSS_SELECTOR, '[name="keyword"]')
    LocationField = (By.CSS_SELECTOR, "input[placeholder='Location']")
    SearchButton = (By.XPATH, "(//button[normalize-space()='Search'])[1]")
    SalaryRange = (By.CSS_SELECTOR, 'input[type="number"]')
    NoCandidateFound = (By.XPATH, "//div[@class='my-10 text-xl font-semibold text-center']")
    Location = (By.XPATH, "//input[@placeholder='Location']")
    Locations = (By.XPATH, "//div[@class='pac-item']")

    def input_keywords(self, text):
        self.input_text(text, *self.KeyWords)

    def click_search_button(self):
        self.click(*self.SearchButton)
        time.sleep(5)

    def input_location(self, text):
        self.input_text(text, *self.Location)

    def select_location(self):
        locations = self.find_elements(*self.Locations)
        print(len(locations))

        for location in locations:
            element = location.text
            if element == 'Dhaka Bangladesh':
                self.click(element)
                break
        time.sleep(5)



