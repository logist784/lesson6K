from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        """Ввести имя пользователя"""
        username_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
        username_input.send_keys(username)

    def enter_password(self, password):
        """Ввести пароль"""
        password_input = self.driver.find_element(
            By.CSS_SELECTOR, "#password")
        password_input.send_keys(password)

    def click_login(self):
        """Нажать кнопку входа"""
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, "#login-button")
        login_button.click()

    def login(self, username, password):
        """Выполнить полный процесс авторизации"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
