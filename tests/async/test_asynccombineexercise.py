import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.saucedemo.com/")
        await page.pause()
        await page.get_by_placeholder("Username").fill("standard_user")
        await page.get_by_placeholder("Password").fill("secret_sauce")
        await page.locator("[data-test=\"login-button\"]").click()
        await expect(page.get_by_text("Swag Labs")).to_be_visible()
        await page.screenshot(path="screenshot.png")
        title = await page.title()
        print("Page Title:", title)
        await page.get_by_role("button", name="Open Menu").click()
        await page.locator("[data-test=\"logout-sidebar-link\"]").click()
        await expect(page).to_have_url("https://www.saucedemo.com/")
        print(page.url)

        
        
        
        await browser.close()

asyncio.run(main())