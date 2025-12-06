from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_shop():
    """Тест покупки товаров в магазине"""
    # Инициализация драйвера для Firefox
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Открытие сайта магазина
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        # Авторизация
        username_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
        username_input.send_keys("standard_user")

        password_input = driver.find_element(By.CSS_SELECTOR, "#password")
        password_input.send_keys("secret_sauce")

        login_button = driver.find_element(
            By.CSS_SELECTOR, "#login-button")
        login_button.click()

        # Ожидание загрузки каталога товаров
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".inventory_list")))

        # Добавление товаров в корзину
        # Sauce Labs Backpack
        backpack_xpath = ("//div[text()='Sauce Labs Backpack']/"
                          "ancestor::div[@class='inventory_item']//button")
        backpack_button = driver.find_element(By.XPATH, backpack_xpath)
        backpack_button.click()

        # Sauce Labs Bolt T-Shirt
        tshirt_xpath = ("//div[text()='Sauce Labs Bolt T-Shirt']/"
                        "ancestor::div[@class='inventory_item']//button")
        tshirt_button = driver.find_element(By.XPATH, tshirt_xpath)
        tshirt_button.click()

        # Sauce Labs Onesie
        onesie_xpath = ("//div[text()='Sauce Labs Onesie']/"
                        "ancestor::div[@class='inventory_item']//button")
        onesie_button = driver.find_element(By.XPATH, onesie_xpath)
        onesie_button.click()

        # Переход в корзину
        cart_icon = driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link")
        cart_icon.click()

        # Ожидание загрузки корзины
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".cart_list")))

        # Нажатие Checkout
        checkout_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout_button.click()

        # Ожидание формы
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#first-name")))

        # Заполнение формы
        first_name_input = driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        first_name_input.send_keys("Иван")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name_input.send_keys("Петров")

        postal_code_input = driver.find_element(
            By.CSS_SELECTOR, "#postal-code")
        postal_code_input.send_keys("123456")

        # Нажатие Continue
        continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()

        # Ожидание загрузки страницы с итоговой стоимостью
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")))

        # Чтение итоговой стоимости
        total_element = driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text

        # Извлечение суммы из текста (формат: "Total: $58.29")
        total_amount = total_text.split("$")[1]

        # Проверка итоговой суммы
        assert total_amount == "58.29", (
            f"Ожидалась сумма $58.29, получена ${total_amount}")

    finally:
        driver.quit()
