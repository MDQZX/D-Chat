from time import sleep

from base.Fulei import Fulei


class One_use(Fulei):
    def send_message(self, value):  # 单聊发送文本消息
        ele4 = ("id", "com.didichuxing.internalapp:id/et_messages_input")
        self.send(ele4, value)  # 输入文本消息发送
        ele5 = ('id', 'com.didichuxing.internalapp:id/btn_send')
        self.click(ele5)

    def send_expression(self, data):  # 单聊发送表情
        self.click(data)  # 切换表情包
        ele2 = ('xpath',
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView')
        sleep(1.5)
        self.click(ele2)  # 点击每个表情包的第二个
    # def send_Voicemessage(self):
    #     try:

    def send_IdCard(self):
        print('hah')