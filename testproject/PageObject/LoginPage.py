import sys

from selenium.webdriver.common.by import By


class Login:
    def __init__(self,swag):
        self.swag = swag

        self.uname_xpath = "//*[@placeholder='Username']"
        self.pname_xpath = "//*[@id='password']"
        self.invalidmsg_xpath = "//*[@class='login_password']"
        self.login_xpath = "//*[@id='login-button']"
        self.txtmesg = "Password for all users:"
        self.after_login = "Swag Labs"

    def input_username(self,Username):
        self.swag.find_element(By.XPATH, value= self.uname_xpath).send_keys(Username)

    def input_password(self,Password):
        self.swag.find_element(By.XPATH,value=self.pname_xpath).send_keys(Password)

    def invalidmsg(self):
       return self.swag.find_element(By.XPATH, value=self.invalidmsg_xpath).text

    def login(self):
        self.swag.find_element(By.XPATH, value= self.login_xpath).click()
