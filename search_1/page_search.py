# import random
# import time
# import re
# import os
# import xlrd
# import xlwt
# from selenium import webdriver
# from selenium.common import StaleElementReferenceException, NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup
# # 关闭左上方 Chrome 正受到自动测试软件的控制的提示
# # options = webdriver.ChromeOptions()
# options = Options()
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# options.add_argument('lang=en_US')
# class ExcelWrite(object):
#     def __init__(self):
#         self.excel = xlwt.Workbook()  # 创建一个工作簿
#         self.sheet = self.excel.add_sheet('Sheet1')  # 创建一个工作表
#         self.excel_path = r'D:\Down\test.xlsx'
#
#     def save(self):
#         self.excel.save(self.excel_path)
#     # 写入单个值
#     def write_value(self, cell, value):
#         '''
#             - cell: 传入一个单元格坐标参数，例如：cell=(0,0),表示修改第一行第一列
#         '''
#         self.sheet.write(*cell, value)
#
#
#
#     # 写入多个值
#     def write_values(self, cells, values):
#         '''
#             - cells: 传入一个单元格坐标参数的list，
#             - values: 传入一个修改值的list，
#             例如：cells = [(0, 0), (0, 1)],values = ('a', 'b')
#             表示将列表第一行第一列和第一行第二列，分别修改为 a 和 b
#         '''
#         # 判断坐标参数和写入值的数量是否相等
#         if len(cells) == len(values):
#             for i in range(len(values)):
#                 self.write_value(cells[i], values[i])
#         else:
#             print("传参错误,单元格：%i个,写入值：%i个" % (len(cells), len(values)))
#
#
# pattern = re.compile("(http[s]://)[.\w-]*(:\d{,8})?((?=/)|(?!/))")
#
# wb = xlrd.open_workbook(r"C:\Users\test\Desktop\test3.xlsx")
# sh = wb.sheet_by_name("Sheet1")
# driver = webdriver.Chrome(options=options)
# # driver = webdriver.Firefox()
#
#
#
# def download(source):
#     # 使用lxml XML解析器
#     bs = BeautifulSoup(source, "lxml")
#     print(type(bs))
#     # 根据class获取全部li标签，参考图1
#     ul_list = bs.find_all("cite")
#     link_list = []
#     for cite_t in ul_list:
#
#         url_re = pattern.search('%s'%cite_t).group()
#         if url_re:
#             link_list.append(url_re)
#
#     return link_list
#
# def save_url_list(urls):
#     excel_obj = ExcelWrite()
#     row_num = 0
#     for url_obj in urls:
#
#         excel_obj.write_value([row_num,0],url_obj)
#         row_num+=1
#     excel_obj.save()
# driver.get("https://www.google.com")
# # driver.get("https://www.baidu.com/")
# driver.implicitly_wait(15)
# # index_search= 0
# # for row in range(sh.nrows):
# #     # print(sh.row_values(row))
# #     search_obj = sh.row_values(row)[0]
# #     print(index_search, search_obj)
# #     elem = None
# #     while not elem:
# #         try:
# #             elem = driver.find_element(By.CLASS_NAME,"gLFyf")
# #         except NoSuchElementException:
# #             driver.implicitly_wait(15)
# #     time.sleep(random.choice([0.5,1,2]))
# #     elem.send_keys(search_obj)
# #     time.sleep(random.choice([0.5,1,2]))
# #     elem.send_keys(Keys.RETURN)
# #     time.sleep(random.choice([0.5,1,2]))
# #     ActionChains(driver).send_keys(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
# #     time.sleep(random.choice([0.5,1,2]))
# #     for i in range(1):
# #         ActionChains(driver).send_keys(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
# #         time.sleep(random.choice([0.5,1]))
# #     # url_list = download(driver.page_source)
# #     #
# #     # save_url_list(url_list)
# #     index_search += 1
# #     elem.clear()
# #     break
#
#
#
# elem = None
# while not elem:
#     try:
#         elem = driver.find_element(By.CLASS_NAME,"gLFyf")
#         # elem = driver.find_element(By.CLASS_NAME,"s_ipt")
#     except NoSuchElementException:
#         time.sleep(3)
# time.sleep(random.choice([0.5,1,2]))
# elem.send_keys("feed grain")
# time.sleep(random.choice([0.5,1,2]))
# elem.send_keys(Keys.RETURN)
# time.sleep(3)
#
#
#
# elem111 = driver.find_element(By.ID,"APjFqb")
# # elem111 = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
# value = elem111.get_attribute("value")
# print(value,">>>>>>")
# # elem111 = driver.find_element(By.CLASS_NAME,"s_ipt")
# # 全选搜索框中的文本
# time.sleep(2)
# elem111.clear()
# # time.sleep(2)
# elem111.send_keys("feed grain11")
# time.sleep(2)
# url_list = download(driver.page_source)
# time.sleep(300)
# driver.close()
import time

import pandas as pd

df = pd.read_excel(r"D:\project\search_1\222.xlsx", sheet_name="Sheet1")
print(df)
for index, row in df.iterrows():
    print(index, row.values[0])

    time.sleep(2)