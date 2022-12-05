#!/usr/bin/python
# -*- coding: utf-8 -*-
# Leek_Investment_Advisor@outlook.com
# leeks@sh
# Server name: smtp.office365.com
# Port: 587
# Encryption method: STARTTLS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
import smtplib,ssl


class Emails():
    def __init__(self,info):
        self.subject = u"每日行情播报"
        self.info = info

    def genEmail(self,user_name):
        self.msg = MIMEMultipart()
        self.msg['Subject'] =  self.subject
        con = MIMEText(self.genFromTemplate(user_name, self.info),'html')
        self.msg.attach(con)
    
        return self.msg
    
    def genFromTemplate(self,user_name,info):         
        data = '''<h3>你好,{{name}}</h3>
                <p>今天推荐关注的股票是：</p>
                <table border="2">
                {% for item in items -%}
                <tr> <td>{{ item.name }} </td> <td>{{ item.id }}</td> </tr>
                {% endfor %}
                </table>
        '''
        tm = Template(data)
        msg = tm.render(items=info,name=user_name)
        return msg

    
    def send(self,user_name,user_email):
        context=ssl.create_default_context()
        with smtplib.SMTP("smtp.office365.com", port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(user="Leek_Investment_Advisor@outlook.com", password="leeks@sh")
            smtp.sendmail(from_addr="Leek_Investment_Advisor@outlook.com", to_addrs=user_email, msg=self.genEmail(user_name).as_string())

if  __name__ == '__main__':
    items =[{"name":"中国平安", "id":"000001.SZ"},{"name":"三一重工", "id":"600031.SH"}]
    email = Emails(items)
    email.send("leoliu","lsl8315@163.com")

