from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
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

    page.wait_for_timeout(5000)

    context.storage_state(path='stage_courses.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='stage_courses.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text('Courses')

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    title_no_result = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_no_result).to_be_visible()
    expect(title_no_result).to_have_text('There is no results')

    title_desc = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(title_desc).to_be_visible()
    expect(title_desc).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)
