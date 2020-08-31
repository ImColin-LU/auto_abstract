# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sumcreating.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import jieba
from string_replace import pyltp_model, preprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import paper_icons
import os
import jieba


import  tensorflow as tf
import numpy as np
from six.moves import xrange
import tensorflow as tf



AB1=''
AB2=''
AB3=''
text_for_AB=''
text_for_words = ''

class Ui_MainWindow_sumcreating(QWidget):

    def __init__(self):
        super(Ui_MainWindow_sumcreating, self).__init__()

    def setupUi(self, MainWindow_sumcreating):
        self.main_widget = QtWidgets.QWidget(self)
        MainWindow_sumcreating.setObjectName("MainWindow_sumcreating")
        MainWindow_sumcreating.resize(900, 650)
        MainWindow_sumcreating.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow_sumcreating.setMaximumSize(QtCore.QSize(900, 650))
        MainWindow_sumcreating.setBaseSize(QtCore.QSize(900, 650))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        MainWindow_sumcreating.setFont(font)
        MainWindow_sumcreating.setStyleSheet("QMainWindow#MainWindow_sumcreating{\n"
            "    background:#FFFEF8\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow_sumcreating)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar1 = QtWidgets.QProgressBar(self.centralwidget)
        #self.progressBar1 = QtWidgets.QProgressBar(self.main_widget)
        self.progressBar1.setGeometry(QtCore.QRect(274, 310, 371, 16))
        self.progressBar1.setStyleSheet("QProgressBar#progressBar1{\n"
            "    border: none;\n"
            "    color: white;\n"
            "       text-align: center;\n"
            "    background:#f9f4dc;\n"
            "    border-radius:5px;\n"
            "\n"
            "}\n"
            "\n"
            "QProgressBar#progressBar1::chunk {\n"
            "        border: none;\n"
            "        background: #B2A68F;\n"
            "        border-radius:5px;\n"
            "}")
        self.progressBar1.setProperty("value", "loading")
        self.progressBar1.setObjectName("progressBar1")
        # 创建并启用子线程
        self.thread_1 = Worker()
        self.thread_1.progressBarValue.connect(self.copy_file)
        self.thread_1.start()

        self.label_sumcreate = QtWidgets.QLabel(self.centralwidget)
        self.label_sumcreate.setGeometry(QtCore.QRect(419, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_sumcreate.setFont(font)
        self.label_sumcreate.setStyleSheet("QLabel#label_sumcreate{\n"
            "    color:#383028\n"
            "}")
        self.label_sumcreate.setObjectName("label_sumcreate")
        self.pushButton_sumcreate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sumcreate.setGeometry(QtCore.QRect(427, 230, 61, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.pushButton_sumcreate.setFont(font)
        self.pushButton_sumcreate.setStyleSheet("QPushButton#pushButton_sumcreate{\n"
            "    background:#FFFEF8;\n"
            "    border:1px solid #FFFEF8;\n"
            "}")
        self.pushButton_sumcreate.setText("")
        icon = QtGui.QIcon()
#        icon.addPixmap(QtGui.QPixmap("icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#        icon.addPixmap(QtGui.QPixmap(":/new/prefix1/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(':/file.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(':/file.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_sumcreate.setIcon(icon)
        self.pushButton_sumcreate.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_sumcreate.setObjectName("pushButton_sumcreate")
        MainWindow_sumcreating.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_sumcreating)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow_sumcreating.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_sumcreating)
        self.statusbar.setObjectName("statusbar")
        MainWindow_sumcreating.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_sumcreating)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_sumcreating)

    def retranslateUi(self, MainWindow_sumcreating):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_sumcreating.setWindowTitle(_translate("MainWindow_sumcreating", "MainWindow"))
        self.label_sumcreate.setText(_translate("MainWindow_sumcreating", "摘要生成中"))

    def copy_file(self, i):
        self.progressBar1.setValue(i)

class Worker(QThread):

    progressBarValue = pyqtSignal(int)  # 更新进度条

    def __init__(self):
        super(Worker, self).__init__()


    def run(self):
        from PreEdit import get_readsss
        from TextRank4Keyword import TextRank4Keyword
        from TextRank4Sentence import TextRank4Sentence
        from seq2seqAttSum import eval, data_utils
        from seq2seqAttSum.headline import LargeConfig
        config = LargeConfig()  # new Large Config,
        FLAGS = tf.app.flags.FLAGS  # Reuse the tf.app.flags from headline module
        from seq2seqAttSum.headline import create_model
        from seq2seqAttSum.headline import buckets
        buckets = buckets
        global  AB1
        global  AB2
        global  AB3
        global text_for_AB
        global  text_for_words
        self.progressBarValue.emit(0)
        read=get_readsss()
        tr4w = TextRank4Keyword()
        print(1)
        tr4w.analyze(text=read, lower=True, window=2)
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=read, lower=True, source='all_filters')
        print(2)
        for i in range(1,20):
            time.sleep(0.1)
            self.progressBarValue.emit(i)

        for item in tr4w.get_keywords(10, word_min_len=2):
            text_for_words = text_for_words + ' ' + item.word
        print(text_for_words)

        text_for_ab1 = '  '

        text_for_ab2 = '  '
        text_for_ab3 = '  '
        for item in tr4s.get_key_sentences(num=3):
            text_for_ab1 = text_for_ab1 + item.sentence + '。' + '  '
        print(text_for_ab1)
        for item in tr4s.get_key_sentences(num=5):
            text_for_ab2 = text_for_ab2 + item.sentence + '。' + '  '
        print(text_for_ab2)
        for item in tr4s.get_key_sentences(num=8):
            text_for_ab3 = text_for_ab3 + item.sentence + '。' + '  '
        print(text_for_ab3)
        text_for_AB=text_for_ab2
        print(text_for_AB)
        a1=jieba.cut(text_for_ab1)
        b1=' '.join(a1)
        a2=jieba.cut(text_for_ab2)
        b2=' '.join(a2)
        a3=jieba.cut(text_for_ab3)
        b3=' '.join(a3)
        print(b1)
        print(b2)
        print(b3)

        text_for_ab1 =b1
        text_for_ab2 =b2
        text_for_ab3 =b3

        for i in range(20,40):
            time.sleep(0.05)
            self.progressBarValue.emit(i)
        with tf.Session() as sess:
            model = create_model(sess, True)
            model.batch_size = FLAGS.batch_size  # repeat single sentence 10 times as one batch  # We decode one sentence at a time.
            vocab_path = os.path.join(FLAGS.data_dir, "vocab")

            vocab, rev_vocab = data_utils.initialize_vocabulary(vocab_path)
            models=pyltp_model()
            #__________

            for i in range(40, 50):
                time.sleep(0.05)
                self.progressBarValue.emit(i)
            sentence=text_for_ab1
            sentence=preprocess(sentence,models)
            sentence=' '.join(sentence).replace('TAGDATE','TAG_DATE').replace('S-Ni','TAG_NAME_EN').replace('S-Nh','TAG_NAME_EN').replace('TAGNUM','TAG_NUMBER')
            sen = tf.compat.as_bytes(sentence)
            sen = sen.decode('utf-8')
            token_ids = data_utils.sentence_to_token_ids(sen, vocab, normalize_digits=False)
            bucket_id = min([b for b in xrange(len(buckets)) if buckets[b][0] > len(token_ids)])
            encoder_inputs, decoder_inputs, target_weights = model.get_batch(
                {bucket_id: [(token_ids, [])]}, bucket_id)
            _, _, output_logits_batch = model.step(sess, encoder_inputs, decoder_inputs, target_weights, bucket_id,
                                                   True)
            output_logits = []
            for item in output_logits_batch:
                output_logits.append(item[0])
            outputs = []
            for logit in output_logits:
                m = int(np.argmax(logit))
                if m == 3:
                    logit[3] = logit[np.argmin(logit)]
                    m = int(np.argmax(logit))
                outputs.append(m)
            #outputs = [int(np.argmax(logit)) for logit in output_logits]
            print(output_logits)
            # If there is an EOS symbol in outputs, cut them at that point.
            if data_utils.EOS_ID in outputs:
                outputs = outputs[:outputs.index(data_utils.EOS_ID)]
            AB1 = " ".join([tf.compat.as_str(rev_vocab[output]) for output in outputs])
            # __________
            for i in range(50, 65):
                time.sleep(0.05)
                self.progressBarValue.emit(i)
            sentence = text_for_ab2
            sentence=preprocess(sentence,models)
            sentence=' '.join(sentence).replace('TAGDATE','TAG_DATE').replace('S-Ni','TAG_NAME_EN').replace('S-Nh','TAG_NAME_EN').replace('TAGNUM','TAG_NUMBER')
            sen = tf.compat.as_bytes(sentence)
            sen = sen.decode('utf-8')
            token_ids = data_utils.sentence_to_token_ids(sen, vocab, normalize_digits=False)
            bucket_id = min([b for b in xrange(len(buckets)) if buckets[b][0] > len(token_ids)])
            encoder_inputs, decoder_inputs, target_weights = model.get_batch(
                {bucket_id: [(token_ids, [])]}, bucket_id)
            _, _, output_logits_batch = model.step(sess, encoder_inputs, decoder_inputs, target_weights, bucket_id,
                                                   True)
            output_logits = []
            for item in output_logits_batch:
                output_logits.append(item[0])
            outputs = []
            for logit in output_logits:
                m = int(np.argmax(logit))
                if m == 3:
                    logit[3] = logit[np.argmin(logit)]
                    m = int(np.argmax(logit))
                outputs.append(m)
           # outputs = [int(np.argmax(logit)) for logit in output_logits]
            print(output_logits)
            # If there is an EOS symbol in outputs, cut them at that point.
            if data_utils.EOS_ID in outputs:
                outputs = outputs[:outputs.index(data_utils.EOS_ID)]
            AB2 = " ".join([tf.compat.as_str(rev_vocab[output]) for output in outputs])
            # __________
            for i in range(65, 90):
                time.sleep(0.05)
                self.progressBarValue.emit(i)
            sentence = text_for_ab3
            sentence=preprocess(sentence,models)
            sentence=' '.join(sentence).replace('TAGDATE','TAG_DATE').replace('S-Ni','TAG_NAME_EN').replace('S-Nh','TAG_NAME_EN').replace('TAGNUM','TAG_NUMBER')
            sen = tf.compat.as_bytes(sentence)
            sen = sen.decode('utf-8')
            token_ids = data_utils.sentence_to_token_ids(sen, vocab, normalize_digits=False)
            bucket_id = min([b for b in xrange(len(buckets)) if buckets[b][0] > len(token_ids)])
            encoder_inputs, decoder_inputs, target_weights = model.get_batch(
                {bucket_id: [(token_ids, [])]}, bucket_id)
            _, _, output_logits_batch = model.step(sess, encoder_inputs, decoder_inputs, target_weights, bucket_id,
                                                   True)
            output_logits = []
            for item in output_logits_batch:
                output_logits.append(item[0])
            outputs = []
            for logit in output_logits:
                m = int(np.argmax(logit))
                if m == 3:
                    logit[3] = logit[np.argmin(logit)]
                    m = int(np.argmax(logit))
                outputs.append(m)

            #outputs = [int(np.argmax(logit)) for logit in output_logits]
            print(output_logits)
            # If there is an EOS symbol in outputs, cut them at that point.
            if data_utils.EOS_ID in outputs:
                outputs = outputs[:outputs.index(data_utils.EOS_ID)]
            AB3 = " ".join([tf.compat.as_str(rev_vocab[output]) for output in outputs])
        for i in range(90,101):
            time.sleep(0.1)
            self.progressBarValue.emit(i)
            if i==101:# 发送进度条的值 信号
                self.close()
def getAB1():
    return AB1
def getAB2():
    return AB2
def getAB3():
    return AB3
def get_text_for_AB():
    return text_for_AB
def get_text_for_words():
    return  text_for_words
#if __name__ == "__main__":
def sumcreatingshow():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_sumcreating()
    ui.setupUi(MainWindow)
    MainWindow.show()

    app.exec_()
  #  sys.exit()

#sumcreatingshow()