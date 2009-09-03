# -*- coding: utf-8 -*-

"""Airspeed Indicator"""

import sys
from PyQt4 import QtCore, QtGui


## Main Dial
class Airspeed_Indicator(QtGui.QGroupBox):

	def __init__(self,  parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.debug = True

		layout = QtGui.QGridLayout()
		self.setLayout( layout )

		self.setTitle("Airspeed")

		#self.label = QtGui.QLabel("Airspeed")
		#layout.addWidget( self.label, 0, 0, QtCore.Qt.AlignCenter )
		self.setFixedWidth(200)


		self.labelSpeed = QtGui.QLabel("170")
		self.labelSpeed.setStyleSheet("border: 2px solid #999999; color: magenta; padding: 3px; font-weight: bold; margin: 5px;")
		self.labelSpeed.setFixedWidth( 60 )
		self.labelSpeed.setAlignment(QtCore.Qt.AlignCenter)
		layout.addWidget( self.labelSpeed, 0, 2, 1, 1, QtCore.Qt.AlignCenter )

		self.speedDial = QtGui.QDial()
		self.speedDial.setMinimum( 0)
		self.speedDial.setMaximum( 500 )
		self.speedDial.setValue( 170 )
		self.speedDial.setNotchesVisible(True)
		self.speedDial.setSingleStep(50)
		self.speedDial.setWrapping(False)
		#self.speedDial.setFixedWidth( 220 )
		self.connect(self.speedDial, QtCore.SIGNAL("valueChanged(int)"), self.on_speed_change)
		layout.addWidget( self.speedDial, 1, 0, 1, 3, QtCore.Qt.AlignCenter )

		sty = "color: white;"
		self.labelMin = QtGui.QLabel( str(self.speedDial.minimum()) )
		self.labelMin.setStyleSheet( sty )
		self.labelMax = QtGui.QLabel( str(self.speedDial.maximum()) )
		self.labelMax.setStyleSheet( sty )

		layout.addWidget( self.labelMin, 2, 0, QtCore.Qt.AlignRight )
		layout.addWidget( self.labelMax, 2, 2, QtCore.Qt.AlignLeft )

		#layout.addWidget ( QtGui.QSpacerItem(), 2, 0 )
		#layout.setRowStretch(3, 10 )
		self.chkSpeedAutopilotRequestActive = QtGui.QCheckBox("Switch", self)
		layout.addWidget( self.chkSpeedAutopilotRequestActive, 3, 1, 1, 2)

		self.chkSpeedAutopilotActive = QtGui.QCheckBox("Speed Active", self)
		layout.addWidget( self.chkSpeedAutopilotActive, 3, 3, 1, 2)


	def update_speed(self, knots):
		if self.debug:
			print "airspeed update", knots
		#self.speedDial.setValue( int(knots) )

	def update_autopilot(self, state):
		if self.debug:
			print "airspeed autopilot update", state, bool(state), state == "1"
		self.chkSpeedAutopilotActive.setChecked( state == "1" )

	def on_speed_change(self, newVal):
		self.labelSpeed.setText( str(newVal) )

if __name__ == '__main__':

	app = QtGui.QApplication(sys.argv)

	widget =  Airspeed_Indicator()
	widget.show()

	sys.exit(app.exec_())