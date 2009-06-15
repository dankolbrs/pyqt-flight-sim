# -*- coding: utf-8 -*-

"""Basic_T displayr"""

import sys
from PyQt4 import QtCore, QtGui

from Airspeed_Indicator import Airspeed_Indicator
from Attitude_Indicator import Attitude_Indicator
from Altimeter_Indicator import Altimeter_Indicator

from Turn_Bank_Indicator import Turn_Bank_Indicator
from Heading_Indicator import Heading_Indicator
from VerticalSpeed_Indicator import VerticalSpeed_Indicator

## Main Dial
class Basic_T(QtGui.QWidget):

    def __init__(self,  parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setObjectName("InstrumentPanel")

        gridLayout = QtGui.QGridLayout()
        self.setLayout( gridLayout )

        gridLayout.setColumnStretch(0, 3)
        gridLayout.setColumnStretch(1, 5)
        gridLayout.setColumnStretch(2, 1)

        self.airspeedIndicator = Airspeed_Indicator()
        gridLayout.addWidget( self.airspeedIndicator, 0, 0 )

        self.attitudeIndicator = Attitude_Indicator()
        gridLayout.addWidget( self.attitudeIndicator, 0, 1 )

        self.altimeterIndicator= Altimeter_Indicator()
        gridLayout.addWidget( self.altimeterIndicator, 0, 2 )


        self.turnBankIndicator = Turn_Bank_Indicator()
        gridLayout.addWidget( self.turnBankIndicator, 1, 0 )

        self.headingIndicator = Heading_Indicator()
        gridLayout.addWidget( self.headingIndicator, 1, 1 )

        self.verticalSpeedIndicator = VerticalSpeed_Indicator()
        gridLayout.addWidget( self.verticalSpeedIndicator, 1, 2 )


if __name__ == '__main__':

    styleSheetString = open('style/cockpit.txt').read()
    #print styleSheetString
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet( styleSheetString )

    widget =  Basic_T()
    widget.show()

    sys.exit(app.exec_())