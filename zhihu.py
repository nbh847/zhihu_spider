# 模拟登录知乎
import requests
from selenium import webdriver

class zhihu:
    def __init__(self):
        self.url = 'https://www.zhihu.com/'

    def get_cookies_by_network(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        input()

    def run(self):
        self.get_cookies_by_network()


if __name__ == "__main__":
    z = zhihu()
    z.run()