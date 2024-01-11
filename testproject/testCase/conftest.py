import pytest
from selenium import webdriver
import configparser

@pytest.fixture
def setup(request):
    import time
    request.cls.swag = webdriver.Firefox()
    request.cls.swag.maximize_window()
    request.cls.swag.get("https://www.saucedemo.com/")
    yield
    request.cls.swag.quit()
