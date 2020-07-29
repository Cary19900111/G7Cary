# from django.core.mail import send_mail
# def mailcode(content):
#     err = send_mail(subject='0814test', message='666666', from_email='271252074@qq.com',recipient_list=['1516945385@qq.com'], fail_silently=False)
#     print("err:{}".format(err))
#     return content
import smtplib
import datetime 
from email.mime.text import MIMEText
from .readConfig import readconfig
class SendEmailError(Exception):
    pass
def mailcode(name,content):
    try:
        server = readconfig("qq","qq_stmp")
        fromaddr= readconfig("qq","qq_username") #看配置
        toaddr = readconfig("qq","qq_toaddr") 
        pwd = readconfig("qq","qq_pwd")
        print(server)
        print(fromaddr)
        print(toaddr)
        print(pwd)
        s = smtplib.SMTP(server)
        print(2)
        msg = MIMEText(content,'plain','utf-8')
        sub_suffix = datetime.datetime.now().strftime('%Y%m%d')
        msg['Subject'] = "{}{}".format(name,sub_suffix)
        msg['From'] = fromaddr
        msg['TO'] = toaddr
        s.login(fromaddr,pwd)#须修改
        s.sendmail(fromaddr,toaddr,msg.as_string())
        s.quit()
    except Exception as err:
        raise SendEmailError("send fail,reason:{}".format(err))

if __name__ == "__main__":
    mailcode("test","test")