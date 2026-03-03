import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.google.com")
        await page.wait_for_timeout(3000)

        title = await page.title()
        print("Page Title:", title)

        await browser.close()

asyncio.run(main())