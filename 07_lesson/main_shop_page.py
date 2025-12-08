from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    """Page Object для главной страницы магазина"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_page_load(self):
        """Ожидание загрузки каталога товаров"""
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".inventory_list")))

    def add_product_to_cart(self, product_name):
        """Добавить товар в корзину по названию"""
        product_xpath = (
            f"//div[text()='{product_name}']/"
            "ancestor::div[@class='inventory_item']//button")
        product_button = self.driver.find_element(By.XPATH, product_xpath)
        product_button.click()

    def go_to_cart(self):
        """Перейти в корзину"""
        cart_icon = self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link")
        cart_icon.click()
