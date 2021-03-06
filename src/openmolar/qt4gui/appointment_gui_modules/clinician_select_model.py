#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
##                                                                           ##
##  Copyright 2011-2012,  Neil Wallace <neil@openmolar.com>                  ##
##                                                                           ##
##  This program is free software: you can redistribute it and/or modify     ##
##  it under the terms of the GNU General Public License as published by     ##
##  the Free Software Foundation, either version 3 of the License, or        ##
##  (at your option) any later version.                                      ##
##                                                                           ##
##  This program is distributed in the hope that it will be useful,          ##
##  but WITHOUT ANY WARRANTY; without even the implied warranty of           ##
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            ##
##  GNU General Public License for more details.                             ##
##                                                                           ##
##  You should have received a copy of the GNU General Public License        ##
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.    ##
##                                                                           ##
###############################################################################

from PyQt4 import QtGui, QtCore
from openmolar.dbtools import appointments
from openmolar.settings import localsettings

class ClinicianSelectModel(QtCore.QAbstractListModel):
    '''
    A simple model used to populate a combobox to select how the
    appointment books are managed.
    '''
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)

        self.options_list = [
            _("Available Clinicians"),
            _("Available Dentists"),
            _("Available Hygenists"),
            _("All")
            ]

        self.om_gui = parent
        #if localsettings.activehygs == []:
        #    self.options_list.remove(_("Available Hygenists"))

        self.manual_index = 5 #used if manual is called by another widget

    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.options_list)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole:
            option = self.options_list[index.row()]
            return QtCore.QVariant(option)
        return QtCore.QVariant()

    @property
    def all_clinicians(self):
        '''
        returns a numeric version of
        localsettings.activedents + localsettings.activehygs
        '''
        retlist = []
        for dent in localsettings.activedents + localsettings.activehygs:
            retlist.append(localsettings.apptix.get(dent))
        return tuple(retlist)

    def clinician_list(self, row, date):
        '''
        returns a tuple of values showing who is working.
        '''
        if row == 0:
            return appointments.getWorkingDents(date,
                include_non_working=False)
        elif row == 1:
            chkset = localsettings.activedent_ixs
            return appointments.getWorkingDents(date, chkset,
                include_non_working=False)
        elif row == 2:
            chkset = localsettings.activehyg_ixs
            return appointments.getWorkingDents(date, chkset,
                include_non_working=False)

        return appointments.getAllClinicians(date)


if __name__ == "__main__":

    def but_clicked():
        message = ""
        for d_day in model.clinician_list(
            cb.currentIndex(), cal.date().toPyDate()):
            message += "%s <br />"% d_day
        QtGui.QMessageBox.information(mw, "result", message)

    localsettings.initiate()
    app = QtGui.QApplication([])

    model = ClinicianSelectModel()

    mw = QtGui.QMainWindow()
    frame = QtGui.QWidget()
    cb = QtGui.QComboBox()
    cb.setModel(model)
    cal = QtGui.QDateEdit()
    cal.setDate(QtCore.QDate(2013, 2, 1))
    button = QtGui.QPushButton("who's chosen?")
    button.clicked.connect(but_clicked)

    layout = QtGui.QVBoxLayout(frame)
    layout.addWidget(cb)
    layout.addWidget(cal)
    layout.addWidget(button)

    mw.setCentralWidget(frame)
    mw.show()
    app.exec_()
