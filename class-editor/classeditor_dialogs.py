# --------------------------------------------------------
#    classeditor_dialogs - Dialog classes for classeditor
#
# --------------------------------------------------------

# import os.path
import operator
import tempfile
import datetime

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from classeditor_library import *


from os import path, access, R_OK

import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")


TEMPFILE = '/classeditor_tmp'


# --------------------------------------------------------
#    classeditor_update_selected - Update selected feature field
# --------------------------------------------------------

from classeditor_form import *

def get_class_dic():
    
    level_1 = ['TIERRAS FORESTALES', 'PRADERAS', 'HUMEDAL', 'TIERRAS DE USO AGRICOLA', 'CUERPO DE AGUA', 'ASENTAMIENTOS', 'OTROS', 'INDEFINIDO']
    level_2 = {
               'TIERRAS FORESTALES':['BOSQUE DE CONIFERAS',
                                     'BOSQUE DE ENCINO',
                                     'BOSQUE MEZCLADO',
                                     'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO',
                                     'SELVAS SECAS',
                                     'MATORRAL XEROFILO SUBARBOREO',
                                     'MATORRAL XEROFILO ARBUSTIVO'],
               'PRADERAS':['PASTIZALES'],
               'HUMEDAL':['VEGETACION HIDROFILA'],
               'TIERRAS DE USO AGRICOLA':['AGRICULTURA'],
               'CUERPO DE AGUA':['CUERPO DE AGUA'],
               'ASENTAMIENTOS':['URBANO Y CONSTRUIDO'],
               'OTROS':['SUELO DESNUDO', 'NIEVE Y HIELO'],
               'INDEFINIDO':['INDEFINIDO']
               }
    level_3 = {
                'BOSQUE DE CONIFERAS':['BOSQUE DE AYARIN', 'BOSQUE DE CEDRO', 'BOSQUE DE OYAMEL', 'BOSQUE DE PINO', 'BOSQUE DE TASCATE'],
                'BOSQUE DE ENCINO':['BOSQUE DE ENCINO'],
                'BOSQUE MEZCLADO':['BOSQUE DE ENCINO-PINO', 'BOSQUE DE PINO-ENCINO', 'BOSQUE CULTIVADO', 'BOSQUE INDUCIDO'],
                'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO':['BOSQUE MESOFILO DE MONTANA', 'SELVA ALTA PERENNIFOLIA', 'SELVA BAJA PERENNIFOLIA', 'SELVA MEDIANA PERENNIFOLIA', 'PALMAR NATURAL', 'PETEN', 'SELVA DE GALERIA', 'SELVA ALTA SUBPERENNIFOLIA', 'SELVA MEDIANA SUBPERENNIFOLIA', 'SELVA BAJA ESPINOSA SUBPERENNIFOLIA', 'BOSQUE DE GALERIA', 'PALMAR', 'PALMAR INDUCIDO', 'VEGETACION DE PETEN', 'MANGLAR'],
                'SELVAS SECAS':['SELVA BAJA CADUCIFOLIA', 'SELVA MEDIANA CADUCIFOLIA', 'SELVA BAJA ESPINOSA CADUCIFOLIA', 'SELVA BAJA SUBCADUCIFOLIA', 'SELVA BAJA ESPINOSA', 'SELVA MEDIANA SUBCADUCIFOLIA'],
                'MATORRAL XEROFILO SUBARBOREO':['MATORRAL SUBTROPICAL', 'MATORRAL SUBMONTANO', 'MATORRAL ESPINOSO TAMAULIPECO', 'MATORRAL CRASICAULE', 'CHAPARRAL', 'MEZQUITAL DESERTICO', 'MEZQUITAL', 'MEZQUITAL TROPICAL', 'BOSQUE DE MEZQUITE', 'MATORRAL DE CONIFERAS'],
                'MATORRAL XEROFILO ARBUSTIVO':['MATORRAL DESERTICO MICROFILO', 'MATORRAL DESERTICO ROSETOFILO', 'MATORRAL ROSETOFILO COSTERO', 'MATORRAL SARCO-CRASICAULE', 'MATORRAL SARCO-CRASICAULE DE NEBLINA', 'MATORRAL SARCOCAULE', 'VEGETACION DE DESIERTOS ARENOSOS', 'VEGETACION GIPSOFILA', 'VEGETACION HALOFILA XEROFILA', 'VEGETACION HALOFILA', 'VEGETACION DE GALERIA'],
                'PASTIZALES':['PASTIZAL GIPSOFILO', 'PASTIZAL HALOFILO', 'PASTIZAL NATURAL', 'PRADERA DE ALTA MONTANA', 'SABANA', 'DUNAS COSTERAS', 'PASTIZAL INDUCIDO', 'VEGETACION DE DUNAS COSTERAS', 'SABANOIDE', 'PASTIZAL CULTIVADO'],
                'VEGETACION HIDROFILA':['POPAL', 'TULAR', 'VEGETACION HALOFILA HIDROFILA'],
                'AGRICULTURA':['AGRICULTURA DE HUMEDAD', 'AGRICULTURA DE RIEGO', 'AGRICULTURA DE TEMPORAL'],
                'CUERPO DE AGUA':['ACUICOLA', 'AGUA'],
                'URBANO Y CONSTRUIDO':['ASENTAMIENTOS HUMANOS', 'ZONA URBANA'],
                'SUELO DESNUDO':['SIN VEGETACION APARENTE', 'DESPROVISTO DE VEGETACION'],
                'NIEVE Y HIELO':['NIEVE', 'HIELO'],
                'INDEFINIDO':['INDEFINIDO']
               }
    level_4 = {
                'BOSQUE DE CONIFERAS':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'BOSQUE DE ENCINO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'BOSQUE MEZCLADO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'SELVAS HUMEDAS Y SUBHUMEDAS Y BOSQUE MESOFILO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'SELVAS SECAS':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'MATORRAL XEROFILO SUBARBOREO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'MATORRAL XEROFILO ARBUSTIVO':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'PASTIZALES':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'VEGETACION HIDROFILA':['ARBUSTIVO', 'ARBOREO', 'HERBACEO', 'NO APLICABLE', 'QUEMADO'],
                'AGRICULTURA':['NO APLICABLE', 'QUEMADO'],
                'CUERPO DE AGUA':['NO APLICABLE'],
                'URBANO Y CONSTRUIDO':['NO APLICABLE'],
                'SUELO DESNUDO':['NO APLICABLE', 'QUEMADO'],
                'NIEVE Y HIELO':['NO APLICABLE'],
                'INDEFINIDO':['INDEFINIDO', 'SOMBRA', 'NUBE', 'QUEMADO']
               }    
    
  
    return [level_1, level_2, level_3, level_4]

