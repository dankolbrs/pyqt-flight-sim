# -*- coding: utf-8 -*-

"""Basic_T displayr"""

import sys
import struct
import binascii
from PyQt5 import QtCore, QtNetwork
from PyQt5.QtWidgets import QWidget, QGridLayout, QCheckBox
from PyQt5.QtWidgets import QPlainTextEdit, QApplication

from aircraft.cockpit.Altimeter_Indicator import Altimeter_Indicator
from aircraft.cockpit.Attitude_Indicator import Attitude_Indicator
from aircraft.cockpit.Airspeed_Indicator import Airspeed_Indicator
from aircraft.cockpit.Compass_Indicator import Compass_Indicator
from aircraft.cockpit.ControlSurfaces import ControlSurfaces
from aircraft.cockpit.Engines import Engines
from aircraft.cockpit.Heading_Indicator import Heading_Indicator
from aircraft.cockpit.Turn_Bank_Indicator import Turn_Bank_Indicator
from aircraft.cockpit.VerticalSpeed_Indicator import VerticalSpeed_Indicator


# Main Dial
class Basic_T(QWidget):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)

        self.setObjectName("InstrumentPanel")

        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        gridLayout.setColumnStretch(0, 3)
        gridLayout.setColumnStretch(1, 5)
        gridLayout.setColumnStretch(2, 1)

        self.airspeedIndicator = Airspeed_Indicator()
        gridLayout.addWidget(self.airspeedIndicator, 0, 0)

        self.attitudeIndicator = Attitude_Indicator()
        gridLayout.addWidget(self.attitudeIndicator, 0, 1)

        self.altimeterIndicator = Altimeter_Indicator()
        gridLayout.addWidget(self.altimeterIndicator, 0, 2)

        self.bankIndicator = Turn_Bank_Indicator()
        gridLayout.addWidget(self.bankIndicator, 1, 0)

        self.headingIndicator = Heading_Indicator()
        gridLayout.addWidget(self.headingIndicator, 1, 1)

        self.verticalSpeedIndicator = VerticalSpeed_Indicator()
        gridLayout.addWidget(self.verticalSpeedIndicator, 1, 2)

        row = 2
        self.controlSurfaces = ControlSurfaces()
        gridLayout.addWidget(self.controlSurfaces, row, 1, 1, 1)

        self.engines = Engines()
        gridLayout.addWidget(self.engines, row, 2, 1, 1)

        self.compass = Compass_Indicator()
        gridLayout.addWidget(self.compass, row, 0, 1, 1)

        row += 1
        self.txtSocket = QPlainTextEdit()
        self.txtSocket.setStyleSheet("color: yellow")
        gridLayout.addWidget(self.txtSocket, row, 0, 1, 2)


        self.udpSocket = QtNetwork.QUdpSocket(self)
        self.udpSocket.bind(49003)
        self.udpSocket.readyRead.connect(self.processPendingDatagrams)

    def processPendingDatagrams(self):
        while self.udpSocket.hasPendingDatagrams():
            datagram, host, port = self.udpSocket.readDatagram(self.udpSocket.pendingDatagramSize())
            try:
                # Get the datagram sent from xplane, unpack it to bytes
                data_bytes = struct.unpack(str(len(datagram)) + "b", datagram)

                # Convert the bytes to lists of bytes
                results = []
                # The first five bytes we don't care about, it just says DATA
                beg_index = 5
                while beg_index < len(data_bytes):
                    raw_bytes = data_bytes[beg_index:beg_index+4]
                    results.append(raw_bytes)
                    beg_index +=4
                beg_index = 0
                #byte_list = []
                while beg_index < len(results):
                    chopped_byte_list = results[beg_index:beg_index+9]
                    self.processByteList(chopped_byte_list)
                    #byte_list.append(chopped_byte_list)
                    beg_index += 9
                #print(byte_list)

            except Exception as e:
                print("error: " + str(e))

    def convert_to_float(self, byte_set):
        tmp_data = byte_set
        return float(struct.unpack('<f', struct.pack(str(
            len(tmp_data)) + "b", *tmp_data))[0])

    def processByteList(self, byte_list):
        '''
        Processes byte list unpacked from xplane datagram 
        :param byte_list: list of bytes from xplane dataset
        :return: 
        '''

        # 3 - Airspeed [Vind_kias, Vind_keas, VTrue_ktas, VTrue_ktgs,
        # Vind_mpg, VTrue_mphas, VTrue_mphgs]
        if byte_list[0][0] == 3:
            self.airspeedIndicator.update_speed(
                int(self.convert_to_float(byte_list[2])))

        # 3 - [mach_rat, , VVI_fpm, , Gload_norm, Gload_axial, Gload_side]
        if byte_list[0][0] == 4:
            self.verticalSpeedIndicator.update_vertical(
                int(self.convert_to_float(byte_list[3])))

        # 17 - [pitch_deg, roll_deg, head_true, head_mag]
        if byte_list[0][0] == 17:
            self.bankIndicator.update_bank(self.convert_to_float(byte_list[2]))
            self.headingIndicator.update_heading(self.convert_to_float(byte_list[3]))



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
        print("send")

    def send_property(self, prop, val):
        #print "send", prop, val
        #self.socket.writeData())
 
        datagram = "set /sim/gui/dialogs/autopilot/speed-active %s" % (val)
        datagram = "speed-active=%s\n" % (val)
        print(datagram)
        self.udpSocket.writeDatagram(datagram, QtNetwork.QHostAddress(QtNetwork.QHostAddress.Broadcast), 6788)


class FlightGearListener(QtCore.QObject):

    def __init__(self, parent):
        QtCore.QObject.__init__(self, parent)

        self.socket = QtNetwork.QUdpSocket(self)
        self.socket.bind(6789) #QtNetwork.QHostAddress.LocalHost, 6789)
        #self.connect(self.socket, QtCore.SIGNAL("readyRead()"), self.process_flightgear_datagrams)

    def process_flightgear_datagrams(self):
        while self.socket.hasPendingDatagrams():
            datagram, host, port = self.socket.readDatagram(self.socket.pendingDatagramSize())
            print("In>>")
            print(datagram)
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
    app = QApplication(sys.argv)
    app.setStyleSheet( styleSheetString )

    widget =  Basic_T()
    widget.show()

    sys.exit(app.exec_())