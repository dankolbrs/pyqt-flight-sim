# -*- coding: utf-8 -*-

"""Turn_Bank Indicator"""

import sys
from PyQt4 import QtCore, QtGui


## Main Dial
class Turn_Bank_Indicator(QtGui.QGroupBox):

    def __init__(self,  parent=None):
        QtGui.QWidget.__init__(self, parent)

        layout = QtGui.QGridLayout()
        self.setLayout( layout )

        self.setTitle("Bank")
        #self.label = QtGui.QLabel("Bank")
        #layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.headingDial = QtGui.QDial()
        self.headingDial.setMinimum( 0)
        self.headingDial.setMaximum( 180 )
        self.headingDial.setValue( 100 )
        self.headingDial.setNotchesVisible(True)
        self.headingDial.setSingleStep(20)
        self.headingDial.setWrapping(True)
        layout.addWidget( self.headingDial, 1, 0, QtCore.Qt.AlignCenter )



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    widget =  Turn_Bank_Indicator()
    widget.show()

    sys.exit(app.exec_())