# -*- coding: utf-8 -*-

"""Heading Indicator"""

import sys
from PyQt4 import QtCore, QtGui


## Main Dial
class Heading_Indicator(QtGui.QGroupBox):

    def __init__(self,  parent=None):
        QtGui.QWidget.__init__(self, parent)

        layout = QtGui.QGridLayout()
        self.setLayout( layout )

        self.setTitle("Heading")
        #self.label = QtGui.QLabel("Heading")
        #layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.headingDial = QtGui.QDial()
        self.headingDial.setMinimum( 0)
        self.headingDial.setMaximum( 360 )
        self.headingDial.setValue( 200 )
        self.headingDial.setNotchesVisible(True)
        self.headingDial.setSingleStep(20)
        self.headingDial.setWrapping(True)
        layout.addWidget( self.headingDial, 1, 0, QtCore.Qt.AlignCenter )



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    widget =  Heading_Indicator()
    widget.show()

    sys.exit(app.exec_())