import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
def sendmail_to_some():
    """第三发送测试报告"""
    # ----------1.跟发件相关的参数------
    smtpserver = "smtp.exmail.qq.com"  # 发件服务器
    port = 25  # 非SSL协议端口号
    # sender发件人账号
    sender = "chengrenzhi@021.com"
    psw = "Aa123456789!"
    #receiver收件人账号
    # receiver = "770718630@qq.com" # 单个接收人也可以是 list
    receiver = ['chengrenzhi@021.com']
    # receiver   # 多个收件人 list 对象

    # ----------2.编辑邮件的内容------
    with open('D:\project_shumai\Report\\report.html',"rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    # msg["to"] = receiver  # 收件人
    '''如果收件人是list，则使用下面的join方法'''
    msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
    msg["subject"] = "接口自动化测试"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"' #附件的名称
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port) # QQ 邮箱
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()


def main():
    sendmail_to_some()