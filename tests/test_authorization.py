import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
def test_authorisation(chromium_page: Page):
    # Необходимо написать скрипт, который откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнит поле "Email" значением user.name@gmail.com
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполнит поле "Password" значением password
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    # Нажмет на кнопку "Login"
    chromium_page.get_by_test_id('login-page-login-button').click()

    # Проверит наличие алерта с текстом "Wrong email or password"
    wrong_email = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email).to_be_visible()
    expect(wrong_email).to_have_text('Wrong email or password')

    # Просто посмотреть на страницу, так как все выполняется очень быстро
    chromium_page.wait_for_timeout(3000)
