# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designtipcalc.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(650, 450))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 40, 561, 421))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtoncalculate = QPushButton(self.layoutWidget)
        self.pushButtoncalculate.setObjectName(u"pushButtoncalculate")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.pushButtoncalculate.setFont(font)

        self.gridLayout.addWidget(self.pushButtoncalculate, 4, 0, 1, 1)

        self.labelpeople = QLabel(self.layoutWidget)
        self.labelpeople.setObjectName(u"labelpeople")
        self.labelpeople.setFont(font)
        self.labelpeople.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelpeople, 2, 0, 1, 1)

        self.labelresulttotalnumber = QLabel(self.layoutWidget)
        self.labelresulttotalnumber.setObjectName(u"labelresulttotalnumber")
        self.labelresulttotalnumber.setFont(font)
        self.labelresulttotalnumber.setFrameShape(QFrame.Shape.NoFrame)
        self.labelresulttotalnumber.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelresulttotalnumber, 6, 1, 1, 1)

        self.comboBoxpeople = QComboBox(self.layoutWidget)
        self.comboBoxpeople.addItem("")
        self.comboBoxpeople.addItem("")
        self.comboBoxpeople.addItem("")
        self.comboBoxpeople.addItem("")
        self.comboBoxpeople.setObjectName(u"comboBoxpeople")
        self.comboBoxpeople.setFont(font)

        self.gridLayout.addWidget(self.comboBoxpeople, 2, 1, 1, 1)

        self.doubleSpinBoxbill = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxbill.setObjectName(u"doubleSpinBoxbill")
        self.doubleSpinBoxbill.setFont(font)
        self.doubleSpinBoxbill.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.doubleSpinBoxbill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBoxbill.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBoxbill.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.doubleSpinBoxbill.setMinimum(0.010000000000000)
        self.doubleSpinBoxbill.setMaximum(1000000.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBoxbill, 0, 1, 1, 1)

        self.labelresulttotaltext = QLabel(self.layoutWidget)
        self.labelresulttotaltext.setObjectName(u"labelresulttotaltext")
        self.labelresulttotaltext.setFont(font)
        self.labelresulttotaltext.setFrameShape(QFrame.Shape.NoFrame)
        self.labelresulttotaltext.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelresulttotaltext, 6, 0, 1, 1)

        self.doubleSpinBoxtax = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxtax.setObjectName(u"doubleSpinBoxtax")
        self.doubleSpinBoxtax.setFont(font)
        self.doubleSpinBoxtax.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBoxtax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBoxtax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.gridLayout.addWidget(self.doubleSpinBoxtax, 3, 1, 1, 1)

        self.labeltip = QLabel(self.layoutWidget)
        self.labeltip.setObjectName(u"labeltip")
        self.labeltip.setFont(font)
        self.labeltip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labeltip, 1, 0, 1, 1)

        self.labelbill = QLabel(self.layoutWidget)
        self.labelbill.setObjectName(u"labelbill")
        self.labelbill.setFont(font)
        self.labelbill.setTextFormat(Qt.TextFormat.AutoText)
        self.labelbill.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelbill, 0, 0, 1, 1)

        self.pushButtonreset = QPushButton(self.layoutWidget)
        self.pushButtonreset.setObjectName(u"pushButtonreset")
        self.pushButtonreset.setFont(font)

        self.gridLayout.addWidget(self.pushButtonreset, 4, 1, 1, 1)

        self.labelresultperpersontext = QLabel(self.layoutWidget)
        self.labelresultperpersontext.setObjectName(u"labelresultperpersontext")
        self.labelresultperpersontext.setEnabled(True)
        self.labelresultperpersontext.setFont(font)
        self.labelresultperpersontext.setFrameShape(QFrame.Shape.NoFrame)
        self.labelresultperpersontext.setTextFormat(Qt.TextFormat.AutoText)
        self.labelresultperpersontext.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelresultperpersontext, 5, 0, 1, 1)

        self.labeltax = QLabel(self.layoutWidget)
        self.labeltax.setObjectName(u"labeltax")
        self.labeltax.setFont(font)
        self.labeltax.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labeltax, 3, 0, 1, 1)

        self.comboBoxtipprecent = QComboBox(self.layoutWidget)
        self.comboBoxtipprecent.addItem("")
        self.comboBoxtipprecent.addItem("")
        self.comboBoxtipprecent.addItem("")
        self.comboBoxtipprecent.setObjectName(u"comboBoxtipprecent")
        self.comboBoxtipprecent.setFont(font)
        self.comboBoxtipprecent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBoxtipprecent.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout.addWidget(self.comboBoxtipprecent, 1, 1, 1, 1)

        self.labelresultperpersonnumber = QLabel(self.layoutWidget)
        self.labelresultperpersonnumber.setObjectName(u"labelresultperpersonnumber")
        self.labelresultperpersonnumber.setFont(font)
        self.labelresultperpersonnumber.setFrameShape(QFrame.Shape.NoFrame)
        self.labelresultperpersonnumber.setTextFormat(Qt.TextFormat.AutoText)
        self.labelresultperpersonnumber.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelresultperpersonnumber, 5, 1, 1, 1)

        self.pushButtonHistory = QPushButton(self.centralwidget)
        self.pushButtonHistory.setObjectName(u"pushButtonHistory")
        self.pushButtonHistory.setGeometry(QRect(250, 480, 291, 61))
        self.pushButtonHistory.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"tip calculator", None))
        self.pushButtoncalculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.labelpeople.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0441\u0442\u0438:", None))
        self.labelresulttotalnumber.setText(QCoreApplication.translate("MainWindow", u"0,00\u0440\u0443\u0431.", None))
        self.comboBoxpeople.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBoxpeople.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBoxpeople.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBoxpeople.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.labelresulttotaltext.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430:", None))
        self.labeltip.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0435\u0432\u044b\u0435:", None))
        self.labelbill.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0441\u0447\u0435\u0442\u0430:", None))
        self.pushButtonreset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.labelresultperpersontext.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e \u043d\u0430 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430:", None))
        self.labeltax.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u043e\u0433:", None))
        self.comboBoxtipprecent.setItemText(0, QCoreApplication.translate("MainWindow", u"10%", None))
        self.comboBoxtipprecent.setItemText(1, QCoreApplication.translate("MainWindow", u"15%", None))
        self.comboBoxtipprecent.setItemText(2, QCoreApplication.translate("MainWindow", u"20%", None))

        self.comboBoxtipprecent.setCurrentText(QCoreApplication.translate("MainWindow", u"15%", None))
        self.labelresultperpersonnumber.setText(QCoreApplication.translate("MainWindow", u"0,00\u0440\u0443\u0431.", None))
        self.pushButtonHistory.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432", None))
    # retranslateUi

