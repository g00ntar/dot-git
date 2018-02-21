# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DatabaseWms
                                 A QGIS plugin
 Baza WMS
                              -------------------
        begin                : 2017-02-22
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Sebastian Schulz / GIS Support
        email                : ss@gis-support.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
import resources
from wms_module import WmsModule
import os.path


class DatabaseWms:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'DatabaseWms_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        self.wmsModule = WmsModule(self)
        self.actions = []
        self.menu = self.tr(u'&Baza WMS')
        self.toolbar = self.iface.addToolBar(u'DatabaseWms')
        self.toolbar.setObjectName(u'DatabaseWms')

    def tr(self, message):
        return QCoreApplication.translate('DatabaseWms', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if add_to_toolbar:
            self.toolbar.addAction(action)
        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)
        self.actions.append(action)
        return action

    def initGui(self):
        icon_path = ':/plugins/DatabaseWms/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Baza WMS'),
            callback=self.wmsModule.openDialog,
            parent=self.iface.mainWindow())


    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Baza WMS'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar
