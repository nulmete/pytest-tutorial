import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
import logging

logger = logging.getLogger(__name__)


class Test_SearchCustomerByName_004:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        logger.info("************* Login succesful **********")

        logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomerPage(self.driver)
        # searchcust.clickSearchRow()
        time.sleep(2)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert status
        logger.info("***************  TC_SearchCustomerByName_004 Finished  *********** ")