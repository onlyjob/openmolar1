#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/record_tools.ui'
#
# Created: Mon Jun 30 12:44:27 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(497, 585)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.money_scrollArea = QtGui.QScrollArea(self.tab)
        self.money_scrollArea.setWidgetResizable(True)
        self.money_scrollArea.setObjectName(_fromUtf8("money_scrollArea"))
        self.money_scrollAreaWidgetContents = QtGui.QWidget()
        self.money_scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 455, 503))
        self.money_scrollAreaWidgetContents.setObjectName(
            _fromUtf8("money_scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(
            self.money_scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.money0_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money0_spinBox.setMaximum(1000000)
        self.money0_spinBox.setObjectName(_fromUtf8("money0_spinBox"))
        self.gridLayout.addWidget(self.money0_spinBox, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.money2_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money2_spinBox.setMaximum(1000000)
        self.money2_spinBox.setObjectName(_fromUtf8("money2_spinBox"))
        self.gridLayout.addWidget(self.money2_spinBox, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.money4_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money4_spinBox.setMaximum(1000000)
        self.money4_spinBox.setObjectName(_fromUtf8("money4_spinBox"))
        self.gridLayout.addWidget(self.money4_spinBox, 7, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.money5_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money5_spinBox.setMaximum(1000000)
        self.money5_spinBox.setObjectName(_fromUtf8("money5_spinBox"))
        self.gridLayout.addWidget(self.money5_spinBox, 8, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.money6_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money6_spinBox.setMaximum(1000000)
        self.money6_spinBox.setObjectName(_fromUtf8("money6_spinBox"))
        self.gridLayout.addWidget(self.money6_spinBox, 9, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.money7_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money7_spinBox.setMaximum(1000000)
        self.money7_spinBox.setObjectName(_fromUtf8("money7_spinBox"))
        self.gridLayout.addWidget(self.money7_spinBox, 10, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.money8_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money8_spinBox.setMaximum(1000000)
        self.money8_spinBox.setObjectName(_fromUtf8("money8_spinBox"))
        self.gridLayout.addWidget(self.money8_spinBox, 11, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.money9_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money9_spinBox.setMaximum(1000000)
        self.money9_spinBox.setObjectName(_fromUtf8("money9_spinBox"))
        self.gridLayout.addWidget(self.money9_spinBox, 12, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 13, 0, 1, 1)
        self.money10_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money10_spinBox.setMaximum(1000000)
        self.money10_spinBox.setObjectName(_fromUtf8("money10_spinBox"))
        self.gridLayout.addWidget(self.money10_spinBox, 13, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 14, 0, 1, 1)
        self.money11_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money11_spinBox.setMaximum(1000000)
        self.money11_spinBox.setObjectName(_fromUtf8("money11_spinBox"))
        self.gridLayout.addWidget(self.money11_spinBox, 14, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.money1_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money1_spinBox.setMaximum(1000000)
        self.money1_spinBox.setObjectName(_fromUtf8("money1_spinBox"))
        self.gridLayout.addWidget(self.money1_spinBox, 3, 1, 1, 1)
        self.money3_spinBox = QtGui.QSpinBox(
            self.money_scrollAreaWidgetContents)
        self.money3_spinBox.setMaximum(1000000)
        self.money3_spinBox.setObjectName(_fromUtf8("money3_spinBox"))
        self.gridLayout.addWidget(self.money3_spinBox, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(
            20,
            40,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 2)
        self.label_14 = QtGui.QLabel(self.money_scrollAreaWidgetContents)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 2)
        self.money_scrollArea.setWidget(self.money_scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.money_scrollArea, 0, 0, 1, 2)
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.total_label = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.total_label.setFont(font)
        self.total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_label.setObjectName(_fromUtf8("total_label"))
        self.gridLayout_2.addWidget(self.total_label, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 455, 520))
        self.scrollAreaWidgetContents.setObjectName(
            _fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pd5_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.pd5_dateEdit.setCalendarPopup(True)
        self.pd5_dateEdit.setObjectName(_fromUtf8("pd5_dateEdit"))
        self.horizontalLayout.addWidget(self.pd5_dateEdit)
        self.pd5_pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pd5_pushButton.setObjectName(_fromUtf8("pd5_pushButton"))
        self.horizontalLayout.addWidget(self.pd5_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pd6_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.pd6_dateEdit.setCalendarPopup(True)
        self.pd6_dateEdit.setObjectName(_fromUtf8("pd6_dateEdit"))
        self.horizontalLayout_2.addWidget(self.pd6_dateEdit)
        self.pd6_pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pd6_pushButton.setObjectName(_fromUtf8("pd6_pushButton"))
        self.horizontalLayout_2.addWidget(self.pd6_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pd7_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.pd7_dateEdit.setCalendarPopup(True)
        self.pd7_dateEdit.setObjectName(_fromUtf8("pd7_dateEdit"))
        self.horizontalLayout_3.addWidget(self.pd7_dateEdit)
        self.pd7_pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pd7_pushButton.setObjectName(_fromUtf8("pd7_pushButton"))
        self.horizontalLayout_3.addWidget(self.pd7_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pd8_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.pd8_dateEdit.setCalendarPopup(True)
        self.pd8_dateEdit.setObjectName(_fromUtf8("pd8_dateEdit"))
        self.horizontalLayout_4.addWidget(self.pd8_dateEdit)
        self.pd8_pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pd8_pushButton.setObjectName(_fromUtf8("pd8_pushButton"))
        self.horizontalLayout_4.addWidget(self.pd8_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pd9_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.pd9_dateEdit.setCalendarPopup(True)
        self.pd9_dateEdit.setObjectName(_fromUtf8("pd9_dateEdit"))
        self.horizontalLayout_5.addWidget(self.pd9_dateEdit)
        self.pd9_pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pd9_pushButton.setObjectName(_fromUtf8("pd9_pushButton"))
        self.horizontalLayout_5.addWidget(self.pd9_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pd10_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.pd10_dateEdit.setCalendarPopup(True)
        self.pd10_dateEdit.setObjectName(_fromUtf8("pd10_dateEdit"))
        self.horizontalLayout_6.addWidget(self.pd10_dateEdit)
        self.pd10_pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pd10_pushButton.setObjectName(_fromUtf8("pd10_pushButton"))
        self.horizontalLayout_6.addWidget(self.pd10_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 6, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.billdate_dateEdit = QtGui.QDateEdit(self.scrollAreaWidgetContents)
        self.billdate_dateEdit.setCalendarPopup(True)
        self.billdate_dateEdit.setObjectName(_fromUtf8("billdate_dateEdit"))
        self.horizontalLayout_7.addWidget(self.billdate_dateEdit)
        self.billdate_pushButton = QtGui.QPushButton(
            self.scrollAreaWidgetContents)
        self.billdate_pushButton.setObjectName(
            _fromUtf8("billdate_pushButton"))
        self.horizontalLayout_7.addWidget(self.billdate_pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 6, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(
            20,
            40,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 7, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_26 = QtGui.QLabel(self.tab_5)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout_4.addWidget(self.label_26)
        self.hidden_notes_tableWidget = QtGui.QTableWidget(self.tab_5)
        self.hidden_notes_tableWidget.setObjectName(
            _fromUtf8("hidden_notes_tableWidget"))
        self.hidden_notes_tableWidget.setColumnCount(0)
        self.hidden_notes_tableWidget.setRowCount(0)
        self.hidden_notes_tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.hidden_notes_tableWidget)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("NHS current fees (money0)"))
        self.label_2.setText(_("NHS payments (money2)"))
        self.label_5.setText(_("NHS estimated (money4)"))
        self.label_6.setText(_("private estimate (money5)"))
        self.label_7.setText(
            _("Exempt - nhs gross - completed treatment (money6)"))
        self.label_8.setText(
            _("Exempt - NHS gross - estimated current (money7)"))
        self.label_9.setText(_("credit (money8)"))
        self.label_10.setText(_("debt (money9)"))
        self.label_11.setText(_("debt2 (money10)"))
        self.label_12.setText(_("money 11"))
        self.label_3.setText(_("private current fees (money1) "))
        self.label_4.setText(_("private payments (money3)"))
        self.label_14.setText(_("ALL AMOUNTS ARE IN PENCE (cents)"))
        self.label_13.setText(_("Outstanding amount"))
        self.total_label.setText(_("0.00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("Money"))
        self.label_15.setText(_("Last CE (pd5)"))
        self.pd5_pushButton.setText(_("Add Date"))
        self.label_16.setText(_("Last ECE (pd6)"))
        self.pd6_pushButton.setText(_("Add Date"))
        self.label_17.setText(_("Last FCA (pd7)"))
        self.pd7_pushButton.setText(_("Add Date"))
        self.label_18.setText(_("Last OPT (pd8)"))
        self.pd8_pushButton.setText(_("Add Date"))
        self.label_19.setText(_("Last intraoral Xrays (pd9)"))
        self.pd9_pushButton.setText(_("Add Date"))
        self.label_20.setText(_("Last SP (pd10)"))
        self.pd10_pushButton.setText(_("Add Date"))
        self.label_21.setText(_("Last Account sent (billdate)"))
        self.billdate_pushButton.setText(_("Add Date"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            _("Dates"))
        self.label_26.setText(_("Hidden Notes"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            _("Miscellaneous"))


if __name__ == "__main__":
    import gettext
    gettext.install("openmolar")
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
