# -*- coding: utf-8 -*-

#******************************************************************************
#
# QConsolidate
# ---------------------------------------------------------
# Consolidates all layers from current QGIS project into one directory and
# creates copy of current project using this consolidated layers.
#
# Copyright (C) 2012-2013 Alexander Bruy (alexander.bruy@gmail.com)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
#******************************************************************************


import os
import ConfigParser

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.ui_aboutdialogbase import Ui_Dialog

import resources_rc


class AboutDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.btnHelp = self.buttonBox.button(QDialogButtonBox.Help)

        self.lblLogo.setPixmap(QPixmap(":/icons/qconsolidate.png"))

        cfg = ConfigParser.SafeConfigParser()
        cfg.read(os.path.join(os.path.dirname(__file__), "metadata.txt"))
        version = cfg.get("general", "version")

        self.lblVersion.setText(self.tr("Version: %s") % (version))
        doc = QTextDocument()
        doc.setHtml(self.getAboutText())
        self.textBrowser.setDocument(doc)
        self.textBrowser.setOpenExternalLinks(True)

        self.buttonBox.helpRequested.connect(self.openHelp)

    def reject(self):
        QDialog.reject(self)

    def openHelp(self):
        overrideLocale = bool(QSettings().value("locale/overrideFlag", False))
        if not overrideLocale:
            localeFullName = QLocale.system().name()
        else:
            localeFullName = QSettings().value("locale/userLocale", "")

        localeShortName = localeFullName[0:2]
        if localeShortName in ["ru", "uk"]:
            QDesktopServices.openUrl(QUrl("http://hub.qgis.org/projects/qconsolidate/wiki"))
        else:
            QDesktopServices.openUrl(QUrl("http://hub.qgis.org/projects/qconsolidate/wiki"))

    def getAboutText(self):
        return self.tr("""<p>Consolidates all layers from current QGIS project into one directory.</p>
    <p><strong>Developers</strong>: Alexander Bruy</p>
    <p><strong>Homepage</strong>: <a href="http://hub.qgis.org/projects/qconsolidate">http://hub.qgis.org/projects/qconsolidate</a></p>
    <p>Please report bugs at <a href="http://hub.qgis.org/projects/qconsolidate/issues">bugtracker</a>.</p>
    """)
