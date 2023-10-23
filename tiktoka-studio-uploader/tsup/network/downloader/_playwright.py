# -*- coding: utf-8 -*-
"""
Created on 2022/9/7 4:05 PM
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""

import tsup.setting as setting
import tsup.utils.tools as tools
from tsup.network.downloader.base import RenderDownloader
from tsup.network.response import Response
from tsup.utils.webdriver import WebDriverPoolPlayWright, PlaywrightAsyncDriver


class PlaywrightDownloader(RenderDownloader):
    webdriver_pool: WebDriverPoolPlayWright = None

    @property
    def _webdriver_pool(self):
        if not self.__class__.webdriver_pool:
            self.__class__.webdriver_pool = WebDriverPoolPlayWright(
                **setting.PLAYWRIGHT, driver_cls=PlaywrightAsyncDriver, thread_safe=True
            )

        return self.__class__.webdriver_pool

    def download(self, request) -> Response:
        # 代理优先级 自定义 > 配置文件 > 随机
        if request.custom_proxies:
            proxy = request.get_proxy()
        elif setting.PLAYWRIGHT.get("proxy"):
            proxy = setting.PLAYWRIGHT.get("proxy")
        else:
            proxy = request.get_proxy()

        # user_agent优先级 自定义 > 配置文件 > 随机
        if request.custom_ua:
            user_agent = request.get_user_agent()
        elif setting.PLAYWRIGHT.get("user_agent"):
            user_agent = setting.PLAYWRIGHT.get("user_agent")
        else:
            user_agent = request.get_user_agent()

        cookies = request.get_cookies()
        url = request.url
        render_time = request.render_time or setting.PLAYWRIGHT.get("render_time")
        wait_until = setting.PLAYWRIGHT.get("wait_until") or "domcontentloaded"
        if request.get_params():
            url = tools.joint_url(url, request.get_params())

        driver: PlaywrightAsyncDriver = self._webdriver_pool.get(
            user_agent=user_agent, proxy=proxy
        )
        try:
            if cookies:
                driver.url = url
                driver.cookies = cookies
            driver.page.goto(url, wait_until=wait_until)

            if render_time:
                tools.delay_time(render_time)

            html = driver.page.content()
            response = Response.from_dict(
                {
                    "url": driver.page.url,
                    "cookies": driver.cookies,
                    "_content": html.encode(),
                    "status_code": 200,
                    "elapsed": 666,
                    "headers": {
                        "User-Agent": driver.user_agent,
                        "Cookie": tools.cookies2str(driver.cookies),
                    },
                }
            )

            response.driver = driver
            response.browser = driver
            return response
        except Exception as e:
            self._webdriver_pool.remove(driver)
            raise e

    def close(self, driver):
        if driver:
            self._webdriver_pool.remove(driver)

    def put_back(self, driver):
        """
        释放浏览器对象
        """
        self._webdriver_pool.put(driver)

    def close_all(self):
        """
        关闭所有浏览器
        """
        # 不支持
        # self._webdriver_pool.close()
        pass
