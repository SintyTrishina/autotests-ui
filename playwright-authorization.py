from playwright.sync_api import sync_playwright, expect

# это контекст запуска браузера (при выходе из блока кода браузер закрывается)
with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)  # запуск браузера хром headless (False - с UI/True - без UI)
    page = chromium.new_page()  # создание новой вкладки

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')  # открыть страницу по ссылке

    email_input = page.locator(
        '//div[@data-testid="login-form-email-input"]//div//input')  # находим по локатору поле email
    email_input.fill('user.name@gmail.com')  # заполняем поле email

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill('password')

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()  # нажатие на кнопку

    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()  # ожидаем что локатор виден (проверка видимости элемента)
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")  # проверка текста внутри элемента

    page.wait_for_timeout(5000)  # playwright подождет 5 сек (НЕ ИСПОЛЬЗУЕМ В РЕАЛЬНЫХ ПРОЕКТАХ)
