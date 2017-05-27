# -*- coding: utf-8 -*-

"""Altimeter Indicator"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QWidget, QLabel, QDial
from PyQt5.QtWidgets import QGridLayout, QApplication


# Main Dial
class AltimeterIndicator(QGroupBox):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Altimeter")
        self.setFixedWidth(200)
        self.styleSheetText = "border: 2px solid #999999; color: magenta;" \
                              " padding: 3px; font-weight: bold; margin: 5px;"

        # Text output
        self.labelAlt = QLabel("170")
        self.labelAlt.setStyleSheet(self.styleSheetText)
        layout.addWidget(self.labelAlt, 0, 0, Qt.AlignCenter)

        self.mainDial = QDial()
        self.mainDial.setMinimum(0)
        self.mainDial.setMaximum(30000)
        self.mainDial.setValue(170)
        self.mainDial.setNotchesVisible(True)
        self.mainDial.setSingleStep(10)
        self.mainDial.setWrapping(False)
        layout.addWidget(self.mainDial, 1, 0, Qt.AlignCenter)

    def update_alt(self, alt):
        self.mainDial.setValue(int(alt))
        self.labelAlt.setText(str(int(alt)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AltimeterIndicator()
    widget.show()
    sys.exit(app.exec_())
