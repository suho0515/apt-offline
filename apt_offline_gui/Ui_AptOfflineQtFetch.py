# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtFetch.ui'
#
# Created: Sun Aug 22 10:55:44 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AptOfflineQtFetch(object):
    def setupUi(self, AptOfflineQtFetch):
        AptOfflineQtFetch.setObjectName("AptOfflineQtFetch")
        AptOfflineQtFetch.setWindowModality(QtCore.Qt.ApplicationModal)
        AptOfflineQtFetch.resize(468, 495)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AptOfflineQtFetch.sizePolicy().hasHeightForWidth())
        AptOfflineQtFetch.setSizePolicy(sizePolicy)
        AptOfflineQtFetch.setMinimumSize(QtCore.QSize(468, 495))
        AptOfflineQtFetch.setMaximumSize(QtCore.QSize(468, 495))
        self.profileFilePath = QtGui.QLineEdit(AptOfflineQtFetch)
        self.profileFilePath.setGeometry(QtCore.QRect(30, 46, 270, 30))
        self.profileFilePath.setObjectName("profileFilePath")
        self.browseFilePathButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.browseFilePathButton.setGeometry(QtCore.QRect(320, 46, 110, 30))
        self.browseFilePathButton.setObjectName("browseFilePathButton")
        self.startDownloadButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.startDownloadButton.setEnabled(False)
        self.startDownloadButton.setGeometry(QtCore.QRect(90, 165, 130, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startDownloadButton.setIcon(icon)
        self.startDownloadButton.setShortcut("None")
        self.startDownloadButton.setCheckable(False)
        self.startDownloadButton.setChecked(False)
        self.startDownloadButton.setFlat(False)
        self.startDownloadButton.setObjectName("startDownloadButton")
        self.cancelButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.cancelButton.setGeometry(QtCore.QRect(240, 165, 140, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/dialog-cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName("cancelButton")
        self.label = QtGui.QLabel(AptOfflineQtFetch)
        self.label.setGeometry(QtCore.QRect(30, 16, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.statusProgressBar = QtGui.QProgressBar(AptOfflineQtFetch)
        self.statusProgressBar.setGeometry(QtCore.QRect(30, 230, 410, 20))
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setObjectName("statusProgressBar")
        self.label_2 = QtGui.QLabel(AptOfflineQtFetch)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressStatusDescription = QtGui.QLabel(AptOfflineQtFetch)
        self.progressStatusDescription.setGeometry(QtCore.QRect(90, 210, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressStatusDescription.setFont(font)
        self.progressStatusDescription.setObjectName("progressStatusDescription")
        self.rawLogHolder = QtGui.QTextEdit(AptOfflineQtFetch)
        self.rawLogHolder.setGeometry(QtCore.QRect(30, 268, 411, 211))
        self.rawLogHolder.setObjectName("rawLogHolder")
        self.browseZipFileButton = QtGui.QPushButton(AptOfflineQtFetch)
        self.browseZipFileButton.setGeometry(QtCore.QRect(320, 107, 110, 30))
        self.browseZipFileButton.setObjectName("browseZipFileButton")
        self.label_3 = QtGui.QLabel(AptOfflineQtFetch)
        self.label_3.setGeometry(QtCore.QRect(30, 77, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.zipFilePath = QtGui.QLineEdit(AptOfflineQtFetch)
        self.zipFilePath.setGeometry(QtCore.QRect(30, 107, 270, 30))
        self.zipFilePath.setObjectName("zipFilePath")

        self.retranslateUi(AptOfflineQtFetch)
        QtCore.QMetaObject.connectSlotsByName(AptOfflineQtFetch)

    def retranslateUi(self, AptOfflineQtFetch):
        AptOfflineQtFetch.setWindowTitle(QtGui.QApplication.translate("AptOfflineQtFetch", "Fetch Packages or Upgrade", None, QtGui.QApplication.UnicodeUTF8))
        self.browseFilePathButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.startDownloadButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Select the signature file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.progressStatusDescription.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.browseZipFileButton.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AptOfflineQtFetch", "Save archive as", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
