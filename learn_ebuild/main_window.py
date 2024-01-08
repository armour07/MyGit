# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(554, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.editorTab = QtWidgets.QWidget()
        self.editorTab.setObjectName("editorTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.editorTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(430, 370, 51, 88))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.cnRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.cnRadioButton.setObjectName("cnRadioButton")
        self.verticalLayout.addWidget(self.cnRadioButton)
        self.enRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.enRadioButton.setObjectName("enRadioButton")
        self.verticalLayout.addWidget(self.enRadioButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.openLangFolderBtn = QtWidgets.QPushButton(self.editorTab)
        self.openLangFolderBtn.setGeometry(QtCore.QRect(10, 20, 171, 23))
        self.openLangFolderBtn.setObjectName("openLangFolderBtn")
        self.openLangFolderSelectBtn = QtWidgets.QPushButton(self.editorTab)
        self.openLangFolderSelectBtn.setGeometry(QtCore.QRect(10, 60, 171, 23))
        self.openLangFolderSelectBtn.setObjectName("openLangFolderSelectBtn")
        self.startBtn = QtWidgets.QPushButton(self.editorTab)
        self.startBtn.setGeometry(QtCore.QRect(10, 420, 61, 23))
        self.startBtn.setObjectName("startBtn")
        self.pauseBtn = QtWidgets.QPushButton(self.editorTab)
        self.pauseBtn.setGeometry(QtCore.QRect(10, 450, 61, 23))
        self.pauseBtn.setObjectName("pauseBtn")
        self.listWidget = QtWidgets.QListWidget(self.editorTab)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 171, 311))
        self.listWidget.setObjectName("listWidget")
        self.resumeBtn = QtWidgets.QPushButton(self.editorTab)
        self.resumeBtn.setGeometry(QtCore.QRect(90, 450, 61, 23))
        self.resumeBtn.setObjectName("resumeBtn")
        self.stopBtn = QtWidgets.QPushButton(self.editorTab)
        self.stopBtn.setGeometry(QtCore.QRect(90, 420, 61, 23))
        self.stopBtn.setObjectName("stopBtn")
        self.tabWidget.addTab(self.editorTab, "")
        self.packageTab = QtWidgets.QWidget()
        self.packageTab.setObjectName("packageTab")
        self.tabWidget.addTab(self.packageTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "窗口"))
        self.cnRadioButton.setText(_translate("mainWindow", "中文"))
        self.enRadioButton.setText(_translate("mainWindow", "英文"))
        self.openLangFolderBtn.setText(_translate("mainWindow", "打开语言配置文件夹"))
        self.openLangFolderSelectBtn.setText(_translate("mainWindow", "打开语言配置文件夹并选中"))
        self.startBtn.setText(_translate("mainWindow", "开始"))
        self.pauseBtn.setText(_translate("mainWindow", "暂停"))
        self.resumeBtn.setText(_translate("mainWindow", "恢复"))
        self.stopBtn.setText(_translate("mainWindow", "停止"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editorTab), _translate("mainWindow", "编辑器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.packageTab), _translate("mainWindow", "包体"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionSave.setText(_translate("mainWindow", "Save"))