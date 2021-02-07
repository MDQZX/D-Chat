from time import sleep

import pytest

from base.Fulei import Fulei
from base.parameter import driver

self = Fulei(driver)


@pytest.fixture(scope="module")
# 全局搜索进入单聊
def search_all():
    # 进入单聊
    ele1 = ('id', "com.didichuxing.internalapp:id/et_search")  # 点击全局搜索框
    print("点击进入搜索框")
    self.click(ele1)
    ele2 = ('id', "com.didichuxing.internalapp:id/actSearch")  # 输入搜索框输入内容
    self.send(ele2, "colinzhangjiale_v")  # 输入联系人
    ele3 = ("xpath",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")
    self.click(ele3)  # 点击进入单人会话页面
    ele4 = ("id", "com.didichuxing.internalapp:id/btn_emoticon")
    self.click(ele4)  # 点击表情icon


@pytest.fixture(scope='module')
# 会话更多按钮
def chat_more_button():
    ele = ('id', 'com.didichuxing.internalapp:id/btn_function')  # 点击更多"+"号
    self.click(ele)
