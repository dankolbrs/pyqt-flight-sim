# -*- coding: utf-8 -*-

"""Turn_Bank Indicator"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


## Main Dial
class ControlSurfaces(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setMinimumHeight(200)

        self.setTitle("Control Surfaces")

        
        gridLayout = QtWidgets.QGridLayout()
        #gridLayout.setColumnStretch(1, 2)
        #gridLayout.setColumnStretch(2, 2)
        #gridLayout.setColumnStretch(3, 2)
        #gridLayout.setColumnStretch(4, 2)
        self.setLayout( gridLayout )

        #self.setStyleSheet("background-color: black; QSplitter::groove { color: red;}")

        row = 0
        gridLayout.addWidget(QtWidgets.QLabel("Left"), row, 0, QtCore.Qt.AlignCenter)
        gridLayout.addWidget(QtWidgets.QLabel("Elevator"), row, 1, QtCore.Qt.AlignCenter)
        gridLayout.addWidget(QtWidgets.QLabel("Right"), row, 2, QtCore.Qt.AlignCenter)

        row += 1
        self.elevator = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.elevator.setMinimum(-100)
        self.elevator.setMaximum(100)
        self.elevator.setValue(0)
        self.elevator.setTickInterval( 10 )
        self.elevator.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        #self.elevator.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.elevator, row, 1, QtCore.Qt.AlignCenter)

        self.leftAileron = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.leftAileron.setMinimum(-100)
        self.leftAileron.setMaximum(100)
        self.leftAileron.setValue(0)
        self.leftAileron.setTickInterval( 5 )
        self.leftAileron.setTickPosition(QtWidgets.QSlider.TicksLeft)
        #self.leftAileron.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.leftAileron,row, 0, 2, 1)


        self.rightAileron = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.rightAileron.setMinimum(-100)
        self.rightAileron.setMaximum(100)
        self.rightAileron.setValue(0)
        self.rightAileron.setTickInterval( 5 )
        self.rightAileron.setTickPosition(QtWidgets.QSlider.TicksRight)
        #self.rightAileron.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.rightAileron, row, 2, 2, 1)

        row += 2
        self.rudder = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.rudder.setMinimum(0)
        self.rudder.setMaximum(2)
        self.rudder.setValue(1)
        self.rudder.setTickInterval( 1 )
        self.rudder.setTickPosition(QtWidgets.QSlider.TicksBelow)
        #self.rudder.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.rudder, row, 1, 1, 1)


    def update(self, angle):
        print("bank update", float(angle) * 100)
        self.headingDial.setValue( float(angle) * 100 )

    def on_change(self, newVal):
        self.label.setText("%s" % newVal)

    def set_aileron(self, val):
        no = float(val) * 100
        self.leftAileron.setValue( no )
        self.rightAileron.setValue( no * -1 )

    def set_elevator(self, val):
        no = float(val) * 100
        self.elevator.setValue( no )

    def set_rudder(self, val):
        no = float(val) * 100
        self.rudder.setValue( no )

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget = Turn_Bank_Indicator()
    widget.show()

    sys.exit(app.exec_())