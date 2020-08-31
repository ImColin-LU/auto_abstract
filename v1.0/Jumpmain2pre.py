# Jumpmain2pre.py
from PyQt5 import QtCore, QtGui, QtWidgets
from home import Ui_MainWindow_home        # 跳转按钮所在界面
from PreEdit import Ui_Form                # 跳转到的界面

#class Ui_PreEdit(QtWidgets.QWidget,Ui_Form):    # 定义的跳转函数名字
class Ui_PreEdit(Ui_Form):    # 定义的跳转函数名字
    def __init__(self):
        super(Ui_PreEdit,self).__init__()       # 跳转函数类名
        self.setupUi(self)

#主界面
class Mainshow(Ui_MainWindow_home):             # Mainshow_n(跳转前的界面)
    def __init__(self):
        super(Mainshow,self).__init__()         # Mainshow_n
        self.setupUi(self)
    #定义按钮的功能
    def loginEvent(self):
        self.hide()
        self.dia = Ui_PreEdit()                 # 跳转到的界面类名（）
        self.dia.show()

#运行窗口Login
#if __name__=="__main__":
def homeshow():                                 # 调用这个函数来执行
    import sys
    app=QtWidgets.QApplication(sys.argv)
    first=Mainshow()
    first.show()
    first.pushButton_openfile.clicked.connect(first.loginEvent) # 绑定跳转功能的按钮
    app.exec_()
    #sys.exit()