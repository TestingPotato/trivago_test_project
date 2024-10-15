import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def setup():
    # Set up the Chrome WebDriver
    service = Service(executable_path=r"C:\test\chromedriver.exe")

    # Initialize the WebDriver with the service
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.trivago.com/en-US")
    driver.implicitly_wait(5)
    yield driver  # This allows the test to run using this driver instance

    # Teardown
    driver.quit()
