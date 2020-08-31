# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

from sumcreating import get_text_for_AB,get_text_for_words,getAB1,getAB2,getAB3
from PyQt5.QtWidgets import QFileDialog
from success import Ui_MainWindow_success
import paper_icons


class Ui_MainWindow_result(object):
    def setupUi(self, MainWindow_result):
        MainWindow_result.setObjectName("MainWindow_result")
        MainWindow_result.resize(900, 650)
        MainWindow_result.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow_result.setMaximumSize(QtCore.QSize(900, 650))
        MainWindow_result.setBaseSize(QtCore.QSize(900, 650))
        MainWindow_result.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow_result.setStyleSheet("QMainWindow#MainWindow_result{\n"
                "    background:#FFFEF8\n"
                "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow_result)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(750, 570, 100, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_save.setStyleSheet("QPushButton#pushButton_save{  \n"
                "    border: 1px solid #FFFEF8;  \n"
                "    background-color:#E7DDCF;\n"
                "    border-style: solid;  \n"
                "    border-radius:0px;  \n"
                "    width: 40px; \n"
                "    height:20px;  \n"
                "    padding:0 0px;  \n"
                "    margin:0 0px;  \n"
                "}  \n"
                "\n"
                "QPushButton#pushButton_save:pressed{\n"
                "    background-color:#d4c4b7;\n"
                "    border:0.5px solid #c1b2a3;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_save:hover{\n"
                "    border:0.5px solid #c1b2a3;\n"
                "}")
        icon = QtGui.QIcon()
