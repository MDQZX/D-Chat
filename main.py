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

def test_IdCard():
    try:
        print("发送名片中...\n")
        One_use(driver).send_IdCard()
    except Exception as i:
        print("发送名片失败，请检查！",i)
def test_VoiceMessage():
    try:
        print("发送语音中...\n")
        One_use(driver).send_VoiceMessage()
    except:
        print("发送失败请检查下\n",i)
if __name__ == '__main__':
    pytest.main()
