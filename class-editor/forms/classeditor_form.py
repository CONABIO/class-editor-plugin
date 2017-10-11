# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classeditor_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        classeditor_form.resize(543, 398)
        self.gridLayout_3 = QtGui.QGridLayout(classeditor_form)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(classeditor_form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.classlevel1_comboBox = QtGui.QComboBox(self.groupBox_2)
        self.classlevel1_comboBox.setObjectName(_fromUtf8("classlevel1_comboBox"))
        self.gridLayout_4.addWidget(self.classlevel1_comboBox, 0, 0, 1, 1)
        self.classlevel2_comboBox = QtGui.QComboBox(self.groupBox_2)
        self.classlevel2_comboBox.setObjectName(_fromUtf8("classlevel2_comboBox"))
        self.gridLayout_4.addWidget(self.classlevel2_comboBox, 1, 0, 1, 1)
        self.classlevel3_comboBox = QtGui.QComboBox(self.groupBox_2)
        self.classlevel3_comboBox.setObjectName(_fromUtf8("classlevel3_comboBox"))
        self.gridLayout_4.addWidget(self.classlevel3_comboBox, 2, 0, 1, 1)
        self.classlevel4_comboBox = QtGui.QComboBox(self.groupBox_2)
        self.classlevel4_comboBox.setObjectName(_fromUtf8("classlevel4_comboBox"))
        self.gridLayout_4.addWidget(self.classlevel4_comboBox, 3, 0, 1, 1)
        self.classlevel4_comboBox.raise_()
        self.classlevel3_comboBox.raise_()
        self.classlevel1_comboBox.raise_()
        self.classlevel2_comboBox.raise_()
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(classeditor_form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.classlevel4_label_2 = QtGui.QLabel(self.groupBox_3)
        self.classlevel4_label_2.setObjectName(_fromUtf8("classlevel4_label_2"))
        self.gridLayout_6.addWidget(self.classlevel4_label_2, 0, 0, 1, 1)
        self.editor_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.editor_lineEdit.setObjectName(_fromUtf8("editor_lineEdit"))
        self.gridLayout_6.addWidget(self.editor_lineEdit, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox_3)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_6.addWidget(self.buttonBox, 0, 2, 2, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 2)
        self.buttonBox.raise_()
        self.classlevel4_label_2.raise_()
        self.editor_lineEdit.raise_()
        self.label_3.raise_()
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(classeditor_form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_7.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.classlevel1_label = QtGui.QLabel(self.groupBox)
        self.classlevel1_label.setObjectName(_fromUtf8("classlevel1_label"))
        self.gridLayout_2.addWidget(self.classlevel1_label, 0, 0, 1, 1)
        self.classlevel1_fields_comboBox = QtGui.QComboBox(self.groupBox)
        self.classlevel1_fields_comboBox.setObjectName(_fromUtf8("classlevel1_fields_comboBox"))
        self.gridLayout_2.addWidget(self.classlevel1_fields_comboBox, 0, 1, 1, 1)
        self.classlevel2_label = QtGui.QLabel(self.groupBox)
        self.classlevel2_label.setObjectName(_fromUtf8("classlevel2_label"))
        self.gridLayout_2.addWidget(self.classlevel2_label, 1, 0, 1, 1)
        self.classlevel2_fields_comboBox = QtGui.QComboBox(self.groupBox)
        self.classlevel2_fields_comboBox.setObjectName(_fromUtf8("classlevel2_fields_comboBox"))
        self.gridLayout_2.addWidget(self.classlevel2_fields_comboBox, 1, 1, 1, 1)
        self.classlevel3_label = QtGui.QLabel(self.groupBox)
        self.classlevel3_label.setObjectName(_fromUtf8("classlevel3_label"))
        self.gridLayout_2.addWidget(self.classlevel3_label, 2, 0, 1, 1)
        self.classlevel3_fields_comboBox = QtGui.QComboBox(self.groupBox)
        self.classlevel3_fields_comboBox.setObjectName(_fromUtf8("classlevel3_fields_comboBox"))
        self.gridLayout_2.addWidget(self.classlevel3_fields_comboBox, 2, 1, 1, 1)
        self.classlevel4_label = QtGui.QLabel(self.groupBox)
        self.classlevel4_label.setObjectName(_fromUtf8("classlevel4_label"))
        self.gridLayout_2.addWidget(self.classlevel4_label, 3, 0, 1, 1)
        self.classlevel4_fields_comboBox = QtGui.QComboBox(self.groupBox)
        self.classlevel4_fields_comboBox.setObjectName(_fromUtf8("classlevel4_fields_comboBox"))
        self.gridLayout_2.addWidget(self.classlevel4_fields_comboBox, 3, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(classeditor_form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(classeditor_form)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 0, 16))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(classeditor_form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), classeditor_form.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), classeditor_form.reject)
        QtCore.QMetaObject.connectSlotsByName(classeditor_form)

    def retranslateUi(self, classeditor_form):
        classeditor_form.setWindowTitle(_translate("classeditor_form", "Class Editor", None))
        self.groupBox_2.setTitle(_translate("classeditor_form", "Object class definition", None))
        self.groupBox_3.setTitle(_translate("classeditor_form", "GroupBox", None))
        self.classlevel4_label_2.setText(_translate("classeditor_form", "Editor", None))
        self.label_3.setText(_translate("classeditor_form", "You can also activate this form with F11 function key", None))
        self.groupBox.setTitle(_translate("classeditor_form", "Table column definition", None))
        self.classlevel1_label.setText(_translate("classeditor_form", "Class Level 1", None))
        self.classlevel2_label.setText(_translate("classeditor_form", "Class Level 2", None))
        self.classlevel3_label.setText(_translate("classeditor_form", "Class Level 3", None))
        self.classlevel4_label.setText(_translate("classeditor_form", "Class Level 4", None))
        self.groupBox_4.setTitle(_translate("classeditor_form", "Console", None))
        self.label.setText(_translate("classeditor_form", "For all selected elements set the value of field:", None))

