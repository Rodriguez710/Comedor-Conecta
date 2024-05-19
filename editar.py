# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QDoubleValidator,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton, QMessageBox,
    QSizePolicy, QVBoxLayout, QWidget)
from src.resources import *
from Connector.AlumnoConnector import *
import json

class Ui_Dialog_editar_alumno(QDialog, object):
    def setupUi(self, Dialog, origen):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(572, 480)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        with open('config.json', 'r', encoding='utf-8')as json_file:
            data = json.load(json_file)
        
        self.curso = data['curso'] 
        
        self.origen = origen
        
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(Dialog)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(550, 100))
        self.logo.setMaximumSize(QSize(200, 250))
        self.logo.setStyleSheet(u"")
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.logo)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(160, -1, -1, -1)
        self.label_nre = QLabel(Dialog)
        self.label_nre.setObjectName(u"label_nre")
        self.label_nre.setMaximumSize(QSize(102, 16777215))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_nre.setFont(font)
        self.label_nre.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"padding: 5px 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_nre)

        self.lineEdit_nre = QLineEdit(Dialog)
        self.lineEdit_nre.setMaxLength(7)
        self.lineEdit_nre.setValidator(double_validator)
        self.lineEdit_nre.textChanged.connect(self.habilitar_campos)
        self.lineEdit_nre.setObjectName(u"lineEdit_nre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_nre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nre.setSizePolicy(sizePolicy1)
        self.lineEdit_nre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nre.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"margin-top: 10px;\n"
"background-color: transparent;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_nre)

        self.label_nombre = QLabel(Dialog)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setMaximumSize(QSize(102, 16777215))
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_nombre)

        self.lineEdit_nombre = QLineEdit(Dialog)
        self.lineEdit_nombre.setEnabled(False)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        sizePolicy1.setHeightForWidth(self.lineEdit_nombre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nombre.setSizePolicy(sizePolicy1)
        self.lineEdit_nombre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nombre.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_nombre)

        self.label_curso = QLabel(Dialog)
        self.label_curso.setObjectName(u"label_curso")
        self.label_curso.setMaximumSize(QSize(102, 16777215))
        self.label_curso.setFont(font)
        self.label_curso.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_curso)

        self.lineEdit_curso = QLineEdit(Dialog)
        self.lineEdit_curso.setEnabled(False)
        self.lineEdit_curso.setObjectName(u"lineEdit_curso")
        sizePolicy1.setHeightForWidth(self.lineEdit_curso.sizePolicy().hasHeightForWidth())
        self.lineEdit_curso.setSizePolicy(sizePolicy1)
        self.lineEdit_curso.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_curso.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_curso)

        self.label_clase = QLabel(Dialog)
        self.label_clase.setObjectName(u"label_clase")
        self.label_clase.setMaximumSize(QSize(102, 16777215))
        self.label_clase.setFont(font)
        self.label_clase.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_clase)

        self.lineEdit_clase = QLineEdit(Dialog)
        self.lineEdit_clase.setEnabled(False)
        self.lineEdit_clase.setObjectName(u"lineEdit_clase")
        self.lineEdit_clase.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_clase.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_clase)

        self.label_padres = QLabel(Dialog)
        self.label_padres.setObjectName(u"label_padres")
        self.label_padres.setMaximumSize(QSize(102, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_padres.setFont(font1)
        self.label_padres.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #2a5c94;\n"
"border: 1px solid black;\n"
"border-top: none;\n"
"padding: 5px 10px;\n"
"margin-top: 0px;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_padres)

        self.lineEdit_padres = QLineEdit(Dialog)
        self.lineEdit_padres.setEnabled(False)
        self.lineEdit_padres.setObjectName(u"lineEdit_padres")
        self.lineEdit_padres.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_padres.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: #b5b5b5;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_padres)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.btn_anadir = QPushButton(Dialog)
        self.btn_anadir.setObjectName(u"btn_anadir")
        sizePolicy1.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.btn_anadir.setFont(font2)
        self.btn_anadir.clicked.connect(self.editar_alumno)
        self.btn_anadir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_anadir.setStyleSheet(u"QPushButton{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 5px 35px 5px 35px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(11, 5, 71)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_anadir)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Editar alumno", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_nre.setText(QCoreApplication.translate("Dialog", u"NRE:       ", None))
        self.lineEdit_nre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el NRE del alumno...", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.lineEdit_nombre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el nombre del alumno...", None))
        self.label_curso.setText(QCoreApplication.translate("Dialog", u"Curso:     ", None))
        self.lineEdit_curso.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el curso del alumno...", None))
        self.label_clase.setText(QCoreApplication.translate("Dialog", u"Clase:      ", None))
        self.lineEdit_clase.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce la clase del alumno...", None))
        self.label_padres.setText(QCoreApplication.translate("Dialog", u"Padre:           ", None))
        self.lineEdit_padres.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce padre/madre del alumno...", None))
        self.btn_anadir.setText(QCoreApplication.translate("Dialog", u"Editar alumno", None))
    # retranslateUi

    def editar_alumno(self):
        nre = self.lineEdit_nre.text()
        nombre = self.lineEdit_nombre.text()
        curso = self.lineEdit_curso.text()
        clase = self.lineEdit_clase.text()
        madre = self.lineEdit_padres.text()
        conector = AlumnoConnector()
        
        if self.origen == 'curso':
            try:
                if curso == self.curso:
                    conector.actualizarAlumno(nre, nombre, curso, clase, madre)
                    QMessageBox.information(self, "Éxito", "Alumno editado correctamente")
                    self.close()
                else:
                    QMessageBox.critical(self, 'Error', 'No se ha podido editar al alumno. Curso introducido incorrecto.')
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se ha podido editar al alumno: {str(e)}")
        elif self.origen == 'listado':
            try:
                conector.actualizarAlumno(nre, nombre, curso, clase, madre)
                QMessageBox.information(self, "Éxito", "Alumno editado correctamente")
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se ha podido editar al alumno: {str(e)}")    
                
    def habilitar_campos(self):
        nre = self.lineEdit_nre.text()
        conector = AlumnoConnector()
        alumno = conector.devuelvePorNRE(nre)
        
        if self.origen == 'curso':
            if nre and len(nre) == 7:
                self.lineEdit_nombre.setEnabled(True)
                self.lineEdit_nombre.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_curso.setEnabled(True)
                self.lineEdit_curso.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_clase.setEnabled(True)
                self.lineEdit_clase.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_padres.setEnabled(True)
                self.lineEdit_padres.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                if alumno[1] != self.curso:
                    QMessageBox.critical(self, 'Error', 'No se ha podido encontrar al alumno ya que no pertenece a este curso')
                    self.lineEdit_nre.clear()
                else:
                    self.lineEdit_nombre.setText(alumno[0])
                    self.lineEdit_curso.setText(alumno[1])
                    self.lineEdit_clase.setText(alumno[2])
                    self.lineEdit_padres.setText(alumno[3])
            else:
                self.lineEdit_nombre.setEnabled(False)
                self.lineEdit_nombre.clear()
                self.lineEdit_nombre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_curso.setEnabled(False)
                self.lineEdit_curso.clear()
                self.lineEdit_curso.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_clase.setEnabled(False)
                self.lineEdit_clase.clear()
                self.lineEdit_clase.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_padres.setEnabled(False)
                self.lineEdit_padres.clear()
                self.lineEdit_padres.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
        elif self.origen == 'listado':
            if nre and len(nre) == 7:
                if not alumno: 
                    QMessageBox.critical(self, 'Error', 'Alumno no encontrado en la base de datos.')
                else:
                    self.lineEdit_nombre.setEnabled(True)
                    self.lineEdit_nombre.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                        
                    self.lineEdit_curso.setEnabled(True)
                    self.lineEdit_curso.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                        
                    self.lineEdit_clase.setEnabled(True)
                    self.lineEdit_clase.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                        
                    self.lineEdit_padres.setEnabled(True)
                    self.lineEdit_padres.setStyleSheet("background-color: transparent; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                    
                    self.lineEdit_nombre.setText(alumno[0])
                    self.lineEdit_curso.setText(alumno[1])
                    self.lineEdit_clase.setText(alumno[2])
                    self.lineEdit_padres.setText(alumno[3])
            else:
                self.lineEdit_nombre.setEnabled(False)
                self.lineEdit_nombre.clear()
                self.lineEdit_nombre.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_curso.setEnabled(False)
                self.lineEdit_curso.clear()
                self.lineEdit_curso.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_clase.setEnabled(False)
                self.lineEdit_clase.clear()
                self.lineEdit_clase.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
                
                self.lineEdit_padres.setEnabled(False)
                self.lineEdit_padres.clear()
                self.lineEdit_padres.setStyleSheet("background-color: #b5b5b5; border: 0px; border-bottom: 1px solid black; margin-top: 10px;")
            
            
