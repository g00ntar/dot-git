# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_place_orientation.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PlaceOrientation(object):
    def setupUi(self, PlaceOrientation):
        PlaceOrientation.setObjectName(_fromUtf8("PlaceOrientation"))
        PlaceOrientation.resize(321, 162)
        self.gridLayout = QtGui.QGridLayout(PlaceOrientation)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(PlaceOrientation)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PlaceOrientation)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.label_8 = QtGui.QLabel(PlaceOrientation)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.precision = QtGui.QDoubleSpinBox(PlaceOrientation)
        self.precision.setEnabled(True)
        self.precision.setDecimals(4)
        self.precision.setMaximum(10.0)
        self.precision.setSingleStep(0.05)
        self.precision.setProperty("value", 0.5)
        self.precision.setObjectName(_fromUtf8("precision"))
        self.gridLayout.addWidget(self.precision, 4, 4, 1, 1)
        self.label = QtGui.QLabel(PlaceOrientation)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.length = QtGui.QDoubleSpinBox(PlaceOrientation)
        self.length.setDecimals(1)
        self.length.setProperty("value", 8.0)
        self.length.setObjectName(_fromUtf8("length"))
        self.gridLayout.addWidget(self.length, 3, 4, 1, 1)
        self.observation = QtGui.QDoubleSpinBox(PlaceOrientation)
        self.observation.setDecimals(4)
        self.observation.setMaximum(360.0)
        self.observation.setObjectName(_fromUtf8("observation"))
        self.gridLayout.addWidget(self.observation, 1, 4, 1, 1)

        self.retranslateUi(PlaceOrientation)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PlaceOrientation.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PlaceOrientation.reject)
        QtCore.QMetaObject.connectSlotsByName(PlaceOrientation)

    def retranslateUi(self, PlaceOrientation):
        PlaceOrientation.setWindowTitle(_translate("PlaceOrientation", "Place orientation", None))
        self.label_4.setText(_translate("PlaceOrientation", "Precision of prolongation [°]", None))
        self.label_8.setText(_translate("PlaceOrientation", "Length of drawn line", None))
        self.label.setText(_translate("PlaceOrientation", "Angle [°]", None))

