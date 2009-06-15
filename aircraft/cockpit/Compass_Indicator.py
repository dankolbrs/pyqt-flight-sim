# -*- coding: utf-8 -*-

"""Airspeed Indicator"""

import sys
from PyQt4 import QtCore, QtGui


## Main Dial
class Compass_Indicator(QtGui.QWidget):

    def __init__(self,  parent=None):
        QtGui.QWidget.__init__(self, parent)

        layout = QtGui.QGridLayout()
        self.setLayout( layout )


        self.label = QtGui.QLabel("Compass")
        layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.compassDial = QtGui.QDial()
        self.compassDial.setMinimum( 0)
        self.compassDial.setMaximum( 360 )
        self.compassDial.setValue( 220 )
        self.compassDial.setNotchesVisible(True)
        self.compassDial.setSingleStep(20)
        self.compassDial.setWrapping(True)
        layout.addWidget( self.compassDial, 1, 0, QtCore.Qt.AlignCenter )

        self.labelSpeed = QtGui.QLabel("170")
        layout.addWidget( self.labelSpeed, 2, 0, QtCore.Qt.AlignCenter )


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    widget =  Compass_Indicator()
    widget.show()

    sys.exit(app.exec_())