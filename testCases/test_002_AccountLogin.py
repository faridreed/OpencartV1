import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.testProperties import ReadConfig
import os


class Test_002_AccountLogin:
    baseUrl = ReadConfig().getApplicationURL()
    logger = LogGen().getLogger()

    user = ReadConfig().GetEmail()
    password = ReadConfig().GetPassword()

    @pytest.mark.sanity
    def test_account_login(self, setup):
        self.logger.info("****Test_002_AccountLogin started****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("Clicking on Login")
        self.hp = HomePage(self.driver)
        self.hp.click_myaccount()
        self.hp.click_login()

        self.logger.info("Filling the login information")
        self.lp = LoginPage(self.driver)
        self.lp.login_email(self.user)
        self.lp.login_password(self.password)
        self.logger.info("Clicking on login button")
        self.lp.login_click()
        self.target_page = self.lp.MyAccountPageExists()
        if self.target_page == True:
            self.logger.info("Account login passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Account login failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshot.png\\" + "test_login.png")
            self.driver.close()
            assert False

        self.logger.info("****Test_002_AccountLogin finished****")




