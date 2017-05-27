# -*- coding: utf-8 -*-

"""Compass Indicator"""

import sys
from PyQt5.QtWidgets import QGroupBox, QGridLayout
from PyQt5.QtWidgets import QApplication, QWidget, QDial
from PyQt5.QtCore import Qt


# Main Dial
class CompassIndicator(QGroupBox):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)

        layout = QGridLayout()
        self.setLayout(layout)
        self.setTitle("Compass")

        self.compassDial = QDial()
        self.compassDial.setMinimum(0)
        self.compassDial.setMaximum(360)
        self.compassDial.setValue(220)
        self.compassDial.setNotchesVisible(True)
        self.compassDial.setSingleStep(20)
        self.compassDial.setWrapping(True)
        layout.addWidget(self.compassDial, 1, 0, Qt.AlignCenter)

    def update_compass(self, north):
        self.compassDial.setValue(int(north))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CompassIndicator()
    widget.show()
    sys.exit(app.exec_())
