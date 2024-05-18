# Snapshot Automation

This project contains a Playwright script in Python that searches for a video on YouTube, clicks on the first link, skips any ads, pauses the video, moves the slider every 10 seconds, and takes a snapshot each time. Once the length of the video is exhausted, the script stops and outputs the path to where the snapshots are saved.

Additionally, the script generates a trace of the process which can be viewed by uploading the `trace.zip` file to [Playwright Trace Viewer](https://trace.playwright.dev/).

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
Run the script:
    ```bash
    python path_to_your_script/snapshot_automation.py
    ```
    Replace `path_to_your_script` with the actual path where you saved `snapshot_automation.py`.

## Viewing the Trace

After running the script, a `trace.zip` file will be generated. You can view the trace by uploading this file to the [Playwright Trace Viewer](https://trace.playwright.dev/).

## Script Overview

The script performs the following steps:
1. Launches a Chromium browser.
2. Navigates to YouTube and searches for "Python tutorial".
3. Clicks on the first video result.
4. Skips any ad that appears.
5. Pauses the video.
6. Moves the video slider every 10 seconds and takes a snapshot each time.
7. Saves the snapshots to a directory named `snapshots`.
8. Outputs the paths to the saved snapshots.
