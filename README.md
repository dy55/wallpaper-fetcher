# Bing Wallpaper Fetcher

A simple python program for downloading Bing wallpaper and saving it locally.

> **NOTE**
> 
> Performance or function of this program may be effected due to different Bing locale websites.

## Usage Step by Step

1. **Make sure you have Python interpreter installed in your computer**

1. Customize the destination path in config.json
    ```json
    {
        "destination": "Your destination folder path here",
        "url": "https://bing.com",
        "params": { "ensearch": 1, "mkt": "zh-CN" },
        "selector": "a[id=DownloadHPImage]",
        "filebase": "BingWallpaper"
    }
    ```

2. Run main.py
    
    Double click or use command like
    ```bash
    python ./main.py
    ```