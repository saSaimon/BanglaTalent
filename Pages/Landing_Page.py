from Pages.Base_Page import Page
import time
from selenium.webdriver.common.by import By


class LandingPage(Page):
    Logo = (By.XPATH, "//div[@class='cursor-pointer']//img[@alt='Logo']")
    FindAJob = (By.XPATH,
                '//ul[@class="bg-white sm:bg-transparent md:flex md:items-center mx-auto md:pb-0 pb-12 absolute md:static md:z-auto right-0 w-full md:w-auto md:pr-0 pr-9 transition-all duration-500 ease-in sm:transition-none top-[-490px]"]/li[1]')
    PostAJob = (By.XPATH,
                '//ul[@class="bg-white sm:bg-transparent md:flex md:items-center mx-auto md:pb-0 pb-12 absolute md:static md:z-auto right-0 w-full md:w-auto md:pr-0 pr-9 transition-all duration-500 ease-in sm:transition-none top-[-490px]"]/li[2]')
    AboutUs = (By.XPATH,
               '//ul[@class="bg-white sm:bg-transparent md:flex md:items-center mx-auto md:pb-0 pb-12 absolute md:static md:z-auto right-0 w-full md:w-auto md:pr-0 pr-9 transition-all duration-500 ease-in sm:transition-none top-[-490px]"]/li[3]')
    TitleText = (By.XPATH, "//h1[@class='mb-6 text-2xl md:text-3xl lg:text-4xl font-bold text-text-primary']")
    FindAJob2 = (By.XPATH, '//div[@class="flex items-center justify-center mt-6 gap-x-4"]/a[1]')
    PostAJob2 = (By.XPATH, '//div[@class="flex items-center justify-center mt-6 gap-x-4"]/a[2]')
    SearchBar = (By.CSS_SELECTOR,
                 '[class="grid items-center grid-cols-1 gap-4 px-4 py-3 rounded-md !bg-opacity-5 bg-text-primary md:grid-cols-4 "] ')
    JobCarts = (By.XPATH, '//div[@class="px-5 pt-4 pb-6 bg-white border border-transparent rounded-lg"]')
    TopJobPicksCarts = (
        By.XPATH,
        '//div[@class="p-4 bg-white custom-onboarding-company-card h-full border border-transparent rounded-lg"]')
    SuccessStorySlides = (By.XPATH, '//div[@class="slick-slider custom-slider slick-initialized"]/div/div/div')
    AvailableVacancies = (By.CSS_SELECTOR, '[class="text-xs md:text-base text-text-primary text-center py-4"]')
    KeyWords = (By.CSS_SELECTOR, '[name="keyword"]')
    LocationField = (By.CSS_SELECTOR, "input[placeholder='Location']")
    Locations = (By.CSS_SELECTOR, '[class="pac-item"] [class="pac-item-query"]')
    SearchButton = (By.XPATH, '//*[@id="__next"]/main/div[1]/div[3]/div/div[1]/div/div[2]/div[4]/button')
    NoJob = (By.CSS_SELECTOR, '[class="my-10 text-xl font-semibold text-center"]')
    SalaryRange = (By.CSS_SELECTOR, 'input[type="number"]')
    ApplyJobButton = (By.XPATH, '//div[@class="flex items-center gap-3 mt-4"]/button')
    ApplyYesButton = (By.XPATH, '//div[@class="flex items-center justify-center mt-8 gap-x-6"]/button[2]')
    ApplyNoButton = (By.XPATH, '//div[@class="flex items-center justify-center mt-8 gap-x-6"]/button[1]')
    FloatingSignInButton = (By.XPATH, '//div[@role="tablist"]/button[1]')
    CartTitle = (By.CSS_SELECTOR, '[class="text-xl font-medium text-secondary-foreground"]')
    ViewDetailsButton = (By.XPATH, '//div[@class="flex items-end justify-between"]/div/button')

    def logo_present(self):
        self.find_element(*self.Logo)

    def find_a_job_upper(self, context):
        self.find_element(*self.FindAJob)
        self.verify_text('Find a job', *self.FindAJob, context=context)

    def post_a_job_upper(self, context):
        self.find_element(*self.PostAJob)
        self.verify_text('Post a job', *self.PostAJob, context=context)

    def about_us(self, context):
        self.find_element(*self.AboutUs)
        self.verify_text('About us', *self.AboutUs, context=context)

    def find_a_job_lower(self, context):
        self.find_element(*self.FindAJob2)
        self.verify_text('Find a job', *self.FindAJob2, context=context)

    def post_a_job_lower(self, context):
        self.find_element(*self.PostAJob2)
        self.verify_text('Post a job', *self.PostAJob2, context=context)

    def search_bar_is_present(self):
        self.find_element(*self.SearchBar)

    def job_carts_are_present(self, context):
        self.find_elements(*self.JobCarts)
        total_carts = len(self.find_elements(*self.JobCarts))
        print(f'Total {total_carts} Carts are found')

    def top_pic_carts_are_present(self, context):
        self.find_elements(*self.TopJobPicksCarts)
        total_carts = len(self.find_elements(*self.TopJobPicksCarts))
        print(f'Total {total_carts} Top Pick Carts are found')

    def success_story_slides_are_present(self, context):
        self.find_elements(*self.SuccessStorySlides)
        total_carts = len(self.find_elements(*self.SuccessStorySlides))
        print(f'Total {total_carts} SuccessStory Slides are found')

    def click_find_a_job(self):
        self.click(*self.FindAJob)
        time.sleep(6)

    def check_available_vacancies(self):
        text = self.find_element(*self.AvailableVacancies).text
        print(text)
        if text == '0 available job vacancies here':
            print(f'Available vacancy is 0, so the click could not happen perfectly.')
            assert False

        else:
            assert True

    def input_keywords(self, text):
        self.input_text(text, *self.KeyWords)

    def input_location(self, text):
        self.input_text(text, *self.LocationField)

    def select_location_by_name_matched(self, text):
        locations = self.find_elements(*self.Locations)
        if len(locations) == 1:
            # Directly check the text of the single location element
            if locations[0].text == text:
                locations[0].click()  # Click if the text matches
        else:
            print(locations)
            for location in locations:
                place = location.text  # Directly use the .text property
                print(place)
                if text == place:
                    location.click()  # Click on the matching location
                    break  # Optional: break after the first match if only one click is intended

    def select_location_by_order(self, index):
        locations = self.find_elements(*self.Locations)
        # Check if the index is within the range of locations found
        if 0 <= index < len(locations):
            locations[index].click()
        else:
            print(f"Index {index} is out of range for the locations found.")

    def click_search(self):
        self.click(*self.SearchButton)

    def verify_job_carts_return(self, context):
        # Find job carts elements
        carts = self.find_elements(*self.JobCarts)

        # Find the 'No Job' element
        no_job_element = self.find_element(*self.NoJob)

        # Check if the 'No Jobs Found!' message is displayed
        if no_job_element:
            # Verify the text is exactly what we expect
            self.verify_text('No Jobs Found!', *self.NoJob, context=context)

            # The presence of 'No Jobs Found!' means the search functionality is working but returned no results
            # No need to assert True here, since it doesn't contribute to the test outcome;
            # instead, we could log the success or simply pass
            print('No jobs found. Search functionality is working as expected.')
        elif carts:
            # Jobs found, so we print the total number of jobs
            total_jobs = len(carts)
            print(f'Total {total_jobs} found.')

            # Similar to the 'No Jobs Found!' case, asserting True is redundant.
            # If the intention was to fail the test when jobs are found, the assertion message should be corrected.
            # Assuming the presence of jobs indicates success:
            print('Search job functionality is working as expected, jobs are found.')
        else:
            # If no jobs are found and the 'No Jobs Found!' message is not displayed, this is unexpected
            # Therefore, we raise an AssertionError to indicate a failure in the test
            raise AssertionError(
                'Search Job functionality may not be working as expected: no jobs and no message found.')

    def input_salary_range(self, text):
        self.input_text(text, *self.SalaryRange)

    def select_job_by_name_matched(self, text):
        carts_title = self.find_elements(*self.CartTitle)
        view_details_button = self.find_elements(*self.ViewDetailsButton)
        match_found = False  # Flag to track if a match was found

        for i in range(len(carts_title)):
            if text in carts_title[i].text:
                view_details_button[i].click()
                match_found = True  # Update flag to indicate a match was found
                break  # Exit the loop after finding a match

        # Assert after checking all elements, if no match was found
        assert match_found, "No job cart title matched the given text."

    def select_job_cart_by_order(self, index):
        elements = self.find_elements(*self.JobCarts)
        for i in range(len(elements)):
            if i == int(index):
                elements[i].click()

    def verify_apply_job_button(self, context):
        self.verify_text('Apply Job', *self.ApplyJobButton, context=context)

    def click_apply_job_button(self):
        time.sleep(1)
        self.click(*self.ApplyJobButton)

    def click_yes_button(self):
        time.sleep(1)
        self.click(*self.ApplyYesButton)

    def click_no_button(self):
        self.click(*self.ApplyNoButton)

    def verify_sign_in_pop_up(self, context):
        self.verify_text('Sign in', *self.FloatingSignInButton, context=context)
