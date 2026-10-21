import concurrent.futures
import time


def slow_fetch(url):
    time.sleep(2)
    return f"Fetched data from {url}"


urls = ["site.com/1", "site.com/2", "site.com/3"]


# 1. Create a pool of 3 reusable threads
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

    # 2. Submit tasks and get 'Futures' back instantly
    futures_list = [executor.submit(slow_fetch, url) for url in urls]

    # 3. As each Future completes, grab the result
    for future in concurrent.futures.as_completed(futures_list):
        print(future.result())

