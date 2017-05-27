# -*- coding: utf-8 -*-

"""Trim Indicator"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QWidget
from PyQt5.QtWidgets import QLabel, QSlider, QApplication


# Main Dial
class TrimIndicator(QGroupBox):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)
        self.setMinimumHeight(200)
        self.setTitle("Trim Indicator")
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        row = 0
        gridLayout.addWidget(QLabel("Left"), row, 0, Qt.AlignCenter)
        gridLayout.addWidget(QLabel("Elevator"), row, 1, Qt.AlignCenter)
        gridLayout.addWidget(QLabel("Right"), row, 2, Qt.AlignCenter)

        row += 1
        self.elevator = QSlider(Qt.Vertical, self)
        self.elevator.setMinimum(-100)
        self.elevator.setMaximum(100)
        self.elevator.setValue(0)
        self.elevator.setTickInterval(10)
        self.elevator.setTickPosition(QSlider.TicksBothSides)
        gridLayout.addWidget(self.elevator, row, 1, Qt.AlignCenter)

        self.leftAileron = QSlider(Qt.Vertical, self)
        self.leftAileron.setMinimum(-100)
        self.leftAileron.setMaximum(100)
        self.leftAileron.setValue(0)
        self.leftAileron.setTickInterval(5)
        self.leftAileron.setTickPosition(QSlider.TicksLeft)
        gridLayout.addWidget(self.leftAileron, row, 0, 2, 1)

        self.rightAileron = QSlider(Qt.Vertical, self)
        self.rightAileron.setMinimum(-100)
        self.rightAileron.setMaximum(100)
        self.rightAileron.setValue(0)
        self.rightAileron.setTickInterval(5)
        self.rightAileron.setTickPosition(QSlider.TicksRight)
        gridLayout.addWidget(self.rightAileron, row, 2, 2, 1)

        row += 2
        self.rudder = QSlider(Qt.Horizontal, self)
        self.rudder.setMinimum(-100)
        self.rudder.setMaximum(100)
        self.rudder.setValue(1)
        self.rudder.setTickInterval(1)
        self.rudder.setTickPosition(QSlider.TicksBelow)
        gridLayout.addWidget(self.rudder, row, 1, 1, 1)

    def update_elevator(self, surf):
        self.elevator.setValue(int(surf * 100))

    def update_aileron(self, surf):
        self.leftAileron.setValue(int(surf * -100))
        self.rightAileron.setValue(int(surf * 100))

    def update_rudder(self, surf):
        self.rudder.setValue(int(surf * 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TrimIndicator()
    widget.show()
    sys.exit(app.exec_())
