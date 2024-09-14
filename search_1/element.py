import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement:
    def __get__(self, instance, owner):
        driver = instance.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.CLASS_NAME, "gLFyf"))
        element = driver.find_element(By.ID, self.locator)
        return element.get_attribute("value")

    def __set__(self, instance, value):
        driver = instance.driver
        element = driver.find_element(By.ID, self.locator)
        WebDriverWait(driver, 100).until(lambda driver: element)
        element.send_keys(value)
        time.sleep(random.choice([0.5, 0.9, 1]))
        element.send_keys(Keys.RETURN)

    def __delete__(self, instance):
        driver = instance.driver
        driver.find_element(By.ID, self.locator).clear()