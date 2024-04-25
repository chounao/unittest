# coding=utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from time import strftime, localtime, time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from framework.log import Logger
import logging


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


def setemail(content, title, from_name, from_address, to_address, smtpserver, username, password, filename):

    # 邮件容器MIMEMultipart来标示这个邮件是多个部分组成的,创建一个带附件的实例
    msg = MIMEMultipart()
    msg['Subject'] = Header(title, 'utf-8')  # 邮件的主题，也可以说是标题
    # 这里的to_address只用于显示，必须是一个string
    msg['To'] = ','.join(to_address)
    msg['From'] = from_name
    # 邮件正文内容
    textapart = MIMEText(content, _subtype='html', _charset='utf-8')
    # html格式附件
    htmlapart = MIMEApplication(open(filename, 'rb').read())
    htmlapart.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(textapart)
    msg.attach(htmlapart)
    log.logger.info('添加附件')
    try:
        s = smtplib.SMTP_SSL(smtpserver, 465)
        # s.connect(smtpserver)
        s.login(username, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        log.logger.info('连接成功')
        # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
        s.sendmail(from_address, to_address, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        s.quit()  # 关闭连接
        log.logger.info('%s----发送邮件成功' % strftime("%Y-%m-%d-%H_%M_%S", localtime(time())))
    except Exception:
        log.logger.exception("邮件发送失败")


def sendemail(filename):
    to = ['xianlimei@cai-inc.com', 'zcy-qa111@cai-inc.com']  # 收件人，多个收件人以逗号分隔
    config = {
        "from": "jmeter@cai-inc.com",  # 邮件发送地址
        "from_name": 'UI自动化测试:',    # 邮件发送人
        "to": to,
        "smtpserver": "smtp.cai-inc.com",
        "username": "jmeter@cai-inc.com",  # 邮件发送人账号
        "password": "Lingyun123456",       # 邮件发送人密码
        "title": "疫苗Vaccine自动化测试报告--柏衣"  # 邮件主题
    }

    f = open(filename, 'rb')
    mail_body = f.read()
    f.close()
    setemail(mail_body, config['title'], config['from_name'], config['from'], config['to'],
             config['smtpserver'], config['username'], config['password'], filename)
