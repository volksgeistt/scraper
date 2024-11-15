import aiohttp
import asyncio
from datetime import datetime
import pyfiglet
from colorama import Fore, Style

author = "volksgeistt"

async def getAttachmentURL(token, guild, gChannel):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://discord.com/api/v9/guilds/{guild}/channels', headers={'Authorization': f'{token}'}) as resp:
            channels = await resp.json()
            channel = next(c for c in channels if c['id'] == str(gChannel))
            attachURL = []
            recentMsgUiD = None
            while True:
                params = {'limit': 100}
                if recentMsgUiD:
                    params['before'] = recentMsgUiD
                async with session.get(f'https://discord.com/api/v9/channels/{channel["id"]}/messages', headers={'Authorization': f'{token}'}, params=params) as resp:
                    messages = await resp.json()
                    if not messages:
                        break
                    for message in messages:
                        if 'attachments' in message:
                            for attachment in message['attachments']:
                                if attachment['content_type'] in ['image/png', 'image/jpeg', 'image/gif']:
                                    attachURL.append(attachment['url'])
                    recentMsgUiD = messages[-1]['id']
            return attachURL

async def main():
    print(Fore.GREEN + Style.BRIGHT + pyfiglet.Figlet(font='standard').renderText('Scraper') + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + f"[ Author @ {author} ]\n" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Enter your Discord token:" + Style.RESET_ALL)
    token = input()
    print(Fore.GREEN + Style.BRIGHT + "Enter the ID of the guild you want to scrape:" + Style.RESET_ALL)
    guild = int(input())
    print(Fore.GREEN + Style.BRIGHT + "Enter the ID of the channel you want to scrape:" + Style.RESET_ALL)
    gChannel = int(input())
    print(Fore.YELLOW + Style.BRIGHT + "Scraping images and GIFs from the specified channel. This may take some time." + Style.RESET_ALL)
    attachURL = await getAttachmentURL(token, guild, gChannel)
    print(Fore.BLUE + Style.BRIGHT + f"{len(attachURL)} attachment URLs found." + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Saving attachment links to 'scraped.txt'." + Style.RESET_ALL)
    with open("scraped.txt", "w") as file:
        for link in attachURL:
            file.write(link + "\n")
    print(Fore.GREEN + Style.BRIGHT + "Saving complete." + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Scraping finished." + Style.RESET_ALL)

if __name__ == '__main__':
    start_time = datetime.now()
    asyncio.run(main())
    end_time = datetime.now()
    print(Fore.YELLOW + Style.BRIGHT + f"Total Time Taken: {end_time - start_time}" + Style.RESET_ALL)
