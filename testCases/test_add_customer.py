from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from utilities.readProperties import ReadConfig
import string
import random
import logging
import pytest

logger = logging.getLogger(__name__)


class Test_003_AddCustomer:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        logger.info("************* Login succesful **********")

        logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        logger.info("************* Saving customer info **********")
        logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))