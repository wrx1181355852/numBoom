# coding:utf-8
# @创建时间：2021/4/10 18:26
# @Author  ：Administrator 
# @Email :  1181355852@qq.com
# @文件名：数字炸弹PyQt5.py
# @IDEName:PyCharm
# @工程名：7dayshudypyqt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint
from playsound import *
from threading import Thread
import sys

minding = 0
maxding = 0
state=0

def play_sound(file):  # 播放声音
    playsound(file)


class Setnumber:
    def __init__(self):
        super(Setnumber, self).__init__()
        self.ui = loadUi('../UI/setnumber.ui')
        # reg = QRegExp('[0-9]+$')
        # self.validator = QRegExpValidator()
        # self.validator.setRegExp(reg)
        self.ui.okbutton.setEnabled(False)
        self.ui.cancelbutton.clicked.connect(self.ui.close)
        self.minnum = 0
        self.maxnum = 0

        self.intValidator = QIntValidator()
        self.intValidator.setRange(0, 99999)

        self.ui.minlineEdit.setValidator(self.intValidator)

        self.ui.minlineEdit.setPlaceholderText('最小值')

        self.ui.maxlineEdit.setValidator(self.intValidator)

        self.ui.maxlineEdit.setPlaceholderText('最大值')

        self.intnum()


    def intnum(self):

        Thread(target=play_sound, args=('../sound/setin.mp3',), daemon=True).start()

        # self.ui.minlineEdit.clear()
        # self.ui.maxlineEdit.clear()
        self.ui.minlineEdit.setFocus()
        self.ui.minlineEdit.returnPressed.connect(self.ui.maxlineEdit.setFocus)

        self.ui.maxlineEdit.returnPressed.connect(self.cmp)
        self.ui.maxlineEdit.textChanged.connect(self.okbuttonsetEnabled)

        self.ui.okbutton.clicked.connect(self.cmp)

    def okbuttonsetEnabled(self):
        self.ui.okbutton.setEnabled(True)

    def cmp(self):
        global minding, maxding,state

        while True:

            # self.minnum = int(self.ui.minlineEdit.text())
            # self.maxnum = int(self.ui.maxlineEdit.text())

            if self.maxnum - self.minnum < 2:
                QMessageBox.warning(self.ui, '错误提示！', '请输入正确范围。')
                self.ui.minlineEdit.clear()
                self.ui.maxlineEdit.clear()
                self.intnum()


            else:

                break
        # print('ok')
        minding = self.minnum
        maxding = self.maxnum
        self.mainwindow = Mainwindow()
        self.ui.close()
        self.mainwindow.ui.show()


class Mainwindow:
    global minding, maxding,state

    def __init__(self):

        super(Mainwindow, self).__init__()
        self.ui =loadUi('../UI/mainwindow.ui')
        self.i = 0
        self.j = 0
        self.ui.endbutton.clicked.connect(self.ui.close)
        self.minNum = minding
        self.maxNum = maxding
        self.guess = 0
        self.state=state
        self.num = randint(self.minNum + 1, self.maxNum - 1)
        self.ui.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
        self.intValidator = QIntValidator()
        self.intValidator.setRange(0, 99999)
        self.ui.inlineEdit.setPlaceholderText('猜测的值')

        self.ui.statusbar.showMessage('就绪')
        self.ui.inlineEdit.setValidator(self.intValidator)
        Thread(target=play_sound, args=('../sound/guess.mp3',), daemon=True).start()
        self.ui.inlineEdit.editingFinished.connect(self.innum)
        self.ui.okbutton.released.connect(self.ui.inlineEdit.setFocus)
        self.ui.okbutton.released.connect(self.innum)
        self.ui.flushbutton.released.connect(self.flush)
        self.ui.flushbutton.released.connect(self.ui.inlineEdit.setFocus)

        self.ui.updatepattaern.triggered.connect(self.updatepatt)
        self.ui.updatepattaern.triggered.connect(self.ui.inlineEdit.setFocus)
        self.ui.updatenum.triggered.connect(self.updatee)
        self.ui.updatenum.triggered.connect(self.ui.inlineEdit.setFocus)

    def innum(self):
        global state
        self.i += 1
        try:
            self.guess = int(self.ui.inlineEdit.text())

            # print(self.guess,type(self.guess))
        except ValueError:
            return
        else:
            # 猜小了，更新低点
            if self.num > self.guess > self.minNum:
                self.minNum = self.guess
                self.ui.label1.setText('猜小了，再大点！')
                Thread(target=play_sound, args=('../sound/up.mp3',), daemon=True).start()
                self.ui.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
                self.ui.inlineEdit.clear()  # 猜小了，更新低点
            # 猜大了，更新高点
            elif self.num < self.guess < self.maxNum:
                self.maxNum = self.guess
                self.ui.label1.setText('猜大了，再小点！')
                self.ui.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
                Thread(target=play_sound, args=('../sound/down.mp3',), daemon=True).start()
                self.ui.inlineEdit.clear()
            # 猜对了
            elif self.guess == self.num:
                Thread(target=play_sound, args=('../sound/ding.mp3',), daemon=True).start()
                self.ui.inlineEdit.setFocus()
                self.ui.label1.setText('猜对啦！就是：')

                self.ui.label2.setText(f'{self.guess}')
                self.ui.inlineEdit.clear()
                QMessageBox.about(self.ui, '恭喜',
                                  f'恭喜你，猜对啦！\n\t就是{self.guess}\n共用了{self.i}次,其中有效{self.i - self.j}，\n\t无效{self.j}次。')

                self.flush()

            # 范围错误
            else:
                self.ui.label1.setText('请输入正确范围!')
                self.j += 1
                Thread(target=play_sound, args=('../sound/wrong.mp3',), daemon=True).start()
                self.ui.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
                self.ui.inlineEdit.clear()

    def flush(self):
        if self.state==0:
            Thread(target=play_sound, args=('../sound/guess.mp3',), daemon=True).start()
        elif self.state == 1:
            self.ui.close()
            self.setnum = Setnumber()
            self.setnum.ui.show()
        self.minNum = minding
        self.maxNum = maxding
        self.i = 0
        self.j = 0
        self.num = randint(self.minNum + 1, self.maxNum - 1)
        self.ui.label1.setText('请输数字：')
        self.ui.label2.setText(f'{self.minNum}-{self.maxNum}不包含{self.minNum}和{self.maxNum}')
        # Thread(target=play_sound, args=('../sound/guess.mp3',), daemon=True).start()

    def updatee(self):
        global state
        self.state = 0
        self.ui.close()
        self.setnum = Setnumber()
        self.setnum.ui.show()
        state=self.state

    def updatepatt(self):
        global state
        self.state = 1
        self.ui.hide()
        self.setnum = Setnumber()
        self.setnum.ui.show()
        state=self.state

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wm = Setnumber()
    wm.ui.show()
    sys.exit(app.exec_())
