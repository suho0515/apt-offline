# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtMain.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AptOfflineMain(object):
    def setupUi(self, AptOfflineMain):
        AptOfflineMain.setObjectName("AptOfflineMain")
        AptOfflineMain.resize(432, 544)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AptOfflineMain.sizePolicy().hasHeightForWidth())
        AptOfflineMain.setSizePolicy(sizePolicy)
        AptOfflineMain.setMinimumSize(QtCore.QSize(432, 544))
        AptOfflineMain.setMaximumSize(QtCore.QSize(432, 544))
        AptOfflineMain.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        AptOfflineMain.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(AptOfflineMain)
        self.centralwidget.setObjectName("centralwidget")
        self.createProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.createProfileButton.setGeometry(QtCore.QRect(30, 20, 371, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createProfileButton.setFont(font)
        self.createProfileButton.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/contact-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createProfileButton.setIcon(icon)
        self.createProfileButton.setObjectName("createProfileButton")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(30, 80, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.downloadButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon1)
        self.downloadButton.setObjectName("downloadButton")
        self.restoreButton = QtWidgets.QPushButton(self.centralwidget)
        self.restoreButton.setGeometry(QtCore.QRect(30, 140, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restoreButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setObjectName("restoreButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 220, 371, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.descriptionField = QtWidgets.QLabel(self.frame)
        self.descriptionField.setGeometry(QtCore.QRect(0, 0, 371, 211))
        self.descriptionField.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionField.setWordWrap(True)
        self.descriptionField.setObjectName("descriptionField")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(280, 450, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon3)
        self.exitButton.setObjectName("exitButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        AptOfflineMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AptOfflineMain)
        self.statusbar.setObjectName("statusbar")
        AptOfflineMain.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(AptOfflineMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 28))
        self.menubar.setObjectName("menubar")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        AptOfflineMain.setMenuBar(self.menubar)
        self.menuCreateProfile = QtWidgets.QAction(AptOfflineMain)
        self.menuCreateProfile.setIcon(icon)
        self.menuCreateProfile.setObjectName("menuCreateProfile")
        self.menuDownload = QtWidgets.QAction(AptOfflineMain)
        self.menuDownload.setIcon(icon1)
        self.menuDownload.setObjectName("menuDownload")
        self.menuInstall = QtWidgets.QAction(AptOfflineMain)
        self.menuInstall.setIcon(icon2)
        self.menuInstall.setObjectName("menuInstall")
        self.menuExit = QtWidgets.QAction(AptOfflineMain)
        self.menuExit.setIcon(icon3)
        self.menuExit.setObjectName("menuExit")
        self.menuHelp_2 = QtWidgets.QAction(AptOfflineMain)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/help-contents.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHelp_2.setIcon(icon4)
        self.menuHelp_2.setObjectName("menuHelp_2")
        self.menuAbout = QtWidgets.QAction(AptOfflineMain)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/help-about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAbout.setIcon(icon5)
        self.menuAbout.setObjectName("menuAbout")
        self.menuOperations.addAction(self.menuCreateProfile)
        self.menuOperations.addAction(self.menuDownload)
        self.menuOperations.addAction(self.menuInstall)
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.menuExit)
        self.menuHelp.addAction(self.menuHelp_2)
        self.menuHelp.addAction(self.menuAbout)
        self.menubar.addAction(self.menuOperations.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AptOfflineMain)
        QtCore.QMetaObject.connectSlotsByName(AptOfflineMain)

    def retranslateUi(self, AptOfflineMain):
        _translate = QtCore.QCoreApplication.translate
        AptOfflineMain.setWindowTitle(_translate("AptOfflineMain", "APT Offline"))
        self.createProfileButton.setText(_translate("AptOfflineMain", "Generate Signature"))
        self.downloadButton.setText(_translate("AptOfflineMain", "Download Packages or Updates"))
        self.restoreButton.setText(_translate("AptOfflineMain", "Install Packages or Updates"))
        self.descriptionField.setText(_translate("AptOfflineMain", "Hover your mouse over the buttons to get the description"))
        self.exitButton.setText(_translate("AptOfflineMain", "Exit"))
        self.label_2.setText(_translate("AptOfflineMain", "Description"))
        self.menuOperations.setTitle(_translate("AptOfflineMain", "Operations"))
        self.menuHelp.setTitle(_translate("AptOfflineMain", "Help"))
        self.menuCreateProfile.setText(_translate("AptOfflineMain", "Generate Signature"))
        self.menuCreateProfile.setShortcut(_translate("AptOfflineMain", "Ctrl+N"))
        self.menuDownload.setText(_translate("AptOfflineMain", "Download Packages or Updates"))
        self.menuDownload.setShortcut(_translate("AptOfflineMain", "Ctrl+O"))
        self.menuInstall.setText(_translate("AptOfflineMain", "Install Packages or Updates"))
        self.menuInstall.setShortcut(_translate("AptOfflineMain", "Ctrl+I"))
        self.menuExit.setText(_translate("AptOfflineMain", "Exit"))
        self.menuExit.setShortcut(_translate("AptOfflineMain", "Ctrl+Q"))
        self.menuHelp_2.setText(_translate("AptOfflineMain", "Help"))
        self.menuHelp_2.setShortcut(_translate("AptOfflineMain", "F1"))
        self.menuAbout.setText(_translate("AptOfflineMain", "About apt-offline"))

import resources_rc
