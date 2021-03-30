from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import excelUtils
import logging
import time
import pytest


logger = logging.getLogger(__name__)


class Test_002_DDT_Login:
    path = ".//TestData/LoginData.xlsx"
    baseURL = ReadConfig.get_url()

    @pytest.mark.regression
    def test_login(self, setup):
        logger.info("********** Test_002_DDT_Login **********")
        logger.info("********** Verifying login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)

        self.rows = excelUtils.getRowCount(self.path, "Sheet1")
        print(f"Number of rows {self.rows}")

        status = []

        for r in range(2, self.rows + 1):
            self.username = excelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = excelUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = excelUtils.readData(self.path, 'Sheet1', r, 3)

            self.login_page.setUserName(self.username)
            self.login_page.setPassword(self.password)
            self.login_page.clickLogin()

            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected == 'pass':
                    logger.info('********** Login test passed **********')
                    self.login_page.clickLogout()
                    status.append("pass")
                elif self.expected == 'fail':
                    logger.info('********** Login test failed **********')
                    self.login_page.clickLogout()
                    status.append("fail")
            elif actual_title != expected_title:
                if self.expected == 'pass':
                    logger.info('********** Login test failed **********')
                    status.append("fail")
                elif self.expected == 'fail':
                    logger.info('********** Login test passed **********')
                    status.append("pass")

        if "fail" not in status:
            logger.info('********** Login DDT test passed **********')
            self.driver.close()
            assert True
        else:
            logger.info('********** Login DDT test failed **********')
            self.driver.close()
            assert False

        logger.info('********** End of Login DDT test **********')