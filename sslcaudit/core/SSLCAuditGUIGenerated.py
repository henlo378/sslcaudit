# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu May 24 22:36:23 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(800, 600)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
    self.splitter = QtGui.QSplitter(self.centralwidget)
    self.splitter.setOrientation(QtCore.Qt.Horizontal)
    self.splitter.setObjectName(_fromUtf8("splitter"))
    self.widget = QtGui.QWidget(self.splitter)
    self.widget.setObjectName(_fromUtf8("widget"))
    self.verticalLayout = QtGui.QVBoxLayout(self.widget)
    self.verticalLayout.setMargin(0)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.formLayout = QtGui.QFormLayout()
    self.formLayout.setObjectName(_fromUtf8("formLayout"))
    self.listenOnLabel = QtGui.QLabel(self.widget)
    self.listenOnLabel.setObjectName(_fromUtf8("listenOnLabel"))
    self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.listenOnLabel)
    self.horizontalLayout_8 = QtGui.QHBoxLayout()
    self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
    self.hostnameLineEdit = QtGui.QLineEdit(self.widget)
    self.hostnameLineEdit.setMinimumSize(QtCore.QSize(175, 0))
    self.hostnameLineEdit.setText(_fromUtf8(""))
    self.hostnameLineEdit.setMaxLength(15)
    self.hostnameLineEdit.setObjectName(_fromUtf8("hostnameLineEdit"))
    self.horizontalLayout_8.addWidget(self.hostnameLineEdit)
    self.portLineEdit = QtGui.QLineEdit(self.widget)
    self.portLineEdit.setMinimumSize(QtCore.QSize(50, 0))
    self.portLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
    self.portLineEdit.setMaxLength(5)
    self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
    self.horizontalLayout_8.addWidget(self.portLineEdit)
    self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)
    self.selfTestLabel = QtGui.QLabel(self.widget)
    self.selfTestLabel.setObjectName(_fromUtf8("selfTestLabel"))
    self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.selfTestLabel)
    self.selfTestComboBox = QtGui.QComboBox(self.widget)
    self.selfTestComboBox.setObjectName(_fromUtf8("selfTestComboBox"))
    self.selfTestComboBox.addItem(_fromUtf8(""))
    self.selfTestComboBox.addItem(_fromUtf8(""))
    self.selfTestComboBox.addItem(_fromUtf8(""))
    self.selfTestComboBox.addItem(_fromUtf8(""))
    self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.selfTestComboBox)
    self.numerOfRoundsLabel = QtGui.QLabel(self.widget)
    self.numerOfRoundsLabel.setObjectName(_fromUtf8("numerOfRoundsLabel"))
    self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.numerOfRoundsLabel)
    self.numerOfRoundsSpinBox = QtGui.QSpinBox(self.widget)
    self.numerOfRoundsSpinBox.setMinimum(1)
    self.numerOfRoundsSpinBox.setMaximum(999999999)
    self.numerOfRoundsSpinBox.setObjectName(_fromUtf8("numerOfRoundsSpinBox"))
    self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numerOfRoundsSpinBox)
    self.verticalLayout.addLayout(self.formLayout)
    spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.verticalLayout.addItem(spacerItem)
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.progressBar = QtGui.QProgressBar(self.widget)
    self.progressBar.setMinimumSize(QtCore.QSize(185, 0))
    self.progressBar.setProperty("value", 24)
    self.progressBar.setObjectName(_fromUtf8("progressBar"))
    self.horizontalLayout.addWidget(self.progressBar)
    self.startButton = QtGui.QPushButton(self.widget)
    self.startButton.setObjectName(_fromUtf8("startButton"))
    self.horizontalLayout.addWidget(self.startButton)
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.tabWidget = QtGui.QTabWidget(self.splitter)
    self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
    self.tab = QtGui.QWidget()
    self.tab.setObjectName(_fromUtf8("tab"))
    self.gridLayout_9 = QtGui.QGridLayout(self.tab)
    self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
    self.groupBox_3 = QtGui.QGroupBox(self.tab)
    self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
    self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_3)
    self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
    self.radioButton = QtGui.QRadioButton(self.groupBox_3)
    self.radioButton.setChecked(True)
    self.radioButton.setObjectName(_fromUtf8("radioButton"))
    self.gridLayout_8.addWidget(self.radioButton, 0, 0, 1, 1)
    self.horizontalLayout_2 = QtGui.QHBoxLayout()
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    self.customCommonNameRadioButton = QtGui.QRadioButton(self.groupBox_3)
    self.customCommonNameRadioButton.setText(_fromUtf8(""))
    self.customCommonNameRadioButton.setObjectName(_fromUtf8("customCommonNameRadioButton"))
    self.horizontalLayout_2.addWidget(self.customCommonNameRadioButton)
    self.customCommonName = QtGui.QLineEdit(self.groupBox_3)
    self.customCommonName.setEnabled(False)
    self.customCommonName.setObjectName(_fromUtf8("customCommonName"))
    self.horizontalLayout_2.addWidget(self.customCommonName)
    self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
    self.gridLayout_9.addWidget(self.groupBox_3, 0, 0, 1, 1)
    self.groupBox_4 = QtGui.QGroupBox(self.tab)
    self.groupBox_4.setFlat(False)
    self.groupBox_4.setCheckable(True)
    self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
    self.formLayout_2 = QtGui.QFormLayout(self.groupBox_4)
    self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
    self.label = QtGui.QLabel(self.groupBox_4)
    self.label.setObjectName(_fromUtf8("label"))
    self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
    self.horizontalLayout_3 = QtGui.QHBoxLayout()
    self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
    self.certificateEdit1 = QtGui.QLineEdit(self.groupBox_4)
    self.certificateEdit1.setObjectName(_fromUtf8("certificateEdit1"))
    self.horizontalLayout_3.addWidget(self.certificateEdit1)
    self.certificateBrowse1 = QtGui.QPushButton(self.groupBox_4)
    self.certificateBrowse1.setObjectName(_fromUtf8("certificateBrowse1"))
    self.horizontalLayout_3.addWidget(self.certificateBrowse1)
    self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
    self.label_2 = QtGui.QLabel(self.groupBox_4)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
    self.horizontalLayout_4 = QtGui.QHBoxLayout()
    self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
    self.keyEdit1 = QtGui.QLineEdit(self.groupBox_4)
    self.keyEdit1.setObjectName(_fromUtf8("keyEdit1"))
    self.horizontalLayout_4.addWidget(self.keyEdit1)
    self.keyBrowse1 = QtGui.QPushButton(self.groupBox_4)
    self.keyBrowse1.setObjectName(_fromUtf8("keyBrowse1"))
    self.horizontalLayout_4.addWidget(self.keyBrowse1)
    self.formLayout_2.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
    self.gridLayout_9.addWidget(self.groupBox_4, 1, 0, 1, 1)
    self.groupBox_5 = QtGui.QGroupBox(self.tab)
    self.groupBox_5.setFlat(False)
    self.groupBox_5.setCheckable(True)
    self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
    self.formLayout_3 = QtGui.QFormLayout(self.groupBox_5)
    self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
    self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
    self.label_3 = QtGui.QLabel(self.groupBox_5)
    self.label_3.setObjectName(_fromUtf8("label_3"))
    self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
    self.horizontalLayout_5 = QtGui.QHBoxLayout()
    self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
    self.certificateEdit2 = QtGui.QLineEdit(self.groupBox_5)
    self.certificateEdit2.setObjectName(_fromUtf8("certificateEdit2"))
    self.horizontalLayout_5.addWidget(self.certificateEdit2)
    self.certificateBrowse2 = QtGui.QPushButton(self.groupBox_5)
    self.certificateBrowse2.setObjectName(_fromUtf8("certificateBrowse2"))
    self.horizontalLayout_5.addWidget(self.certificateBrowse2)
    self.formLayout_3.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
    self.label_4 = QtGui.QLabel(self.groupBox_5)
    self.label_4.setObjectName(_fromUtf8("label_4"))
    self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
    self.horizontalLayout_6 = QtGui.QHBoxLayout()
    self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
    self.keyEdit2 = QtGui.QLineEdit(self.groupBox_5)
    self.keyEdit2.setObjectName(_fromUtf8("keyEdit2"))
    self.horizontalLayout_6.addWidget(self.keyEdit2)
    self.keyBrowse2 = QtGui.QPushButton(self.groupBox_5)
    self.keyBrowse2.setObjectName(_fromUtf8("keyBrowse2"))
    self.horizontalLayout_6.addWidget(self.keyBrowse2)
    self.formLayout_3.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
    self.horizontalLayout_7 = QtGui.QHBoxLayout()
    self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
    self.pushButton_6 = QtGui.QPushButton(self.groupBox_5)
    self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
    self.horizontalLayout_7.addWidget(self.pushButton_6)
    self.pushButton_7 = QtGui.QPushButton(self.groupBox_5)
    self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
    self.horizontalLayout_7.addWidget(self.pushButton_7)
    self.formLayout_3.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
    self.gridLayout_9.addWidget(self.groupBox_5, 2, 0, 1, 1)
    self.checkBox_2 = QtGui.QCheckBox(self.tab)
    self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
    self.gridLayout_9.addWidget(self.checkBox_2, 3, 0, 1, 1)
    self.checkBox_3 = QtGui.QCheckBox(self.tab)
    self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
    self.gridLayout_9.addWidget(self.checkBox_3, 4, 0, 1, 1)
    spacerItem1 = QtGui.QSpacerItem(38, 134, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout_9.addItem(spacerItem1, 5, 0, 1, 1)
    self.tabWidget.addTab(self.tab, _fromUtf8(""))
    self.tab_2 = QtGui.QWidget()
    self.tab_2.setObjectName(_fromUtf8("tab_2"))
    self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
    self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
    self.groupBox = QtGui.QGroupBox(self.tab_2)
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
    self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
    self.protocolList = QtGui.QListWidget(self.groupBox)
    self.protocolList.setObjectName(_fromUtf8("protocolList"))
    item = QtGui.QListWidgetItem()
    self.protocolList.addItem(item)
    item = QtGui.QListWidgetItem()
    self.protocolList.addItem(item)
    item = QtGui.QListWidgetItem()
    self.protocolList.addItem(item)
    item = QtGui.QListWidgetItem()
    self.protocolList.addItem(item)
    self.gridLayout_4.addWidget(self.protocolList, 0, 0, 1, 1)
    self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
    self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
    self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
    self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
    self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
    self.cipherList = QtGui.QListWidget(self.groupBox_2)
    self.cipherList.setObjectName(_fromUtf8("cipherList"))
    item = QtGui.QListWidgetItem()
    self.cipherList.addItem(item)
    item = QtGui.QListWidgetItem()
    self.cipherList.addItem(item)
    item = QtGui.QListWidgetItem()
    self.cipherList.addItem(item)
    item = QtGui.QListWidgetItem()
    self.cipherList.addItem(item)
    self.gridLayout_5.addWidget(self.cipherList, 0, 0, 1, 1)
    self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)
    self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
    self.tab_3 = QtGui.QWidget()
    self.tab_3.setObjectName(_fromUtf8("tab_3"))
    self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
    self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
    self.treeWidget = QtGui.QTreeWidget(self.tab_3)
    self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
    self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 1)
    self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
    self.tab_4 = QtGui.QWidget()
    self.tab_4.setObjectName(_fromUtf8("tab_4"))
    self.gridLayout_2 = QtGui.QGridLayout(self.tab_4)
    self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
    self.showDebugMessagesCheckBox = QtGui.QCheckBox(self.tab_4)
    self.showDebugMessagesCheckBox.setObjectName(_fromUtf8("showDebugMessagesCheckBox"))
    self.gridLayout_2.addWidget(self.showDebugMessagesCheckBox, 1, 0, 1, 1)
    self.testLog = QtGui.QListWidget(self.tab_4)
    self.testLog.setObjectName(_fromUtf8("testLog"))
    self.gridLayout_2.addWidget(self.testLog, 0, 0, 1, 1)
    self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
    self.tab_5 = QtGui.QWidget()
    self.tab_5.setObjectName(_fromUtf8("tab_5"))
    self.gridLayout = QtGui.QGridLayout(self.tab_5)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    spacerItem2 = QtGui.QSpacerItem(250, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
    self.copyToClipboardButton = QtGui.QPushButton(self.tab_5)
    self.copyToClipboardButton.setObjectName(_fromUtf8("copyToClipboardButton"))
    self.gridLayout.addWidget(self.copyToClipboardButton, 1, 1, 1, 1)
    self.reportText = QtGui.QTextEdit(self.tab_5)
    self.reportText.setReadOnly(True)
    self.reportText.setObjectName(_fromUtf8("reportText"))
    self.gridLayout.addWidget(self.reportText, 0, 0, 1, 2)
    self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
    self.gridLayout_7.addWidget(self.splitter, 0, 0, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)

    self.retranslateUi(MainWindow)
    self.tabWidget.setCurrentIndex(3)
    QtCore.QObject.connect(self.customCommonNameRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.customCommonName.setEnabled)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "sslcaudit", None, QtGui.QApplication.UnicodeUTF8))
    self.listenOnLabel.setText(QtGui.QApplication.translate("MainWindow", "Listen on", None, QtGui.QApplication.UnicodeUTF8))
    self.hostnameLineEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Hostname (defaults to any)", None, QtGui.QApplication.UnicodeUTF8))
    self.portLineEdit.setText(QtGui.QApplication.translate("MainWindow", "8443", None, QtGui.QApplication.UnicodeUTF8))
    self.portLineEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
    self.selfTestLabel.setText(QtGui.QApplication.translate("MainWindow", "Self Test", None, QtGui.QApplication.UnicodeUTF8))
    self.selfTestComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
    self.selfTestComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "TCP client", None, QtGui.QApplication.UnicodeUTF8))
    self.selfTestComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Common Name verifying client", None, QtGui.QApplication.UnicodeUTF8))
    self.selfTestComboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "curl", None, QtGui.QApplication.UnicodeUTF8))
    self.numerOfRoundsLabel.setText(QtGui.QApplication.translate("MainWindow", "Numer of Rounds", None, QtGui.QApplication.UnicodeUTF8))
    self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
    self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Common Name (CN)", None, QtGui.QApplication.UnicodeUTF8))
    self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "Use default CN", None, QtGui.QApplication.UnicodeUTF8))
    self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Use a certificate", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setText(QtGui.QApplication.translate("MainWindow", "Certificate file", None, QtGui.QApplication.UnicodeUTF8))
    self.certificateBrowse1.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a certificate file", None, QtGui.QApplication.UnicodeUTF8))
    self.certificateBrowse1.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
    self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Key file", None, QtGui.QApplication.UnicodeUTF8))
    self.keyBrowse1.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a key file", None, QtGui.QApplication.UnicodeUTF8))
    self.keyBrowse1.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
    self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Use a Certificate Authority", None, QtGui.QApplication.UnicodeUTF8))
    self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Certificate file", None, QtGui.QApplication.UnicodeUTF8))
    self.certificateBrowse2.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a certificate file", None, QtGui.QApplication.UnicodeUTF8))
    self.certificateBrowse2.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
    self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Key file", None, QtGui.QApplication.UnicodeUTF8))
    self.keyBrowse2.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a key file", None, QtGui.QApplication.UnicodeUTF8))
    self.keyBrowse2.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
    self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Generate", None, QtGui.QApplication.UnicodeUTF8))
    self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "Export PKCS #12", None, QtGui.QApplication.UnicodeUTF8))
    self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "Use self-signed cerficiates", None, QtGui.QApplication.UnicodeUTF8))
    self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "User certificates signed by user certificate", None, QtGui.QApplication.UnicodeUTF8))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "SSLCert", None, QtGui.QApplication.UnicodeUTF8))
    self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Protocols", None, QtGui.QApplication.UnicodeUTF8))
    __sortingEnabled = self.protocolList.isSortingEnabled()
    self.protocolList.setSortingEnabled(False)
    item = self.protocolList.item(0)
    item.setText(QtGui.QApplication.translate("MainWindow", "Protocol A", None, QtGui.QApplication.UnicodeUTF8))
    item = self.protocolList.item(1)
    item.setText(QtGui.QApplication.translate("MainWindow", "Protocol B", None, QtGui.QApplication.UnicodeUTF8))
    item = self.protocolList.item(2)
    item.setText(QtGui.QApplication.translate("MainWindow", "Protocol C", None, QtGui.QApplication.UnicodeUTF8))
    item = self.protocolList.item(3)
    item.setText(QtGui.QApplication.translate("MainWindow", "Protocol D", None, QtGui.QApplication.UnicodeUTF8))
    self.protocolList.setSortingEnabled(__sortingEnabled)
    self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Ciphers", None, QtGui.QApplication.UnicodeUTF8))
    __sortingEnabled = self.cipherList.isSortingEnabled()
    self.cipherList.setSortingEnabled(False)
    item = self.cipherList.item(0)
    item.setText(QtGui.QApplication.translate("MainWindow", "Cipher A", None, QtGui.QApplication.UnicodeUTF8))
    item = self.cipherList.item(1)
    item.setText(QtGui.QApplication.translate("MainWindow", "Cipher B", None, QtGui.QApplication.UnicodeUTF8))
    item = self.cipherList.item(2)
    item.setText(QtGui.QApplication.translate("MainWindow", "Cipher C", None, QtGui.QApplication.UnicodeUTF8))
    item = self.cipherList.item(3)
    item.setText(QtGui.QApplication.translate("MainWindow", "Cipher D", None, QtGui.QApplication.UnicodeUTF8))
    self.cipherList.setSortingEnabled(__sortingEnabled)
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "SSLProto", None, QtGui.QApplication.UnicodeUTF8))
    self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Client Address", None, QtGui.QApplication.UnicodeUTF8))
    self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Server Profile", None, QtGui.QApplication.UnicodeUTF8))
    self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Report", None, QtGui.QApplication.UnicodeUTF8))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Connections", None, QtGui.QApplication.UnicodeUTF8))
    self.showDebugMessagesCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Show debug messages", None, QtGui.QApplication.UnicodeUTF8))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Test Log", None, QtGui.QApplication.UnicodeUTF8))
    self.copyToClipboardButton.setText(QtGui.QApplication.translate("MainWindow", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
    self.reportText.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'monospace\';\">This is the report text. It will be copied to your clipboard.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Report", None, QtGui.QApplication.UnicodeUTF8))

