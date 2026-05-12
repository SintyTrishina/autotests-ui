from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    # чтобы сохранять данные в local storage создаем context
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    page.wait_for_timeout(5000)  # теперь мы можем сохранить состояние браузера (куки/ local storage)
    context.storage_state(path='browser_stage.json')  # сохранит в виде json файла

# открываем новую сессию
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # чтобы вписать данные в local storage из файла и зайти без авторизации
    context = browser.new_context(storage_state='browser_stage.json')
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)
