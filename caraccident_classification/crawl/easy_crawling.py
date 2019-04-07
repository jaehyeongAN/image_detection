'''
Created on 2018. 1. 17.

@author: jaehyeong
'''
from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': '../data'})

google_crawler.crawl(keyword='car crash', max_num=100,
                     date_min=None, date_max=None,
                     min_size=(200,200), max_size=None)
