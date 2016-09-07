#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage

class Imail:

    def __init__(self,uname,passwd,nick = ''):
        self.uname = uname
        self.passwd = passwd
        self.nick = nick
        self.mail = MIMEMultipart()

    '''
    创建一份邮件，主要创建邮件内容。images,和attachs提供路径
    '''
    def createMail(self,subject,tolist,content,images ='',attachs='',html = False):
        if html:
            cont = MIMEText(content,'plain','utf-8')
        else:
            cont = MIMEText(content,'html','utf-8')
        self.mail.attach(cont)#添加正文，文字或者HTML

        num = 0
        self.mail['to']=tolist
        self.mail['subject']=subject
        self.mail['from'] = '%s<%s>'%(self.nick,self.uname)
        self.mail['']
        #添加图片
        for image in images:
            num = num+1
            img = MIMEImage(open(image.decode('utf-8'),'rb').read())
            img.add_header('Content-ID','<image%d>'%num)
            msg.attach(img)

        #添加附件
        for attach in attachs:
            att = MIMEText(open(attach.decode('utf-8'), 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"'%attach #这里的filename可以任意写，写什么名字，邮件中显示什么名字
            self.mail.attach(att)

    '''
    收件人列表
    '''
    def sendMail(self,server = 'smtp.163.com'):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(server)
            smtp.login(self.uname,self.passwd)
            smtp.sendmail(self.mail['from'],self.mail['to'],self.mail.as_string())
            smtp.quit()
        except Exception,e:
            print e
            return False
        return True

if __name__ == '__main__':
    imail = Imail('用户名','密码')
    imail.createMail('标题','收件人','正文')
    imail.sendMail()
