from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', wait_until='networkidle')
    # wait ждет полной загрузки js скриптов

    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """)  # запуск JS кода

    page.wait_for_timeout(5000)
