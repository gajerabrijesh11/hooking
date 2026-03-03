import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
        await page.click("button")
        await page.wait_for_selector("#finish h4")
        
        
        await browser.close()

asyncio.run(main())