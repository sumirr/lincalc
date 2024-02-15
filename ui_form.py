# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1066, 843)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionContents = QAction(MainWindow)
        self.actionContents.setObjectName(u"actionContents")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    color: #f0f0f0;\n"
"    background-color: #303030;\n"
"    selection-background-color: #555555;\n"
"    selection-color: #f0f0f0;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #404040;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #555555;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #404040;\n"
"    color: #f0f0f0;\n"
"    selection-background-color: #555555;\n"
"    selection-color: #f0f0f0;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #555555;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QLineEdit, QPlainTextEdit, QTextEdit, QListView, QTreeView {\n"
"    background-color: #202020;\n"
"    color: #f0f0f0;\n"
"    selection-background-color: #555555;\n"
"    selection-color: #f0f0f0;\n"
"    border: 1px solid #707070;\n"
"}\n"
"\n"
"QComboBox, QAbstractSpinBox {\n"
"    background-color: #202020;\n"
"    color: #f0f0f0;\n"
"    se"
                        "lection-background-color: #555555;\n"
"    selection-color: #f0f0f0;\n"
"    border: 1px solid #707070;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #404040;\n"
"    color: #f0f0f0;\n"
"    border: 1px solid #707070;\n"
"    padding: 5px;\n"
"    min-width: 60px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    background-color: #404040;\n"
"    border: 1px solid #707070;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: #202020;\n"
"    border: 1px solid #707070;\n"
"    margin-top: 10px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.edtOutput = QTextEdit(self.groupBox_2)
        self.edtOutput.setObjectName(u"edtOutput")
        sizePolicy1.setHeightForWidth(self.edtOutput.sizePolicy().hasHeightForWidth())
        self.edtOutput.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        self.edtOutput.setFont(font)
        self.edtOutput.setLineWrapMode(QTextEdit.NoWrap)

        self.gridLayout_5.addWidget(self.edtOutput, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy2)
        self.gridLayout_8 = QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_5 = QGroupBox(self.groupBox_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblVectorA = QLabel(self.groupBox_5)
        self.lblVectorA.setObjectName(u"lblVectorA")
        sizePolicy2.setHeightForWidth(self.lblVectorA.sizePolicy().hasHeightForWidth())
        self.lblVectorA.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.lblVectorA)

        self.vectorA = QPlainTextEdit(self.groupBox_5)
        self.vectorA.setObjectName(u"vectorA")
        sizePolicy2.setHeightForWidth(self.vectorA.sizePolicy().hasHeightForWidth())
        self.vectorA.setSizePolicy(sizePolicy2)
        self.vectorA.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.vectorA)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblVectorB = QLabel(self.groupBox_5)
        self.lblVectorB.setObjectName(u"lblVectorB")
        sizePolicy2.setHeightForWidth(self.lblVectorB.sizePolicy().hasHeightForWidth())
        self.lblVectorB.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.lblVectorB)

        self.vectorB = QPlainTextEdit(self.groupBox_5)
        self.vectorB.setObjectName(u"vectorB")
        sizePolicy2.setHeightForWidth(self.vectorB.sizePolicy().hasHeightForWidth())
        self.vectorB.setSizePolicy(sizePolicy2)
        self.vectorB.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.vectorB)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)


        self.gridLayout_8.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnVectorSubtraction = QPushButton(self.groupBox_7)
        self.btnVectorSubtraction.setObjectName(u"btnVectorSubtraction")

        self.horizontalLayout_8.addWidget(self.btnVectorSubtraction)

        self.btnVectorSwap = QPushButton(self.groupBox_7)
        self.btnVectorSwap.setObjectName(u"btnVectorSwap")

        self.horizontalLayout_8.addWidget(self.btnVectorSwap)

        self.btnVectorAddition = QPushButton(self.groupBox_7)
        self.btnVectorAddition.setObjectName(u"btnVectorAddition")

        self.horizontalLayout_8.addWidget(self.btnVectorAddition)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnVectorMultiply = QPushButton(self.groupBox_4)
        self.btnVectorMultiply.setObjectName(u"btnVectorMultiply")

        self.gridLayout_3.addWidget(self.btnVectorMultiply, 4, 0, 1, 1)

        self.btnMagnitude = QPushButton(self.groupBox_4)
        self.btnMagnitude.setObjectName(u"btnMagnitude")

        self.gridLayout_3.addWidget(self.btnMagnitude, 1, 0, 1, 1)

        self.btnVectorDotProduct = QPushButton(self.groupBox_4)
        self.btnVectorDotProduct.setObjectName(u"btnVectorDotProduct")

        self.gridLayout_3.addWidget(self.btnVectorDotProduct, 2, 0, 1, 1)

        self.btnVectorCrossProduct = QPushButton(self.groupBox_4)
        self.btnVectorCrossProduct.setObjectName(u"btnVectorCrossProduct")

        self.gridLayout_3.addWidget(self.btnVectorCrossProduct, 2, 1, 1, 1)

        self.edtVectorMultiplyBy = QLineEdit(self.groupBox_4)
        self.edtVectorMultiplyBy.setObjectName(u"edtVectorMultiplyBy")
        sizePolicy1.setHeightForWidth(self.edtVectorMultiplyBy.sizePolicy().hasHeightForWidth())
        self.edtVectorMultiplyBy.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.edtVectorMultiplyBy, 4, 1, 1, 1)

        self.btnAngleBetween = QPushButton(self.groupBox_4)
        self.btnAngleBetween.setObjectName(u"btnAngleBetween")

        self.gridLayout_3.addWidget(self.btnAngleBetween, 1, 1, 1, 1)

        self.btnUnitVector = QPushButton(self.groupBox_4)
        self.btnUnitVector.setObjectName(u"btnUnitVector")

        self.gridLayout_3.addWidget(self.btnUnitVector, 0, 1, 1, 1)

        self.btnProjection = QPushButton(self.groupBox_4)
        self.btnProjection.setObjectName(u"btnProjection")

        self.gridLayout_3.addWidget(self.btnProjection, 0, 0, 1, 1)

        self.btnVectorPowerTo = QPushButton(self.groupBox_4)
        self.btnVectorPowerTo.setObjectName(u"btnVectorPowerTo")

        self.gridLayout_3.addWidget(self.btnVectorPowerTo, 3, 0, 1, 1)

        self.edtVectorPowerTo = QLineEdit(self.groupBox_4)
        self.edtVectorPowerTo.setObjectName(u"edtVectorPowerTo")
        sizePolicy1.setHeightForWidth(self.edtVectorPowerTo.sizePolicy().hasHeightForWidth())
        self.edtVectorPowerTo.setSizePolicy(sizePolicy1)
        self.edtVectorPowerTo.setMaxLength(5)

        self.gridLayout_3.addWidget(self.edtVectorPowerTo, 3, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_4, 2, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.groupBox_7)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)

        self.gridLayout_9.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.lblOutput = QLabel(self.centralwidget)
        self.lblOutput.setObjectName(u"lblOutput")
        sizePolicy1.setHeightForWidth(self.lblOutput.sizePolicy().hasHeightForWidth())
        self.lblOutput.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.lblOutput, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.groupBox_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(self.groupBox_10)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.edtA = QPlainTextEdit(self.groupBox_3)
        self.edtA.setObjectName(u"edtA")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.edtA.sizePolicy().hasHeightForWidth())
        self.edtA.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Mono"])
        self.edtA.setFont(font1)
        self.edtA.setLayoutDirection(Qt.RightToLeft)
        self.edtA.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.edtA.setPlainText(u"")

        self.verticalLayout_2.addWidget(self.edtA)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.random_a = QPushButton(self.groupBox_3)
        self.random_a.setObjectName(u"random_a")

        self.horizontalLayout_2.addWidget(self.random_a)

        self.sliderA = QSlider(self.groupBox_3)
        self.sliderA.setObjectName(u"sliderA")
        self.sliderA.setMinimum(1)
        self.sliderA.setMaximum(10)
        self.sliderA.setValue(2)
        self.sliderA.setOrientation(Qt.Horizontal)
        self.sliderA.setTickPosition(QSlider.TicksAbove)
        self.sliderA.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.sliderA)

        self.lblSliderA = QLabel(self.groupBox_3)
        self.lblSliderA.setObjectName(u"lblSliderA")

        self.horizontalLayout_2.addWidget(self.lblSliderA)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.btnInsertA = QPushButton(self.groupBox_3)
        self.btnInsertA.setObjectName(u"btnInsertA")

        self.horizontalLayout_3.addWidget(self.btnInsertA)

        self.cmbA = QComboBox(self.groupBox_3)
        self.cmbA.setObjectName(u"cmbA")

        self.horizontalLayout_3.addWidget(self.cmbA)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.vlInputButtons = QVBoxLayout()
        self.vlInputButtons.setSpacing(1)
        self.vlInputButtons.setObjectName(u"vlInputButtons")
        self.AMultiplyB = QPushButton(self.groupBox_3)
        self.AMultiplyB.setObjectName(u"AMultiplyB")

        self.vlInputButtons.addWidget(self.AMultiplyB)

        self.APlusB = QPushButton(self.groupBox_3)
        self.APlusB.setObjectName(u"APlusB")

        self.vlInputButtons.addWidget(self.APlusB)

        self.AMinuB = QPushButton(self.groupBox_3)
        self.AMinuB.setObjectName(u"AMinuB")
        icon = QIcon()
        iconThemeName = u"appointment-missed"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.AMinuB.setIcon(icon)

        self.vlInputButtons.addWidget(self.AMinuB)

        self.btnSwap = QPushButton(self.groupBox_3)
        self.btnSwap.setObjectName(u"btnSwap")

        self.vlInputButtons.addWidget(self.btnSwap)


        self.gridLayout.addLayout(self.vlInputButtons, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.edtB = QPlainTextEdit(self.groupBox_3)
        self.edtB.setObjectName(u"edtB")
        self.edtB.setFont(font1)
        self.edtB.setLayoutDirection(Qt.RightToLeft)
        self.edtB.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.edtB.setPlainText(u"")

        self.verticalLayout_4.addWidget(self.edtB)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.random_b = QPushButton(self.groupBox_3)
        self.random_b.setObjectName(u"random_b")

        self.horizontalLayout_5.addWidget(self.random_b)

        self.sliderB = QSlider(self.groupBox_3)
        self.sliderB.setObjectName(u"sliderB")
        self.sliderB.setMinimum(1)
        self.sliderB.setMaximum(10)
        self.sliderB.setValue(2)
        self.sliderB.setOrientation(Qt.Horizontal)
        self.sliderB.setTickPosition(QSlider.TicksAbove)
        self.sliderB.setTickInterval(1)

        self.horizontalLayout_5.addWidget(self.sliderB)

        self.lblSliderB = QLabel(self.groupBox_3)
        self.lblSliderB.setObjectName(u"lblSliderB")

        self.horizontalLayout_5.addWidget(self.lblSliderB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.btnInsertB = QPushButton(self.groupBox_3)
        self.btnInsertB.setObjectName(u"btnInsertB")

        self.horizontalLayout_6.addWidget(self.btnInsertB)

        self.cmbB = QComboBox(self.groupBox_3)
        self.cmbB.setObjectName(u"cmbB")

        self.horizontalLayout_6.addWidget(self.cmbB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_10)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnMultiply = QPushButton(self.groupBox)
        self.btnMultiply.setObjectName(u"btnMultiply")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(5)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnMultiply.sizePolicy().hasHeightForWidth())
        self.btnMultiply.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnMultiply, 7, 0, 1, 1)

        self.edtPower = QLineEdit(self.groupBox)
        self.edtPower.setObjectName(u"edtPower")
        sizePolicy1.setHeightForWidth(self.edtPower.sizePolicy().hasHeightForWidth())
        self.edtPower.setSizePolicy(sizePolicy1)
        self.edtPower.setMaxLength(5)

        self.gridLayout_2.addWidget(self.edtPower, 6, 1, 1, 1)

        self.edtMultiply = QLineEdit(self.groupBox)
        self.edtMultiply.setObjectName(u"edtMultiply")
        sizePolicy1.setHeightForWidth(self.edtMultiply.sizePolicy().hasHeightForWidth())
        self.edtMultiply.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.edtMultiply, 7, 1, 1, 1)

        self.btnAdjoint = QPushButton(self.groupBox)
        self.btnAdjoint.setObjectName(u"btnAdjoint")
        sizePolicy5.setHeightForWidth(self.btnAdjoint.sizePolicy().hasHeightForWidth())
        self.btnAdjoint.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnAdjoint, 0, 0, 1, 1)

        self.btnPower = QPushButton(self.groupBox)
        self.btnPower.setObjectName(u"btnPower")
        sizePolicy5.setHeightForWidth(self.btnPower.sizePolicy().hasHeightForWidth())
        self.btnPower.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnPower, 6, 0, 1, 1)

        self.btnEigenvalues = QPushButton(self.groupBox)
        self.btnEigenvalues.setObjectName(u"btnEigenvalues")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btnEigenvalues.sizePolicy().hasHeightForWidth())
        self.btnEigenvalues.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnEigenvalues, 2, 0, 1, 1)

        self.btnEchelon = QPushButton(self.groupBox)
        self.btnEchelon.setObjectName(u"btnEchelon")
        sizePolicy6.setHeightForWidth(self.btnEchelon.sizePolicy().hasHeightForWidth())
        self.btnEchelon.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnEchelon, 1, 2, 1, 1)

        self.btnDeterminant = QPushButton(self.groupBox)
        self.btnDeterminant.setObjectName(u"btnDeterminant")
        sizePolicy5.setHeightForWidth(self.btnDeterminant.sizePolicy().hasHeightForWidth())
        self.btnDeterminant.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnDeterminant, 1, 1, 1, 1)

        self.btnConjugate = QPushButton(self.groupBox)
        self.btnConjugate.setObjectName(u"btnConjugate")
        sizePolicy6.setHeightForWidth(self.btnConjugate.sizePolicy().hasHeightForWidth())
        self.btnConjugate.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnConjugate, 1, 0, 1, 1)

        self.btnCoFactor = QPushButton(self.groupBox)
        self.btnCoFactor.setObjectName(u"btnCoFactor")
        sizePolicy6.setHeightForWidth(self.btnCoFactor.sizePolicy().hasHeightForWidth())
        self.btnCoFactor.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnCoFactor, 0, 2, 1, 1)

        self.btnAdjugate = QPushButton(self.groupBox)
        self.btnAdjugate.setObjectName(u"btnAdjugate")

        self.gridLayout_2.addWidget(self.btnAdjugate, 0, 1, 1, 1)

        self.btnJordanForm = QPushButton(self.groupBox)
        self.btnJordanForm.setObjectName(u"btnJordanForm")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btnJordanForm.sizePolicy().hasHeightForWidth())
        self.btnJordanForm.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.btnJordanForm, 2, 1, 1, 1)

        self.btnHerimitian = QPushButton(self.groupBox)
        self.btnHerimitian.setObjectName(u"btnHerimitian")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(5)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btnHerimitian.sizePolicy().hasHeightForWidth())
        self.btnHerimitian.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.btnHerimitian, 2, 2, 1, 1)

        self.btnNorm = QPushButton(self.groupBox)
        self.btnNorm.setObjectName(u"btnNorm")
        sizePolicy5.setHeightForWidth(self.btnNorm.sizePolicy().hasHeightForWidth())
        self.btnNorm.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnNorm, 3, 0, 1, 1)

        self.btnInverse = QPushButton(self.groupBox)
        self.btnInverse.setObjectName(u"btnInverse")
        sizePolicy6.setHeightForWidth(self.btnInverse.sizePolicy().hasHeightForWidth())
        self.btnInverse.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnInverse, 3, 1, 1, 1)

        self.btnPermanent = QPushButton(self.groupBox)
        self.btnPermanent.setObjectName(u"btnPermanent")
        sizePolicy6.setHeightForWidth(self.btnPermanent.sizePolicy().hasHeightForWidth())
        self.btnPermanent.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnPermanent, 3, 2, 1, 1)

        self.btnRank = QPushButton(self.groupBox)
        self.btnRank.setObjectName(u"btnRank")
        sizePolicy5.setHeightForWidth(self.btnRank.sizePolicy().hasHeightForWidth())
        self.btnRank.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnRank, 4, 0, 1, 1)

        self.btnRref = QPushButton(self.groupBox)
        self.btnRref.setObjectName(u"btnRref")
        sizePolicy6.setHeightForWidth(self.btnRref.sizePolicy().hasHeightForWidth())
        self.btnRref.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnRref, 4, 1, 1, 1)

        self.btnSymmetric = QPushButton(self.groupBox)
        self.btnSymmetric.setObjectName(u"btnSymmetric")
        sizePolicy6.setHeightForWidth(self.btnSymmetric.sizePolicy().hasHeightForWidth())
        self.btnSymmetric.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnSymmetric, 4, 2, 1, 1)

        self.btnSkewSymmetric = QPushButton(self.groupBox)
        self.btnSkewSymmetric.setObjectName(u"btnSkewSymmetric")
        sizePolicy5.setHeightForWidth(self.btnSkewSymmetric.sizePolicy().hasHeightForWidth())
        self.btnSkewSymmetric.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btnSkewSymmetric, 5, 0, 1, 1)

        self.btnTrace = QPushButton(self.groupBox)
        self.btnTrace.setObjectName(u"btnTrace")
        sizePolicy6.setHeightForWidth(self.btnTrace.sizePolicy().hasHeightForWidth())
        self.btnTrace.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.btnTrace, 5, 1, 1, 1)

        self.btnTranspose = QPushButton(self.groupBox)
        self.btnTranspose.setObjectName(u"btnTranspose")
        sizePolicy8.setHeightForWidth(self.btnTranspose.sizePolicy().hasHeightForWidth())
        self.btnTranspose.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.btnTranspose, 5, 2, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_10, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1066, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.exit_app)
        self.actionAbout.triggered.connect(MainWindow.about)
        self.actionContents.triggered.connect(MainWindow.contents)
        self.btnHerimitian.clicked.connect(MainWindow.hermitian)
        self.btnTrace.clicked.connect(MainWindow.trace)
        self.btnRank.clicked.connect(MainWindow.rank)
        self.btnRref.clicked.connect(MainWindow.rref)
        self.btnDeterminant.clicked.connect(MainWindow.determinant)
        self.btnConjugate.clicked.connect(MainWindow.conjugate)
        self.btnEchelon.clicked.connect(MainWindow.echelon)
        self.btnEigenvalues.clicked.connect(MainWindow.eigen_values)
        self.btnSkewSymmetric.clicked.connect(MainWindow.skew_symmetric)
        self.btnNorm.clicked.connect(MainWindow.norm)
        self.btnAdjoint.clicked.connect(MainWindow.adjoint)
        self.btnSymmetric.clicked.connect(MainWindow.symmetric)
        self.btnPower.clicked.connect(MainWindow.power_of)
        self.btnInverse.clicked.connect(MainWindow.inverse)
        self.btnCoFactor.clicked.connect(MainWindow.cofactor_matrix)
        self.btnMultiply.clicked.connect(MainWindow.multiply_by)
        self.btnTranspose.clicked.connect(MainWindow.transpose)
        self.btnPermanent.clicked.connect(MainWindow.permanent)
        self.sliderB.valueChanged.connect(self.lblSliderB.setNum)
        self.sliderA.valueChanged.connect(self.lblSliderA.setNum)
        self.AMinuB.clicked.connect(MainWindow.difference)
        self.pushButton_5.clicked.connect(self.edtA.clear)
        self.btnInsertA.clicked.connect(MainWindow.insertA)
        self.btnSwap.clicked.connect(MainWindow.swap_matrices)
        self.random_a.clicked.connect(MainWindow.random_matrix)
        self.pushButton_7.clicked.connect(self.edtB.clear)
        self.sliderB.valueChanged.connect(MainWindow.random_matrixb)
        self.sliderA.valueChanged.connect(MainWindow.random_matrix)
        self.random_b.clicked.connect(MainWindow.random_matrixb)
        self.AMultiplyB.clicked.connect(MainWindow.multiplication)
        self.APlusB.clicked.connect(MainWindow.sum)
        self.btnInsertB.clicked.connect(MainWindow.insertB)
        self.btnVectorDotProduct.clicked.connect(MainWindow.vector_dot_product)
        self.btnVectorCrossProduct.clicked.connect(MainWindow.vector_cross_product)
        self.btnProjection.clicked.connect(MainWindow.projection)
        self.btnMagnitude.clicked.connect(MainWindow.vector_magnitude)
        self.btnUnitVector.clicked.connect(MainWindow.vector_unit_vector)
        self.btnAngleBetween.clicked.connect(MainWindow.vector_angle_between)
        self.btnVectorPowerTo.clicked.connect(MainWindow.vector_power_to)
        self.btnVectorMultiply.clicked.connect(MainWindow.vector_multiply_by)
        self.btnJordanForm.clicked.connect(MainWindow.jordan_form)
        self.btnVectorAddition.clicked.connect(MainWindow.vector_addition)
        self.btnVectorSubtraction.clicked.connect(MainWindow.vector_subtraction)
        self.btnVectorSwap.clicked.connect(MainWindow.swap_vectors)
        self.btnAdjugate.clicked.connect(MainWindow.adjugate)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("MainWindow", u"CTRL + Q", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionContents.setText(QCoreApplication.translate("MainWindow", u"Contents", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Vectors", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Vector Input", None))
        self.lblVectorA.setText(QCoreApplication.translate("MainWindow", u"Vector A", None))
        self.lblVectorB.setText(QCoreApplication.translate("MainWindow", u"Vector B", None))
        self.btnVectorSubtraction.setText(QCoreApplication.translate("MainWindow", u"A - B", None))
        self.btnVectorSwap.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        self.btnVectorAddition.setText(QCoreApplication.translate("MainWindow", u"A + B", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Vector Functions", None))
        self.btnVectorMultiply.setText(QCoreApplication.translate("MainWindow", u"Multiply By", None))
        self.btnMagnitude.setText(QCoreApplication.translate("MainWindow", u"Magnitude", None))
        self.btnVectorDotProduct.setText(QCoreApplication.translate("MainWindow", u"Dot Product", None))
        self.btnVectorCrossProduct.setText(QCoreApplication.translate("MainWindow", u"Cross Product", None))
        self.edtVectorMultiplyBy.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btnAngleBetween.setText(QCoreApplication.translate("MainWindow", u"Angle Between", None))
        self.btnUnitVector.setText(QCoreApplication.translate("MainWindow", u"Unit Vector", None))
        self.btnProjection.setText(QCoreApplication.translate("MainWindow", u"Projection", None))
        self.btnVectorPowerTo.setText(QCoreApplication.translate("MainWindow", u"Power To", None))
        self.edtVectorPowerTo.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.lblOutput.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Matrices", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Matrix Input", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Matrix A", None))
        self.random_a.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.lblSliderA.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnInsertA.setText(QCoreApplication.translate("MainWindow", u"Insert Into", None))
        self.AMultiplyB.setText(QCoreApplication.translate("MainWindow", u"A x B", None))
        self.APlusB.setText(QCoreApplication.translate("MainWindow", u"A + B", None))
        self.AMinuB.setText(QCoreApplication.translate("MainWindow", u"A - B", None))
        self.btnSwap.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Matrix B", None))
        self.random_b.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.lblSliderB.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnInsertB.setText(QCoreApplication.translate("MainWindow", u"Insert Into", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Matrix Functions", None))
        self.btnMultiply.setText(QCoreApplication.translate("MainWindow", u"Multiply By", None))
        self.edtPower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.edtMultiply.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btnAdjoint.setText(QCoreApplication.translate("MainWindow", u"Adjoint", None))
        self.btnPower.setText(QCoreApplication.translate("MainWindow", u"Power to", None))
        self.btnEigenvalues.setText(QCoreApplication.translate("MainWindow", u"Eigenvalues", None))
        self.btnEchelon.setText(QCoreApplication.translate("MainWindow", u"Echelon Form", None))
        self.btnDeterminant.setText(QCoreApplication.translate("MainWindow", u"Determinant", None))
        self.btnConjugate.setText(QCoreApplication.translate("MainWindow", u"Conjugate", None))
        self.btnCoFactor.setText(QCoreApplication.translate("MainWindow", u"CoFactor", None))
        self.btnAdjugate.setText(QCoreApplication.translate("MainWindow", u"Adjugate", None))
        self.btnJordanForm.setText(QCoreApplication.translate("MainWindow", u"Jordan From", None))
        self.btnHerimitian.setText(QCoreApplication.translate("MainWindow", u"Hermitian", None))
        self.btnNorm.setText(QCoreApplication.translate("MainWindow", u"Norm", None))
        self.btnInverse.setText(QCoreApplication.translate("MainWindow", u"Inverse", None))
        self.btnPermanent.setText(QCoreApplication.translate("MainWindow", u"Permanent", None))
        self.btnRank.setText(QCoreApplication.translate("MainWindow", u"Rank", None))
        self.btnRref.setText(QCoreApplication.translate("MainWindow", u"Reduced  Echelon", None))
        self.btnSymmetric.setText(QCoreApplication.translate("MainWindow", u"Symmetric", None))
        self.btnSkewSymmetric.setText(QCoreApplication.translate("MainWindow", u"Skew-Symmetric", None))
        self.btnTrace.setText(QCoreApplication.translate("MainWindow", u"Trace", None))
        self.btnTranspose.setText(QCoreApplication.translate("MainWindow", u"Transpose", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

