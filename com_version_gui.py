# -*- coding:utf-8 -*-
import sys,os
from PyQt5 import QtCore,QtGui
from PyQt5 import sip
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QGridLayout, QApplication,QLabel,qApp,QMessageBox,QTextEdit)
from com_dirs import CombineCMOversion

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

class Example(QWidget):
    def __init__(self):
        super().__init__()
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stder = EmittingStream(textWritten=self.normalOutputWritten)
        self.initUI()

    def initUI(self):
        '''
        # 标签1
        lb1 = QLabel("源目录", self)
        #lb1.move(20,30)
        # 标签2
        lb2=QLabel("目标目录",self)
        #lb2.move(20, 70)
        # 输入框1
        self.ledit1 = QLineEdit(self)
        #self.ledit1.setGeometry(QtCore.QRect(110, 30, 200, 30))
        # 输入框2
        self.ledit2 = QLineEdit(self)
        #self.ledit2.setGeometry(QtCore.QRect(110, 70, 200, 30))
        # 按钮1
        btn_start=QPushButton('开始处理',self)
        #btn_start.move(20,120)
        btn_start.setToolTip('<b>开始合并CMO的版本</b>')
        btn_start.clicked.connect(self.process_dir)
        #按钮2
        btn_quit = QPushButton('退出', self)
        #btn_quit.move(220, 120)
        btn_quit.setToolTip('<b>退出程序</b>')
        btn_quit.clicked.connect(qApp.quit)
        '''

        srcdir = QLabel('源目录')
        destdir = QLabel('目标目录')

        self.srcdir_edit = QLineEdit()
        self.destdir_edit = QLineEdit()

        ok_button = QPushButton("开始处理")
        ok_button.setToolTip('<b>开始合并CMO的版本</b>')
        ok_button.clicked.connect(self.process_dir)
        quit_button=QPushButton("退出")
        quit_button.setToolTip('<b>退出程序</b>')
        quit_button.clicked.connect(qApp.quit)

        log_lab = QLabel('日志信息')
        self.log_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(srcdir, 1, 0)
        grid.addWidget(self.srcdir_edit, 1, 1,2,1)

        grid.addWidget(destdir, 3, 0)
        grid.addWidget(self.destdir_edit, 3, 1,2,1)

        grid.addWidget(quit_button, 5, 0, 1, 1)
        grid.addWidget(ok_button, 5, 1, 1, 1)

        grid.addWidget(log_lab, 7, 0, 1, 1)
        grid.addWidget(self.log_edit, 7, 1, 1, 1)
        self.setLayout(grid)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle("版本预处理")
        self.setWindowIcon(QtGui.QIcon('./download.png'))
        self.show()

    def normalOutputWritten(self, text):
        cursor = self.log_edit.textCursor()
        #cursor.moveCursor(QtGui.QTextCursor.End)
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.log_edit.setTextCursor(cursor)
        self.log_edit.ensureCursorVisible()

    def process_dir(self):
        print("src directory is",self.srcdir_edit.text())
        print("dest directory is",self.destdir_edit.text())
        if self.srcdir_edit.text() and self.destdir_edit.text():
            if os.path.exists(self.srcdir_edit.text()):
                try:
                    com=CombineCMOversion(self.srcdir_edit.text(),self.destdir_edit.text())
                    com.MainProcess()
                    reply = QMessageBox.information(self,"提示","合并CMO版本完成",QMessageBox.Yes | QMessageBox.No)
                except:
                    print ("process error")
                    reply = QMessageBox.information(self, "提示", "合并CMO版本失败", QMessageBox.Yes | QMessageBox.No)
            else:
                print ("src directory not found")
        else:
            print ("input path is invalid")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())