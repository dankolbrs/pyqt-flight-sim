# -*- coding: utf-8 -*-

"""BasicT display"""

import sys
import struct
from PyQt5.QtNetwork import QUdpSocket
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtWidgets import QApplication

from aircraft.cockpit.Altimeter_Indicator import AltimeterIndicator
from aircraft.cockpit.Trim_Indicator import TrimIndicator
from aircraft.cockpit.Airspeed_Indicator import AirspeedIndicator
from aircraft.cockpit.Compass_Indicator import CompassIndicator
from aircraft.cockpit.ControlSurfaces import ControlSurfaces
from aircraft.cockpit.Engines import Engines
from aircraft.cockpit.Heading_Indicator import HeadingIndicator
from aircraft.cockpit.Turn_Bank_Indicator import TurnBankIndicator
from aircraft.cockpit.VerticalSpeed_Indicator import VerticalSpeedIndicator


# Main Dial
class BasicT(QWidget):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)
        self.setObjectName("InstrumentPanel")
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        gridLayout.setColumnStretch(0, 3)
        gridLayout.setColumnStretch(1, 5)
        gridLayout.setColumnStretch(2, 1)

        self.airspeedIndicator = AirspeedIndicator()
        gridLayout.addWidget(self.airspeedIndicator, 0, 0)

        self.trimIndicator = TrimIndicator()
        gridLayout.addWidget(self.trimIndicator, 0, 1)

        self.altimeterIndicator = AltimeterIndicator()
        gridLayout.addWidget(self.altimeterIndicator, 0, 2)

        self.bankIndicator = TurnBankIndicator()
        gridLayout.addWidget(self.bankIndicator, 1, 0)

        self.headingIndicator = HeadingIndicator()
        gridLayout.addWidget(self.headingIndicator, 1, 1)

        self.verticalSpeedIndicator = VerticalSpeedIndicator()
        gridLayout.addWidget(self.verticalSpeedIndicator, 1, 2)

        row = 2
        self.controlSurfaces = ControlSurfaces()
        gridLayout.addWidget(self.controlSurfaces, row, 1, 1, 1)

        self.engines = Engines()
        gridLayout.addWidget(self.engines, row, 2, 1, 1)

        self.compass = CompassIndicator()
        gridLayout.addWidget(self.compass, row, 0, 1, 1)

        self.udpSocket = QUdpSocket(self)
        self.udpSocket.bind(49003)
        self.udpSocket.readyRead.connect(self.processPendingDatagrams)

    def processPendingDatagrams(self):
        while self.udpSocket.hasPendingDatagrams():
            datagram, host, port = self.udpSocket.readDatagram(
                self.udpSocket.pendingDatagramSize())
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
                    beg_index += 4
                beg_index = 0
                # Go through each list from the datagram
                while beg_index < len(results):
                    chopped_byte_list = results[beg_index:beg_index+9]
                    self.processByteList(chopped_byte_list)
                    beg_index += 9

            except Exception as e:
                print("error: " + str(e))

    def convert_to_float(self, byte_set):
        tmp_data = byte_set
        return float(struct.unpack('<f', struct.pack(str(
            len(tmp_data)) + "b", *tmp_data))[0])

    def processByteList(self, byte_list):
        """
        Processes byte list unpacked from xplane datagram
        :param byte_list: list of bytes from xplane dataset
        :return:
        """

        # 3 - Airspeed [Vind_kias, Vind_keas, VTrue_ktas, VTrue_ktgs,
        # Vind_mpg, VTrue_mphas, VTrue_mphgs]
        if byte_list[0][0] == 3:
            self.airspeedIndicator.update_speed(
                int(self.convert_to_float(byte_list[2])))

        # 4 - [mach_rat, , VVI_fpm, , Gload_norm, Gload_axial, Gload_side]
        if byte_list[0][0] == 4:
            self.verticalSpeedIndicator.update_vertical(
                int(self.convert_to_float(byte_list[3])))

        # 11 - [elev, ailrn, ruddr]
        if byte_list[0][0] == 11:
            self.controlSurfaces.update_elevator(
                self.convert_to_float(byte_list[1]))
            self.controlSurfaces.update_aileron(
                self.convert_to_float(byte_list[2]))
            self.controlSurfaces.update_rudder(
                self.convert_to_float(byte_list[3]))

        # 13 - [trim_elev, trim_ailrn, trim_ruddr, flap_hand, flap_postn,
        #       slat_rat, sbrak_hand, sbrak_postn]
        if byte_list[0][0] == 13:
            self.trimIndicator.update_elevator(
                self.convert_to_float(byte_list[1]))
            self.trimIndicator.update_aileron(
                self.convert_to_float(byte_list[2]))
            self.trimIndicator.update_rudder(
                self.convert_to_float(byte_list[3]))

        # 17 - [pitch_deg, roll_deg, head_true, head_mag]
        if byte_list[0][0] == 17:
            self.bankIndicator.update_bank(
                self.convert_to_float(byte_list[2]))
            self.headingIndicator.update_heading(
                self.convert_to_float(byte_list[3]))
            self.compass.update_compass(
                self.convert_to_float(byte_list[4]))

        # 20 - [lat_deg, lon_deg, alt_ftmsl,
        #       alt_ftagl, on_runwy, alt_ind, lat_s, lat_w]
        if byte_list[0][0] == 20:
            self.altimeterIndicator.update_alt(
                self.convert_to_float(byte_list[3]))

        # 26 - [throttle_actual]
        if byte_list[0][0] == 26:
            self.engines.update_throttle(
                self.convert_to_float(byte_list[1]))


if __name__ == '__main__':
    styleSheetString = open('style/cockpit.txt').read()
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheetString)
    widget = BasicT()
    widget.show()
    sys.exit(app.exec_())
