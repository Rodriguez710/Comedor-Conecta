# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listadoAlumnos.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from src.resources import *
from anadir import *
from editar import *
from eliminaAlumnos import *
from mandarMensaje import *
from Connector.AlumnoConnector import *

class Ui_Dialog_listadoAlumnos(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1104, 886)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(Dialog)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 60))
        self.frame_superior.setStyleSheet(u"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_logo = QLabel(self.frame_superior)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(120, 150))
        self.label_logo.setPixmap(QPixmap(u":/logo/logoProyecto.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_logo)


        self.verticalLayout.addWidget(self.frame_superior)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.btn_volver_atras = QPushButton(Dialog)
        self.btn_volver_atras.clicked.connect(self.close)
        self.btn_volver_atras.setObjectName(u"btn_volver_atras")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_volver_atras.sizePolicy().hasHeightForWidth())
        self.btn_volver_atras.setSizePolicy(sizePolicy)
        self.btn_volver_atras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_volver_atras.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 10px 20px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_volver_atras)

        self.horizontalSpacer = QSpacerItem(800, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)
        
        self.btn_enviar_mensaje = QPushButton(Dialog)
        self.btn_enviar_mensaje.clicked.connect(self.abrir_ventana_enviar_mensaje)
        self.btn_enviar_mensaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_mensaje.setObjectName(u"btn_enviar_mensaje")
        sizePolicy.setHeightForWidth(self.btn_enviar_mensaje.sizePolicy().hasHeightForWidth())
        self.btn_enviar_mensaje.setSizePolicy(sizePolicy)
        self.btn_enviar_mensaje.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 10px 20px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconosLaterales/mensaje.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_enviar_mensaje.setIcon(icon1)
        self.horizontalLayout_2.addWidget(self.btn_enviar_mensaje)

        self.btn_anadir = QPushButton(Dialog)
        self.btn_anadir.clicked.connect(self.abrir_ventana_anadir)
        self.btn_anadir.setObjectName(u"btn_anadir")
        sizePolicy.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy)
        self.btn_anadir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_anadir.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 10px 20px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconosLaterales/anadir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_anadir.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_anadir)

        self.btn_editar = QPushButton(Dialog)
        self.btn_editar.clicked.connect(self.abrir_ventana_editar)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 10px 20px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconosLaterales/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editar.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(Dialog)
        self.btn_eliminar.clicked.connect(self.abrir_ventana_eliminar)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        sizePolicy.setHeightForWidth(self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy)
        self.btn_eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 10px 20px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconosLaterales/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eliminar.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_sexto = QLabel(Dialog)
        self.label_sexto.setObjectName(u"label_sexto")
        self.label_sexto.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_sexto)

        self.tabla_sexto = QTableWidget(Dialog)
        if (self.tabla_sexto.columnCount() < 5):
            self.tabla_sexto.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_sexto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_sexto.setObjectName(u"tabla_sexto")
        self.tabla_sexto.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_sexto.horizontalHeader().setDefaultSectionSize(163)
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_sexto.horizontalHeader().setStretchLastSection(True)
        self.tabla_sexto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.verticalLayout.addWidget(self.tabla_sexto)

        self.label_quinto = QLabel(Dialog)
        self.label_quinto.setObjectName(u"label_quinto")
        self.label_quinto.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_quinto)

        self.tabla_quinto = QTableWidget(Dialog)
        if (self.tabla_quinto.columnCount() < 5):
            self.tabla_quinto.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_quinto.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_quinto.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_quinto.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_quinto.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_quinto.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tabla_quinto.setObjectName(u"tabla_quinto")
        self.tabla_quinto.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_quinto.horizontalHeader().setDefaultSectionSize(163)
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_quinto.horizontalHeader().setStretchLastSection(True)
        self.tabla_quinto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_quinto)

        self.label_cuarto = QLabel(Dialog)
        self.label_cuarto.setObjectName(u"label_cuarto")
        self.label_cuarto.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_cuarto)

        self.tabla_cuarto = QTableWidget(Dialog)
        if (self.tabla_cuarto.columnCount() < 5):
            self.tabla_cuarto.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_cuarto.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_cuarto.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_cuarto.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_cuarto.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_cuarto.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tabla_cuarto.setObjectName(u"tabla_cuarto")
        self.tabla_cuarto.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_cuarto.horizontalHeader().setDefaultSectionSize(163)
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_cuarto.horizontalHeader().setStretchLastSection(True)
        self.tabla_cuarto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_cuarto)

        self.label_tercero = QLabel(Dialog)
        self.label_tercero.setObjectName(u"label_tercero")
        self.label_tercero.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_tercero)

        self.tabla_tercero = QTableWidget(Dialog)
        if (self.tabla_tercero.columnCount() < 5):
            self.tabla_tercero.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_tercero.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_tercero.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_tercero.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_tercero.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_tercero.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        self.tabla_tercero.setObjectName(u"tabla_tercero")
        self.tabla_tercero.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_tercero.horizontalHeader().setDefaultSectionSize(163)
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_tercero.horizontalHeader().setStretchLastSection(True)
        self.tabla_tercero.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_tercero)

        self.label_segundo = QLabel(Dialog)
        self.label_segundo.setObjectName(u"label_segundo")
        self.label_segundo.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_segundo)

        self.tabla_segundo = QTableWidget(Dialog)
        if (self.tabla_segundo.columnCount() < 5):
            self.tabla_segundo.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_segundo.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_segundo.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_segundo.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_segundo.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_segundo.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.tabla_segundo.setObjectName(u"tabla_segundo")
        self.tabla_segundo.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_segundo.horizontalHeader().setDefaultSectionSize(163)
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_segundo.horizontalHeader().setStretchLastSection(True)
        self.tabla_segundo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_segundo)

        self.label_primero = QLabel(Dialog)
        self.label_primero.setObjectName(u"label_primero")
        self.label_primero.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label_primero)

        self.tabla_primero = QTableWidget(Dialog)
        if (self.tabla_primero.columnCount() < 5):
            self.tabla_primero.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_primero.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_primero.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_primero.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_primero.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_primero.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.tabla_primero.setObjectName(u"tabla_primero")
        self.tabla_primero.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tabla_primero.horizontalHeader().setDefaultSectionSize(163)
        
        # Ajustar el ancho de la última columna para llenar el espacio restante
        self.tabla_primero.horizontalHeader().setStretchLastSection(True)
        self.tabla_primero.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout.addWidget(self.tabla_primero)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tablas = [self.tabla_primero, self.tabla_segundo, self.tabla_tercero, self.tabla_cuarto, self.tabla_quinto, self.tabla_sexto]

        self.actualiza_todos_alumnos()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Listado de alumnos del centro", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Listado de alumnos del centro:", None))
        self.btn_volver_atras.setText(QCoreApplication.translate("Dialog", u"Volver atr\u00e1s", None))
        self.btn_enviar_mensaje.setText(QCoreApplication.translate("Dialog", u"Enviar mensaje", None))
        self.btn_anadir.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir alumno", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"Editar alumno", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar alumno", None))
        self.label_sexto.setText(QCoreApplication.translate("Dialog", u"Curso 6\u00ba:", None))
        ___qtablewidgetitem = self.tabla_sexto.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem1 = self.tabla_sexto.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla_sexto.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem3 = self.tabla_sexto.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem4 = self.tabla_sexto.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
        self.label_quinto.setText(QCoreApplication.translate("Dialog", u"Curso 5\u00ba:", None))
        ___qtablewidgetitem5 = self.tabla_quinto.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem6 = self.tabla_quinto.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem7 = self.tabla_quinto.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem8 = self.tabla_quinto.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem9 = self.tabla_quinto.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
        self.label_cuarto.setText(QCoreApplication.translate("Dialog", u"Curso 4\u00ba:", None))
        ___qtablewidgetitem10 = self.tabla_cuarto.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem11 = self.tabla_cuarto.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem12 = self.tabla_cuarto.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem13 = self.tabla_cuarto.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem14 = self.tabla_cuarto.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
        self.label_tercero.setText(QCoreApplication.translate("Dialog", u"Curso 3\u00ba:", None))
        ___qtablewidgetitem15 = self.tabla_tercero.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem16 = self.tabla_tercero.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem17 = self.tabla_tercero.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem18 = self.tabla_tercero.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem19 = self.tabla_tercero.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
        self.label_segundo.setText(QCoreApplication.translate("Dialog", u"Curso 2\u00ba:", None))
        ___qtablewidgetitem20 = self.tabla_segundo.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem21 = self.tabla_segundo.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem22 = self.tabla_segundo.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem23 = self.tabla_segundo.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem24 = self.tabla_segundo.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
        self.label_primero.setText(QCoreApplication.translate("Dialog", u"Curso 1\u00ba:", None))
        ___qtablewidgetitem25 = self.tabla_primero.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem26 = self.tabla_primero.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem27 = self.tabla_primero.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem28 = self.tabla_primero.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem29 = self.tabla_primero.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
    # retranslateUi
    
    def abrir_ventana_anadir(self):
        self.ventana_anadir_alumnos = VentanaAnadirAlumno()
        self.ventana_anadir_alumnos.show()
        self.ventana_anadir_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()

    def abrir_ventana_editar(self):
        self.ventana_editar_alumnos = VentanaEditarAlumno()
        self.ventana_editar_alumnos.show()
        self.ventana_editar_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()

    def abrir_ventana_eliminar(self):
        self.ventana_eliminar_alumnos = VentanaEliminaAlumnos()
        self.ventana_eliminar_alumnos.show()
        self.ventana_eliminar_alumnos.exec_()
        self.limpiar_tablas()
        self.actualiza_todos_alumnos()

    def abrir_ventana_enviar_mensaje(self):
        self.ventana_enviar_mensaje = VentanaMandarMensajeCurso()
        self.ventana_enviar_mensaje.show()
        self.ventana_enviar_mensaje.exec_()
        
    def actualiza_todos_alumnos(self):
        conector = AlumnoConnector()
        # Primero limpia todas las tablas
        for tabla in self.tablas:
            tabla.setRowCount(0)

        # Conectar a la base de datos y obtener los datos de los alumnos
        alumnos = conector.devuelveTodos()  # Supongamos que esto retorna una lista de diccionarios con los datos de los alumnos
        
        for alumno in alumnos:
            curso = alumno[2]
            if curso == "1º":
                self.anadir_fila(self.tabla_primero, alumno)
            elif curso == "2º":
                self.anadir_fila(self.tabla_segundo, alumno)
            elif curso == "3º":
                self.anadir_fila(self.tabla_tercero, alumno)
            elif curso == "4º":
                self.anadir_fila(self.tabla_cuarto, alumno)
            elif curso == "5º":
                self.anadir_fila(self.tabla_quinto, alumno)
            elif curso == "6º":
                self.anadir_fila(self.tabla_sexto, alumno)
    
    def anadir_fila(self, tabla, alumno):
        rowPosition = tabla.rowCount()
        tabla.insertRow(rowPosition)
        items = [QTableWidgetItem(str(alumno[0])), QTableWidgetItem(alumno[1]),
                 QTableWidgetItem(alumno[2]), QTableWidgetItem(alumno[3]),
                 QTableWidgetItem(alumno[4])]
        for col, item in enumerate(items):
            item.setTextAlignment(Qt.AlignCenter)
            tabla.setItem(rowPosition, col, item)

    def actualiza_alumnos(self, curso_alumno):
        # Convertir el curso de string a número entero
        curso_alumno_int = int(curso_alumno[:-1])    
        
        # Limpia la tabla del curso antes de actualizarla
        tabla = self.tablas[curso_alumno_int - 1]
        
        # Obtener datos de alumnos del curso actual
        alumno_connector = AlumnoConnector()
        alumnos_curso = alumno_connector.devuelvePorCurso(curso_alumno)
        
        for alumno in alumnos_curso:
                nre, nombre, curso, clase, madre = alumno
                # Agregar alumno solo si pertenece al curso
                if alumno[2] == curso_alumno:
                        # Configurar el número de filas en la tabla
                        tabla.setRowCount(tabla.rowCount() + 1)
                        # Llenar la tabla con los datos del alumno
                        row = tabla.rowCount() - 1
                        for col, data in enumerate(alumno):
                                item = QTableWidgetItem(str(data))
                                tabla.setItem(row, col, item)
                                item.setTextAlignment(Qt.AlignCenter)

    # Función para limpiar todas las tablas
    def limpiar_tablas(self):
        for tabla in self.tablas:
            tabla.clearContents()
            tabla.setRowCount(0)
    
class VentanaAnadirAlumno(Ui_Dialog_anadir_alumno, QDialog):
        def __init__(self):
                super(VentanaAnadirAlumno, self).__init__()
                self.setupUi(self, origen='listado')

class VentanaEditarAlumno(Ui_Dialog_editar_alumno, QDialog):
        def __init__(self):
                super(VentanaEditarAlumno, self).__init__()
                self.setupUi(self, origen='listado')
                
class VentanaEliminaAlumnos(Ui_Dialog_eliminaAlumnos, QDialog):
        def __init__(self):
                super(VentanaEliminaAlumnos, self).__init__()
                self.setupUi(self, origen='listado')

class VentanaMandarMensajeCurso(Ui_Dialog_mensaje, QDialog):
    def __init__(self):
        super(VentanaMandarMensajeCurso, self).__init__()
        self.setupUi(self, origen='listado')
