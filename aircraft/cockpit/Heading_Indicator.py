# -*- coding: utf-8 -*-

"""Heading Indicator"""

import sys
from PyQt5 import QtCore, QtWidgets


## Main Dial
class Heading_Indicator(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QGridLayout()
        self.setLayout( layout )

        self.setTitle("Heading")
        #self.label = QtWidgetsQLabel("Heading")
        #layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.headingDial = QtWidgets.QDial()
        self.headingDial.setMinimum( 0)
        self.headingDial.setMaximum( 359 )
        self.headingDial.setValue( 200 )
        self.headingDial.setNotchesVisible(True)
        self.headingDial.setSingleStep(20)
        self.headingDial.setWrapping(True)
        layout.addWidget( self.headingDial, 1, 0, QtCore.Qt.AlignCenter )



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  Heading_Indicator()
    widget.show()

    sys.exit(app.exec_())