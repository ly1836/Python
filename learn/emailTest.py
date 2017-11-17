#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText

mailto_list = "491816301@qq.com"

mail_host = "smtp.163.com"
mail_user = "ly_1836"
mail_pass = "leiyang123"
mail_postfix = "163.com"


def send_mail(to_list, sub, content):
    me = "Ryan Mok" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    # msg['To'] = ';'.join(to_list)
    msg['To'] = to_list
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print (e)
        return False


if __name__ == '__main__':
    rate = 3323 / 18658
    rate_num = float(rate * 100)
    if send_mail(mailto_list, "爬虫错误日志", "%s\n进度:%.5f%%\n进行重连..." % ("error",rate_num)):
        print("Send succeed!\n")
    else:
        print("Send failed!\n")