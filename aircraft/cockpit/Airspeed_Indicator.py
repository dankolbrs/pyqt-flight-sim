# -*- coding: utf-8 -*-

"""Airspeed Indicator"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QWidget, QLabel, QDial
from PyQt5.QtWidgets import QGridLayout, QApplication


# Main Dial
class AirspeedIndicator(QGroupBox):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.debug = True
        layout = QGridLayout()
        self.setLayout(layout)
        self.setTitle("Airspeed")
        self.setFixedWidth(200)
        self.styleSheetText = "border: 2px solid #999999; color: magenta;" \
                              " padding: 3px; font-weight: bold; margin: 5px;"

        # Text output
        self.labelSpeed = QLabel("170")
        self.labelSpeed.setStyleSheet(self.styleSheetText)
        layout.addWidget(self.labelSpeed, 0, 0, Qt.AlignCenter)

        # Speed dial
        self.speedDial = QDial()
        self.speedDial.setMinimum(0)
        self.speedDial.setMaximum(200)
        self.speedDial.setValue(170)
        self.speedDial.setNotchesVisible(True)
        self.speedDial.setSingleStep(50)
        self.speedDial.setWrapping(True)
        layout.addWidget(self.speedDial, 1, 0, Qt.AlignCenter)

        self.update_speed(750)

    def update_speed(self, knots):
        '''
        Provides function to update Airspeed indicator dial and label
        :param knots: Speed to update to
        :return: void
        '''

        if self.debug:
            print("airspeed update", knots)
        self.labelSpeed.setText(str(int(knots)))
        if int(knots) <= self.speedDial.minimum():
            self.speedDial.setValue(self.speedDial.minimum())
        elif int(knots) >= self.speedDial.maximum():
            self.speedDial.setValue(self.speedDial.maximum())
        else:
            self.speedDial.setValue(int(knots))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AirspeedIndicator()
    widget.show()
    sys.exit(app.exec_())
