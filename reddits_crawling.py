import requests
from bs4 import BeautifulSoup

#reddit crawling
headers = {
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
}

html = requests.get('https://reddit.com', headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

reddits = {}
tag_list = soup.select('#siteTable .top-matter > .title > a')
result = '<html><body><h2>reddits_crawling.html</h2><ol>'

for idx, tag in enumerate(tag_list, 1):
    
    key = tag.text
    value = (tag['href'] if tag['href'].find('/r/') else 'https://reddit.com{}'.format(tag['href']))
    reddits[key] = value

    result+= '<li><strong><a href={}>{}</a></strong></li>'.format(value, key)

result+='</ol></body></html>'

save_file = open('reddits_crawling.html', 'wt', encoding='utf8')
save_file.write(result)
save_file.close()

print('reddits_crawling.html이 생성되었습니다.')