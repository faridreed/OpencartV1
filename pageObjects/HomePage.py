from selenium.webdriver.common.by import By

class HomePage:
    lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
    lnk_register_xpath = "//a[normalize-space()='Register']"
    lnk_login_xpath = "//a[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def click_myaccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
    def click_register(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()
    def click_login(self):
        self.driver.find_element(By.XPATH, self.lnk_login_xpath).click()