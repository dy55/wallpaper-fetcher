# Bing Wallpaper Fetcher

A simple python program for downloading Bing wallpaper and saving it locally.

## Usage Step by Step

1. **Make sure you have Python interpreter installed in your computer**

1. Customize config.json
    ```json
    {
        "destination": "Your destination folder path here",
        "url": "https://bing.com",
        "params": { "ensearch": 1, "user-agent": "chrome/83" },
        "selector": "a[id=DownloadHPImage]",
        "filebase": "BingWallpaper"
    }
    ```

2. Run main.py
