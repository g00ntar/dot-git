# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DatabaseWmsDialog
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

import os
import urllib
import urlparse
import json
import re
from PyQt4 import uic
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QDialog, QHeaderView, QTableWidgetItem, QAbstractItemView
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer
from qgis.gui import QgsMessageBar

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wms_module.ui'))


class WmsModule(QDialog, FORM_CLASS):
    def __init__(self, parent, parents=None):
        super(WmsModule, self).__init__(parents)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.keyLineEdit.setText(QSettings().value('gissupport/api/key'))
        self.saveKeyButton.clicked.connect(self.saveKey)
        self.api_url = 'http://api.gis-support.pl/'
        self.layersTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.layersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sourceList.currentIndexChanged.connect(self.updateWmsList)
        self.wmsList.currentIndexChanged.connect(self.getLayers)
        self.layersTable.itemSelectionChanged.connect(self.updateButton)
        self.addButton.clicked.connect(self.addWmsToMap)
        self.sourceList.setFocus()
        self.currentLayers = {}
        self.currentData = self.getWmsData()

    def addWmsToMap(self):
        selected = [i.row() for i in
                    self.layersTable.selectionModel().selectedRows()]
        layer_names = [v['name'].encode('utf-8') for i, v in
                       enumerate(self.currentLayers['wms_layers']) if i in selected]
        layers = 'layers='.join([i+'&' for i in layer_names])
        styles = 'styles=&' * len(layer_names)
        wms = [i for i in self.selectedSource['list'] if i['name'] == self.wmsList.currentText()][0]
        wms_url = urlparse.urlparse(wms['url'])
        extra_params = urlparse.parse_qs(wms_url.query)
        url = ''
        if extra_params:
            for k, v in extra_params.iteritems():
                url += k + '=' + v[0] + '&'
        url += ("contextualWMSLegend=0&"
                "crs=EPSG:2180&"
                "dpiMode=7&"
                "featureCount=10&"
                "format=image/png&"
                "layers={}"
                "{}"
                "url={}".format(layers, styles, wms_url.scheme + "://" + wms_url.netloc + wms_url.path))
        layer = QgsRasterLayer(url, self.generateLayerName(wms['name']), 'wms')
        QgsMapLayerRegistry.instance().addMapLayer(layer)

    def getWmsData(self):
        source_list = []
        key = self.keyLineEdit.text().strip()
        if key:
            try:
                r = urllib.urlopen(self.api_url+'wms_list?key={}'.format(key))
            except:
                return []
            if r.getcode() == 403:
                self.iface.messageBar().pushMessage(
                    'Baza WMS',
                    u'Niepoprawny klucz GIS Support',
                    level=QgsMessageBar.WARNING)
                return []
            elif r.getcode() != 200:
                return []
        else:
            return []
        return json.loads(r.read())['wms_list']

    def getLayers(self):
        if self.wmsList.currentText():
            wms = [i for i in self.selectedSource['list'] if i['name'] == self.wmsList.currentText()][0]
            self.wmsDescription.setText(wms['description'])
            wms_id = wms['id']
            key = self.keyLineEdit.text().strip()
            try:
                r = urllib.urlopen(self.api_url+'wms_layers?key={}&id={}'.format(key, wms_id))
            except:
                self.iface.messageBar().pushMessage(
                    'Baza WMS',
                    u'Problem połączenia z WMS',
                    level=QgsMessageBar.WARNING)
                return
            if r.getcode() == 403:
                self.iface.messageBar().pushMessage(
                    'Baza WMS',
                    u'Niepoprawny klucz GIS Support',
                    level=QgsMessageBar.WARNING)
                return
            elif r.getcode() != 200:
                self.iface.messageBar().pushMessage(
                    'Baza WMS',
                    u'Problem połączenia z WMS',
                    level=QgsMessageBar.WARNING)
                return
            self.currentLayers = json.loads(r.read())
            self.updateLayerList()

    def updateSourceList(self):
        self.sourceList.clear()
        self.sourceList.addItems([i['name'] for i in self.currentData])

    def updateWmsList(self):
        self.wmsList.clear()
        self.selectedSource = [i for i in self.currentData if i['name'] == self.sourceList.currentText()][0]
        self.sourceDescription.setText(self.selectedSource['description'])
        items = sorted([i['name'] for i in self.selectedSource['list']])
        self.wmsList.blockSignals(True)
        self.wmsList.addItems(items)
        self.wmsList.setCurrentIndex(-1)
        self.wmsList.blockSignals(False)

    def updateLayerList(self):
        self.layersTable.clearSelection()
        self.layersTable.setRowCount(len(self.currentLayers['wms_layers']))
        for i, row in enumerate(self.currentLayers['wms_layers']):
            self.layersTable.setItem(i, 0, QTableWidgetItem(row['title']))
            self.layersTable.setItem(i, 1, QTableWidgetItem(row['abstract']))

    def updateButton(self):
        if self.layersTable.selectionModel().selectedRows():
            self.addButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)

    def saveKey(self):
        QSettings().setValue('gissupport/api/key',
                             self.keyLineEdit.text())
        self.getData()

    def generateLayerName(self, wms_name):
        if not QgsMapLayerRegistry.instance().mapLayersByName(wms_name):
            return wms_name
        iterator = re.findall(r"_\((\d)\)", wms_name)
        if iterator:
            wms_name = re.sub(r"_\((\d)\)", "_({})".format(str(int(iterator[0])+1)), wms_name)
            return self.generateLayerName(wms_name)
        return self.generateLayerName(wms_name + '_(1)')

    def getData(self):
        if self.keyLineEdit.text():
            if not self.currentData:
                self.currentData = self.getWmsData()
                if not self.currentData:
                    self.iface.messageBar().pushMessage(
                        'Baza WMS',
                        u'Błąd serwera lub brak połączenia z internetem',
                        level=QgsMessageBar.WARNING)
                    return
            if not self.sourceList:
                self.updateSourceList()

    def openDialog(self):
        self.getData()
        super(WmsModule, self).show()