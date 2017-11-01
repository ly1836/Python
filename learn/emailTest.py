import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = 'smtp.163.com'  # 设置服务器
mail_user = "ly_1836@163.com"  # 用户名
mail_pass = "leiyang123"  # 口令

sender = "ly_1836@163.com"

receivers = ['491816301@qq.com']  # 接收邮件

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText("wdqvqvev蚊v我evevee额 额发方便他人那不如一年一头牛下标", "plain", "utf-8")

message['From'] = Header("ly3", "utf-8")

message['To'] = Header("测试2", "utf-8")

subject = "邮件测试1"

message['Subject'] = Header(subject, 'utf-8')


def send():
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("发送邮件失败")

        send()

if __name__ == "__main__":
    send()