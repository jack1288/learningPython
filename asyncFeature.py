import asyncio
import time


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('ok {}'.format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)


asyncio.run(main(['url_1', 'url_1', 'url_1', 'url_1']))
