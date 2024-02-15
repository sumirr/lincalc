# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QPlainTextEdit, QSizePolicy, QTreeView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(796, 597)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeView = QTreeView(Form)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"\n"
"        background-color: #222;\n"
"        color: #fff;\n"
"        selection-background-color: #444;\n"
"        selection-color: #fff;\n"
"        border: none;\n"
"")

        self.horizontalLayout.addWidget(self.treeView)

        self.edtHelp = QPlainTextEdit(Form)
        self.edtHelp.setObjectName(u"edtHelp")
        font = QFont()
        font.setFamilies([u"Courier"])
        self.edtHelp.setFont(font)
        self.edtHelp.setStyleSheet(u"background-color: #222;\n"
"        color: #fff;\n"
"        border: none;")
        self.edtHelp.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.edtHelp.setReadOnly(True)
        self.edtHelp.setPlainText(u"")

        self.horizontalLayout.addWidget(self.edtHelp)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

