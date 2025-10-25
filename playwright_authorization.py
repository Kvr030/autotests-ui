from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch()
    