from selenium import webdriver
import pytest
#from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():

        driver=webdriver.Chrome(executable_path="C:\\Users\\mehaboob choudri\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.implicitly_wait(10)
        return driver
