import os
import time

base_url = os.path.dirname(os.getcwd())
# print(base_url)
newtime = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
screenshot_url = base_url + '/screenshot/'+newtime+'.png'
print(screenshot_url)