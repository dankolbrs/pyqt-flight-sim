# -*- coding: utf-8 -*-

"""Turn_Bank Indicator"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QWidget, QLabel
from PyQt5.QtWidgets import QDial, QGridLayout, QApplication


# Main Dial
class Turn_Bank_Indicator(QGroupBox):

    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)

        layout = QGridLayout()
        self.setLayout(layout)
        self.setTitle("Bank")
        self.label = QLabel("Bank")
        self.styleSheetText = "border: 2px solid #999999; color: magenta;" \
                              " padding: 3px; font-weight: bold; margin: 5px;"
        self.label.setStyleSheet(self.styleSheetText)
        layout.addWidget(self.label, 0, 0, Qt.AlignCenter)

        # Main dial
        self.bankDial = QDial()
        self.bankDial.setMinimum(-180)
        self.bankDial.setMaximum(180)
        self.bankDial.setValue(0)
        self.bankDial.setNotchesVisible(True)
        self.bankDial.setSingleStep(10)
        self.bankDial.setWrapping(True)
        layout.addWidget(self.bankDial, 1, 0, Qt.AlignCenter)


    def update_bank(self, bank):
        print("bank update: ",  bank)
        self.label.setText(str(int(bank)))
        self.bankDial.setValue(int(bank))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    widget = Turn_Bank_Indicator()
    widget.show()
    sys.exit(app.exec_())
