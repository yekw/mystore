from tkinter import *
from tkinter.messagebox import *
from MainPage import *
import pymysql


conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 470))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        self.page.destroy()
        MainPage(self.root)

    # def loginCheck(self):
    #     name = self.username.get()
    #     secret = self.password.get()
    #     cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
    #     sql = 'select * from adminLogin where adminid="%s" and adminpwd ="%s"'%(name, secret)
    #     print(sql)
    #     res = cursor.execute(sql)
    #     print(res)
    #     if res:
    #         self.page.destroy()
    #         MainPage(self.root)
    #     else:
    #         showinfo(title='错误', message='账号或密码错误！')
    #         LoginPage()

        #cursor.close()
        conn.close()