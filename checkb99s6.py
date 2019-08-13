import os
import time

import requests # <pip3 install requests>

TOTAL = 18

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    
i = 1
while i <= TOTAL:
	url = "https://ww2.watch-series.co/series/brooklyn-nine-nine-season-6-episode-{}".format(i)
	page = requests.get(url)
	
	print("Checking status for Ep {:2}:  ".format(i), end = "")

	if page.status_code == 200:

		print("Exists; ", end = "")
		if "Page not found" in page.text:
			status = "Unavailable"
			print(status)
			time.sleep(60)

		else:
			status = "Available"
			print(status)
			notify("Brookly Nine-nine", "Episode {} is now available".format(i))
			i += 1

	else:
		print("Webpage is down")



"""
from urllib.request import urlopen, Request, HTTPError

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

site = input("Enter site: ")

req = Request(url=site, headers=headers) 
req.get_method = lambda: "HEAD"

try:
    urlopen(req)
    print("True")
except HTTPError:
	print("False")
"""
