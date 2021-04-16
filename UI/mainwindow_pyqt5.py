# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
import image_pyqt5_rc
