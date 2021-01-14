from lxml import etree

import random
import time
import csv
import requests

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
]

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.106 Safari/537.36 "
}

url = 'http://www.gutenberg.org/ebooks/{}'
requests.adapters.DEFAULT_RETRIES = 5
session = requests.Session()
head = ['EBook_No', 'Title', 'Author', 'Language', 'Class', 'Release_date', 'Price', 'Copyright_status']
data = []
index = 0
max = 2000
with open('ebook_data.csv', 'a', newline='', encoding='utf-8')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in range(2000):
        headers['User-Agent'] = random.choice(user_agent_list)
        try:
            res = session.get(url.format(str(i + 1)), timeout=3)
        except:
            print('Data in page ' + str(i + 1) + 'obtained fail')
            continue
        selector = etree.HTML(res.text)
        data.append([])
        data[index].append(str(index + 1))
        data[index].append(selector.xpath('//*[@itemprop="headline"]/text()')[0].split('\n')[1].replace('\r', '')
                           if selector.xpath('//*[@itemprop="headline"]/text()') else '')
        data[index].append(selector.xpath('//*[@itemprop="creator"]/text()')[0]
                           if selector.xpath('//*[@itemprop="creator"]/text()') else '')
        data[index].append(selector.xpath('//*[@itemprop="inLanguage"]/td/text()')[0]
                           if selector.xpath('//*[@itemprop="inLanguage"]/td/text()') else '')
        data[index].append(selector.xpath('//*[@itemprop="inLanguage"]/following-sibling::tr[1]/td/a/text()')[0]
                           if selector.xpath('//*[@itemprop="inLanguage"]/following-sibling::tr[1]/td/a/text()') else '')
        data[index].append(selector.xpath('//*[@itemprop="datePublished"]/text()')[0]
                           if selector.xpath('//*[@itemprop="datePublished"]/text()') else '')
        data[index].append(selector.xpath('//*[@itemprop="price"]/text()')[0]
                           if selector.xpath('//*[@itemprop="price"]/text()') else '')
        data[index].append(selector.xpath('//*[@itemprop="datePublished"]/../following-sibling::tr[1]/td/text()')[0]
                           if selector.xpath(
            '//*[@itemprop="datePublished"]/../following-sibling::tr[1]/td/text()') else '')
        f_csv.writerow(data[index])
        print(data[index], '\nData in page' + str(i + 1) + 'got sucessfully')
        index += 1

