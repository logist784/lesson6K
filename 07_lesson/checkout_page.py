from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_form(self):
        """Ожидание загрузки формы"""
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#first-name")))

    def enter_first_name(self, first_name):
        """Ввести имя"""
        first_name_input = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        """Ввести фамилию"""
        last_name_input = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name")
        last_name_input.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """Ввести почтовый индекс"""
        postal_code_input = self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code")
        postal_code_input.send_keys(postal_code)

    def fill_form(self, first_name, last_name, postal_code):
        """Заполнить форму данными"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        """Нажать кнопку Continue"""
        continue_button = self.driver.find_element(
            By.CSS_SELECTOR, "#continue")
        continue_button.click()

    def wait_for_total(self):
        """Ожидание загрузки страницы с итоговой стоимостью"""
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")))

    def get_total_amount(self):
        """Получить итоговую стоимость"""
        total_element = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text
        # Извлечение суммы из текста (формат: "Total: $58.29")
        total_amount = total_text.split("$")[1]
        return total_amount
