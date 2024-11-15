# Scraper
This is a Python script that scrapes images and GIFs from a specified channel.
# Features
- Fetches all image and GIF attachments from the specified Discord channel
- Saves the attachment URLs to a `scraped.txt` file
- Supports asynchronous HTTP requests for faster scraping
# Working?
1. The `getAttachmentURL` function uses the Discord API to fetch the messages from the specified channel and extract the URLs of all image and GIF attachments.
2. The `main` function prompts the user for the necessary input, calls `getAttachmentURL`, and saves the result to a file.
3. The script uses the `aiohttp` library to make asynchronous HTTP requests to the Discord API, which allows for faster scraping compared to synchronous requests.


