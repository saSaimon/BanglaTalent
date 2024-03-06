from Pages.Applied_Job import AppliedJob
from Pages.Edit_profile_for_candidate import EditProfileForCandidate
from Pages.Login_Page import LoginPage
from Pages.Landing_Page import LandingPage
from Pages.Footer_Page import FooterPage
from Pages.Home_page_for_employer import HomePageForEmployer
from Pages.Settings_and_preferences_for_employer import SettingsAndPreferences
from Pages.SingUp_Page import SingUpPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.landing_page = LandingPage(self.driver)
        self.footer_page = FooterPage(self.driver)
        self.singUp_page = SingUpPage(self.driver)
        self.employer_home_page = HomePageForEmployer(self.driver)
        self.settings_and_preferences = SettingsAndPreferences(self.driver)
        self.apply_job = AppliedJob(self.driver)
        self.edit_profile_for_candidate = EditProfileForCandidate(self.driver)


