# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(627, 437)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(120, 90, 391, 231))
        font = QFont()
        font.setPointSize(18)
        self.gridLayoutWidget.setFont(font)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(39)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.player_name_line_edit = QLineEdit(self.gridLayoutWidget)
        self.player_name_line_edit.setObjectName(u"player_name_line_edit")
        self.player_name_line_edit.setFont(font)

        self.gridLayout.addWidget(self.player_name_line_edit, 0, 1, 1, 1)

        self.player_name_label = QLabel(self.gridLayoutWidget)
        self.player_name_label.setObjectName(u"player_name_label")
        self.player_name_label.setFont(font)

        self.gridLayout.addWidget(self.player_name_label, 0, 0, 1, 1)

        self.difficulty_label = QLabel(self.gridLayoutWidget)
        self.difficulty_label.setObjectName(u"difficulty_label")

        self.gridLayout.addWidget(self.difficulty_label, 1, 0, 1, 1)

        self.difficulty_combo_box = QComboBox(self.gridLayoutWidget)
        self.difficulty_combo_box.addItem("")
        self.difficulty_combo_box.addItem("")
        self.difficulty_combo_box.addItem("")
        self.difficulty_combo_box.addItem("")
        self.difficulty_combo_box.setObjectName(u"difficulty_combo_box")

        self.gridLayout.addWidget(self.difficulty_combo_box, 1, 1, 1, 1)

        self.language_label = QLabel(self.gridLayoutWidget)
        self.language_label.setObjectName(u"language_label")

        self.gridLayout.addWidget(self.language_label, 2, 0, 1, 1)

        self.language_combo_box = QComboBox(self.gridLayoutWidget)
        self.language_combo_box.addItem("")
        self.language_combo_box.addItem("")
        self.language_combo_box.setObjectName(u"language_combo_box")

        self.gridLayout.addWidget(self.language_combo_box, 2, 1, 1, 1)

        self.title_label = QLabel(Widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(20, 10, 621, 61))
        font1 = QFont()
        font1.setPointSize(28)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 350, 141, 61))
        font2 = QFont()
        font2.setPointSize(23)
        font2.setBold(False)
        self.pushButton.setFont(font2)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.player_name_label.setText(QCoreApplication.translate("Widget", u"Nom du Joueur", None))
        self.difficulty_label.setText(QCoreApplication.translate("Widget", u"Difficult\u00e9", None))
        self.difficulty_combo_box.setItemText(0, QCoreApplication.translate("Widget", u"Facile", None))
        self.difficulty_combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Normal", None))
        self.difficulty_combo_box.setItemText(2, QCoreApplication.translate("Widget", u"Difficile", None))
        self.difficulty_combo_box.setItemText(3, QCoreApplication.translate("Widget", u"Inf\u00e2me", None))

        self.language_label.setText(QCoreApplication.translate("Widget", u"Language", None))
        self.language_combo_box.setItemText(0, QCoreApplication.translate("Widget", u"Fran\u00e7ais", None))
        self.language_combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Anglais", None))

        self.title_label.setText(QCoreApplication.translate("Widget", u"PARAM\u00c8TRES DE LA PARTIE", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Lancer", None))
    # retranslateUi

