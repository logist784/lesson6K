from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_calculator():
    """Тест калькулятора с использованием Page Object"""
    # Инициализация драйвера для Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Создание объекта страницы
        calculator_page = CalculatorPage(driver)

        # Открытие страницы калькулятора
        calculator_page.open()

        # Ввод значения задержки
        calculator_page.set_delay(45)

        # Нажатие кнопок: 7 + 8 =
        calculator_page.click_number(7)
        calculator_page.click_plus()
        calculator_page.click_number(8)
        calculator_page.click_equals()

        # Получение результата
        result = calculator_page.get_result()

        # Проверка результата
        assert result == "15", f"Ожидался результат 15, получен {result}"

    finally:
        driver.quit()
