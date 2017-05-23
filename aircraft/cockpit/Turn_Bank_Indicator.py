# -*- coding: utf-8 -*-

"""Turn_Bank Indicator"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


## Main Dial
class Turn_Bank_Indicator(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QGridLayout()
        self.setLayout( layout )

        self.setTitle("Bank")
        self.label = QtWidgets.QLabel("Bank")
        self.label.setStyleSheet("border: 2px solid #999999; color: magenta; padding: 3px; font-weight: bold; margin: 5px;")
        layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )



        self.headingDial = QtWidgets.QDial()
        self.headingDial.setMinimum( -900)
        self.headingDial.setMaximum( 900 )
        self.headingDial.setValue( 0 )
        self.headingDial.setNotchesVisible(True)
        self.headingDial.setSingleStep(20)
        self.headingDial.setWrapping(True)
        layout.addWidget( self.headingDial, 1, 0, QtCore.Qt.AlignCenter )
        #self.connect(self.headingDial, QtCore.SIGNAL("valueChanged(int)"), self.on_change)

    def update(self, angle):
        print("bank update", float(angle) * 100)
        self.headingDial.setValue( float(angle) * 100 )

    def on_change(self, newVal):
    
        self.label.setText("%s" % newVal)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  Turn_Bank_Indicator()
    widget.show()

    sys.exit(app.exec_())