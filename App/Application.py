from Pages.Login_Page import LoginPage
from Pages.Landing_Page import LandingPage
from Pages.SingUp_Page import SingUpPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.landing_page = LandingPage(self.driver)
        self.singUp_page = SingUpPage(self.driver)
