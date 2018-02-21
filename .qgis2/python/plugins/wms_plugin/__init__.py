# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DatabaseWms
                                 A QGIS plugin
 Baza WMS
                             -------------------
        begin                : 2017-02-22
        copyright            : (C) 2017 by Sebastian Schulz / GIS Support
        email                : ss@gis-support.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    from .database_wms import DatabaseWms
    return DatabaseWms(iface)
