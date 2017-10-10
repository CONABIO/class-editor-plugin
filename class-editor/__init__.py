# --------------------------------------------------------
#    __init__ - MADMEX Class Editor
# --------------------------------------------------------

from classeditor_menu import classeditor_menu

def name():
	return "madmex_classeditor"

def description():
	return "Edit and assing same column value in the attribute table for the selected elements"

def version():
	return "2.0"

def qgisMinimumVersion():
	return "2.0"

def authorName():
	return "Steffen Gebhardt"

def icon():
    return "icons/pmn_logo.png"
	
def classFactory(iface):
	return classeditor_menu(iface)
