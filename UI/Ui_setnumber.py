# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python Project\numBoom\UI\setnumber.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