#        icon.addPixmap(QtGui.QPixmap("icon/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(':/download.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(':/download.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_save.setIcon(icon)
        self.pushButton_save.setObjectName("pushButton_save")

        # self.pushButton_back2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_back2.setGeometry(QtCore.QRect(98, 571, 60, 35))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(16)
        # font.setBold(True)
        # font.setWeight(75)
        # self.pushButton_back2.setFont(font)
        # self.pushButton_back2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.pushButton_back2.setStyleSheet("QPushButton#pushButton_back2{  \n"
        #         "    border: 1px solid #FFFEF8;  \n"
        #         "    background-color:#E7DDCF;\n"
        #         "    border-style: solid;  \n"
        #         "    border-radius:0px;  \n"
        #         "    width: 40px; \n"
        #         "    height:20px;  \n"
        #         "    padding:0 0px;  \n"
        #         "    margin:0 0px;  \n"
        #         "}  \n"
        #         "\n"
        #         "QPushButton#pushButton_back2:pressed{\n"
        #         "    background-color:#d4c4b7;\n"
        #         "    border:0.5px solid #c1b2a3;\n"
        #         "}\n"
        #         "\n"
        #         "QPushButton#pushButton_back2:hover{\n"
        #         "    border:0.5px solid #c1b2a3;\n"
        #         "}")
        # self.pushButton_back2.setObjectName("pushButton_back2")


        self.pushButton_path = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_path.setGeometry(QtCore.QRect(639, 570, 100, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_path.setFont(font)
        self.pushButton_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_path.setStyleSheet("QPushButton#pushButton_path{  \n"
                "    border: 1px solid #FFFEF8;  \n"
                "    background-color:#E7DDCF;\n"
                "    border-style: solid;  \n"
                "    border-radius:0px;  \n"
                "    width: 40px; \n"
                "    height:20px;  \n"
                "    padding:0 0px;  \n"
                "    margin:0 0px;  \n"
                "}  \n"
                "\n"
                "QPushButton#pushButton_path:hover{\n"
                "    border:0.5px solid #c1b2a3;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_path:pressed{\n"
                "    background-color:#d4c4b7;\n"
                "    border:0.5px solid #c1b2a3;\n"
                "}")
        #self.pushButton_path.setIcon(icon)
        self.pushButton_path.setObjectName("pushButton_path")
        self.plainTextEdit_summary = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_summary.setGeometry(QtCore.QRect(100, 180, 750, 291))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.plainTextEdit_summary.setFont(font)
        self.plainTextEdit_summary.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.plainTextEdit_summary.setStyleSheet("QPlainTextEdit#plainTextEdit_summary{\n"
                "    border:1px solid #97846c\n"
                "}")
        self.plainTextEdit_summary.setObjectName("plainTextEdit_summary")
        self.label_summaryresult = QtWidgets.QLabel(self.centralwidget)
        self.label_summaryresult.setGeometry(QtCore.QRect(28, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_summaryresult.setFont(font)
        self.label_summaryresult.setStyleSheet("QLabel#label_summaryresult{\n"
                "    color:#383028\n"
                "}")
        self.label_summaryresult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_summaryresult.setObjectName("label_summaryresult")
        self.label_titleresult = QtWidgets.QLabel(self.centralwidget)
        self.label_titleresult.setGeometry(QtCore.QRect(28, 30, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_titleresult.setFont(font)
        self.label_titleresult.setStyleSheet("QLabel#label_titleresult{\n"
                "    color:#383028\n"
                "}")
        self.label_titleresult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleresult.setObjectName("label_titleresult")
        self.lineEdit_title1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title1.setGeometry(QtCore.QRect(100, 50, 750, 25))
        self.lineEdit_title1.setStyleSheet("QLineEdit#lineEdit_title1{\n"
                "    border:1px solid #97846c\n"
                "}")
        self.lineEdit_title1.setObjectName("lineEdit_title1")
        self.lineEdit_title2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title2.setGeometry(QtCore.QRect(100, 83, 750, 25))
        self.lineEdit_title2.setStyleSheet("QLineEdit#lineEdit_title2{\n"
                "    border:1px solid #97846c\n"
                "}")
        self.lineEdit_title2.setObjectName("lineEdit_title2")
        self.lineEdit_title3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title3.setGeometry(QtCore.QRect(100, 116, 750, 25))
        self.lineEdit_title3.setStyleSheet("QLineEdit#lineEdit_title3{\n"
                "    border:1px solid #97846c\n"
                "}")
        self.lineEdit_title3.setObjectName("lineEdit_title3")
        self.label_keywordresult = QtWidgets.QLabel(self.centralwidget)
        self.label_keywordresult.setGeometry(QtCore.QRect(18, 491, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_keywordresult.setFont(font)
        self.label_keywordresult.setStyleSheet("QLabel#label_keywordresult{\n"
                "    color:#383028\n"
                "}")
        self.label_keywordresult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_keywordresult.setObjectName("label_keywordresult")
        self.lineEdit_keywords = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_keywords.setGeometry(QtCore.QRect(100, 510, 750, 25))
        self.lineEdit_keywords.setStyleSheet("QLineEdit#lineEdit_keywords{\n"
                "    border:1px solid #97846c\n"
                "}")
        self.lineEdit_keywords.setObjectName("lineEdit_keywords")
        MainWindow_result.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow_result.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_result)
        self.statusbar.setObjectName("statusbar")
        MainWindow_result.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_result)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_result)

        # 保存地址
        self.save_path_text = QtWidgets.QLineEdit(MainWindow_result)
        self.save_path_text.setGeometry(QtCore.QRect(100, 572, 520, 32))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.save_path_text.setFont(font)
        self.save_path_text.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.save_path_text.setStyleSheet("QLineEdit#save_path_text{\n"
                                          "    border:1px solid #7a7374\n"
                                          "}"
                                          "QLineEdit#save_path_text:hover{\n"
                                          "    border:1px solid #4f4032\n"
                                          "}")
        self.save_path_text.setObjectName("save_path_text")

    def retranslateUi(self, MainWindow_result):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_result.setWindowTitle(_translate("MainWindow_result", "MainWindow"))
        self.pushButton_save.setText(_translate("MainWindow_result", "保存"))
        #self.pushButton_back2.setText(_translate("MainWindow_result", "←"))
        self.pushButton_path.setText(_translate("MainWindow_result", "选择路径"))

        # ==========
        # 【待对接】模型跑出来的结果存几个string然后替换下面的文字就好了~
        # ==========
        a= get_text_for_AB()
        b=getAB1()
        c= getAB2()
        d=getAB3()
        e=get_text_for_words()
        self.plainTextEdit_summary.setPlainText(_translate("MainWindow_result", a))
        self.label_summaryresult.setText(_translate("MainWindow_result","摘要" ))
        self.label_titleresult.setText(_translate("MainWindow_result", "标题"))
        self.lineEdit_title1.setText(_translate("MainWindow_result", b))
        self.lineEdit_title2.setText(_translate("MainWindow_result", c))
        self.lineEdit_title3.setText(_translate("MainWindow_result", d))
        self.label_keywordresult.setText(_translate("MainWindow_result", "关键词"))
        self.lineEdit_keywords.setText(_translate("MainWindow_result",e))  #换这个

        # 保存事件
        self.pushButton_path.clicked.connect(self.save_event)
        self.pushButton_save.clicked.connect(self.save_text) # 跳转也写在这里了

    # 保存
    def save_event(self):
        global save_path
        _translate = QtCore.QCoreApplication.translate
        fileName3, ok2 = QFileDialog.getSaveFileName(None, "保存路径", "C:/", "Word文档 (*.docx;*.doc);;文本文件 (*.txt);;pdf (*.pdf);;")
        print(fileName3)  # 打印保存文件的全部路径（包括文件名和后缀名）
        save_path = str(fileName3)
        print(save_path)
        self.save_path_text.setText(_translate("Form", save_path))

    def save_text(self):

        if save_path is not None:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write("标题为：" + '\n')
                file.write(getAB1() + '\n'+getAB2()+'\n'+getAB3()+'\n')
                file.write("关键字为："+'\n')
                file.write(get_text_for_words()+'\n')
                file.write("生成的摘要为"+'\n')
                file.write(get_text_for_AB()+'\n')

                #from PreEdit import  get_readsss
                #file.write('原文为'+'\n'+get_readsss())
                # ===================
                # 【对接】file.write这里直接把程序里的string加起来写入保存的结果就好了~就不用读上面展示的内容了
                # ===================
                #file.write("hello,Tibbarr")
            print('已保存！')

        self.MainWindow = QtWidgets.QMainWindow()
        self.newshow = Ui_MainWindow_success()
        self.newshow.setupUi(self.MainWindow)
        # self.hide()
        self.MainWindow.show()

        print('生成中…')

def resultshow():
 #if __name__ == "__main__":
    import sys



    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_result()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#resultshow()