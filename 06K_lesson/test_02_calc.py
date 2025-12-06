from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    """Тест калькулятора с задержкой"""
    # Инициализация драйвера для Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие страницы
        url = ("https://bonigarcia.dev/selenium-webdriver-java/"
               "slow-calculator.html")
        driver.get(url)

        # Увеличенное время ожидания для задержки 45 секунд
        wait = WebDriverWait(driver, 50)

        # Ввод значения задержки
        delay_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажатие кнопок: 7 + 8 =
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()

        # Ожидание появления результата (через 45 секунд)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))

        # Проверка результата
        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        result = screen.text
        assert result == "15", f"Ожидался результат 15, получен {result}"

    finally:
        driver.quit()
