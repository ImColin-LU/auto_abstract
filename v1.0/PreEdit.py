# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QFileDialog
#from sumcreating import sumcreatingshow
from sumcreating import Ui_MainWindow_sumcreating
import  time

import sys
#from TextRank4Keyword import TextRank4Keyword
#from TextRank4Sentence import TextRank4Sentence



m=False
read=''
class Ui_Form(QtWidgets.QMainWindow):

    save_path = ''
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(900, 650)
        Form.setMinimumSize(QtCore.QSize(900, 650))
        Form.setMaximumSize(QtCore.QSize(900, 650))
        Form.setBaseSize(QtCore.QSize(900, 650))
        Form.setStyleSheet("background:#FFFEF8\n")

        # 预览
        self.label_preview = QtWidgets.QLabel(Form)
        self.label_preview.setGeometry(QtCore.QRect(28, 89, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_preview.setFont(font)
        self.label_preview.setStyleSheet("QLabel#label_preview{\n"
                                         "    color:#383028\n"
                                         "}")
        self.label_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_preview.setObjectName("label_preview")

        # 打开地址
        self.open_path_text = QtWidgets.QLineEdit(Form)
        self.open_path_text.setGeometry(QtCore.QRect(100, 24, 640, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.open_path_text.setFont(font)
        self.open_path_text.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.open_path_text.setStyleSheet("QLineEdit#open_path_text{\n"
                                                 "    border:1px solid #7a7374\n"
                                                 "}"
                                          "QLineEdit#open_path_text:hover{\n"
                                                "    border:1px solid #4f4032\n"
                                                "}"
                                          )
        self.open_path_text.setObjectName("open_path_text")

        # 打开地址浏览按钮
        self.open_path_but = QtWidgets.QPushButton(Form)
        self.open_path_but.setGeometry(QtCore.QRect(755, 23, 75, 23))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_path_but.setFont(font)
        self.open_path_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_path_but.setStyleSheet("QPushButton#open_path_but{  \n"
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
                                    "QPushButton#open_path_but:pressed{\n"
                                    "    background-color:#d4c4b7;\n"
                                    "    border:0.5px solid #c1b2a3;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#open_path_but:hover{\n"
                                    "    border:0.5px solid #c1b2a3;\n"
                                    "}")
        self.open_path_but.setObjectName("open_path_but")

        # 保存地址浏览按钮
        self.save_path_but = QtWidgets.QPushButton(Form)
        self.save_path_but.setGeometry(QtCore.QRect(755, 55, 75, 23))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_path_but.setFont(font)
        self.save_path_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_path_but.setStyleSheet("QPushButton#save_path_but{  \n"
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
                                         "QPushButton#save_path_but:pressed{\n"
                                         "    background-color:#d4c4b7;\n"
                                         "    border:0.5px solid #c1b2a3;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#save_path_but:hover{\n"
                                         "    border:0.5px solid #c1b2a3;\n"
                                         "}")
        self.save_path_but.setObjectName("save_path_but")


        # 保存地址
        self.save_path_text = QtWidgets.QLineEdit(Form)
        self.save_path_text.setGeometry(QtCore.QRect(100, 56, 640, 20))
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

        # 编辑区
        self.text_value = QtWidgets.QPlainTextEdit(Form)
        self.text_value.setGeometry(QtCore.QRect(100, 110, 731, 450))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.text_value.setFont(font)
        self.text_value.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.text_value.setStyleSheet("QPlainTextEdit#text_value{\n"
                                                 "    border:1px solid #4f4032\n"
                                                 "}")
        self.text_value.setObjectName("text_value")

        # 保存按钮
        self.save_but = QtWidgets.QPushButton(Form)
        self.save_but.setGeometry(QtCore.QRect(100, 580, 100, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_but.setFont(font)
        self.save_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_but.setStyleSheet("QPushButton#save_but{  \n"
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
                                                 "QPushButton#save_but:pressed{\n"
                                                 "    background-color:#d4c4b7;\n"
                                                 "    border:0.5px solid #c1b2a3;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton#save_but:hover{\n"
                                                 "    border:0.5px solid #c1b2a3;\n"
                                                 "}")
        self.save_but.setObjectName("save_but")

        # 生成按钮
        self.pushButton_create = QtWidgets.QPushButton(Form)
        self.pushButton_create.setGeometry(QtCore.QRect(731, 580, 100, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_create.setStyleSheet("QPushButton#pushButton_create{  \n"
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
                                             "QPushButton#pushButton_create:pressed{\n"
                                             "    background-color:#d4c4b7;\n"
                                             "    border:0.5px solid #c1b2a3;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#pushButton_create:hover{\n"
                                             "    border:0.5px solid #c1b2a3;\n"
                                             "}")
        self.pushButton_create.setObjectName("pushButton_create")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_preview.setText(_translate("MainWindow_preview", "预览"))
        self.open_path_text.setPlaceholderText(_translate("Form", "打开地址"))
        self.open_path_but.setText(_translate("Form", "浏览"))
        self.save_path_but.setText(_translate("Form", "浏览"))
        self.save_path_text.setPlaceholderText(_translate("Form", "保存地址"))
        self.save_but.setText(_translate("Form", "保存"))
        self.open_path_but.clicked.connect(self.open_event)
        self.save_path_but.clicked.connect(self.save_event)
        self.save_but.clicked.connect(self.save_text)
        self.pushButton_create.clicked.connect(self.showwaiting)
        self.pushButton_create.setText(_translate("MainWindow_preview", "生成"))

    def open_event(self):
        global path
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "选择文件", "C:/","Word文档 (*.docx;*.doc);;文本文件 (*.txt);;pdf (*.pdf);;")
        print(directory1)  # 打印文件夹路径
        path = directory1[0]
        self.open_path_text.setText(_translate("Form", path))
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.text_value.setPlainText(file.read())

    # 保存
    def save_event(self):
        global save_path
        _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "C:/","Text Files (*.txt)")
        print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        save_path = fileName2
        self.save_path_text.setText(_translate("Form", save_path))

    def save_text(self):
        global path
        if path is not None:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write(self.text_value.toPlainText())
            print('已保存！')
            #self.text_value.clear()
            #问题待解决

    def showwaiting(self):
        import sys
        self.MainWindow = QtWidgets.QMainWindow()
        self.newshow = Ui_MainWindow_sumcreating()
        self.newshow.setupUi(self.MainWindow)
        self.hide()
        self.MainWindow.show()

        global path
        global read
        f=open(path,encoding='utf-8')
        read=f.read()
        read=read.replace('\n','')
        '''
        tr4w.analyze(text=read, lower=True, window=2)
        text_for_word = ''
        for item in tr4w.get_keywords(10, word_min_len=2):
            text_for_word = text_for_word + ' ' + item.word
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=read, lower=True, source='all_filters')
        text_for_ab = '  '
        for item in tr4s.get_key_sentences(num=5):
            text_for_ab = text_for_ab + item.sentence + '。' + '\n' + '  '
        f.close()
        '''
        f.close()
        #print('生成中…')


        #self.MainWindow.close()


def get_readsss():
    global read
    return read
'''
def result_for_word():
    return text_for_word
def result_for_sentence():
    return  text_for_ab
'''
def is_ok():
    global m
    return m



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())