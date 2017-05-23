# -*- coding: utf-8 -*-

"""Airspeed Indicator"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


## Main Dial
class Compass_Indicator(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QGridLayout()
        self.setLayout( layout )


        self.label = QtWidgets.QLabel("Compass")
        self.setTitle("Compass")
        layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.compassDial = QtWidgets.QDial()
        self.compassDial.setMinimum( 0)
        self.compassDial.setMaximum( 360 )
        self.compassDial.setValue( 220 )
        self.compassDial.setNotchesVisible(True)
        self.compassDial.setSingleStep(20)
        self.compassDial.setWrapping(True)
        layout.addWidget( self.compassDial, 1, 0, QtCore.Qt.AlignCenter )

        self.labelSpeed = QtWidgets.QLabel("170")
        layout.addWidget( self.labelSpeed, 2, 0, QtCore.Qt.AlignCenter )


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  Compass_Indicator()
    widget.show()

    sys.exit(app.exec_())