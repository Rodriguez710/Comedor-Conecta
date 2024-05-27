# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anadirMadre.ui'
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
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
#import resources_rc

class Ui_Dialog(object):
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
        self.lineEdit_nre.setCursor(QCursor(Qt.IBeamCursor))
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
        self.lineEdit_curso.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_curso)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.btn_anadir = QPushButton(self.layoutWidget)
        self.btn_anadir.setObjectName(u"btn_anadir")
        sizePolicy1.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.btn_anadir.setFont(font1)
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


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"A\u00f1adir alumno", None))
        self.logo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/logo/logoProyecto.png\"/></p></body></html>", None))
        self.label_nre.setText(QCoreApplication.translate("Dialog", u"ID:       ", None))
        self.lineEdit_nre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el ID de la madre...", None))
        self.label_nombre.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.lineEdit_nombre.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el nombre de la madre...", None))
        self.label_curso.setText(QCoreApplication.translate("Dialog", u"ID Hijo:     ", None))
        self.lineEdit_curso.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce el id del hijo...", None))
        self.btn_anadir.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir madre", None))
    # retranslateUi

