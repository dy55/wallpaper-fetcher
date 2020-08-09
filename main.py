from fetcher import WallpaperFetcher
import json

config = json.load(open('./config.json'))

WallpaperFetcher().fetch(config['destination'])
