from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Необходимо написать скрипт, который откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнит поле "Email" значением user.name@gmail.com
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполнит поле "Password" значением password
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    # Нажмет на кнопку "Login"
    page.get_by_test_id('login-page-login-button').click()

    # Проверит наличие алерта с текстом "Wrong email or password"
    wrong_email = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email).to_be_visible()
    expect(wrong_email).to_have_text('Wrong email or password')

    page.wait_for_timeout(3000)
