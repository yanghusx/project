import csv
import logging
import os
import random
import re
import time

import logging
import xlrd
import pandas as pd
from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from element import BasePageElement


class MyClass:
    # 设置日志记录器
    logging.basicConfig(filename='driver.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def log_debug(message):
        logging.debug(message)

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_warning(message):
        logging.warning(message)

    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def log_critical(message):
        logging.critical(message)
class SearchElement(BasePageElement):
    locator = 'APjFqb'


class Driver:

    def __init__(self, driver_name="Chrom"):
        self.driver_options = Options()
        self.driver_options.add_experimental_option('useAutomationExtension', False)
        self.driver_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.start_get_url = "https://www.baidu.com"
        self.driver_name = driver_name
        self.open_file_path = r"C:\Users\test\Desktop\test3.xlsx"
        self.save_urls_path = r"%s\test3_%s.csv" % (os.getcwd(), time.strftime("%Y_%m_%d_%H_%M_%S"))
        self.driver_obj: WebDriver = None
        self.page_image_path = r"%s" % os.getcwd()
        self.max_page_num = 6
        self.logging_driver = MyClass()

    search_element = SearchElement()

    def get_path_time(self):
        return os.getcwd(), time.strftime("%Y_%m_%d_%H_%M_%S"), os.sep

    def time_sleep(self, num=None):
        if num:
            time.sleep(num)
        else:
            time.sleep(random.choice([0.3, 0.8, 1.5]))

    def re_compile_urls(self, link_txt):
        pattern = re.compile("(http[s]://)[.\w-]*(:\d{,8})?((?=/)|(?!/))")
        try:
            url = pattern.search('%s' % link_txt).group()
        except AttributeError:
            return None
        return url

    def get_page_urls(self, get_page_source):
        # 使用lxml XML解析器
        bs = BeautifulSoup(get_page_source, "lxml")
        # 根据class获取全部li标签，参考图1
        link_txt_list = bs.find_all("cite")
        link_list = []
        for link_txt in link_txt_list:
            url_re = self.re_compile_urls(link_txt)
            if url_re:
                link_list.append(url_re)
        return link_list

    def action_chains_page(self, driver_obj):
        for i in range(10):
            ActionChains(driver_obj).send_keys(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
            self.time_sleep()
        return driver_obj.page_source

    def open_file(self, file_path):
        file_path_r = r"%s" % file_path

        wb = xlrd.open_workbook(file_path_r)
        sh = wb.sheet_by_name("Sheet1")
        return sh

    def pandas_file(self, file_path, read_file_type="csv"):
        file_path_o = r"%s" % file_path
        print("file_path_o:%s" % file_path_o)
        if read_file_type == "csv":
            df = pd.read_csv("%s" % file_path_o)
        elif read_file_type == "xlsx":
            df = pd.read_excel("%s" % file_path_o)
        return df

    def write_to_file(self, urls):
        with open(self.save_urls_path, 'a', newline='') as csvfile:  # 使用 'a' 模式以追加而不是覆盖
            writer = csv.writer(csvfile)
            for row in urls:
                writer.writerow([row])

    def test_new_handle(self, url):
        self.driver_obj.get(url)
        self.time_sleep(1)
        # 打开新标签页并切换到新标签页
        self.driver_obj.switch_to.new_window('tab')
        self.time_sleep()
        # # 打开一个新窗口并切换到新窗口
        # self.driver_obj.switch_to.new_window('window')
        # time.sleep(2)

    def get_page_img(self, file_path):
        df_sh = self.pandas_file(file_path, read_file_type="xlsx")
        max_tab_num = 0
        path, str_time, system_sep = self.get_path_time()
        file_name = "%s%s%s" % (path, system_sep, str_time)
        os.mkdir(file_name)

        for index, row in df_sh.iterrows():
            # print(index, row.values[0])
            self.time_sleep(0.5)
            try:
                self.test_new_handle(row.values[0])
            except Exception as e:
                # print("e>>>>>>>>>%s" % e)
                print("第%s个错误，地址：%s" % (index, row.values[0]))
                self.logging_driver.log_error("INDEX_ERR %s<<<%s>>> %s" % (index, row.values[0]), e)
                continue
            self.logging_driver.log_info("SUCCESS INDEX:%s" % index)
            max_tab_num += 1
            print("####### SUCCESS INDEX:%s #######" % index)
            if max_tab_num >= self.max_page_num:
                all_handlers = self.driver_obj.window_handles
                end_handler = all_handlers[-1]
                for target_handler in all_handlers:
                    if target_handler != end_handler:
                        self.driver_obj.switch_to.window(target_handler)
                        url = self.driver_obj.current_url.split(".")[1]
                        self.driver_obj.get_screenshot_as_file(r'%s%s%s.png' % (file_name, system_sep, url))
                        self.driver_obj.close()
                self.driver_obj.switch_to.window(end_handler)
                max_tab_num = 0

    def init_driver_obj(self, driver_name):
        if self.driver_name == "Chrom":
            self.driver_obj = webdriver.Chrome(options=self.driver_options)
            self.driver_obj.set_page_load_timeout(10)
            self.driver_obj.maximize_window()
            self.start_get_url = "https://www.google.com"
        else:
            self.driver_obj = webdriver.Edge(options=self.driver_options)
        return self.driver_obj

    def send_query(self, driver_obj, file_sh):
        i = 0
        del self.search_element
        try:
            for row in range(file_sh.nrows):
                # print(sh.row_values(row))
                search_obj = file_sh.row_values(row)[0]
                self.search_element = search_obj
                get_page_source = self.action_chains_page(driver_obj)
                url_list = self.get_page_urls(get_page_source)
                self.write_to_file(url_list)
                del self.search_element
                self.time_sleep(0.5)
                # i += 1
                # if i > 1:
                #     break
        except Exception:
            print("出错关键字：%s" % search_obj)

    def driver_search(self, driver_obj):

        driver_obj.get("%s" % self.start_get_url)
        self.search_element = "fff"
        self.time_sleep(0.5)
        file_sh = self.open_file(self.open_file_path)
        self.send_query(driver_obj, file_sh)

    def start(self, page_img=False, url_file_path=None):
        self.driver = self.init_driver_obj(self.driver_name)
        if not page_img:
            self.time_sleep()
            self.driver_search(self.driver)
        else:
            self.get_page_img(url_file_path)


my_driver = Driver()

my_driver.start(page_img=True, url_file_path=r'D:\project\search_1\11.xlsx')
time.sleep(10)
