# Bing Wallpaper Fetcher

A simple python program for downloading Bing wallpaper and save it locally.

## Usage

1. Customize config.json
```json
{
    "destination": "a/b/c", // Your destination folder path here
    "url": "https://bing.com",
    "params": { "ensearch": 1, "user-agent": "chrome/83" },
    "selector": "a[id=DownloadHPImage]",
    "filebase": "BingWallpaper"
}
```

2. Run main.py