# Snapshot Automation

This contains a Playwright script in Python that searches for a video on YouTube, clicks on the first link, skips any ads, pauses the video, moves the slider every 10 seconds, and takes a snapshot each time. Once the length of the video is exhausted, the script stops and outputs the path to where the snapshots are saved.

Additionally, the script generates a trace of the process which can be viewed by uploading the `trace.zip` file to [Playwright Trace Viewer](https://trace.playwright.dev/) which I used for debugging purpose.
The browser works in headless=False mode; therefore, you can visualize the snapshot automation.

## Installation

1. Install Playwright:
    ```bash
    pip install playwright
    ```
2. Install Playwright browsers:
    ```bash
    python -m playwright install
    ```

## Usage
1. Run the script:
    ```bash
    python path_to_your_script/snapshot_automation.py
    ```
