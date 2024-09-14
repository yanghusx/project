import os
import time

from selenium import webdriver




class Descriptor:

    def __get__(self, instance, owner):
        if instance is None:
            print('__get__(): Accessing x from the class: %s,%s,%s,%s'% (self, instance,owner, instance.local))

            return self

        print('__get__(): Accessing x from the object: %s,%s,%s,%s'% (self, instance,owner, instance.local))
        return 'X from descriptor'

    def __set__(self, instance, value):
        print('__set__(): Setting x on the object', instance)
        instance.__dict__['_x'] = value


class Foo:
    local=2
    x = Descriptor()

# Foo.x

class Stu(Descriptor):
    local=2

class Main:
    def __init__(self,name):
        self.name=name
        print(self.name)
        self.url = self.func()
    std = Stu()

    def func(self):
        self.std=2
main =Main("a")
main.func()
def get_path_time():
    return os.getcwd(), time.strftime("%Y_%m_%d_%H_%M_%S"), os.sep
path, str_time, system_sep = get_path_time()
def test_new_handle():
    driver = webdriver.Chrome()
    num = 0
    for i in ["https://www.baidu.com", "https://www.google.com.hk/", "https://www.sogou.com/"]:
        print(i)
        driver.set_page_load_timeout(15)
        driver.get(i)

        time.sleep(2)
        # 打开新标签页并切换到新标签页
        driver.switch_to.new_window('tab')
        time.sleep(2)
        # # 打开一个新窗口并切换到新窗口
        # driver.switch_to.new_window('window')

        num+=1
        if num>=3:

            all_handlers = driver.window_handles
            print(all_handlers,">>>>>>")
            end_handler = all_handlers[-1]
            for target_handler in all_handlers:

                if target_handler != end_handler:
                    driver.switch_to.window(target_handler)
                    url = driver.current_url.split(".")[1]
                    print(url)
                    time.sleep(2)
                    driver.get_screenshot_as_file(r'%s_%s.png' % (time.strftime("%H_%M_%S"), url))
                    driver.close()
            time.sleep(10)

test_new_handle()
# def get_path_time():
#     return os.getcwd(), time.strftime("%Y_%m_%d_%H_%M_%S"), os.sep
# path, str_time, system_sep = get_path_time()
# 
# file_name = "%s%s%s"%(path, system_sep, str_time)
# print(file_name)
# print(os.mkdir(file_name))