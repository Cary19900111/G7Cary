 #coding=utf-8
import smtplib
import datetime 
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
def mailcode(name,content,attachment=None):
    print("sending......")
    server = "smtp.qq.com"
    fromaddr= "271252074@qq.com" #须修改
    toaddr = "1516945385@qq.com" #须修改
    s = smtplib.SMTP(server)
    m = MIMEMultipart()
    msg = MIMEText(content,'plain','utf-8')
    m.attach(msg)
    if attachment!=None:
        attach_document = MIMEText(open(attachment,'r').read(),_subtype='html',_charset='gb2312')
        attach_document.add_header('Content-Disposition', 'attachment', filename=('gbk',"","testReport测试报告.html"))
        m.attach(attach_document)
    sub_suffix = datetime.datetime.now().strftime('%Y%m%d')
    m['Subject'] = "{}{}".format(name,sub_suffix)
    m["Accept-Language"]="zh-CN"
    m["Accept-Charset"]="ISO-8859-1,utf-8"
    # msg['From'] = fromaddr
    # msg['TO'] = toaddr
    s.login("271252074@qq.com","khkpwletszoccaab")#须修改
    s.sendmail(fromaddr,toaddr,m.as_string())
    s.quit()
    return content
def exe_testcase():
    # import os 
    # os.system("cd /Users/cary/Documents/go/src/git.chinawayltd.com/g7pay/pay-tests && npm run env:test -- jest --testRegex  /Users/cary/Documents/go/src/git.chinawayltd.com/g7pay/pay-tests/tests/card2/business_entry/testCreateBussinessEntry.ts")
    # path = "/Users/cary/Documents/go/src/git.chinawayltd.com/g7pay/pay-tests/dist/Reporter/report.html"
    content = "This is test"
    mailcode("daily report",content,attachment=None)
if __name__=='__main__':
    exe_testcase()

