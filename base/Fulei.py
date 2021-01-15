from appium import webdriver

from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.parameter import driver
from data.data import screenshot_url


class eleNotFindEroor(Exception):
    pass


class Fulei:
    def __init__(self, driver):
        self.driver = driver

    def find(self, ele):
        if isinstance(ele, tuple):
            print("定位元素中：方式:{0},内容:{1}".format(ele[0], ele[1]))
            try:
                wait = WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(ele))
            except:
                raise eleNotFindEroor("元素定位超时了")
            return wait
        else:
            raise ("元素定位失败格式：（'id','value')")

    def send(self, ele, c=''):
        find = self.find(ele)
        if find.is_displayed():
            find.send_keys(c)
        else:
            print("元素找不到，检查下元素是否正确")

    def click(self, ele):
        find = self.find(ele)
        if find.is_displayed():
            find.click()
        else:
            raise ("元素找不到,检查下元素是否正确")

    def back(self):
        print("正在返回")
        self.driver.back()

    def page_screenshot(self):
        try:
            print("正在截图...")
            sleep(2)
            self.driver.get_screenshot_as_file(screenshot_url)
            print('截图成功')
        except Exception as i:
            print("截图失败，报错了快去检查下", i)

    def Long_press(self,ele,x,y):  # 根据坐标发送语音
        ac = TouchAction(driver)
        self.find(ele)  # 显示等待
        ac.long_press(x=x, y=y).wait(1000).perform()

