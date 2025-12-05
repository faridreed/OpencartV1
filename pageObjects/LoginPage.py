from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage:

    txtbox_email_id = "input-email"
    txtbox_password_id = "input-password"
    button_login_xpath = "//button[normalize-space()='Login']"
    msg_myaccount_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def login_email(self, email_id):
        self.email = self.driver.find_element(By.ID, self.txtbox_email_id)
        self.email.send_keys(email_id)
    def login_password(self, password_id):
        self.password = self.driver.find_element(By.ID, self.txtbox_password_id)
        self.password.send_keys(password_id)
    def login_click(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def MyAccountPageExists(self):
        try:
           return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        except:
            return False