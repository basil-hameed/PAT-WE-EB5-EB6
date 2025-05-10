import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.guvi.in/")
    page.get_by_text("LIVE Classes", exact=True).click()
    page.get_by_role("link", name="IIT-M Pravartak Certified Full Stack Development Program (FSD) Learn Javascript").click()
    page.goto("https://www.guvi.in/zen-class/full-stack-development-course/")
    page.get_by_role("link", name="Syllabus").click()
    page.get_by_text("Module 1").click()
    expect(page.get_by_text("Syllabus Overview")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
