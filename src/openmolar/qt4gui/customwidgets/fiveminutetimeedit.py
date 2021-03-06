# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License for
# more details.


from PyQt4 import QtGui, QtCore

class FiveMinuteTimeEdit(QtGui.QTimeEdit):
    '''
    A custom timeEdit which enforces only 5 minutes
    NB - connect to slot "verifiedTime"
    '''
    def __init__(self,parent=None):
        super(FiveMinuteTimeEdit, self).__init__(parent)
        self.setDisplayFormat("hh:mm")
        QtCore.QObject.connect(self, 
        QtCore.SIGNAL("timeChanged (const QTime&)"), self.timeChanged)

    def stepBy(self, steps):
        if self.currentSection() == self.MinuteSection:
            QtGui.QTimeEdit.stepBy(self, steps * 5)
        else:
            QtGui.QTimeEdit.stepBy(self, steps)
        
    def timeChanged(self, t):
        min = self.time().minute()
        if min % 5 != 0:
            min -= min % 5 
            self.setTime(QtCore.QTime(self.time().hour(), min))
        self.emit(QtCore.SIGNAL("verifiedTime"), self.time())
        
if __name__ == "__main__":
    def test(t):
        print "signal received", t
    
    import sys
    app = QtGui.QApplication([])
    te = FiveMinuteTimeEdit()
    QtCore.QObject.connect(te,
    QtCore.SIGNAL("verifiedTime"), test)
    te.show()
    sys.exit(app.exec_())