# -*- coding: utf-8 -*-

"""Turn_Bank Indicator"""

import sys
from PyQt4 import QtCore, QtGui


## Main Dial
class Engines(QtGui.QGroupBox):

	def __init__(self,  parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.setMinimumHeight(200)

		self.setTitle("Engines")

		
		gridLayout = QtGui.QGridLayout()
		#gridLayout.setColumnStretch(1, 2)
		#gridLayout.setColumnStretch(2, 2)
		#gridLayout.setColumnStretch(3, 2)
		#gridLayout.setColumnStretch(4, 2)
		self.setLayout( gridLayout )

		#self.setStyleSheet("background-color: black; QSplitter::groove { color: red;}")

		row = 0
		gridLayout.addWidget(QtGui.QLabel("Throttle"), row, 0, QtCore.Qt.AlignCenter)
		#gridLayout.addWidget(QtGui.QLabel("Elevator"), row, 1, QtCore.Qt.AlignCenter)
		#gridLayout.addWidget(QtGui.QLabel("Right"), row, 2, QtCore.Qt.AlignCenter)

		row += 1
		self.throttle = QtGui.QSlider(QtCore.Qt.Vertical, self)
		self.throttle.setMinimum(0)
		self.throttle.setMaximum(100)
		self.throttle.setValue(0)
		self.throttle.setTickInterval( 10 )
		self.throttle.setTickPosition(QtGui.QSlider.TicksBothSides)
		#self.throttle.setStyleSheet("background-color: #bbbbbb")
		gridLayout.addWidget(self.throttle, row, 1, QtCore.Qt.AlignCenter)
		self.connect(self.throttle, QtCore.SIGNAL("valueChanged(int)"), self.on_throttle_change)

		row += 1
		self.throttleLabel = QtGui.QLabel("0 %")
		gridLayout.addWidget(self.throttleLabel, row, 0, QtCore.Qt.AlignCenter)

	def on_throttle_change(self, v):
		self.throttleLabel.setText("%s %%" % v )

	def set_throttle(self, val):
		print "thrioottle", float(val) * 100
		self.throttle.setValue( float(val) * 100 )

if __name__ == '__main__':

	app = QtGui.QApplication(sys.argv)

	widget =  Turn_Bank_Indicator()
	widget.show()

	sys.exit(app.exec_())