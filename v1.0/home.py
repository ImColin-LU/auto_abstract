# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import paper_icons
class Ui_MainWindow_home(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow_home,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow_home):
        MainWindow_home.setObjectName("MainWindow_home")
        MainWindow_home.resize(900, 650)
        MainWindow_home.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow_home.setMaximumSize(QtCore.QSize(900, 650))
        MainWindow_home.setBaseSize(QtCore.QSize(900, 650))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        MainWindow_home.setFont(font)
        MainWindow_home.setStyleSheet("QMainWindow#MainWindow_home{\n"
            "    background:#FFFEF8\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow_home)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openfile.setGeometry(QtCore.QRect(320, 328, 258, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_openfile.setFont(font)
        self.pushButton_openfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_openfile.setStyleSheet("QPushButton#pushButton_openfile{  \n"
            "    border: 1px solid #9a8878;  \n"
            "    background-color:#ffffff;\n"
            "    border-style: solid;  \n"
            "    border-radius:0px;  \n"
            "    width: 40px; \n"
            "    height:20px;  \n"
            "    padding:0 0px;  \n"
            "    margin:0 0px;  \n"
            "}  \n"
            "\n"
            "QPushButton#pushButton_openfile:pressed{\n"
            "    background-color:#FBF7F6;\n"
            "    border:0.5px solid #DDCFC2;\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_openfile:hover{\n"
            "    border:0.5px solid #DDCFC2;\n"
            "}")

        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(r".\icon\enter2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap(r".\icon\enter2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(':/enter2.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(':/enter2.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)

        self.pushButton_openfile.setIcon(icon)
        self.pushButton_openfile.setCheckable(False)
        self.pushButton_openfile.setObjectName("pushButton_openfile")
        self.label_maintitle_shadow = QtWidgets.QLabel(self.centralwidget)
        self.label_maintitle_shadow.setGeometry(QtCore.QRect(276, 188, 350, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_maintitle_shadow.setFont(font)
        self.label_maintitle_shadow.setStyleSheet("QLabel#label_maintitle_shadow{\n"
            "    color:#847c74\n"
            "}")
        self.label_maintitle_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_maintitle_shadow.setObjectName("label_maintitle_shadow")
        self.label_format = QtWidgets.QLabel(self.centralwidget)
        self.label_format.setGeometry(QtCore.QRect(325, 395, 251, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_format.setFont(font)
        self.label_format.setStyleSheet("QLabel#label_format{\n"
            "    color:#3A332A\n"
            "}")
        self.label_format.setObjectName("label_format")
        self.label_maintitle = QtWidgets.QLabel(self.centralwidget)
        self.label_maintitle.setGeometry(QtCore.QRect(276, 189, 350, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_maintitle.setFont(font)
        self.label_maintitle.setStyleSheet("QLabel#label_maintitle{\n"
            "    color:#3A332A\n"
            "}")
        self.label_maintitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_maintitle.setObjectName("label_maintitle")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(328, 600, 251, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(8)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("QLabel#label_author{\n"
            "    color:#97846c\n"
            "}")
        self.label_author.setAlignment(QtCore.Qt.AlignCenter)
        self.label_author.setObjectName("label_author")
        MainWindow_home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow_home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_home)
        self.statusbar.setObjectName("statusbar")
        MainWindow_home.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_home)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_home)

        # 打开文件
        #self.pushButton_openfile.clicked.connect(self.openfile)


    def retranslateUi(self, MainWindow_home):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_home.setWindowTitle(_translate("MainWindow_home", "MainWindow"))
        self.pushButton_openfile.setText(_translate("MainWindow_home", "  进入程序"))
        self.label_maintitle_shadow.setText(_translate("MainWindow_home", "论 文 助 手"))
        self.label_format.setText(_translate("MainWindow_home", "支持扩展名： .pdf  .doc  .docx  .txt"))
        self.label_maintitle.setText(_translate("MainWindow_home", "论 文 助 手"))
        self.label_author.setText(_translate("MainWindow_home", "Designed by Hu Tong & Li Shuolin"))

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'files(*.doc , *.docx , *.pdf,  *.txt)')

#if __name__ == "__main__":
def homeshow():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #sys.exit(app.exec_())
