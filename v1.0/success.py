# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from home import Ui_MainWindow_home
import paper_icons
class Ui_MainWindow_success(object):
    def setupUi(self, MainWindow_success):
        MainWindow_success.setObjectName("MainWindow_success")
        MainWindow_success.resize(900, 650)
        MainWindow_success.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow_success.setMaximumSize(QtCore.QSize(900, 650))
        MainWindow_success.setBaseSize(QtCore.QSize(900, 650))
        MainWindow_success.setStyleSheet("QMainWindow#MainWindow_success{\n"
                "    background:#FFFEF8\n"
                "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow_success)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(433, 394, 51, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_home.setStyleSheet("QPushButton#pushButton_home{\n"
                "    background:#FFFEF8;\n"
                "    border:1px solid #FFFEF8;\n"
                "    border-radius:5px;\n"
                "}  \n"
                "\n"
                "QPushButton#pushButton_home:pressed{\n"
                "    border:10px solid #ffffff;\n"
                "    border-radius:5px;\n"
                "    background:#FAF2EE;\n"
                "\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_home:hover{\n"
                "    border:1px solid #ECDAC8;\n"
                "    border-radius:5px;\n"
                "}")
        self.pushButton_home.setText("")
        icon = QtGui.QIcon()
 #       icon.addPixmap(QtGui.QPixmap("icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(':/home.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(':/home.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_home.setIcon(icon)
        self.pushButton_home.setIconSize(QtCore.QSize(38, 38))
        self.pushButton_home.setObjectName("pushButton_home")
        self.label_downloadsuccess = QtWidgets.QLabel(self.centralwidget)
        self.label_downloadsuccess.setGeometry(QtCore.QRect(417, 236, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_downloadsuccess.setFont(font)
        self.label_downloadsuccess.setStyleSheet("QLabel#label_downloadsuccess{\n"
                "    color:#383028\n"
                "}")
        self.label_downloadsuccess.setAlignment(QtCore.Qt.AlignCenter)
        self.label_downloadsuccess.setObjectName("label_downloadsuccess")
        self.progressBar3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar3.setGeometry(QtCore.QRect(273, 295, 371, 16))
        self.progressBar3.setStyleSheet("QProgressBar#progressBar3{\n"
                "    border: none;\n"
                "    color: white;\n"
                "       text-align: center;\n"
                "    background:#f9f4dc;\n"
                "    border-radius:5px;\n"
                "\n"
                "}\n"
                "\n"
                "QProgressBar#progressBar3::chunk {\n"
                "        border: none;\n"
                "        background: #B2A68F;\n"
                "        border-radius:5px;\n"
                "}")
        self.progressBar3.setProperty("value", 100)
        self.progressBar3.setObjectName("progressBar3")
        self.label_backhome = QtWidgets.QLabel(self.centralwidget)
        self.label_backhome.setGeometry(QtCore.QRect(418, 440, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_backhome.setFont(font)
        self.label_backhome.setStyleSheet("QLabel#label_backhome{\n"
                "    color:#383028\n"
                "}")
        self.label_backhome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_backhome.setObjectName("label_backhome")
        MainWindow_success.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_success)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow_success.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_success)
        self.statusbar.setObjectName("statusbar")
        MainWindow_success.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_success)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_success)

    def retranslateUi(self, MainWindow_success):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_success.setWindowTitle(_translate("MainWindow_success", "MainWindow"))
        self.label_downloadsuccess.setText(_translate("MainWindow_success", "下载成功"))
        self.label_backhome.setText(_translate("MainWindow_success", "返回主页"))
        self.pushButton_home.clicked.connect(self.showhome)

    def showhome(self):
        import sys
        self.MainWindow = QtWidgets.QMainWindow()
        print("ok 1")
        self.newshow = Ui_MainWindow_home()
        print("ok 2")
        self.newshow.setupUi(self.MainWindow)
        print("ok 3")
        # Ui_MainWindow_success.MainWindow_success.hide()
        # QtWidgets.QMainWindow().hide()
        # self.hide()
        print("ok 4")

        self.MainWindow.show()
        print('求你真的ok一把')


def finalpage():
#if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_success()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#finalpage()