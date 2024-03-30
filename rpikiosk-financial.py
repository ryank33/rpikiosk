import webbrowser
import time

# List of URLs to open
urls = [
    "https://finviz.com/",
    "https://www.tradingview.com/chart/",
    "https://stockcharts.com/marketcarpet/"
]

# Use the default browser set in the system, assuming Chromium is the default
for url in urls:
    if urls.index(url) == 0:
        # Open the first URL
        webbrowser.open(url)
    else:
        # Open subsequent URLs in new tabs
        webbrowser.open_new_tab(url)
    # A brief pause to ensure the browser can initiate each tab properly
    time.sleep(2)
