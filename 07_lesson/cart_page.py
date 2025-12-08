from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page_load(self):
        """Ожидание загрузки корзины"""
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".cart_list")))

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout_button.click()