class classeditor_update_selected_dialog(QDialog, Ui_classeditor_form):
    
    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.run)
        layer = self.iface.mapCanvas().currentLayer()
        delimchars = "#"

        [self.level_1, self.level_2, self.level_3, self.level_4] = get_class_dic()
        
        self.classlevel1_comboBox.activated[str].connect(self.on_combo1_activated)
        self.classlevel2_comboBox.activated[str].connect(self.on_combo2_activated)
        # self.classlevel3_comboBox.activated[str].connect(self.on_combo3_activated)
        self.classlevel1_comboBox.addItems(self.level_1)

        if (layer):

            if layer.type() == QgsMapLayer.VectorLayer:
                haseditorfield = False
                provider = layer.dataProvider()
                
                fields = layer.pendingFields()   
                field_names = [field.name() for field in fields]       
                self.classlevel1_fields_comboBox.clear()
                for name in field_names:
                    name = str(name)
                    #QMessageBox.information(self.iface.mainWindow(), "Hasfield", "Has field %s" % (str(name)))
                    if name == 'editor':
                        #QMessageBox.information(self.iface.mainWindow(), "Hasfield", "Has field %s" % (str(name)))
                    	haseditorfield = True
               
                    self.classlevel1_fields_comboBox.addItem(name)
                    self.classlevel2_fields_comboBox.addItem(name)
                    self.classlevel3_fields_comboBox.addItem(name)
                    self.classlevel4_fields_comboBox.addItem(name)
                    if '1' in name and 'level' in str.lower(name):
                        self.classlevel1_fields_comboBox.setCurrentIndex(self.classlevel1_fields_comboBox.findText(name))
                    elif '2' in name and 'level' in str.lower(name):
                        self.classlevel2_fields_comboBox.setCurrentIndex(self.classlevel2_fields_comboBox.findText(name))
                    elif '3' in name and 'level' in str.lower(name):
                        self.classlevel3_fields_comboBox.setCurrentIndex(self.classlevel3_fields_comboBox.findText(name))
                    elif '4' in name and 'level' in str.lower(name):
                        self.classlevel4_fields_comboBox.setCurrentIndex(self.classlevel4_fields_comboBox.findText(name))
		
		
		
                if haseditorfield == False:
                    #QMessageBox.information(self.iface.mainWindow(), "Hasfiels", "Has field %s" % (str("Ich mach das jettzt")))
                    layer.startEditing()
                    res = layer.dataProvider().addAttributes([ QgsField("editor", QVariant.String) ])
                    layer.commitChanges()
        		    
        		    
                if os.path.exists(tempfile.gettempdir() + TEMPFILE):
                    in_file = open(tempfile.gettempdir() + TEMPFILE, 'r')
                    file_cont = in_file.read()
                    in_file.close()
                    file_cont_splitted = file_cont.split(",")
                    lastlayer = file_cont_splitted[0]
                    lastfield1 = file_cont_splitted[1]
                    lastfield2 = file_cont_splitted[2]
                    lastfield3 = file_cont_splitted[3]
                    lastfield4 = file_cont_splitted[4]
                    lastvalue1 = file_cont_splitted[5]
                    lastvalue2 = file_cont_splitted[6]
                    lastvalue3 = file_cont_splitted[7]
                    lastvalue4 = file_cont_splitted[8]
                    editor = file_cont_splitted[9]
                    self.classlevel1_fields_comboBox.setCurrentIndex(self.classlevel1_fields_comboBox.findText(lastfield1))
                    self.classlevel2_fields_comboBox.setCurrentIndex(self.classlevel2_fields_comboBox.findText(lastfield2))
                    self.classlevel3_fields_comboBox.setCurrentIndex(self.classlevel3_fields_comboBox.findText(lastfield3))
                    self.classlevel4_fields_comboBox.setCurrentIndex(self.classlevel4_fields_comboBox.findText(lastfield4))
                    self.classlevel1_comboBox.setCurrentIndex(self.classlevel1_comboBox.findText(lastvalue1))
                    self.classlevel2_comboBox.addItems(self.level_2[str(self.classlevel1_comboBox.currentText())])
                    self.classlevel2_comboBox.setCurrentIndex(self.classlevel2_comboBox.findText(lastvalue2))
                    self.classlevel3_comboBox.addItems(self.level_3[str(self.classlevel2_comboBox.currentText())])
                    self.classlevel4_comboBox.addItems(self.level_4[str(self.classlevel2_comboBox.currentText())])
                    self.classlevel3_comboBox.setCurrentIndex(self.classlevel3_comboBox.findText(lastvalue3))
                    self.classlevel4_comboBox.setCurrentIndex(self.classlevel4_comboBox.findText(lastvalue4))
                    self.editor_lineEdit.setText(editor)
                     
                            
                            
                #for (f_index, f) in fields.iteritems():
                    # self.classlevel1_fields_comboBox.addItem(f.name(), QVariant(f_index) )
                nF = layer.selectedFeatureCount()
                if (nF > 0):		
                    self.label.setText("<font color='green'>For <b>" + str(nF) + "</b> selected elements in <b>" + layer.name() + "</b> set value of field</font>")
                    self.classlevel1_fields_comboBox.setFocus(True)
                    rm_if_too_old_settings_file(tempfile.gettempdir() + TEMPFILE)
    
                elif (nF == 0):
                    infoString = "<font color='magenta'> Please select some elements into current <b>" + layer.name() + "</b> layer</font>"
                    self.label.setText(infoString)
                    toggle_options(self, False)

            else:
                infoString = "<font color='red'> <b>No vector layer selected... Select a vector layer from the layer list...</b></font>"
                self.label.setText(infoString)
                toggle_options(self, False)

        else:
            infoString = "<font color='red'> <b>No layer selected... Select a layer from the layer list...</b></font>"
            self.label.setText(infoString)
            

    def on_combo1_activated(self, text):
        self.classlevel2_comboBox.clear()
        self.classlevel3_comboBox.clear()
        self.classlevel4_comboBox.clear()
        self.classlevel2_comboBox.addItems(self.level_2[str(self.classlevel1_comboBox.currentText())])
        self.classlevel3_comboBox.addItems(self.level_3[str(self.classlevel2_comboBox.currentText())])
        self.classlevel4_comboBox.addItems(self.level_4[str(self.classlevel2_comboBox.currentText())]) 
        
    def on_combo2_activated(self, text):
        self.classlevel3_comboBox.clear()
        self.classlevel4_comboBox.clear()
        self.classlevel3_comboBox.addItems(self.level_3[str(self.classlevel2_comboBox.currentText())])
        self.classlevel4_comboBox.addItems(self.level_4[str(self.classlevel2_comboBox.currentText())])
    
    def toggle_options(self, enable):
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)
        self.classlevel1_comboBox.setEnabled(enable)
        self.classlevel2_comboBox.setEnabled(enable)
        self.classlevel3_comboBox.setEnabled(enable)
        self.classlevel4_comboBox.setEnabled(enable)
                

    def run(self):
        delimchars = "#"
        layer = self.iface.mapCanvas().currentLayer()
        if (layer == None):
            infoString = "<font color='red'> <b>No layer selected... Select a layer from the layer list...</b></font>"
        

        classvalue_1 = self.classlevel1_comboBox.currentText()
        classvalue_2 = self.classlevel2_comboBox.currentText()
        classvalue_3 = self.classlevel3_comboBox.currentText()
        classvalue_4 = self.classlevel4_comboBox.currentText()
        editorvalue = self.editor_lineEdit.text()
        
        out_file = open(tempfile.gettempdir() + TEMPFILE, 'w')
        
        out_file.write(layer.name() + "," + 
                        self.classlevel1_fields_comboBox.currentText() + "," + 
                        self.classlevel2_fields_comboBox.currentText() + "," + 
                        self.classlevel3_fields_comboBox.currentText() + "," + 
                        self.classlevel4_fields_comboBox.currentText() + "," + 
                        classvalue_1 + "," + 
                        classvalue_2 + "," + 
                        classvalue_3 + "," + 
                        classvalue_4 + "," + 
                        editorvalue)
        out_file.close()
        
        layer = self.iface.mapCanvas().currentLayer()
        if(layer):        
            nF = layer.selectedFeatureCount()
            if (nF > 0):        
                if not layer.isEditable():
                    layer.startEditing()     
                oFea = layer.selectedFeaturesIds()
                nPosField_1 = self.classlevel1_fields_comboBox.currentIndex()
                nPosField_2 = self.classlevel2_fields_comboBox.currentIndex()
                nPosField_3 = self.classlevel3_fields_comboBox.currentIndex()
                nPosField_4 = self.classlevel4_fields_comboBox.currentIndex()
                idx = layer.fieldNameIndex('editor')
                
                if (nF > 1): 
                    for i in oFea:
                        layer.changeAttributeValue(int(i), nPosField_1, classvalue_1) 
                        layer.changeAttributeValue(int(i), nPosField_2, classvalue_2) 
                        layer.changeAttributeValue(int(i), nPosField_3, classvalue_3) 
                        layer.changeAttributeValue(int(i), nPosField_4, classvalue_4)
                        layer.changeAttributeValue(int(i), idx, editorvalue)
                        
                else:  # only one feature selecteds
                    layer.changeAttributeValue(int(oFea[0]), nPosField_1, classvalue_1)
                    layer.changeAttributeValue(int(oFea[0]), nPosField_2, classvalue_2)
                    layer.changeAttributeValue(int(oFea[0]), nPosField_3, classvalue_3)
                    layer.changeAttributeValue(int(oFea[0]), nPosField_4, classvalue_4)
                    layer.changeAttributeValue(int(oFea[0]), idx, editorvalue)
                    
                QMessageBox.information(self.iface.mainWindow(), "Updating", "Updating %s objects" % (str(nF)))
                layer.commitChanges()  


def bool2str(bVar):
    if bVar:
        return 'True'
    else:
        return 'False'

def str2bool(bVar):
    if (bVar == 'True'):
        return True
    else:
        return False

def rm_if_too_old_settings_file(myPath_and_File):
    if os.path.exists(myPath_and_File) and os.path.isfile(myPath_and_File) and os.access(myPath_and_File, R_OK):
        now = time.time()
        tmpfileSectime = os.stat(myPath_and_File)[7]  # get last modified time,[8] would be last creation time
        if(now - tmpfileSectime > 60 * 60 * 12):  # if settings file is older than 6 hour
            os.remove(myPath_and_File)




