from playwright.async_api import async_playwright

async def load_quiz_page(url):
    """Load quiz page with JavaScript execution"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            # Navigate to URL and wait for network to be idle
            await page.goto(url, wait_until="networkidle", timeout=30000)
            
            # Wait for any dynamic content to load
            await page.wait_for_timeout(2000)
            
            # Get the fully rendered HTML
            content = await page.content()
            
            await browser.close()
            return content
            
        except Exception as e:
            await browser.close()
            raise Exception(f"Failed to load page {url}: {str(e)}")