from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    DESTINATION_INPUT = (By.ID, "input-auto-complete")
    DROPDOWN_OPTION = (By.XPATH, '//span[@class="Qrvi3L"]')

    def enter_destination(self, destination):
        self.wait_for_element(self.DESTINATION_INPUT).send_keys(destination)

    def select_destination(self):
        self.wait_for_element(self.DROPDOWN_OPTION).click()
