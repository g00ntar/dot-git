"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *
from collections import OrderedDict

@qgsfunction(args='auto', group='String Advanced')
def splitString(string, delimiter, occurence, feature, parent):
	return string.split(delimiter)[occurence]

@qgsfunction(args='auto', group='String Advanced')
def removeDuplicatesFromString(s, feature, parent):
    return  ' '.join(OrderedDict((w,w) for w in s.split()).keys())
