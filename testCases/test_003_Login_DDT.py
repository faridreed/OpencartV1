import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities.customLogger import LogGen
from utilities.testProperties import ReadConfig
from utilities import XLUtils
import os


class Test_003_Login_DDT:
    baseUrl = ReadConfig().getApplicationURL()
    logger = LogGen().getLogger()

    path = os.path.abspath(os.curdir) + "\\testData\\Opencart_Login.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("*****Starting Test_003_Login_DDT*****")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.hp.click_myaccount()
            self.hp.click_login()

            self.email = XLUtils.readData(self.path, 'Sheet1',r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1',r, 2)
            self.exp_value = XLUtils.readData(self.path, 'Sheet1',r, 3)

            self.lp.login_email(self.email)
            self.lp.login_password(self.password)
            self.login_click()
            time.sleep(3)
            self.target_page = self.lp.MyAccountPageExists()

            if self.exp_value == "Valid":
                if self.target_page == True:
                    lst_status.append("Passed")
                    self.ma.logout()
                else:
                    lst_status.append("Failed")
            elif self.exp_value == "Invalid":
                if self.target_page == True:
                    lst_status.append("Failed")
                    self.ma.logout()
                else:
                    lst_status.append("Passed")

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False

        self.logger.info("*****Ending Test_003_Login_DDT*****")