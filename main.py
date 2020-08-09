from fetcher import WallpaperFetcher
import json

print("Start accessing")
destination = json.load(open('./config.json'))['destination']

WallpaperFetcher().fetch(destination)

print(f"Image saved at {destination}")
print("Done")
