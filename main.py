import URLResponseCheck
import multiprocessing

x = URLResponseCheck.URL()
test_urls = ['https://searx.me/'
            ,'https://searx.info/'
            ,'https://searx.me/?q=python'
            ,'https://searx.info/?q=python'
            ,'https://google.com'
            ,'https://www.google.com/search?q=python'
            ]
numtries = 100

def print_results(url, numtries):
    x.average_response_time(url, numtries)
    print('Average response time for {0} over {1} attempts: {2}'.format(url, numtries, str(x.avg_time)))

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=len(test_urls))
    results = [pool.apply_async(print_results, args=(url, numtries,)) for url in test_urls]
    for r in results:
        r.get()