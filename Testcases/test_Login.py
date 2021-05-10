from selenium import webdriver
import pytest


from PgeObject.LoginPage import LoginPage
from Utilites.read_properties import ReadConfig



class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getuseremailL()
    password=ReadConfig.getuserpassword()


#    logger=logGen.log_gen()

    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("*********Test_001_Login********")
        self.logger.info("*********Verifying Home page title**********")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title

        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("******Home page title test is passed*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle1.png")
            self.driver.close()
            self.logger.error("******Home page title test is failed*******")
            assert False
