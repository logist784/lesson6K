from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """Открыть страницу калькулятора"""
        url = ("https://bonigarcia.dev/selenium-webdriver-java/"
               "slow-calculator.html")
        self.driver.get(url)

    def set_delay(self, delay_value):
        """Установить значение задержки"""
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_number(self, number):
        """Нажать кнопку с цифрой"""
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{number}']")
        button.click()

    def click_plus(self):
        """Нажать кнопку плюс"""
        button = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button.click()

    def click_equals(self):
        """Нажать кнопку равно"""
        button = self.driver.find_element(By.XPATH, "//span[text()='=']")
        button.click()

    def get_result(self):
        """Получить результат вычисления"""
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        screen = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text
