import sys
import os
sys.path.append('/home/cavisson/PycharmProjects/sel/testproject')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dash:
    def __init__(self,swag):
        self.swag = swag
        self.txt_swag_xpath = "//*[@id='header_container']/div[1]/div[2]/div"
        self.static_txtbox = "//*[@id='header_container']/div[2]/div/span/select"
        self.add_item1 = "//*[@id='add-to-cart-sauce-labs-backpack']"
        self.add_item2 = "//*[@id='add-to-cart-sauce-labs-bike-light']"
        self.con_btn = "//*[@id='shopping_cart_container']/a/span"
        self.remove_item1 = "//*[@id='remove-sauce-labs-bike-light']"
        self.add_item3 = "//*[@id='add-to-cart-sauce-labs-fleece-jacket']"
        self.check_out = "//*[@id='checkout']"
        self.adrs_name = "//*[@name='firstName']"
        self.l_name = "//*[@id='last-name']"
        self.pin = "//*[@name='postalCode']"
        self.btncon = "//*[@id='continue']"
        self.finsh = "F//*[@id='cancel']"
        self.btn_back = "//*[@id='back-to-products']"
        self.btnMenu = "//*[@id='react-burger-menu-btn']"
        self.btn_logout = "//*[@id='logout_sidebar_link']"

    def txt_swag(self):
       return self.swag.find_element(By.XPATH, value= self.txt_swag_xpath).text
    def static_txt(self):
       return Select(self.swag.find_element(By.XPATH, value=self.static_txtbox))
    def item1(self):
        self.swag.find_element(By.XPATH, value=self.add_item1).click()
    def item2(self):
        self.swag.find_element(By.XPATH ,value = self.add_item2).click()
    def cont_btn(self):
        self.swag.find_element(By.XPATH ,value = self.con_btn).click()
    def remove1(self):
        self.swag.find_element(By.XPATH ,value = self.remove_item1).click()
    def item3(self):
        self.swag.find_element(By.XPATH ,value = self.add_item3).click()
    def che_out(self):
        self.swag.find_element(By.XPATH, value=self.check_out).click()
    def name_add(self,name):
        self.swag.find_element(By.XPATH, value=self.adrs_name).send_keys(name)
    def name_last(self,lastName):
        self.swag.find_element(By.XPATH, value=self.l_name).send_keys(lastName)
    def pincod(self,Pincode):
        self.swag.find_element(By.XPATH, value=self.pin).send_keys(Pincode)
    def contButton(self):
        self.swag.find_element(By.XPATH, value=self.btncon).click()
    def btn_finish(self):
        #self.swag.find_element(By.PARTIAL_LINK_TEXT, value=self.finsh).click()
        self.swag.find_element(By.XPATH, value=self.finsh).click()
    def backBtn(self):
        self.swag.find_element(By.XPATH, value=self.btn_back).click()
    def menu(self):
        self.swag.find_element(By.XPATH, value=self.btnMenu).click()
    def logout(self):
        self.swag.find_element(By.XPATH, value=self.btn_logout).click()