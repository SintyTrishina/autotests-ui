from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()  # ставит фокус на элемент

    for char in 'user@gmail.com':
        page.keyboard.type(char)

    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(5000)
