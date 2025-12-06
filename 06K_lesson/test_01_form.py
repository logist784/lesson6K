from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_form():
    """Тест формы с проверкой валидации полей"""
    # Инициализация драйвера для Edge
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    try:
        # Открытие страницы
        url = ("https://bonigarcia.dev/selenium-webdriver-java/"
               "data-types.html")
        driver.get(url)

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)

        # Заполнение формы
        first_name_selector = "input[name='first-name']"
        first_name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            first_name_selector))
        )
        first_name.send_keys("Иван")

        last_name = driver.find_element(
            By.CSS_SELECTOR, "input[name='last-name']")
        last_name.send_keys("Петров")

        address = driver.find_element(
            By.CSS_SELECTOR, "input[name='address']")
        address.send_keys("Ленина, 55-3")

        email = driver.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']")
        email.send_keys("test@skypro.com")

        phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
        phone.send_keys("+7985899998787")

        # Zip code оставляем пустым

        city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
        city.send_keys("Москва")

        country = driver.find_element(
            By.CSS_SELECTOR, "input[name='country']")
        country.send_keys("Россия")

        job_position = driver.find_element(
            By.CSS_SELECTOR, "input[name='job-position']")
        job_position.send_keys("QA")

        company = driver.find_element(
            By.CSS_SELECTOR, "input[name='company']")
        company.send_keys("SkyPro")

        # Нажатие кнопки Submit
        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Ожидание применения стилей валидации для zip-code
        wait.until(
            lambda d: "is-invalid" in d.find_element(
                By.CSS_SELECTOR, "input[name='zip-code']"
            ).get_attribute("class")
        )

        # Проверка, что поле Zip code подсвечено красным
        zip_code = driver.find_element(
            By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code_class = zip_code.get_attribute("class")
        assert "is-invalid" in zip_code_class, (
            "Поле Zip code должно быть подсвечено красным")

        # Проверка, что остальные поля подсвечены зеленым
        fields_to_check = [
            ("first-name", "First name"),
            ("last-name", "Last name"),
            ("address", "Address"),
            ("e-mail", "Email"),
            ("phone", "Phone"),
            ("city", "City"),
            ("country", "Country"),
            ("job-position", "Job position"),
            ("company", "Company")
        ]

        for field_name, field_display_name in fields_to_check:
            field = driver.find_element(
                By.CSS_SELECTOR, f"input[name='{field_name}']")
            field_class = field.get_attribute("class")
            assert "is-valid" in field_class, (
                f"Поле {field_display_name} должно быть подсвечено зеленым")

    finally:
        driver.quit()
