# import allure
# import pytest
#
# from Utils.ExcelUtils import Excel
# from base.parameter import driver
# from page.one_use import One_use
#
#
# @allure.title("单聊")
# @allure.description("发送文本消息")
# @allure.step("1.进入单聊\n2.发送各种类型的文本消息")
# @allure.testcase("im.xiaojukeji.com", 'D-Chat')
# @pytest.mark.parametrize("data", Excel().getAllcase())
# def test_message(data, search_all):  # 输入框发送消息
#     # print(c['messages'])
#     print("发送{0}中...".format(data['messages_info']))
#     One_use(driver).send_message(data['messages'])
#
# @allure.step("1.进入单聊\n2.发送各种表情包类型消息")
# @allure.testcase("im.xiaojukeji.com", 'D-Chat')
# @allure.title("单聊")
# @allure.description("发送表情")
# @pytest.mark.parametrize("data", Excel().getAllcase())
# def test_stiker(data):  # 发送各个模块的表情包
#     print("发送{0}中...".format(data["sticker_info"]))
#     ele = (data['sticker_type'], data['sticker'])
#     One_use(driver).send_expression(ele)
#
#
# if __name__ == '__main__':
#     pytest.main()
