import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.home_page import HomePage
from utilities.logger import setup_logger

logger = setup_logger()


@pytest.fixture(scope="module")
def setup():
    # driver = webdriver.Chrome(executable_path='C:\\test\\chromedriver.exe')  # Adjust path as needed

    service = Service(executable_path=r"C:\test\chromedriver.exe")

    # Initialize the WebDriver with the service
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.trivago.com/en-US")
    yield driver
    driver.quit()


def test_search_japan_destination(setup):
    home_page = HomePage(setup)

    logger.info("Entering 'Jap' in the search field.")
    home_page.enter_destination("Jap")

    logger.info("Selecting Japan from the dropdown list.")
    home_page.select_destination()

    # Add assertions to validate the search results
    # Example: assert "Japan" in setup.title
