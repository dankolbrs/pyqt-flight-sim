# -*- coding: utf-8 -*-

"""Heading Indicator"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QWidget, QGridLayout, QDial, QApplication

# Main Dial
class Heading_Indicator(QGroupBox):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)

        layout = QGridLayout()
        self.setLayout( layout )

        self.setTitle("Heading")

        self.headingDial = QDial()
        self.headingDial.setMinimum(0)
        self.headingDial.setMaximum(360)
        self.headingDial.setValue(200)
        self.headingDial.setNotchesVisible(True)
        self.headingDial.setSingleStep(20)
        self.headingDial.setWrapping(True)
        layout.addWidget(self.headingDial, 1, 0, Qt.AlignCenter)

    def update_heading(self, heading):
        self.headingDial.setValue(int(heading) - 180)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = Heading_Indicator()
    widget.show()
    sys.exit(app.exec_())
