import asyncio
from playwright.async_api import async_playwright, TimeoutError
import os

async def main():
    async with async_playwright() as p:
         # Launching browser in headless=False mode to visualize 
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()         #new isolated browser context
        await context.tracing.start(screenshots=True, snapshots=True)
        page = await context.new_page()               #new tab is opened

        try:
            print("Starting YouTube")
            await page.goto("https://www.youtube.com")

            # print("Waiting for the search box to become visible...")
            await page.wait_for_selector("div#search-input input#search", timeout=60000) 

            # Searching for a video
            search_query = "Python Tutorial"
            print(f"Searching for: {search_query}")
            await page.fill('div#search-input input#search', search_query)


            #waiting for the query to get completely typed
            await page.wait_for_function(
                f'document.querySelector("div#search-input input#search").value === "{search_query}"'
            )
            
            await page.wait_for_selector("button#search-icon-legacy[aria-label='Search']", state='visible')
            # making sure that the button is visible

            #clicking the search button 
            await page.click("button#search-icon-legacy")
            await page.click("button#search-icon-legacy")

            # Waiting for the search results container to become visible
            # print("Waiting for the search results container to become visible...")
            await page.wait_for_selector("ytd-item-section-renderer", timeout=60000)
           
            await page.wait_for_selector("ytd-section-list-renderer", timeout=60000)
            # # Get counts of each renderer type
            # item_section_renderers = await page.query_selector_all("ytd-item-section-renderer")
            # section_list_renderers = await page.query_selector_all("ytd-section-list-renderer")
            # print(f"Number of ytd-item-section-renderer: {len(item_section_renderers)}")
            # print(f"Number of ytd-section-list-renderer: {len(section_list_renderers)}")

            # print("Clicking on the first video title...")
            video_titles = await page.query_selector_all('ytd-video-renderer a#video-title')
            if video_titles:
                await video_titles[0].scroll_into_view_if_needed()
                await video_titles[0].click()
                # to scroll if the first video not on top and then click on it
            else:
                print("No video titles found.")
                await browser.close()
                return

            # ensuring that the page is in a stable state, with no ongoing network activity
            # print("Waiting for navigation to complete...")
            await page.wait_for_load_state('networkidle')

            print("Waiting for the video to load...")
            await page.wait_for_selector("video", timeout=120000)  # 2 minute timeout
            
            # Pause the video
            print("Pausing the video...")
            video = page.locator("video")
            await video.evaluate("video => video.pause()")

            # Calculating the video duration
            duration = await video.evaluate("video => video.duration")
            print(f"Video duration: {duration} seconds")

            # Initialize the directory to save snapshots using os
            snapshot_dir = "snapshots"
            if not os.path.exists(snapshot_dir):
                os.makedirs(snapshot_dir)

            # Moving the slider every 10 seconds and take a snapshot
            print("Taking snapshots...")
            for t in range(0, int(duration), 10):
                await video.evaluate(f"video => video.currentTime = {t}")
                await page.screenshot(path=f"{snapshot_dir}/snapshot_{t}.png")
                print(f"Snapshot taken at {t} seconds")

            # path where snapshots are saved
            print(f"Snapshots saved in: {os.path.abspath(snapshot_dir)}")

        except TimeoutError:
            print(f"failed due to timeout.")

        # Stop tracing and save the trace to a file
        await context.tracing.stop(path="trace.zip")

asyncio.run(main())