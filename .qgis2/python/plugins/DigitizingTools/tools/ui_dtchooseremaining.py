# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/ui_dtchooseremaining.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dtchooseremaining(object):
    def setupUi(self, dtchooseremaining):
        dtchooseremaining.setObjectName("dtchooseremaining")
        dtchooseremaining.resize(286, 101)
        dtchooseremaining.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(dtchooseremaining)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(dtchooseremaining)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.chooseId = QtGui.QComboBox(dtchooseremaining)
        self.chooseId.setObjectName("chooseId")
        self.verticalLayout.addWidget(self.chooseId)
        self.buttonBox = QtGui.QDialogButtonBox(dtchooseremaining)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dtchooseremaining)
        QtCore.QMetaObject.connectSlotsByName(dtchooseremaining)

    def retranslateUi(self, dtchooseremaining):
        _translate = QtCore.QCoreApplication.translate
        dtchooseremaining.setWindowTitle(_translate("dtchooseremaining", "Dialog"))
        self.label.setText(_translate("dtchooseremaining", "TextLabel"))

