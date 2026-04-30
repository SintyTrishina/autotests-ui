from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print(f'Request: {request.url}')


# Логирование ответов
def log_response(response: Response):
    print(f'Response: {response.url}')


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # передаем функцию как объект поэтому без скобок (скобки нужны для немедленного вызова функции)
    page.on('request', log_request)  # перехват события ЗАПРОС
    page.on('response', log_response)  # перехват события ОТВЕТ

 # Задержка для завершения всех запросов
    page.wait_for_timeout(3000)