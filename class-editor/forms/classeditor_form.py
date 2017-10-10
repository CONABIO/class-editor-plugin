# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sgebhardt\.qgis\python\plugins\conabio_classeditor\forms\classeditor_form.ui'
#
# Created: Wed Dec 18 13:23:24 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_classeditor_form(object):
    def setupUi(self, classeditor_form):
        classeditor_form.setObjectName(_fromUtf8("classeditor_form"))
        classeditor_form.resize(570, 297)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/pmn_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        classeditor_form.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(classeditor_form)
        self.buttonBox.setGeometry(QtCore.QRect(390, 230, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.classlevel1_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel1_comboBox.setGeometry(QtCore.QRect(290, 70, 261, 22))
        self.classlevel1_comboBox.setObjectName(_fromUtf8("classlevel1_comboBox"))
        self.classlevel2_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel2_comboBox.setGeometry(QtCore.QRect(290, 110, 261, 22))
        self.classlevel2_comboBox.setObjectName(_fromUtf8("classlevel2_comboBox"))
        self.classlevel3_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel3_comboBox.setGeometry(QtCore.QRect(290, 150, 261, 22))
        self.classlevel3_comboBox.setObjectName(_fromUtf8("classlevel3_comboBox"))
        self.classlevel4_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel4_comboBox.setGeometry(QtCore.QRect(290, 190, 261, 22))
        self.classlevel4_comboBox.setObjectName(_fromUtf8("classlevel4_comboBox"))
        self.classlevel1_label = QtGui.QLabel(classeditor_form)
        self.classlevel1_label.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.classlevel1_label.setObjectName(_fromUtf8("classlevel1_label"))
        self.classlevel2_label = QtGui.QLabel(classeditor_form)
        self.classlevel2_label.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.classlevel2_label.setObjectName(_fromUtf8("classlevel2_label"))
        self.classlevel3_label = QtGui.QLabel(classeditor_form)
        self.classlevel3_label.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.classlevel3_label.setObjectName(_fromUtf8("classlevel3_label"))
        self.classlevel4_label = QtGui.QLabel(classeditor_form)
        self.classlevel4_label.setGeometry(QtCore.QRect(20, 190, 71, 21))
        self.classlevel4_label.setObjectName(_fromUtf8("classlevel4_label"))
        self.label = QtGui.QLabel(classeditor_form)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(classeditor_form)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 251, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.classlevel3_fields_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel3_fields_comboBox.setGeometry(QtCore.QRect(100, 150, 171, 22))
        self.classlevel3_fields_comboBox.setObjectName(_fromUtf8("classlevel3_fields_comboBox"))
        self.classlevel1_fields_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel1_fields_comboBox.setGeometry(QtCore.QRect(100, 70, 171, 22))
        self.classlevel1_fields_comboBox.setObjectName(_fromUtf8("classlevel1_fields_comboBox"))
        self.classlevel2_fields_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel2_fields_comboBox.setGeometry(QtCore.QRect(100, 110, 171, 22))
        self.classlevel2_fields_comboBox.setObjectName(_fromUtf8("classlevel2_fields_comboBox"))
        self.classlevel4_fields_comboBox = QtGui.QComboBox(classeditor_form)
        self.classlevel4_fields_comboBox.setGeometry(QtCore.QRect(100, 190, 171, 22))
        self.classlevel4_fields_comboBox.setObjectName(_fromUtf8("classlevel4_fields_comboBox"))
        self.label_2 = QtGui.QLabel(classeditor_form)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(classeditor_form)
        self.label_4.setGeometry(QtCore.QRect(300, 40, 141, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.editor_lineEdit = QtGui.QLineEdit(classeditor_form)
        self.editor_lineEdit.setGeometry(QtCore.QRect(100, 230, 171, 20))
        self.editor_lineEdit.setObjectName(_fromUtf8("editor_lineEdit"))
        self.classlevel4_label_2 = QtGui.QLabel(classeditor_form)
        self.classlevel4_label_2.setGeometry(QtCore.QRect(20, 230, 71, 21))
        self.classlevel4_label_2.setObjectName(_fromUtf8("classlevel4_label_2"))

        self.retranslateUi(classeditor_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), classeditor_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), classeditor_form.reject)
        QtCore.QMetaObject.connectSlotsByName(classeditor_form)

    def retranslateUi(self, classeditor_form):
        classeditor_form.setWindowTitle(_translate("classeditor_form", "Class Editor Dialog", None))
        self.classlevel1_label.setText(_translate("classeditor_form", "Class Level 1", None))
        self.classlevel2_label.setText(_translate("classeditor_form", "Class Level 2", None))
        self.classlevel3_label.setText(_translate("classeditor_form", "Class Level 3", None))
        self.classlevel4_label.setText(_translate("classeditor_form", "Class Level 4", None))
        self.label.setText(_translate("classeditor_form", "For all selected elements set the value of field:", None))
        self.label_3.setText(_translate("classeditor_form", "You can also activate this form with F11 funct key", None))
        self.label_2.setText(_translate("classeditor_form", "Table column definition", None))
        self.label_4.setText(_translate("classeditor_form", "Object class definition", None))
        self.classlevel4_label_2.setText(_translate("classeditor_form", "Editor", None))

