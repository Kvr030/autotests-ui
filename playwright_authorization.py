from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator('//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    password_input = page.locator('//input[@id=":r1:"]')
    password_input.fill("password")

    page.locator('//button[@id="login-page-login-button"]').click()

    wrong_email = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email).to_be_visible()
    expect(wrong_email).to_have_text('Wrong email or password')

    page.wait_for_timeout(2000)