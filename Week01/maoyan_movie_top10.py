import requests
# from bs4 import BeautifulSoup as bs
import lxml.etree
import re

user_agent = 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'
header = {'user-agent': user_agent}
myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header)

selector = lxml.etree.HTML(response.text)
film_ids = selector.xpath( '//dd/div[@class="movie-item film-channel"]/a/@data-val')
top10_ids = []
for id in film_ids:
    film_id = id.split(':')[1].replace('}', '')
    top10_ids.append(film_id)

for i in range(10):
    id = top10_ids[i]
    url = f'https://maoyan.com/films/{id}'
    print(url)
    response = requests.get(url, headers=header)
    # print(response.text)
    # break
    selector = lxml.etree.HTML(response.text)
    film_name = selector.xpath('//div[@class="movie-brief-container"]/h1/text()')[0].strip()
    film_type = ','.join(selector.xpath('//div[@class="movie-brief-container"]/ul/li/a[@class="text-link"]/text()')).replace(' ', '').strip()
    film_date = selector.xpath('//div[@class="movie-brief-container"]/ul/li[last()]/text()')[0].strip()
    film_date = re.sub("[^0-9\-\:\ ]", '', film_date)
    # print(film_name, film_type, film_date)
    row = film_name + '|' + film_type + '|' + film_date + '\n'
    with open('E:\\maoyanmovie.txt', 'a+', encoding='utf-8') as article:
        article.write(row)

# bs_info = bs(response.text, 'html.parser')
# print(bs_info)
# print(f'返回码是: {response.status_code}')
# for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
#     for atags in tags.find_all('div', attrs={'class': 'movie-hover-info'}):
#         text = []
#         for a in atags.find_all('div', attrs={'class': 'movie-hover-title'}):
#             # title = a.find('span', attrs={'class': 'name'}).text
#             s = a.text.strip('\n').strip()
#             if '主演' in s:
#                 pass
#             else:
#                 text.append(s.replace('\n', '').replace(' ', ''))
#         with open('E:\\maoyanmovie.txt', 'a+', encoding='utf-8') as article:
#             article.write('|'.join(text) + '\n')

