# -*- coding: utf-8 -*-

"""VerticalSpeed_Indicator Indicator"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


## Main Dial
class VerticalSpeed_Indicator(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QGridLayout()
        self.setLayout( layout )

        #self.setStyleSheet("border: 1px outset #efefef; background-color: black;")
        self.setTitle("Vertical Speed")
        #self.label = QtWidgetsQLabel("Vertical Speed")
        #layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.speedDial = QtWidgets.QDial()
        self.speedDial.setMinimum( 0)
        self.speedDial.setMaximum( 360 )
        self.speedDial.setValue( 270 )
        self.speedDial.setNotchesVisible(True)
        self.speedDial.setSingleStep(10)
        self.speedDial.setWrapping(True)
        layout.addWidget( self.speedDial, 1, 0, QtCore.Qt.AlignCenter )

        self.labelSpeed = QtWidgets.QLabel("170")
        layout.addWidget( self.labelSpeed, 2, 0, QtCore.Qt.AlignCenter )


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  VerticalSpeed_Indicator()
    widget.show()

    sys.exit(app.exec_())