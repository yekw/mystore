from distutils.util import execute
from tkinter import *
import pymysql
from tkinter.messagebox import *
 #from tkinter import ttk
#from tkinter import messagebox as msgbox

#####管理员
class addmanageFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.manageID = StringVar()
        self.managePwd = StringVar()
        self.manageName = StringVar()
        self.managePhone = StringVar()
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='管理员ID').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.manageID).grid(row=1, column=1, stick=E)
        Label(self, text='密码').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.managePwd).grid(row=2, column=1, stick=E)
        Label(self, text='管理员姓名').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.manageName).grid(row=3, column=1, stick=E)
        Label(self, text='联系方式').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.managePhone).grid(row=4, column=1, stick=E)
        Button(self, text='录入', command=self.insert).grid(row=6, column=1, stick=E, pady=10)
        #Button(self, text='清除', command=None).grid(row=6, column=1, stick= W, pady=10)

    def insert(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        adid=self.manageID.get()
        adpwd=self.managePwd.get()
        adname=self.manageName.get()
        adphone=self.managePhone.get()
        check="select adminid from adminLogin where adminid='%s' "
        res=cursor.execute(check %(adid))
        if res:
            showinfo(title='错误', message='管理员ID已被使用！')
        # quchong='delete from adminLogin where adminid in(select adminname from adminLogin group ' \
        #         'by adminname having(adminname)>1) and adminid not in (select min(adminid) from ' \
        #         'adminLogin group by adminname having count(adminname)>1);'
        # cursor.execute(quchong)
        else:
            sql = 'insert into adminLogin(adminid,adminpwd,adminname,adminphone) values(%s,%s,%s,%s);'
            cursor.execute(sql, [adid, adpwd, adname, adphone])
            conn.commit()
            showinfo(message='录入成功')
        cursor.close()
        conn.close()
    # def inputclear(self):
    #     Entry.delete(0,END)

class xiugaimanageFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.manageName = StringVar()
        self.manageID = StringVar()
        self.manageName1 = StringVar()
        self.manageID1 = StringVar()
        self.managePwd1 = StringVar()
        self.managePhone1 = StringVar()
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='原管理员ID').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.manageID).grid(row=1, column=1, stick=W)
        Label(self, text='原管理员姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.manageName).grid(row=2, column=1, stick=W)
        Label(self, text='新管理员ID').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.manageID1).grid(row=3, column=1, stick=W)
        Label(self, text='新管理员密码').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.managePwd1).grid(row=4, column=1, stick=W)
        Label(self, text='新管理员姓名').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.manageName1).grid(row=5, column=1, stick=W)
        Label(self, text='新联系方式').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.managePhone1).grid(row=6, column=1, stick=W)
        Button(self, text='修改', command=self.amend).grid(row=9, column=1, stick=E, pady=10)

    def amend(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        oldadname = self.manageName.get()
        oldadid = self.manageID.get()
        newadname = self.manageName1.get()
        newadid = self.manageID1.get()
        newadpwd = self.managePwd1.get()
        newadphone = self.managePhone1.get()
        check = "select adminid from adminLogin where adminid='%s' and adminname='%s' "
        res = cursor.execute(check % (oldadid,oldadname))
        if res:
            sql = "update adminLogin set adminid='%s',adminpwd='%s',adminname='%s',adminphone='%s'where adminname='%s' and adminid='%s'"
            cursor.execute(sql % (newadid, newadpwd, newadname, newadphone,oldadname,oldadid))
            conn.commit()
            conn.rollback()
            showinfo(message='修改成功')
        else:
            showinfo(title='错误', message='不存在管理员ID！')

        conn.commit()
        cursor.close()
        conn.close()


class deletemanageFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.manageName = StringVar()
        self.manageID = StringVar()
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='管理员ID').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.manageID).grid(row=1, column=1, stick=E)
        Label(self, text='管理员姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.manageName).grid(row=2, column=1, stick=E)
        Button(self, text='确认删除', command=self.delete).grid(row=3, column=1, stick=E, pady=10)

    def delete(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        adname = self.manageName.get()
        adid = self.manageID.get()
        check = "select adminid from adminLogin where adminid='%s'and adminname='%s' "
        res = cursor.execute(check % (adid,adname))
        if res:
            sql = "delete from adminLogin where adminname='%s'and adminid='%s'"
            cursor.execute(sql % (adname, adid))
            conn.commit()
            conn.rollback()
            showinfo(message='删除成功')
        else:
            showinfo(title='删除失败', message='不存在管理员ID！')
        cursor.close()
        conn.close()

###################读者
class add1Frame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.readerName = StringVar()  # 姓名
        self.readerId = StringVar()  # 借书证号
        self.readerType = StringVar() #读者类型
        self.readerNum = StringVar() #可借阅的数量
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='借书证号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.readerId).grid(row=1, column=1, stick=E)
        Label(self, text='姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.readerName).grid(row=2, column=1, stick=E)
        Label(self, text='类别（教师/学生）').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.readerType).grid(row=3, column=1, stick=E)
        Label(self, text='可借阅数量').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.readerNum).grid(row=4, column=1, stick=E)
        Button(self, text='录入', command=self.insert).grid(row=5, column=1, stick=E, pady=10)

    def insert(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        rid = self.readerId.get()
        rname = self.readerName.get()
        rtype = self.readerType.get()
        rnum = self.readerNum.get()
        check = "select readid from student where readid='%s' "
        res = cursor.execute(check % (rid))
        check2 = "select teacherid from teacher where teacherid='%s'"
        res2 = cursor.execute(check2 % (rid))
        if (res or res2):
            showinfo(title='错误', message='借书证号已被使用！')
        else:
            if rtype == "学生":
                sql = 'insert into student(readid,readname,readtype,readnum) values(%s,%s,%s,%s);'
                cursor.execute(sql, [rid, rname, rtype, rnum])
                setmoney = "insert into money(readerno,mon) values(%s,%s)"
                cursor.execute(setmoney ,[rid,0])
                showinfo(message='录入成功')
            elif rtype == "教师":
                sql2 = 'insert into teacher(teacherid,teachername,type,num) values(%s,%s,%s,%s);'
                cursor.execute(sql2,[rid, rname, rtype, rnum])
                setmoney = "insert into money(readerno,mon) values(%s,%s)"
                cursor.execute(setmoney ,[rid,0])
                showinfo(message='录入成功')
            else:
                showinfo(title="错误",message="读者类型不存在！")
            conn.commit()
            conn.rollback()
        cursor.close()
        conn.close()

class find1Frame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.readerName = StringVar()  # 姓名
        self.readerId = StringVar()  # 借书证号
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='姓名').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.readerName).grid(row=1, column=1, stick=E)
        Label(self, text='借书证号').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.readerId).grid(row=2, column=1, stick=E)
        Button(self, text='查找', command=self.emand).grid(row=3, column=1, stick=E, pady=10)

    def emand(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        rid = self.readerId.get()
        rname = self.readerName.get()
        check = "select readid from reader where readid='%s' "
        res = cursor.execute(check % (rid))
        if res:
            sql = "select * from reader where readid='%s' and readname='%s'"
            cursor.execute(sql % (rid, rname))
            results = cursor.fetchall()
            for row in results:
                readid = row[0]
                readname = row[1]
                readtype = row[2]
                print(readid, readname, readtype)
            Label(self).grid(row=5, stick=W, pady=8)
            label1 = Label(self, text='  姓名  ', bg="pink")
            label2 = Label(self, text='  借书证号  ', bg="pink")
            label3 = Label(self, text='  类型  ', bg="pink")
            label1.grid(row=6, column=0)
            label2.grid(row=6, column=1)
            label3.grid(row=6, column=2)
            Label(self).grid(row=7, stick=W, pady=3)
            label4 = Label(self, text=readname)
            label5 = Label(self, text=readid)
            label6 = Label(self, text=readtype)
            label4.grid(row=8, column=0)
            label5.grid(row=8, column=1)
            label6.grid(row=8, column=2)
        else:
            showinfo(title='错误', message='不存在借书证号！')
        cursor.close()
        conn.close()

    # columns = ('姓名', '学号', '成绩')
    # table = Treeview(tk, height=14, show="headings", columns=columns)
    # table.column('姓名', width=150, anchor='center')
    # table.column('学号', width=150, anchor='center')
    # table.column('成绩', width=150, anchor='center')
    # table.heading('姓名', text="姓名")
    # table.heading('学号', text="学号")
    # table.heading('成绩', text="成绩")
    # all_data()
    # table.grid(row=1, sticky=W + E)

class xiugai1Frame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.readerName = StringVar()  # 原姓名
        self.readerId = StringVar()  # 原借书证号
        self.readerType = StringVar()    #原类型
        self.readerIdl = StringVar()
        self.readerTypel = StringVar()
        self.readerName1 = StringVar()
        self.readerNum1 = StringVar()
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='借书证号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.readerId).grid(row=1, column=1, stick=E)
        Label(self, text='姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.readerName).grid(row=2, column=1, stick=E)
        Label(self, text='新借书证号').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.readerIdl).grid(row=3, column=1, stick=E)
        Label(self, text='新姓名').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.readerName1).grid(row=4, column=1, stick=E)
        Label(self, text='新类别').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.readerTypel).grid(row=5, column=1, stick=E)
        Label(self, text='可借阅数量').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.readerNum1).grid(row=6, column=1, stick=E)
        Button(self, text='修改', command=self.amend).grid(row=11, column=1, stick=E, pady=10)

    def amend(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        oldreaderno = self.readerId.get()
        oldreadername = self.readerName.get()
        newreaderno = self.readerIdl.get()
        newreadername = self.readerName1.get()
        newreadertype = self.readerTypel.get()
        newreadernum = self.readerNum1.get()
        check = "select readid from reader where readid='%s' and readname='%s' "
        res = cursor.execute(check % (oldreaderno, oldreadername))
        if res:
            sql = "update reader set readid='%s',readname='%s',readtype='%s',readnum='%s'" \
                  "where readid='%s'and readname='%s'"
            cursor.execute(sql % (newreaderno, newreadername, newreadertype, newreadernum, oldreaderno, oldreadername))
            conn.commit()
            conn.rollback()
            showinfo(message='修改成功')
        else:
            showinfo(title='修改失败', message='不存在借书证号！')
        cursor.close()
        conn.close()

class delete1Frame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.readerName = StringVar()  # 姓名
        self.readerId = StringVar()  # 借书证号
        self.createPage()

    def createPage(self):
       # Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='借书证号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.readerId).grid(row=1, column=1, stick=E)
        Label(self, text='姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.readerName).grid(row=2, column=1, stick=E)
        Button(self, text='确认删除', command=self.delete).grid(row=3, column=1, stick=E, pady=10)

    def delete(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        readerno = self.readerId.get()
        readername = self.readerName.get()
        check = "select readid from reader where readid='%s' and readname='%s' "
        res = cursor.execute(check % (readerno, readername))
        if res:
            sql = "delete from reader where readid='%s'and readname='%s'"
            cursor.execute(sql % (readerno, readername))
            conn.commit()
            conn.rollback()
            showinfo(message='删除成功')
        else:
            showinfo(title='删除失败', message='不存在借书证号！')
        cursor.close()
        conn.close()

###################图书管理
class addFrame(Frame):# 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master # 定义内部变量root
        self.bookNo = StringVar()    # 编号
        self.bookName = StringVar()  # 书名
        self.authorName = StringVar()  # 作者
        self.bookSeat = StringVar()  # 书籍位置
        self.bookNum = StringVar()  # 数量
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='书籍编号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.bookNo).grid(row=1, column=1, stick=E)
        Label(self, text='书名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.bookName).grid(row=2, column=1, stick=E)
        Label(self, text='作者').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.authorName).grid(row=3, column=1, stick=E)
        Label(self, text='位置').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.bookSeat).grid(row=4, column=1, stick=E)
        #Label(self, text='数量').grid(row=5, stick=W, pady=10)
        #Entry(self, textvariable=self.booknum).grid(row=5, column=1, stick=E)
        Button(self, text='录入', command=self.insert).grid(row=6, column=1, stick=E, pady=10)

    def insert(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        bkno = self.bookNo.get()
        bname = self.bookName.get()
        atname = self.authorName.get()
        bookst = self.bookSeat.get()
        # getname = "select bookname from bookinformation where bookno='%s'"
        # print(bno)
        # cursor.execute(getname % (bno))
        # results = cursor.fetchall()
        # s=results[0]
        # s1=str(s)
        check = "select bookno from bookinformation where bookno='%s' and bookname='%s'"   #  1.输入图书编号和书名 寻找相应的图书编号
        res=cursor.execute(check %(bkno,bname))                                             # ·若能找到相应的图书编号 那么录入图书信息并且数量+1
        print(res)                                                                         # ·若找不到通过输入的图书编号查看书名
        if res:                                                                            #  2.若找到了书名 判断输入的书名与表中的书名不一致   不一致则提示信息
            sql = 'insert into bookinformation(bookno,bookname,bookauthor,bookpress) values(%s,%s,%s,%s);'     # 否则（输入的图书编号不存在，在手动输入时不可能输入重复的编号）  加一条数据并且数量置1
            cursor.execute(sql, [bkno, bname, atname, bookst])
            addone = "update booknumber set number=number+1 where bookno='%s'"
            cursor.execute(addone % (bkno))
            conn.commit()
            showinfo(message='录入成功')
        else:
            getname = "select bookname from bookinformation where bookno='%s'"
            res1=cursor.execute(getname % (bkno))
            print(res1)
            if res1:
                results = cursor.fetchall()
                s = results[0]
                s1 = str(s)
                print(s1)
                bname1 = "(" +"'"+bname+"'" +"'"+","+")"
                print(bname1)
                if s1 != bname1:
                    showinfo(title='错误', message='图书编号已存在！')
                # else:
                #     setone = "insert booknumber set number=1,bookno='%s' where bookno in (select bookno from bookinformation where bookno='%s'and bookname='%s')"
                #     cursor.execute(setone % (bno, bno, bname))
                #     conn.commit()
                #     showinfo(message='录入成功')
            else:
                setone = "insert into booknumber(number,bookno) values(%s,%s);"
                cursor.execute(setone,[1,bkno])
                ins = 'insert into bookinformation(bookno,bookname,bookauthor,bookpress) values(%s,%s,%s,%s);'
                cursor.execute(ins, [bkno, bname, atname, bookst])
                conn.commit()
                showinfo(message='录入成功')
                #addFrame()

        conn.rollback()
        cursor.close()
        conn.close()

class deleteFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.bookName = StringVar()  # 书名
        self.authorName = StringVar()  # 作者
        self.bookPs = StringVar()  #书架号
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='书名').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.bookName).grid(row=1, column=1, stick=E)
        Label(self, text='作者').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.authorName).grid(row=2, column=1, stick=E)
        Label(self, text='位置').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.bookPs).grid(row=3, column=1, stick=E)
        Button(self, text='删除',command=self.delete).grid(row=4, column=1, stick=E, pady=10)

    def delete(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        bname = self.bookName.get()
        aname = self.authorName.get()
        bps = self.bookPs.get()

        check = "select bookno from bookinformation where bookname='%s' and bookauthor='%s'and bookpress='%s' "
        res = cursor.execute(check % (bname, aname, bps))
        if res:
            lessone="update booknumber set number=number-1 where bookname='%s' "
            cursor.execute(lessone %(bname))
            sql = "delete from reader where readid='%s'and readname='%s'"
            cursor.execute(sql % (bname, aname))
            conn.commit()
            conn.rollback()
            showinfo(message='删除成功')

        else:
            showinfo(title='删除失败', message='不存在借书证号！')

        sql = "delete from bookinformation where bookname='%s'and bookauthor='%s'"
        cursor.execute(sql % (bname,aname))
        conn.commit()
        conn.rollback()
        cursor.close()
        conn.close()

class xiugaiFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master # 定义内部变量root
        self.bookNo = StringVar()       #原书籍编号
        self.bookName = StringVar()     # 原书名
        self.bookName1 = StringVar()    # 新书名
        self.bookNo1 = StringVar()      # 新书籍编号
        self.bookSeat1 = StringVar()    # 新书籍位置
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='书籍编号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.bookNo).grid(row=1, column=1, stick=E)
        Label(self, text='书名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.bookName).grid(row=2, column=1, stick=E)
        Label(self, text='新书籍编号').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.bookNo1).grid(row=3, column=1, stick=E)
        Label(self, text='新书名').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.bookName1).grid(row=4, column=1, stick=E)
        Label(self, text='新位置').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.bookSeat1).grid(row=5, column=1, stick=E)
        Button(self, text='确认修改',command=self.amend).grid(row=6, column=1, stick=E, pady=10)

    def amend(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        bno = self.bookNo.get()
        bname = self.bookName.get()
        bno1 = self.bookNo1.get()
        bseat1 = self.bookSeat1.get()
        bname1 = self.bookName1.get()

        check = "select bookno from bookinformation where bookno='%s' and bookname='%s' "
        res = cursor.execute(check % (bno, bname))
        if res:
            sql = "update bookinformation set bookno='%s',bookname='%s',bookpress='%s' " \
                  "where bookno='%s'and bookname='%s'"
            cursor.execute(sql % (bno1,bname1,bseat1,bno,bname))
            conn.commit()
            conn.rollback()
            showinfo(message='修改成功')
        else:
            showinfo(title='修改失败', message='不存在图书编号！')
        cursor.close()
        conn.close()

class findFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.bookName = StringVar()  # 书名
        self.authorName = StringVar()  # 作者    is NULL
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='书名').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.bookName).grid(row=1, column=1, stick=E)
        Label(self, text='作者').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.authorName).grid(row=2, column=1, stick=E)
        Button(self, text='查找', command=self.check).grid(row=3, column=1, stick=E, pady=10)

    def check(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        bname = self.bookName.get()
        aname = self.authorName.get()

        Label(self).grid(row=5, stick=W, pady=8)
        label1 = Label(self, text='  图书编号 ', bg="pink")
        label2 = Label(self, text='  书名  ', bg="pink")
        label3 = Label(self, text='  作者  ', bg="pink")
        label4 = Label(self, text='  位置  ', bg="pink")
        label1.grid(row=6, column=0)
        label2.grid(row=6, column=1)
        label3.grid(row=6, column=2)
        label4.grid(row=6, column=3)

        sql = "select * from bookinformation where bookname='%s' and bookauthor='%s'"
        cursor.execute(sql % (bname,aname))
        results=cursor.fetchall()
        i=0
        for row in results:
            bookno = row[0]
            bookname = row[1]
            bookauthor = row[2]
            booklc = row[3]
            i=i+1
            print(bookno, bookname, bookauthor,booklc)
            Label(self).grid(row=7, stick=W, pady=3)
            label4 = Label(self, text=bookno)
            label5 = Label(self, text=bookname)
            label6 = Label(self, text=bookauthor)
            label7 = Label(self, text=booklc)
            label4.grid(row=7 + i, column=0)
            label5.grid(row=7 + i, column=1)
            label6.grid(row=7 + i, column=2)
            label7.grid(row=7 + i, column=3)

        cursor.close()
        conn.close()

###########################################借阅
class lendFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.lendSID = StringVar()
        self.lendName = StringVar()
        self.lendBID = StringVar()
        self.lendTime = StringVar()
        self.borrowTime = StringVar()
        self.createPage()

    def createPage(self):
       # Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='借书证号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.lendSID).grid(row=1, column=1, stick=E)
        Label(self, text='姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.lendName).grid(row=2, column=1, stick=E)
        Label(self, text='书籍编号').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.lendBID).grid(row=3, column=1, stick=E)
        Label(self, text='借阅时间').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.lendTime).grid(row=4, column=1, stick=E)
        Label(self, text='归还时间').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.borrowTime).grid(row=5, column=1, stick=E)
        Button(self, text='确定',command=self.insert).grid(row=6, column=1, stick=E, pady=10)

    def insert(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        rno = self.lendSID.get()
        rname = self.lendName.get()
        bno = self.lendBID.get()
        ltime = self.lendTime.get()
        btime = self.borrowTime.get()

        getnum2 = "select * from booknumber where bookno='%s'"
        cursor.execute(getnum2 % (bno))
        resul2 = cursor.fetchone()
        bnum2 = int(resul2[1])
        if bnum2 > 0:
            checkid = "select teacherid from teacher where teacherid='%s'and teachername='%s' "
            b = cursor.execute(checkid % (rno, rname))
            checkid2 = "select readid from student where readid='%s'and readname='%s' "
            c = cursor.execute(checkid2 % (rno, rname))
            print(b)
            print(c)
            if (b or c):
                viewtype = "select readtype from student where readid='%s' and readname='%s'"
                cursor.execute(viewtype % (rno, rname))
                results = cursor.fetchall()
                rtype = str(results)
                viewtype2 = "select type from teacher where teacherid='%s' and teachername='%s'"
                cursor.execute(viewtype2 % (rno, rname))
                results2 = cursor.fetchall()
                rtype2 = str(results2)
                print(rtype)
                print(rtype2)
                student = "(('学生',),)"
                teacher = "(('教师',),)"
                if rtype == student:
                    getnum = "select * from student where readid='%s' and readname='%s'"
                    cursor.execute(getnum % (rno, rname))
                    results = cursor.fetchone()
                    bnum = int(results[3])
                    if bnum > 1:
                        lessone = "update student set readnum=readnum-1 where readid=%s"
                        ls = cursor.execute(lessone % (rno))
                        check = "select readid from reader where readid='%s'and readname='%s' "
                        res = cursor.execute(check % (rno, rname))
                        if res:
                            sql = 'insert into borrowtoread(readerno,readername,bookno,lendtime,borrowtime) values(%s,%s,%s,%s,%s);'
                            cursor.execute(sql, [rno, rname, bno, ltime, btime])
                            lessbooknumber = "update booknumber set number=number-1 where bookno='%s'"
                            cursor.execute(lessbooknumber % (bno))
                            conn.commit()
                            conn.rollback()
                            showinfo(message='借阅成功！')
                        else:
                            showinfo(title='错误', message='不存在借书证号！')
                    else:
                        showinfo(title='错误', message='您的借阅数量已达上限！')
                elif rtype2 == teacher:  # 老师
                    getnum1 = "select * from teacher where teacherid='%s' and teachername='%s'"
                    cursor.execute(getnum1 % (rno, rname))
                    resul = cursor.fetchone()
                    bnum1 = int(resul[3])
                    print(type(bnum1))
                    print(bnum1)
                    if bnum1 > 1:
                        lessone = "update teacher set num=num-1 where teacherid=%s"
                        cursor.execute(lessone % (rno))
                        check = "select teacherid from teacher where teacherid='%s'and teachername='%s' "
                        res = cursor.execute(check % (rno, rname))
                        if res:
                            sql = 'insert into borrowtoread(readerno,readername,bookno,lendtime,borrowtime) values(%s,%s,%s,%s,%s);'
                            cursor.execute(sql, [rno, rname, bno, ltime, btime])
                            lessbooknumber = "update booknumber set number=number-1 where bookno='%s'"
                            cursor.execute(lessbooknumber % (bno))
                            conn.commit()
                            conn.rollback()
                            showinfo(message='借阅成功！')
                        else:
                            showinfo(title='错误', message='不存在借书证号！')
                    else:
                        showinfo(title='错误', message='您的借阅数量已达上限！')
            else:
                showinfo(title='错误', message='不存在借书证号！')
        else:
            showinfo(title='错误', message='库存不足！')

        conn.commit()
        conn.close()
class searchFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.lendSID = StringVar()
        self.lendName = StringVar()
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='借书证号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.lendSID).grid(row=1, column=1, stick=E)
        Label(self, text='姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.lendName).grid(row=2, column=1, stick=E)
        Button(self, text='查询',command=self.check).grid(row=3, column=1, stick=E, pady=10)

    def check(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        lid = self.lendSID.get()
        lname = self.lendName.get()
        sql = "select * from borrowtoread where readerno='%s' and readername='%s'"
        cursor.execute(sql % (lid,lname))
        results=cursor.fetchall()
        Label(self).grid(row=5, stick=W, pady=8)
        label1 = Label(self, text='  借书证号 ', bg="pink")
        label2 = Label(self, text='  姓名  ', bg="pink")
        label3 = Label(self, text='  图书编号   ', bg="pink")
        label4 = Label(self, text='  借出时间   ', bg="pink")
        label5 = Label(self, text='  应还时间  ', bg="pink")
        label1.grid(row=6, column=0)
        label2.grid(row=6, column=1)
        label3.grid(row=6, column=2)
        label4.grid(row=6, column=3)
        label5.grid(row=6, column=4)
        j=0
        for row in results:
            rno = row[0]
            rname = row[1]
            bno = row[2]
            ltime = row[3]
            btime = row[4]
            j=j+1
            Label(self).grid(row=7, stick=W, pady=3)
            label6 = Label(self, text=rno)
            label7 = Label(self, text=rname)
            label8 = Label(self, text=bno)
            label9 = Label(self, text=ltime)
            label10 = Label(self, text=btime)
            label6.grid(row=8+j, column=0)
            label7.grid(row=8+j, column=1)
            label8.grid(row=8+j, column=2)
            label9.grid(row=8+j, column=3)
            label10.grid(row=8+j, column=4)
        cursor.close()
        conn.close()


class returnFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.returnSID = StringVar()
        self.returnName = StringVar()
        self.returnBID = StringVar()
        self.returnTime = StringVar()
        self.bPs = StringVar()
        self.createPage()

    def createPage(self):
        #Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='借书证号').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.returnSID).grid(row=1, column=1, stick=E)
        Label(self, text='姓名').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.returnName).grid(row=2, column=1, stick=E)
        Label(self, text='书籍编号').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.returnBID).grid(row=3, column=1, stick=E)
        # Label(self, text='位置').grid(row=4, stick=W, pady=10)
        # Entry(self, textvariable=self.bPs).grid(row=4, column=1, stick=E)
        Button(self, text='确定', command=self.delete).grid(row=6, column=1, stick=E, pady=10)

    def delete(self):
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='bookmanagement', port=3306)
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示  (拿到游标)
        rno = self.returnSID.get()
        rname = self.returnName.get()
        bno = self.returnBID.get()
        # bps = self.bPs.get()

        import time
        gettime = "select * from borrowtoread where readerno='%s'and readername='%s'and bookno='%s'"
        res = cursor.execute(gettime % (rno, rname, bno))
        if res:
            a = cursor.fetchall()
            print(a)
            for row in a:
                print(row[4])
                timeArray = time.strptime(str(row[4]), "%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray))
                print(timeStamp)
                now = time.time()
                if (now > timeStamp):
                    cutmon = "update money set mon=mon-2 where readerno='%s'"
                    cursor.execute(cutmon % (rno))
                    conn.commit()
            sql = "delete from borrowtoread where readerno='%s'and readername='%s'and bookno='%s'"
            cursor.execute(sql % (rno, rname, bno))
            showinfo(message='归还成功')
            addone = "update booknumber set number=number+1 where bookno='%s'"
            cursor.execute(addone % (bno))
            conn.commit()
        else:
            showinfo(message='借书证号或姓名错误!')
    ####给图书数量加一个约束   目前借出的时候只减了借阅额度   没有写图书数量

        conn.commit()
        cursor.close()
        conn.rollback()
        conn.close()