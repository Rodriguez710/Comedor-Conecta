# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mandarMensaje.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from src.resources import *

class Ui_Dialog_mensaje(QDialog, object):
    def setupUi(self, Dialog, origen):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(870, 446)
        icon = QIcon()
        icon.addFile(u":/logo/iconoProyecto.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        
        self.origen = origen
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(Dialog)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 60))
        self.frame_superior.setStyleSheet(u"")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_logo = QLabel(self.frame_superior)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(120, 150))
        self.label_logo.setPixmap(QPixmap(u":/logo/logoProyecto.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_logo)


        self.verticalLayout.addWidget(self.frame_superior)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #2a5c94;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.box_seleccion_mensaje = QComboBox(Dialog)
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.addItem("")
        self.box_seleccion_mensaje.setObjectName(u"box_seleccion_mensaje")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_seleccion_mensaje.sizePolicy().hasHeightForWidth())
        self.box_seleccion_mensaje.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.box_seleccion_mensaje.setFont(font)
        self.box_seleccion_mensaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.box_seleccion_mensaje.setStyleSheet(u"QComboBox{\n"
"background-color: transparent;\n"
"color: #2a5c94;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout_3.addWidget(self.box_seleccion_mensaje)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget, QHeaderView::section{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.btn_enviar_mensaje = QPushButton(Dialog)
        self.btn_enviar_mensaje.setObjectName(u"btn_enviar_mensaje")
        sizePolicy.setHeightForWidth(self.btn_enviar_mensaje.sizePolicy().hasHeightForWidth())
        self.btn_enviar_mensaje.setSizePolicy(sizePolicy)
        self.btn_enviar_mensaje.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_mensaje.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffff;\n"
"color: #2a5c94;\n"
"padding: 5px 15px;\n"
"border: 2px solid #2a5c94;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #2a5c94;\n"
"color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_enviar_mensaje)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Enviar mensaje", None))
        self.label_logo.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Seleccione el mensaje y los alumnos a cuyos padres desea mandarlo:", None))
        self.box_seleccion_mensaje.setItemText(0, QCoreApplication.translate("Dialog", u"--Seleccione un mensaje--", None))
        self.box_seleccion_mensaje.setItemText(1, QCoreApplication.translate("Dialog", u"El alumno no ha comido nada", None))
        self.box_seleccion_mensaje.setItemText(2, QCoreApplication.translate("Dialog", u"El alumno se ha comido el primer plato pero no ha querido segundo plato", None))
        self.box_seleccion_mensaje.setItemText(3, QCoreApplication.translate("Dialog", u"El alumno no ha comido primer plato pero ha comido segundo plato y postre", None))
        self.box_seleccion_mensaje.setItemText(4, QCoreApplication.translate("Dialog", u"El alumno se ha comido los tres platos y ha terminado casi todo", None))
        self.box_seleccion_mensaje.setItemText(5, QCoreApplication.translate("Dialog", u"El alumno se ha comido todos los platos", None))
        self.box_seleccion_mensaje.setItemText(6, QCoreApplication.translate("Dialog", u"El alumno se ha comido todos los platos y ha querido repetir plato", None))

#if QT_CONFIG(tooltip)
        self.box_seleccion_mensaje.setToolTip(QCoreApplication.translate("Dialog", u"Seleccione el mensaje que desea enviar", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"NRE", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Curso", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Clase", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Padre/Madre", None));
        self.btn_enviar_mensaje.setText(QCoreApplication.translate("Dialog", u"Eliminar alumno/s", None))
    # retranslateUi

