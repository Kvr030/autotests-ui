from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Заполнит поле "Email" значением "user.name@gmail.com"
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user@gmail.com")

    # Заполнит поле "Username" значением "username"
    username_input = page.get_by_test_id('registration-form-username-input').locator(
        'input')
    username_input.fill("username")

    # Заполнит поле "Password" значением "password"
    password_input = page.get_by_test_id('registration-form-password-input').locator(
        'input')
    password_input.fill("password")

    # Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
    page.get_by_test_id('registration-page-registration-button').click()

    context.storage_state(path='browser-state.json')

    page.wait_for_timeout(3000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(3000)