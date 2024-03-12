import time

from selenium.webdriver.common.by import By

from Pages.Base_Page import Page


class HomePageForEmployer(Page):
    PostAJobButton = (By.XPATH, "//a[@href = '/employer/post-job']/button")
    SearchIcon = (By.XPATH, "//a[@href = '/employer?keyword=']")
    MessengerIcon = (By.XPATH, "(//*[name()='svg'][@class='stroke-[1.5px]'])[2]")
    ScheduleIcon = (By.XPATH, "(//*[name()='svg'][@class='stroke-[1.5px]'])[3]")
    NotificationIcon = (By.XPATH, "(//*[name()='svg'][@class='stroke-[1.5px]'])[4]")
    SettingIcon = (By.XPATH, "(//*[name()='svg'][@class='stroke-[1.5px]'])[5]")
    SearchCandidatesHere = (By.XPATH, "//h1[normalize-space()='Search Candidates Here']")
    JobListing = (By.CSS_SELECTOR, '[class="text-[#183B56] text-[28px] not-italic font-semibold leading-[150%] my-4"]')
    ViewAllForJobListing = (By.XPATH, "(//a[@href = '/employer/job-list'])[1]")
    InboxText = (By.XPATH, "(//div[@class='text-[#193C56] text-[28px] not-italic font-semibold leading-[150%]'])[1]")
    ViewAllForMessenger = (By.XPATH, "(//a[@href='/employer/messenger'])[2]")
    CalenderText = (By.XPATH, "//div[@class='text-[#183B56] text-[28px] not-italic font-semibold leading-[150%] my-5']")
    BT_logo = (By.XPATH, "//a[@href = '/employer']")



    def verify_post_a_job_button_present(self, context):
        self.verify_text("Post a Job", *self.PostAJobButton, context=context)

    def click_post_a_job_button(self):
        self.click(*self.PostAJobButton)
        time.sleep(5)

    def verify_search_icon_present(self):
        searchIcon = self.find_element(*self.SearchIcon)
        assert searchIcon.is_displayed(), f'Search icon is present and visible'

    def click_search_icon(self):
        self.click(*self.SearchIcon)
        time.sleep(2)

    def verify_messenger_icon_present(self):
        messengerIcon = self.find_element(*self.MessengerIcon)
        assert messengerIcon.is_displayed(), f'Messenger icon is present and visible'

    def click_messenger_icon(self):
        self.click(*self.MessengerIcon)
        time.sleep(2)

    def verify_schedule_icon_present(self):
        scheduleIcon = self.find_element(*self.ScheduleIcon)
        assert scheduleIcon.is_displayed(), f'Schedule icon is present and visible'

    def click_schedule_icon(self):
        self.click(*self.ScheduleIcon)
        time.sleep(2)

    def verify_notification_icon_present(self):
        notificationIcon = self.find_element(*self.NotificationIcon)
        assert notificationIcon.is_displayed(), f'Notification icon is present and visible'


    def verify_setting_icon_present(self):
        settingIcon = self.find_element(*self.SettingIcon)
        assert settingIcon.is_displayed(), f'Setting icon is present and visible'

    def click_setting_icon(self):
        self.click(*self.SettingIcon)
        time.sleep(5)

    def back_to_home_page(self):
        self.click(*self.BT_logo)
        time.sleep(5)

    def verify_search_candidates_here_text(self, context):
        searchCandidatesText = self.find_element(*self.SearchCandidatesHere)
        self.verify_text('Search Candidates Here', *self.SearchCandidatesHere, context=context)
        # assert searchCandidatesText.is_displayed(), f'Search Candidates text is present and visible'

    def verify_job_listing_present(self, context):
        self.verify_text('Job Listings', *self.JobListing, context=context)
        time.sleep(10)

    def verify_view_all_for_job_text_present(self, context):
        self.verify_text('View All', *self.ViewAllForJobListing, context=context)

    def click_view_all_for_job(self):
        self.click(*self.ViewAllForJobListing)
        time.sleep(2)
        self.previous_page()
        time.sleep(5)

    def verify_inbox_text(self, context):
        self.verify_text('Inbox', *self.InboxText, context=context)
        time.sleep(10)

    def verify_view_all_for_messenger_present(self, context):
        self.verify_text('View All', *self.ViewAllForMessenger, context=context)

    def click_view_all_for_messenger(self):
        self.click(*self.ViewAllForMessenger)
        time.sleep(2)
        self.previous_page()
        time.sleep(5)

    def verify_calender_text_present(self, context):
        self.verify_text('Calender', *self.CalenderText, context=context)


