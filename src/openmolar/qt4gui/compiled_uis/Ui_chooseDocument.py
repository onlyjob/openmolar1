# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/chooseDocument.ui'
#
# Created: Wed Nov  6 23:05:24 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(394, 270)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.remuneration_radioButton = QtGui.QRadioButton(self.tab)
        self.remuneration_radioButton.setChecked(True)
        self.remuneration_radioButton.setObjectName(_fromUtf8("remuneration_radioButton"))
        self.verticalLayout_2.addWidget(self.remuneration_radioButton)
        self.info_radioButton = QtGui.QRadioButton(self.tab)
        self.info_radioButton.setObjectName(_fromUtf8("info_radioButton"))
        self.verticalLayout_2.addWidget(self.info_radioButton)
        spacerItem = QtGui.QSpacerItem(128, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.remuneration2009_radioButton = QtGui.QRadioButton(self.tab_2)
        self.remuneration2009_radioButton.setChecked(True)
        self.remuneration2009_radioButton.setObjectName(_fromUtf8("remuneration2009_radioButton"))
        self.verticalLayout_3.addWidget(self.remuneration2009_radioButton)
        self.info2009_radioButton = QtGui.QRadioButton(self.tab_2)
        self.info2009_radioButton.setObjectName(_fromUtf8("info2009_radioButton"))
        self.verticalLayout_3.addWidget(self.info2009_radioButton)
        spacerItem1 = QtGui.QSpacerItem(128, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.remuneration2010_radioButton = QtGui.QRadioButton(self.tab_3)
        self.remuneration2010_radioButton.setChecked(True)
        self.remuneration2010_radioButton.setObjectName(_fromUtf8("remuneration2010_radioButton"))
        self.verticalLayout_6.addWidget(self.remuneration2010_radioButton)
        self.info2010_radioButton = QtGui.QRadioButton(self.tab_3)
        self.info2010_radioButton.setObjectName(_fromUtf8("info2010_radioButton"))
        self.verticalLayout_6.addWidget(self.info2010_radioButton)
        spacerItem2 = QtGui.QSpacerItem(128, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.remuneration2012_radioButton = QtGui.QRadioButton(self.tab_4)
        self.remuneration2012_radioButton.setChecked(True)
        self.remuneration2012_radioButton.setObjectName(_fromUtf8("remuneration2012_radioButton"))
        self.verticalLayout_8.addWidget(self.remuneration2012_radioButton)
        self.info2012_radioButton = QtGui.QRadioButton(self.tab_4)
        self.info2012_radioButton.setObjectName(_fromUtf8("info2012_radioButton"))
        self.verticalLayout_8.addWidget(self.info2012_radioButton)
        self.terms_radioButton = QtGui.QRadioButton(self.tab_4)
        self.terms_radioButton.setObjectName(_fromUtf8("terms_radioButton"))
        self.verticalLayout_8.addWidget(self.terms_radioButton)
        spacerItem3 = QtGui.QSpacerItem(128, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.remuneration2013_radioButton = QtGui.QRadioButton(self.tab_5)
        self.remuneration2013_radioButton.setChecked(True)
        self.remuneration2013_radioButton.setObjectName(_fromUtf8("remuneration2013_radioButton"))
        self.verticalLayout_4.addWidget(self.remuneration2013_radioButton)
        self.tooth_specific_radioButton = QtGui.QRadioButton(self.tab_5)
        self.tooth_specific_radioButton.setObjectName(_fromUtf8("tooth_specific_radioButton"))
        self.verticalLayout_4.addWidget(self.tooth_specific_radioButton)
        self.info2013_radioButton = QtGui.QRadioButton(self.tab_5)
        self.info2013_radioButton.setObjectName(_fromUtf8("info2013_radioButton"))
        self.verticalLayout_4.addWidget(self.info2013_radioButton)
        self.terms2013_radioButton = QtGui.QRadioButton(self.tab_5)
        self.terms2013_radioButton.setObjectName(_fromUtf8("terms2013_radioButton"))
        self.verticalLayout_4.addWidget(self.terms2013_radioButton)
        spacerItem4 = QtGui.QSpacerItem(128, 63, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.terms_buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.terms_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.terms_buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.terms_buttonBox.setObjectName(_fromUtf8("terms_buttonBox"))
        self.verticalLayout.addWidget(self.terms_buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QObject.connect(self.terms_buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.terms_buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Choose a Document"))
        self.remuneration_radioButton.setText(_("NHS Schedule of Remuneration April 2008"))
        self.info_radioButton.setText(_("NHS \"Information Guide\" 2008"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("2008"))
        self.remuneration2009_radioButton.setText(_("NHS Schedule of Remuneration"))
        self.info2009_radioButton.setText(_("NHS \"Information Guide\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("2009"))
        self.remuneration2010_radioButton.setText(_("NHS Schedule of Remuneration"))
        self.info2010_radioButton.setText(_("NHS \"Information Guide\""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("2010"))
        self.remuneration2012_radioButton.setText(_("NHS Schedule of Remuneration"))
        self.info2012_radioButton.setText(_("NHS \"Information Guide\""))
        self.terms_radioButton.setText(_("NHS terms and conditions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _("2012"))
        self.remuneration2013_radioButton.setText(_("NHS Schedule of Remuneration"))
        self.tooth_specific_radioButton.setText(_("Tooth Specific Guidance"))
        self.info2013_radioButton.setText(_("NHS \"Information Guide\""))
        self.terms2013_radioButton.setText(_("NHS terms and conditions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _("2013"))
        self.label.setText(_("Choose a document to view"))


if __name__ == "__main__":
    import gettext
    gettext.install("openmolar")
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

