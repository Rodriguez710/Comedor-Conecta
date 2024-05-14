# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anadir.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton, QMessageBox,
    QSizePolicy, QVBoxLayout, QWidget)
from src.resources import *
from Connector.AlumnoConnector import *
import json

class Ui_Dialog_anadir_alumno(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(583, 468)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 561, 451))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.logo = QLabel(self.layoutWidget)
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
        self.label_nre = QLabel(self.layoutWidget)
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

        self.lineEdit_nre = QLineEdit(self.layoutWidget)
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
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_nre)

        self.label_nombre = QLabel(self.layoutWidget)
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

        self.lineEdit_nombre = QLineEdit(self.layoutWidget)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")
        sizePolicy1.setHeightForWidth(self.lineEdit_nombre.sizePolicy().hasHeightForWidth())
        self.lineEdit_nombre.setSizePolicy(sizePolicy1)
        self.lineEdit_nombre.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nombre.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_nombre)

        self.label_curso = QLabel(self.layoutWidget)
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

        self.lineEdit_curso = QLineEdit(self.layoutWidget)
        self.lineEdit_curso.setObjectName(u"lineEdit_curso")
        sizePolicy1.setHeightForWidth(self.lineEdit_curso.sizePolicy().hasHeightForWidth())
        self.lineEdit_curso.setSizePolicy(sizePolicy1)
        self.lineEdit_curso.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_curso.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_curso)

        self.label_clase = QLabel(self.layoutWidget)
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

        self.lineEdit_clase = QLineEdit(self.layoutWidget)
        self.lineEdit_clase.setObjectName(u"lineEdit_clase")
        self.lineEdit_clase.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_clase.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_clase)

        self.label_padres = QLabel(self.layoutWidget)
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

        self.lineEdit_padres = QLineEdit(self.layoutWidget)
        self.lineEdit_padres.setObjectName(u"lineEdit_padres")
        self.lineEdit_padres.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_padres.setStyleSheet(u"QLineEdit{\n"
"border: 0px;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"margin-top: 10px;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_padres)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.btn_anadir = QPushButton(self.layoutWidget)
        self.btn_anadir.setObjectName(u"btn_anadir")
        sizePolicy1.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.btn_anadir.setFont(font2)
        self.btn_anadir.clicked.connect(self.anadir_alumno)
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

        with open('config.json', 'r')as json_file:
            data = json.load(json_file)
        
        self.curso = str(data['curso']) 

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"A\u00f1adir alumno", None))
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
        self.btn_anadir.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir alumno", None))
    # retranslateUi

    def anadir_alumno(self):
        nre = self.lineEdit_nre.text()
        nombre = self.lineEdit_nombre.text()
        curso = self.lineEdit_curso.text()
        clase = self.lineEdit_clase.text()
        padre = self.lineEdit_padres.text()
        
        if curso != self.curso:
            QMessageBox.critical(self, 'Error', f'El alumno no puede ser de un curso diferente a {self.curso}º')
        else: 
            try:
                conector = AlumnoConnector()
                conector.insertar(nre, nombre, curso, clase, padre)
                QMessageBox.information(self.btn_anadir, "Éxito", "Alumno añadido con éxito.")
                self.accept()

            except Exception as e:
                QMessageBox.critical(self.btn_anadir, "Error", f"Error al insertar datos en la base de datos: {str(e)}")
                print(e)