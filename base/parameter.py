

# 配置手机端自动化相关参数和驱动
from appium import webdriver
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "emulator-5554"  # adb 连接手机设备名
caps["platfromVersion"] = "6.0.1"  # Android版本
caps["appPackage"] = "com.didichuxing.internalapp" # 包名
caps["appActivity"] = "com.didi.comlab.c.main.MainActivity"
caps["autoGrantPermissions"] = True
caps["noReset"] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
