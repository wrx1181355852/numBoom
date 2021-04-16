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
from UI.setnumber_pyqt5 import Ui_Dialog
from UI.mainwindow_pyqt5 import Ui_MainWindow
import sys
from PyQt5.QtCore import pyqtSlot

minding = 0
maxding = 0
state = 0


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

        self.minlineEdit.setPlaceholderText('最小值')

        self.maxlineEdit.setValidator(self.intValidator)

        self.maxlineEdit.setPlaceholderText('最大值')

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
        self.inlineEdit.setPlaceholderText('猜测的值')

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
