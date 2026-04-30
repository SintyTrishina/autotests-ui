from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Находим ссылку Registration
    registration_link = page.get_by_test_id('login-page-registration-link')
    # Выполняем наведение курсора на ссылку
    registration_link.hover()

    # Добавляем паузу для наглядности результата
    page.wait_for_timeout(5000)
