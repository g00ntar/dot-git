# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_intersection.ui'
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

class Ui_Intersection(object):
    def setupUi(self, Intersection):
        Intersection.setObjectName(_fromUtf8("Intersection"))
        Intersection.resize(616, 456)
        self.gridLayout_3 = QtGui.QGridLayout(Intersection)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter = QtGui.QSplitter(Intersection)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.advancedIntersecLSconvergeThreshold = QtGui.QDoubleSpinBox(self.widget)
        self.advancedIntersecLSconvergeThreshold.setDecimals(4)
        self.advancedIntersecLSconvergeThreshold.setProperty("value", 0.0005)
        self.advancedIntersecLSconvergeThreshold.setObjectName(_fromUtf8("advancedIntersecLSconvergeThreshold"))
        self.gridLayout.addWidget(self.advancedIntersecLSconvergeThreshold, 1, 1, 1, 1)
        self.observationTableWidget = ObservationTable(self.widget)
        self.observationTableWidget.setColumnCount(3)
        self.observationTableWidget.setObjectName(_fromUtf8("observationTableWidget"))
        self.observationTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.observationTableWidget, 2, 0, 1, 4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.advancedIntersecLSmaxIteration = QtGui.QSpinBox(self.widget)
        self.advancedIntersecLSmaxIteration.setProperty("value", 15)
        self.advancedIntersecLSmaxIteration.setObjectName(_fromUtf8("advancedIntersecLSmaxIteration"))
        self.gridLayout.addWidget(self.advancedIntersecLSmaxIteration, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.processButton = QtGui.QPushButton(self.widget)
        self.processButton.setCheckable(False)
        self.processButton.setObjectName(_fromUtf8("processButton"))
        self.gridLayout.addWidget(self.processButton, 3, 2, 1, 2)
        self.widget_2 = QtGui.QWidget(self.splitter)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.okButton = QtGui.QPushButton(self.widget_2)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.gridLayout_2.addWidget(self.okButton, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.reportBrowser = QtGui.QTextBrowser(self.widget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.reportBrowser.setFont(font)
        self.reportBrowser.setObjectName(_fromUtf8("reportBrowser"))
        self.gridLayout_2.addWidget(self.reportBrowser, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Intersection)
        QtCore.QMetaObject.connectSlotsByName(Intersection)

    def retranslateUi(self, Intersection):
        Intersection.setWindowTitle(_translate("Intersection", "Intersect It :: Least Squares report", None))
        self.label_3.setText(_translate("Intersection", "Convergence", None))
        self.label_2.setText(_translate("Intersection", "Max iteration", None))
        self.label_4.setText(_translate("Intersection", "mm", None))
        self.processButton.setText(_translate("Intersection", "process", None))
        self.okButton.setText(_translate("Intersection", "Use this solution", None))

from ..gui.observation_table import ObservationTable
