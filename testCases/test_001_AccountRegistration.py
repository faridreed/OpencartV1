import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import RegisterPage
from utilities import random_string
import os
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("***test_001_AccountRegistration started***")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.logger.info("Launching Application")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("Clicking on My Account")
        self.hp.click_myaccount()
        self.hp.click_register()

        self.logger.info("Filling the registration form")
        self.rp = RegisterPage(self.driver)
        self.rp.FirstName("Jackie")
        self.rp.LastName("Chan")
        self.email = random_string.random_string_gen() + '@gmail.com'
        self.rp.Email(self.email)
        self.rp.Password("1234")
        self.rp.Agreement()
        self.rp.Submit()
        self.conf_msg = self.rp.Confirmation()
        if self.conf_msg == 'Your Account Has Been Created!':
            self.logger.info("Account registration is passed")
            assert True
            self.driver.close()
        else:
            self.logger.info("Account registration failed")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshot.png\\" + "test_account_reg.png")
            assert False
        self.logger.info("***test_001_AccountRegistration finished***")






