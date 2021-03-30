import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import logging


logger = logging.getLogger(__name__)


class Test_001_Login:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        logger.info("********** Test_001_Login **********")
        logger.info("********** Verifying home page title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title

        if title == "Your store. Login":
            logger.info("********** Home page title test passed **********")
            self.driver.close()
            assert True
        else:
            logger.error("********** Home page title test failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        logger.info("********** Test_001_Login **********")
        logger.info("********** Verifying login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        title = self.driver.title

        if title == "Dashboard / nopCommerce administration":
            logger.info("********** Login test passed **********")
            self.driver.close()
            assert True
        else:
            logger.error("********** Login test failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
