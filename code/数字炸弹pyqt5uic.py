# coding:utf-8
# @创建时间：2021/4/10 18:31
# @Author  ：Administrator 
# @Email :  1181355852@qq.com
# @文件名：数字炸弹pyqt5uic.py
# @IDEName:PyCharm
# @工程名：7dayshudypyqt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint
from playsound import *
from threading import Thread
# from setnumber_pyqt5 import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets

# from mainwindow_pyqt5 import Ui_MainWindow
import sys
from PyQt5.QtCore import pyqtSlot

minding = 0
maxding = 0
state = 0


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(270, 136)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/RY.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.minlineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minlineEdit.sizePolicy().hasHeightForWidth())
        self.minlineEdit.setSizePolicy(sizePolicy)
        self.minlineEdit.setText("")
        self.minlineEdit.setObjectName("minlineEdit")
        self.gridLayout.addWidget(self.minlineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.maxlineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxlineEdit.sizePolicy().hasHeightForWidth())
        self.maxlineEdit.setSizePolicy(sizePolicy)
        self.maxlineEdit.setText("")
        self.maxlineEdit.setObjectName("maxlineEdit")
        self.gridLayout.addWidget(self.maxlineEdit, 1, 1, 1, 2)
        self.okbutton = QtWidgets.QPushButton(self.widget)
        self.okbutton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbutton.sizePolicy().hasHeightForWidth())
        self.okbutton.setSizePolicy(sizePolicy)
        self.okbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.okbutton.setObjectName("okbutton")
        self.gridLayout.addWidget(self.okbutton, 2, 1, 1, 1)
        self.cancelbutton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbutton.sizePolicy().hasHeightForWidth())
        self.cancelbutton.setSizePolicy(sizePolicy)
        self.cancelbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancelbutton.setObjectName("cancelbutton")
        self.gridLayout.addWidget(self.cancelbutton, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.minlineEdit.returnPressed.connect(self.maxlineEdit.setFocus)
        self.cancelbutton.clicked.connect(Dialog.close)
        self.minlineEdit.returnPressed.connect(self.maxlineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.minlineEdit, self.maxlineEdit)
        Dialog.setTabOrder(self.maxlineEdit, self.okbutton)
        Dialog.setTabOrder(self.okbutton, self.cancelbutton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "数字炸弹"))
        self.label_3.setText(_translate("Dialog", "请输入猜测数字最大值和最小值"))
        self.label.setText(_translate("Dialog", "最小值"))
        self.label_2.setText(_translate("Dialog", "最大值"))
        self.okbutton.setText(_translate("Dialog", "确认"))
        self.cancelbutton.setText(_translate("Dialog", "取消"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 243)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/RY.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label1 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
        self.label2.setFont(font)
        self.label2.setText("")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(64, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inlineEdit.setObjectName("inlineEdit")
        self.verticalLayout.addWidget(self.inlineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okbutton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.okbutton.setFont(font)
        self.okbutton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.okbutton.setObjectName("okbutton")
        self.horizontalLayout.addWidget(self.okbutton)
        self.flushbutton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.flushbutton.setFont(font)
        self.flushbutton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.flushbutton.setObjectName("flushbutton")
        self.horizontalLayout.addWidget(self.flushbutton)
        self.endbutton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.endbutton.setFont(font)
        self.endbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.endbutton.setObjectName("endbutton")
        self.horizontalLayout.addWidget(self.endbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(64, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setToolTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.initpattern = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/Water Elemental.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.initpattern.setIcon(icon1)
        self.initpattern.setObjectName("initpattern")
        self.updatepattaern = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/images/Fire Elemental.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updatepattaern.setIcon(icon2)
        self.updatepattaern.setObjectName("updatepattaern")
        self.updatenum = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/images/doc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updatenum.setIcon(icon3)
        self.updatenum.setObjectName("updatenum")
        self.actionanswer = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pic/images/RY.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionanswer.setIcon(icon4)
        self.actionanswer.setObjectName("actionanswer")
        self.menu.addAction(self.updatenum)
        self.menu.addSeparator()
        self.menu.addAction(self.updatepattaern)
        self.menu_2.addAction(self.actionanswer)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.endbutton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数字炸弹"))
        MainWindow.setStatusTip(_translate("MainWindow", "就绪"))
        self.splitter.setStatusTip(_translate("MainWindow", "就绪"))
        self.label1.setStatusTip(_translate("MainWindow", "就绪"))
        self.label1.setText(_translate("MainWindow", "请输入数字："))
        self.label2.setStatusTip(_translate("MainWindow", "就绪"))
        self.inlineEdit.setStatusTip(_translate("MainWindow", "输入栏"))
        self.okbutton.setStatusTip(_translate("MainWindow", "确认"))
        self.okbutton.setText(_translate("MainWindow", "确认"))
        self.flushbutton.setStatusTip(_translate("MainWindow", "刷新"))
        self.flushbutton.setText(_translate("MainWindow", "刷新"))
        self.endbutton.setStatusTip(_translate("MainWindow", "退出"))
        self.endbutton.setText(_translate("MainWindow", "退出"))
        self.menu.setStatusTip(_translate("MainWindow", "菜单栏"))
        self.menu.setTitle(_translate("MainWindow", "模式选择"))
        self.menu_2.setTitle(_translate("MainWindow", "答案"))
        self.statusbar.setStatusTip(_translate("MainWindow", "状态栏"))
        self.initpattern.setText(_translate("MainWindow", "初始模式"))
        self.updatepattaern.setText(_translate("MainWindow", "更新模式"))
        self.updatepattaern.setStatusTip(_translate("MainWindow", "每局重新更新一次范围"))
        self.updatenum.setText(_translate("MainWindow", "更新范围"))
        self.updatenum.setStatusTip(_translate("MainWindow", "重新输入范围"))
        self.actionanswer.setText(_translate("MainWindow", "显示答案"))
        self.actionanswer.setToolTip(_translate("MainWindow", "显示答案"))
        self.actionanswer.setShortcut(_translate("MainWindow", "Ctrl+D"))

def play_sound(file):  # 播放声音
    playsound(file)


class Setnumber(QDialog, Ui_Dialog):
    def __init__(self):
        super(Setnumber, self).__init__()
        self.setupUi(self)
        self.minnum = 0
        self.maxnum = 0
        # self.okbutton.setEnabled(False)
        self.intValidator = QIntValidator()
        self.intnum()

    def intnum(self):
        self.okbutton.setEnabled(False)
        self.minlineEdit.clear()
        self.maxlineEdit.clear()
        # self.okbutton.setEnabled(False)

        self.intValidator.setRange(0, 99999)

        self.minlineEdit.setValidator(self.intValidator)

        self.minlineEdit.setPlaceholderText('最小值0~99999')

        self.maxlineEdit.setValidator(self.intValidator)

        self.maxlineEdit.setPlaceholderText('最大值0~99999')

        Thread(target=play_sound, args=('../sound/setin.mp3',), daemon=True).start()

        # self.maxlineEdit.textChanged

    @pyqtSlot(str)
    def on_maxlineEdit_textEdited(self):
        self.okbutton.setEnabled(True)
        # self.okbutton.setFocus()

    @pyqtSlot()
    def on_maxlineEdit_returnPressed(self):
        self.okbutton.setFocus()

    @pyqtSlot()
    def on_okbutton_clicked(self):
        minnumstr = self.minlineEdit.text()
        maxnumstr = self.maxlineEdit.text()
        print(minnumstr, maxnumstr)
        self.minnum = int(minnumstr)
        self.maxnum = int(maxnumstr)
        self.cmp()

    def cmp(self):
        global minding, maxding

        if self.maxnum - self.minnum < 2:

            QMessageBox.warning(self, '错误提示！', '请输入正确范围,\n两数之差应大于2。', QMessageBox.Ok, QMessageBox.Ok)

            self.intnum()
        else:
            minding = self.minnum
            maxding = self.maxnum
            self.mainwindow = Mainwindow()
            self.close()
            self.mainwindow.show()


class Mainwindow(QMainWindow, Ui_MainWindow):
    global minding, maxding, state

    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.i = 0
        self.j = 0
        self.minNum = minding
        self.maxNum = maxding
        self.guess = 0
        self.state = state
        self.num = randint(self.minNum + 1, self.maxNum - 1)
        self.intValidator = QIntValidator()
        self.initnum()

    def initnum(self):
        self.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')

        self.intValidator.setRange(0, 99999)
        self.inlineEdit.setPlaceholderText('猜测的值0~99999')

        self.statusbar.showMessage('就绪')
        self.inlineEdit.setValidator(self.intValidator)
        Thread(target=play_sound, args=('../sound/guess.mp3',), daemon=True).start()

    @pyqtSlot()
    def on_inlineEdit_returnPressed(self):
        self.okbutton.setFocus()
        self.guessnum()

        # self.okbutton.clicked

    @pyqtSlot()
    def on_okbutton_clicked(self):
        self.inlineEdit.setFocus()

        self.guessnum()

    def guessnum(self):
        global state
        self.i += 1

        try:
            self.guess = int(self.inlineEdit.text())

        except ValueError:
            return
        else:
            # 猜小了，更新低点
            if self.num > self.guess > self.minNum:
                self.minNum = self.guess
                self.label1.setText('猜小了，再大点！')
                Thread(target=play_sound, args=('../sound/up.mp3',), daemon=True).start()
                self.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
                self.inlineEdit.clear()
                self.inlineEdit.setFocus()

            elif self.num < self.guess < self.maxNum:
                self.maxNum = self.guess
                self.label1.setText('猜大了，再小点！')
                self.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
                Thread(target=play_sound, args=('../sound/down.mp3',), daemon=True).start()
                self.inlineEdit.clear()
                self.inlineEdit.setFocus()
            elif self.guess == self.num:
                Thread(target=play_sound, args=('../sound/ding.mp3',), daemon=True).start()
                self.inlineEdit.setFocus()
                self.label1.setText('猜对啦！就是：')

                self.label2.setText(f'{self.guess}')
                self.inlineEdit.clear()

                QMessageBox.about(self, '恭喜',
                                  f'恭喜你，猜对啦！\n\t就是{self.guess}\n共用了{self.i}次,其中有效{self.i - self.j}，\n\t无效{self.j}次。')
                self.flush()
            # 猜对了,
            else:
                self.label1.setText('请输入正确范围!')
                self.j += 1
                Thread(target=play_sound, args=('../sound/wrong.mp3',), daemon=True).start()
                self.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
                self.inlineEdit.clear()
                self.inlineEdit.setFocus()

    @pyqtSlot()
    def on_flushbutton_clicked(self):
        self.flush()

    def flush(self):
        if self.state == 0:
            Thread(target=play_sound, args=('../sound/guess.mp3',), daemon=True).start()
        elif self.state == 1:
            self.close()
            self.setnum = Setnumber()
            self.setnum.show()
        self.minNum = minding
        self.maxNum = maxding
        self.i = 0
        self.j = 0
        self.num = randint(self.minNum + 1, self.maxNum - 1)
        self.label1.setText('请输数字：')
        self.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
        self.inlineEdit.setFocus()

        # Thread(target=play_sound, args=('../sound/guess.mp3',), daemon=True).start()

    @pyqtSlot()
    def on_updatenum_triggered(self):
        self.updatee()

    def updatee(self):
        global state
        self.state = 0
        self.close()
        self.setnum = Setnumber()
        self.setnum.show()
        state = self.state
        self.inlineEdit.setFocus()

    @pyqtSlot()
    def on_updatepattaern_triggered(self):
        self.updatepatt()

    def updatepatt(self):
        global state
        self.state = 1
        self.hide()
        self.setnum = Setnumber()
        self.setnum.show()
        state = self.state
        self.inlineEdit.setFocus()

    @pyqtSlot()
    def on_actionanswer_triggered(self):
        self.label2.setText(f'答案是{self.num}')
        self.inlineEdit.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wm = Setnumber()
    wm.show()
    sys.exit(app.exec_())
