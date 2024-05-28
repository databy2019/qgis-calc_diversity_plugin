# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CalcDiversity
                                 A QGIS plugin
 Calculates biodiversity indexes (Richness, Shannons, and Simpsons)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-05-28
        copyright            : (C) 2024 by Wawan Hendriawan Nur
        email                : wawanhn@gmail.com
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CalcDiversity class from file CalcDiversity.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .calc_diversity import CalcDiversity
    return CalcDiversity(iface)
