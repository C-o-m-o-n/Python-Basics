## How to get ***AI TRAINING DATA***
## How to get ***AI TRAINING DATA***
## Web Scraping with Python
## TODO - bypas website blockers to get the data ANYWAY!!!!

## arg that is the starting point URL
## fetch then parse for <a> anchor tags


import sys
import queue
import requests
#import threading
import asyncio


## List of URLS we need to fetch
urls = queue.Queue()

## HTML pages ready for parse
pages = queue.Queue()

async def main():
    rootUrl = sys.argv[1]
    urls.put(rootUrl)
    print(f'{rootUrl=}')

asyncio.run(main())
