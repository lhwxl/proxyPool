from playwright.sync_api import sync_playwright

proxy_webs = ["http://www.66ip.cn/index.html",
                 "https://proxy.seofangfa.com/",
                 "https://www.89ip.cn/index.html",
                 "https://www.kuaidaili.com/free/inha/",
                 "http://ip.yqie.com/ipproxy.htm",
                 "https://ip.jiangxianli.com/",
                 "http://www.ip3366.net/free/"]


def main():
    with sync_playwright() as playwright:
        with playwright.chromium.launch(headless=False) as browser:
            with browser.new_context() as context:
                with context.new_page() as page:
                    for proxy_web in proxy_webs:
                        page.goto(proxy_web)


if __name__ == '__main__':
    main()
