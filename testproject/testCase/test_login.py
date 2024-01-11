
import time
import pytest
import sys
import os
sel_dir = os.path.abspath(os.path.join(__file__, "../../.."))
sys.path.append(sel_dir)
from testproject.PageObject.LoginPage import Login
from testproject.testCase.logsfile import logclasss
from testproject.PageObject.Dashboard import Dash

@pytest.mark.usefixtures("setup")
class TestLogin(logclasss):

    def test_101(self):
        lg = Login(self.swag)
        log = self.getlogs()
        log.info("*************Start Test_101********")
        lg.input_username("admin")
        lg.input_password("secret_sauce")
        time.sleep(3)
        lg.login()
        log.info("*************Pass Test_101*********")
        if lg.txtmesg in lg.invalidmsg():
            assert True
        else:
            assert False
        time.sleep(3)


    def test_102(self):
        lg = Login(self.swag)
        log = self.getlogs()
        log.info("*************Start Test_102*********")
        lg.input_username("error_user")
        lg.input_password("admin")
        time.sleep(3)
        lg.login()
        if lg.txtmesg in lg.invalidmsg():
            assert True
        else:
            assert False
        time.sleep(3)
        log.info("*************Pass Test_102*********")
    
    def test_103(self):
        db = Dash(self.swag)
        lg = Login(self.swag)
        log = self.getlogs()
        log.info("*************Start Test_103*********")
        lg.input_username("error_user")
        lg.input_password("secret_sauce")
        time.sleep(3)
        lg.login()
        if lg.after_login in db.txt_swag():
            assert True
        else:
            assert False
        log.info("*************Pass Test_103*********")
    
    def test_201(self):
        lg = Login(self.swag)
        db = Dash(self.swag)
        self.test_103()
        log = self.getlogs()
        log.info("*************Start Test_201*********")
        db.item1()
        db.item2()
        db.cont_btn()
        time.sleep(3)
        db.cont_btn()

        time.sleep(3)
        db.che_out()
        time.sleep(3)

        db.name_add("Ashish")
        db.name_last("asdcf")
        db.pincod("203012")
        time.sleep(3)
        db.contButton()
        time.sleep(2)
        #logout
        db.menu()
        time.sleep(2)

        #logout
        db.logout()
        time.sleep(2)
        log.info("*************Pass Test_201*********")


