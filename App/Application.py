from Pages.Login_Page import LoginPage
from Pages.Landing_Page import LandingPage
from Pages.Footer_Page import FooterPage, FooterPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.landing_page = LandingPage(self.driver)
        self.footer_page = FooterPage(self.driver)
