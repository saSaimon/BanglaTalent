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
    SearchBar = (By.CSS_SELECTOR, '[class="grid items-center grid-cols-1 gap-4 px-4 py-3 rounded-md !bg-opacity-5 bg-text-primary md:grid-cols-4 "] ')
    JobCarts = (By.XPATH, '//div[@class="px-5 pt-4 pb-6 bg-white border border-transparent rounded-lg"]')
    TopJobPicksCarts = (By.XPATH, '//div[@class="p-4 bg-white custom-onboarding-company-card h-full border border-transparent rounded-lg"]')
    SuccessStorySlides = (By.XPATH, '//div[@class="slick-slider custom-slider slick-initialized"]/div/div/div')

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



