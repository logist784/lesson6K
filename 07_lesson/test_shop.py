from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    """Тест покупки товаров в магазине с использованием Page Object"""
    # Инициализация драйвера для Firefox
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Создание объектов страниц
        login_page = LoginPage(driver)
        main_shop_page = MainShopPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Открытие сайта магазина
        login_page.open()

        # Авторизация
        login_page.login("standard_user", "secret_sauce")

        # Ожидание загрузки каталога товаров
        main_shop_page.wait_for_page_load()

        # Добавление товаров в корзину
        main_shop_page.add_product_to_cart("Sauce Labs Backpack")
        main_shop_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        main_shop_page.add_product_to_cart("Sauce Labs Onesie")

        # Переход в корзину
        main_shop_page.go_to_cart()

        # Ожидание загрузки корзины
        cart_page.wait_for_page_load()

        # Нажатие Checkout
        cart_page.click_checkout()

        # Ожидание формы
        checkout_page.wait_for_form()

        # Заполнение формы
        checkout_page.fill_form("Иван", "Петров", "123456")

        # Нажатие Continue
        checkout_page.click_continue()

        # Ожидание загрузки страницы с итоговой стоимостью
        checkout_page.wait_for_total()

        # Получение итоговой стоимости
        total_amount = checkout_page.get_total_amount()

        # Проверка итоговой суммы
        assert total_amount == "58.29", (
            f"Ожидалась сумма $58.29, получена ${total_amount}")

    finally:
        driver.quit()
