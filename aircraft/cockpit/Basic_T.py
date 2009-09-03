# -*- coding: utf-8 -*-

"""Basic_T displayr"""

import sys
from PyQt4 import QtCore, QtGui, QtNetwork

from Airspeed_Indicator import Airspeed_Indicator
from Attitude_Indicator import Attitude_Indicator
from Altimeter_Indicator import Altimeter_Indicator

from Turn_Bank_Indicator import Turn_Bank_Indicator
from Heading_Indicator import Heading_Indicator
from VerticalSpeed_Indicator import VerticalSpeed_Indicator

from ControlSurfaces import ControlSurfaces
from Engines import Engines

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


		self.bankIndicator = Turn_Bank_Indicator()
		gridLayout.addWidget( self.bankIndicator, 1, 0 )

		self.headingIndicator = Heading_Indicator()
		gridLayout.addWidget( self.headingIndicator, 1, 1 )

		self.verticalSpeedIndicator = VerticalSpeed_Indicator()
		gridLayout.addWidget( self.verticalSpeedIndicator, 1, 2 )

		row = 2
		self.controlSurfaces = ControlSurfaces()
		gridLayout.addWidget( self.controlSurfaces, row, 1, 1, 1 )

		self.engines = Engines()
		gridLayout.addWidget( self.engines, row, 2, 1, 1 )

		row += 1
		self.txtSocket = QtGui.QPlainTextEdit()
		self.txtSocket.setStyleSheet("color: yellow")
		gridLayout.addWidget( self.txtSocket, row, 0, 1, 2)



		### TEST
		self.chkSpeedAutopilotRequestActive = QtGui.QCheckBox("Switch", self)
		gridLayout.addWidget( self.chkSpeedAutopilotRequestActive, row, 2, 1, 2)
		self.connect(self.chkSpeedAutopilotRequestActive, QtCore.SIGNAL("clicked()"), self.on_auto_throttle)

		self.transmitSocket = FlightGearTransmit(self)

		self.listeningSocket = FlightGearListener(self)
		self.connect(self.listeningSocket, QtCore.SIGNAL("socketDebug"), self.update_debug)


		self.connect(self.listeningSocket, QtCore.SIGNAL("airspeed"), self.airspeedIndicator.update_speed)
		self.connect(self.listeningSocket, QtCore.SIGNAL("speed-active"), self.airspeedIndicator.update_autopilot)

		self.connect(self.listeningSocket, QtCore.SIGNAL("aileron"), self.controlSurfaces.set_aileron)
		self.connect(self.listeningSocket, QtCore.SIGNAL("elevator"), self.controlSurfaces.set_elevator)

		self.connect(self.listeningSocket, QtCore.SIGNAL("throttle"), self.engines.set_throttle)
		

		#self.connect(self.listeningSocket, QtCore.SIGNAL("bank"), self.bankIndicator.update)

	def update_debug(self, txt):
		self.txtSocket.setPlainText( txt )
	
	def on_auto_throttle(self):
		v = "true" if self.chkSpeedAutopilotRequestActive.checkState() else "false"
		self.transmitSocket.send_property("speed-active", v)

class FlightGearTransmit(QtCore.QObject):

	def __init__(self, parent):
		QtCore.QObject.__init__(self, parent)

		self.udpSocket = QtNetwork.QUdpSocket(self)
		#self.socket.bind(6788) #QtNetwork.QHostAddress.LocalHost, 6789)
		#self.connect(self.socket, QtCore.SIGNAL("readyRead()"), self.process_flightgear_datagrams)

	def process_flightgear_datagrams(self):
		print "send"

	def send_property(self, prop, val):
		#print "send", prop, val
		#self.socket.writeData())
 
		datagram = "set /sim/gui/dialogs/autopilot/speed-active %s" % (val)
		datagram = "speed-active=%s\n" % (val)
		print datagram
		self.udpSocket.writeDatagram(datagram, QtNetwork.QHostAddress(QtNetwork.QHostAddress.Broadcast), 6788)


class FlightGearListener(QtCore.QObject):

	def __init__(self, parent):
		QtCore.QObject.__init__(self, parent)

		self.socket = QtNetwork.QUdpSocket(self)
		self.socket.bind(6789) #QtNetwork.QHostAddress.LocalHost, 6789)
		self.connect(self.socket, QtCore.SIGNAL("readyRead()"), self.process_flightgear_datagrams)

	def process_flightgear_datagrams(self):
		while self.socket.hasPendingDatagrams():
			datagram, host, port = self.socket.readDatagram(self.socket.pendingDatagramSize())
			print "In>>"
			print datagram
			params = datagram.split("\t")
			#print params
			#return
			txt = ''
			for param in params:
				param_name, param_val = param.split("=")
				#print param_name, param_val
				txt += "%s = %s\n" % (param_name, param_val)
				self.emit(QtCore.SIGNAL(param_name), param_val)
			self.emit(QtCore.SIGNAL("socketDebug"), txt)


if __name__ == '__main__':

	styleSheetString = open('style/cockpit.txt').read()
	#print styleSheetString
	app = QtGui.QApplication(sys.argv)
	app.setStyleSheet( styleSheetString )

	widget =  Basic_T()
	widget.show()

	sys.exit(app.exec_())