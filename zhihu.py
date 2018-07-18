# 模拟登录知乎
import requests
# from selenium import webdriver
from config.setting import *
from bs4 import BeautifulSoup


class zhihu:
    def __init__(self):
        # self.person_artical_url = 'https://www.zhihu.com/api/v4/members/excited-vczh/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=5&limit=15&sort_by=created'
        self.search_somebody_url = 'https://www.zhihu.com/search?q=vczh&type=people'
        self.headers = {
            'User-Agent': USERAGENT,
        }

    def get_cookies_by_network(self):
        req = requests.get(self.search_somebody_url, headers=self.headers)
        soup = BeautifulSoup(req.text, 'lxml')
        name_list = soup.find('div', class_='List').find('a', class_='UserLink-link')
        print('https:' + name_list['href'])

    def run(self):
        self.get_cookies_by_network()


if __name__ == "__main__":
    z = zhihu()
    z.run()
