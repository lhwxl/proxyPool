import playwright.sync_api
from playwright.sync_api import sync_playwright
import parsel
from dataCLass import Data
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="log.txt",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("start getProxy.py")


def parse1(page: playwright.sync_api.Page) -> Data:
    """//*[@id="main"]/div[1]/div[2]/div[1]/table/tbody/tr"""
    
    proxys = []

    for times in range(10):
        selector = parsel.Selector(page.content())
        
        proxys_selector = selector.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tbody/tr')
        for proxy_selector in proxys_selector:
            proxy = []
            for info in proxy_selector.xpath(".//td"):
                proxy.append(info.xpath(".//text()").get())
            proxys.append(proxy)

        page.click('xpath=//*[@id="PageList"]/a[last()]')
    
    proxys = Data(proxys)
    return proxys
 

def parse2(page: playwright.sync_api.Page) -> Data:
    pass


def parse3(page: playwright.sync_api.Page) -> Data:
    pass


def parse4(page: playwright.sync_api.Page) -> Data:
    pass


def parse5(page: playwright.sync_api.Page) -> Data:
    pass


def parse6(page: playwright.sync_api.Page) -> Data:
    pass


def parse7(page: playwright.sync_api.Page) -> Data:
    pass


proxy_webs = [{"id": 1, "web": "http://www.66ip.cn/index.html", "parser": parse1},
              {"id": 2, "web": "https://proxy.seofangfa.com/", "parser": parse2},
              {"id": 3, "web": "https://www.89ip.cn/index.html", "parser": parse3},
              {"id": 4, "web": "https://www.kuaidaili.com/free/inha/", "parser": parse4},
              {"id": 5, "web": "http://ip.yqie.com/ipproxy.htm", "parser": parse5},
              {"id": 6, "web": "https://ip.jiangxianli.com/", "parser": parse6},
              {"id": 7, "web": "http://www.ip3366.net/free/", "parser": parse7}]


def main() -> None:
    with sync_playwright() as playwright:
        with playwright.chromium.launch(headless=False) as browser:
            with browser.new_context() as context:
                with context.new_page() as page:
                    for proxy_web in proxy_webs:
                        page.goto(proxy_web["web"])
                        proxy_web["parser"](page)


if __name__ == '__main__':
    main()
