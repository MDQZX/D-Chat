import pytest

import allure
from Utils.ExcelUtils import Excel
from base.parameter import driver
from page.one_use import One_use


@allure.title("单聊")
@allure.description("发送文本消息")
@allure.step("1.进入单聊\n2.发送各种类型的文本消息")
@allure.testcase("im.xiaojukeji.com", 'D-Chat')
@pytest.mark.parametrize("data", Excel().getAllcase())
def test_message(data, search_all):  # 输入框发送消息
    # print(c['messages'])
    print("发送{0}中...\n".format(data['messages_info']))
    print("-------发送{0}成功-------\n".format(data['messages_info']))
    One_use(driver).send_message(data['messages'])


@allure.step("1.进入单聊\n2.发送各种表情包类型消息")
@allure.testcase("im.xiaojukeji.com", 'D-Chat')
@allure.title("单聊")
@allure.description("发送表情")
@pytest.mark.parametrize("data", Excel().getAllcase())
def test_stiker(data):  # 发送各个模块的表情包
    print("发送{0}中...\n".format(data["sticker_info"]))
    print("-------发送{0}成功-------\n".format(data["sticker_info"]))
    ele = (data['sticker_type'], data['sticker'])
    One_use(driver).send_expression(ele)


@allure.step("1.进入单聊\n2.点击+号\n3.点击名片选择用户发送名片。")
@allure.title('单聊')
@allure.description("发送名片")
def test_IdCard(chat_more_button):
    try:
        print("发送名片中...\n")
        One_use(driver).send_IdCard()
    except Exception as i:
        raise ("发送失败请检查下\n", i)


@allure.step("1.进入单聊\n2.长按发送语音消息")
@allure.title("单聊")
@allure.description('发送语音')
@pytest.mark.skip(reason="语音目前运用是坐标定位，不适配所有机型，暂时跳过，后期想用其他办法")
def test_VoiceMessage():
    try:
        print("发送语音中...\n")
        One_use(driver).send_VoiceMessage()
    except Exception as i:
        raise ("发送失败请检查下\n", i)


@allure.step("1.进入单聊\n2.通过图片预览区发送语音消息")
@allure.title("单聊")
@allure.description('通过图片预览区发送图片')
@pytest.mark.parametrize("data", Excel().getAllcase())
def test_preview_picture(chat_more_button, data):  # 通过预览区发送图片
    try:
        print(data['name'])
        value = (data['type'], data['value'])
        One_use(driver).send_preview_picture(value)
    except Exception as i:
        raise ("发送失败请检查下\n", i)
