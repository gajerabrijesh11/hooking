import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://the-internet.herokuapp.com/login")
        await page.fill("#username", "tomsmith")
        await page.fill("#password", "SuperSecretPassword!")
        await page.click("button[type='submit']")
        await expect(page.get_by_role("heading", name="Welcome to the Secure Area.")).to_be_visible()
        await page.get_by_role("link", name="logout").click()
        
        await browser.close()

asyncio.run(main())