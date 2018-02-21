# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gml_loader_dialog_base.ui'
#
# Created: Tue Nov 17 21:11:26 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_GmlLoaderDialogBase(object):
    def setupUi(self, GmlLoaderDialogBase):
        GmlLoaderDialogBase.setObjectName(_fromUtf8("GmlLoaderDialogBase"))
        GmlLoaderDialogBase.resize(596, 188)
        self.cmdSelectGml = QtGui.QPushButton(GmlLoaderDialogBase)
        self.cmdSelectGml.setGeometry(QtCore.QRect(490, 150, 87, 27))
        self.cmdSelectGml.setObjectName(_fromUtf8("cmdSelectGml"))
        self.frmGml = QtGui.QFrame(GmlLoaderDialogBase)
        self.frmGml.setGeometry(QtCore.QRect(10, 10, 571, 131))
        self.frmGml.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGml.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGml.setObjectName(_fromUtf8("frmGml"))
        self.chkAttributesToFields = QtGui.QCheckBox(self.frmGml)
        self.chkAttributesToFields.setGeometry(QtCore.QRect(270, 70, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkAttributesToFields.setFont(font)
        self.chkAttributesToFields.setText(_fromUtf8(""))
        self.chkAttributesToFields.setChecked(True)
        self.chkAttributesToFields.setObjectName(_fromUtf8("chkAttributesToFields"))
        self.lblAttributesToFields = QtGui.QLabel(self.frmGml)
        self.lblAttributesToFields.setGeometry(QtCore.QRect(20, 70, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblAttributesToFields.setFont(font)
        self.lblAttributesToFields.setObjectName(_fromUtf8("lblAttributesToFields"))
        self.lblResolveXlinkHref = QtGui.QLabel(self.frmGml)
        self.lblResolveXlinkHref.setGeometry(QtCore.QRect(20, 40, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblResolveXlinkHref.setFont(font)
        self.lblResolveXlinkHref.setObjectName(_fromUtf8("lblResolveXlinkHref"))
        self.chkResolveXlinkHref = QtGui.QCheckBox(self.frmGml)
        self.chkResolveXlinkHref.setGeometry(QtCore.QRect(270, 40, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chkResolveXlinkHref.setFont(font)
        self.chkResolveXlinkHref.setText(_fromUtf8(""))
        self.chkResolveXlinkHref.setChecked(True)
        self.chkResolveXlinkHref.setObjectName(_fromUtf8("chkResolveXlinkHref"))
        self.lblGmlHeader = QtGui.QLabel(self.frmGml)
        self.lblGmlHeader.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblGmlHeader.setFont(font)
        self.lblGmlHeader.setObjectName(_fromUtf8("lblGmlHeader"))
        self.cmdSelectGfs = QtGui.QPushButton(self.frmGml)
        self.cmdSelectGfs.setGeometry(QtCore.QRect(20, 90, 87, 27))
        self.cmdSelectGfs.setObjectName(_fromUtf8("cmdSelectGfs"))
        self.lblGfs = QtGui.QLabel(self.frmGml)
        self.lblGfs.setGeometry(QtCore.QRect(120, 100, 431, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblGfs.setFont(font)
        self.lblGfs.setText(_fromUtf8(""))
        self.lblGfs.setObjectName(_fromUtf8("lblGfs"))

        self.retranslateUi(GmlLoaderDialogBase)
        QtCore.QMetaObject.connectSlotsByName(GmlLoaderDialogBase)

    def retranslateUi(self, GmlLoaderDialogBase):
        GmlLoaderDialogBase.setWindowTitle(_translate("GmlLoaderDialogBase", "GML Loader", None))
        self.cmdSelectGml.setText(_translate("GmlLoaderDialogBase", "Load .gml", None))
        self.lblAttributesToFields.setText(_translate("GmlLoaderDialogBase", "Convert attributes to fields", None))
        self.lblResolveXlinkHref.setText(_translate("GmlLoaderDialogBase", "Resolve elements (xlink:href)", None))
        self.lblGmlHeader.setText(_translate("GmlLoaderDialogBase", "GML-Reader (OGR/GDAL)", None))
        self.cmdSelectGfs.setText(_translate("GmlLoaderDialogBase", "Select .gfs", None))

