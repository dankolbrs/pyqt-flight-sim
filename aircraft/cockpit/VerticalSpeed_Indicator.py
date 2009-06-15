# -*- coding: utf-8 -*-

"""VerticalSpeed_Indicator Indicator"""

import sys
from PyQt4 import QtCore, QtGui


## Main Dial
class VerticalSpeed_Indicator(QtGui.QWidget):

    def __init__(self,  parent=None):
        QtGui.QWidget.__init__(self, parent)

        layout = QtGui.QGridLayout()
        self.setLayout( layout )


        self.label = QtGui.QLabel("Vertical Speed")
        layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.speedDial = QtGui.QDial()
        self.speedDial.setMinimum( 0)
        self.speedDial.setMaximum( 360 )
        self.speedDial.setValue( 270 )
        self.speedDial.setNotchesVisible(True)
        self.speedDial.setSingleStep(10)
        self.speedDial.setWrapping(True)
        layout.addWidget( self.speedDial, 1, 0, QtCore.Qt.AlignCenter )

        self.labelSpeed = QtGui.QLabel("170")
        layout.addWidget( self.labelSpeed, 2, 0, QtCore.Qt.AlignCenter )


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    widget =  VerticalSpeed_Indicator()
    widget.show()

    sys.exit(app.exec_())