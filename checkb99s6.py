import os
import time

import requests # <pip3 install requests>
from mac_sys_notif import notify

TOTAL = 18


if __name__ == "__main__":
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
