from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        # Заполнить форму регистрации и нажать на кнопку "Registration"
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user@gmail.com")

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        page.get_by_test_id('registration-page-registration-button').click()

        # Сохранить состояние браузера
        context.storage_state(path='./help/browser-state.json')

        # Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='./help/browser-state.json')
        page = context.new_page()

        # Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверить наличие и текст заголовка "Courses"
        title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(title).to_be_visible()
        expect(title).to_have_text("Courses")

        # Проверить наличие и текст блока "There is no results"
        info = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(info).to_be_visible()
        expect(info).to_have_text("There is no results")

        # Проверить наличие и видимость иконки пустого блока
        empty_block = page.get_by_test_id('courses-list-empty-view-icon')
        expect(info).to_be_visible()

        # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        info = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(info).to_be_visible()
        expect(info).to_have_text("Results from the load test pipeline will be displayed here")

        # Просто посмотреть на страницу, так как все выполняется очень быстро
        page.wait_for_timeout(2000)
