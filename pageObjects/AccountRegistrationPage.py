from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox

class RegisterPage:
    txtbox_first_name_id = "input-firstname"
    txtbox_last_name_id = "input-lastname"
    txtbox_email_id = "input-email"
    txtbox_password_id = "input-password"
    button_agree_xpath = "//input[@name='agree']"
    button_submit_xpath = "//button[normalize-space()='Continue']"
    txt_confirmation_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def FirstName(self, first_name):
        firstname_text = self.driver.find_element(By.ID, self.txtbox_first_name_id)
        firstname_text.send_keys(first_name)
    def LastName(self, last_name):
        lastname_text = self.driver.find_element(By.ID, self.txtbox_last_name_id)
        lastname_text.send_keys(last_name)
    def Email(self, email):
        email_text = self.driver.find_element(By.ID, self.txtbox_email_id)
        email_text.send_keys(email)
    def Password(self, password):
        password_text = self.driver.find_element(By.ID, self.txtbox_password_id)
        password_text.send_keys(password)
    def Agreement(self):
        self.driver.find_element(self.button_agree_xpath).click()
    def Submit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()
    def Confirmation(self):
        try:
            self.driver.find_element(By.XPATH, self.txt_confirmation_xpath).text
        except:
            None