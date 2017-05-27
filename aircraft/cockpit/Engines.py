# -*- coding: utf-8 -*-

"""Engines Indicator"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel
from PyQt5.QtWidgets import QSlider, QApplication, QWidget


# Main Dial
class Engines(QGroupBox):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)
        self.setMinimumHeight(200)
        self.setTitle("Engines")
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        row = 0
        gridLayout.addWidget(QLabel("Throttle"), row, 0, Qt.AlignCenter)

        row += 1
        self.throttle = QSlider(Qt.Vertical, self)
        self.throttle.setMinimum(0)
        self.throttle.setMaximum(100)
        self.throttle.setValue(0)
        self.throttle.setTickInterval(10)
        self.throttle.setTickPosition(QSlider.TicksBothSides)
        gridLayout.addWidget(self.throttle, row, 1, Qt.AlignCenter)

        row += 1
        self.throttleLabel = QLabel("0 %")
        gridLayout.addWidget(self.throttleLabel, row, 0, Qt.AlignCenter)

    def update_throttle(self, throt):
        self.throttleLabel.setText("%3.2f %%" % (throt * 100))
        self.throttle.setValue(int(throt * 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Engines()
    widget.show()
    sys.exit(app.exec_())
