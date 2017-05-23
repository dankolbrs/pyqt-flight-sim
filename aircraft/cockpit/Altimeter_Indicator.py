# -*- coding: utf-8 -*-

"""Altimeter Indicator"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


## Main Dial
class Altimeter_Indicator(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QGridLayout()
        self.setLayout( layout )

        self.setTitle("Altimeter")
        #self.label = QtWidgets.QLabel("Altimeter")
        #layout.addWidget( self.label, 0, 0, 1, 3, QtCore.Qt.AlignCenter )
        self.setFixedWidth(200)


        self.mainDial = QtWidgets.QDial()
        self.mainDial.setMinimum( 0)
        self.mainDial.setMaximum( 300 )
        self.mainDial.setValue( 170 )
        self.mainDial.setNotchesVisible(True)
        self.mainDial.setSingleStep(10)
        self.mainDial.setWrapping(False)
        #self.mainDial.setFixedSize( 200, 200)
        layout.addWidget( self.mainDial, 1, 0, 1, 2, QtCore.Qt.AlignCenter )

        self.sideLabel = QtWidgets.QLabel("220")
        self.sideLabel.setStyleSheet("border: 1px solid white; background-color: black; color: white")
        layout.addWidget( self.sideLabel, 1, 2, 1, 1, QtCore.Qt.AlignLeft )

        self.calKnob = QtWidgets.QDial()
        self.calKnob.setFixedSize( 50, 50)
        layout.addWidget( self.calKnob, 2, 0, QtCore.Qt.AlignLeft )


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  Altimeter_Indicator()
    widget.show()

    sys.exit(app.exec_())