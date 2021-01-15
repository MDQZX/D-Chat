from time import sleep

from base.Fulei import Fulei
from base.parameter import driver


class One_use(Fulei):
    def send_message(self, value):  # 单聊发送文本消息
        ele4 = ("id", "com.didichuxing.internalapp:id/et_messages_input")
        sleep(2)# 输入得等两秒，要不太快
        self.send(ele4, value)  # 输入文本消息发送
        ele5 = ('id', 'com.didichuxing.internalapp:id/btn_send')
        self.click(ele5)

    def send_expression(self, data):  # 单聊发送表情
        self.click(data)  # 切换表情包
        ele2 = ('xpath',
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView')
        sleep(1)
        self.click(ele2)  # 点击每个表情包的第二个

    def send_VoiceMessage(self):
        ele = ('id', 'com.didichuxing.internalapp:id/ib_input_switch')
        self.click(ele)  # 点击会话中语音的button
        ele2 = ('xpath',
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')  # 长按操作
        self.Long_press(ele=ele2, x=846, y=1923)  # 长按 发送语音  X:x轴  Y：Y轴


    def send_IdCard(self):
        ele = ('id', 'com.didichuxing.internalapp:id/btn_function')  # 点击更多"+"号
        self.click(ele)
        ele2 = ('xpath', '//android.widget.ImageView[@content-desc="名片"]')  # 点击名片
        self.click(ele2)
        ele3 = ('xpath',
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')
        self.click(ele3)  # 在最近联系人中选择第一位
        ele4 = ('id', "com.didichuxing.internalapp:id/item_confirm")
        self.click(ele4)  # 点击确定发送
