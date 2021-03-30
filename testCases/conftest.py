from selenium import webdriver
import pytest


@pytest.fixture
def setup(browser):
    if (browser == 'chrome'):
        driver = webdriver.Chrome(executable_path='/Users/nicolasulmete/Downloads/chromedriver')
        print("Launching Chrome Browser")
    elif (browser == 'firefox'):
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome(executable_path='/Users/nicolasulmete/Downloads/chromedriver')
        print("Launching Chrome Browser")
    return driver


# get value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# return browser value to setup method
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


### PyTest HTML report

# add environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nicolas'


# delete/modify info from HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)