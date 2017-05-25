# -*- coding: utf-8 -*-

"""VerticalSpeed_Indicator Indicator"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


## Main Dial
class VerticalSpeed_Indicator(QtWidgets.QGroupBox):

    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        self.setTitle("Vertical Speed")

        self.labelSpeed = QtWidgets.QLabel("170")
        self.styleSheetText = "border: 2px solid #999999; color: magenta;" \
                              " padding: 3px; font-weight: bold; margin: 5px;"
        self.labelSpeed.setStyleSheet(self.styleSheetText)
        layout.addWidget(self.labelSpeed, 0, 0, QtCore.Qt.AlignCenter)

        self.speedDial = QtWidgets.QDial()
        self.speedDial.setMinimum(-4000)
        self.speedDial.setMaximum(4000)
        self.speedDial.setValue(270)
        self.speedDial.setNotchesVisible(True)
        self.speedDial.setSingleStep(10)
        self.speedDial.setWrapping(True)
        layout.addWidget(self.speedDial, 1, 0, QtCore.Qt.AlignCenter)


    def update_vertical(self, fpm):
        self.labelSpeed.setText(str(int(fpm)))
        if int(fpm) <= -2000:
            self.speedDial.setValue(-4000)
        elif int(fpm) >= 2000:
            self.speedDial.setValue(0)
        else:
            self.speedDial.setValue(int(fpm)-2000)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  VerticalSpeed_Indicator()
    widget.show()

    sys.exit(app.exec_())