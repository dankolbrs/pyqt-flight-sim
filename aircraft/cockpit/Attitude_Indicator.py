# -*- coding: utf-8 -*-

"""Attitude Indicator"""
# Not currently used or tested
# Replaced with Trim_Indicator


import sys
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtWidgets import QGroupBox, QWidget, QGridLayout, QFrame
from PyQt5.QtWidgets import QDial, QApplication, QLabel, QPushButton
from PyQt5.QtWidgets import QSlider, QVBoxLayout


# widget that appears top left and right
class ADIButtonIndicator(QFrame):

    def __init__(self, label, color, parent=None):
        QWidget.__init__(self, parent)

        self.setProperty("class", QVariant("ADIButtonIndicator"))
        self.setFixedSize(100, 120)

        vBox = QVBoxLayout(self)
        self.setLayout(vBox)

        self.label = QLabel(label)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setProperty("class", QVariant("PFD_IndButton"))
        vBox.addWidget(self.label)

        self.light = QLabel(" ")
        self.light.setStyleSheet("background-color: %s" % color)
        vBox.addWidget(self.light)


# Main panel in the middle
class ADIMainCentral(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setProperty("class", QVariant("panel"))
        gridLayout = QGridLayout()
        gridLayout.setColumnStretch(1, 2)
        gridLayout.setColumnStretch(2, 2)
        gridLayout.setColumnStretch(3, 2)
        gridLayout.setColumnStretch(4, 2)
        self.setLayout(gridLayout)

        self.headingSlider = QSlider(Qt.Horizontal, self)
        self.headingSlider.setMinimum(0)
        self.headingSlider.setMaximum(100)
        self.headingSlider.setValue(40)
        self.headingSlider.setTickInterval(20)
        self.headingSlider.setTickPosition(QSlider.TicksBelow)
        gridLayout.addWidget(self.headingSlider, 0, 1, 1, 4)

        self.leftSlider = QSlider(Qt.Vertical, self)
        self.leftSlider.setMinimum(0)
        self.leftSlider.setMaximum(5)
        self.leftSlider.setValue(2)
        self.leftSlider.setTickInterval(1)
        self.leftSlider.setTickPosition(QSlider.TicksBelow)
        gridLayout.addWidget(self.leftSlider, 1, 0, 2, 1)

        self.rightSlider = QSlider(Qt.Vertical, self)
        self.rightSlider.setMinimum(0)
        self.rightSlider.setMaximum(5)
        self.rightSlider.setValue(3)
        self.rightSlider.setTickInterval(1)
        self.rightSlider.setTickPosition(QSlider.TicksLeft)
        gridLayout.addWidget(self.rightSlider, 1, 5, 2, 1)

        self.bottomSlider = QSlider(Qt.Horizontal, self)
        self.bottomSlider.setMinimum(0)
        self.bottomSlider.setMaximum(2)
        self.bottomSlider.setValue(1)
        self.bottomSlider.setTickInterval(1)
        self.bottomSlider.setTickPosition(QSlider.TicksAbove)
        gridLayout.addWidget(self.bottomSlider, 3, 2, 1, 2)

        self.middleWidget = AttitudeMiddleBlock()
        gridLayout.addWidget(self.middleWidget, 1, 1, 2, 4, Qt.AlignCenter)


class AttitudeMiddleBlock(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.middleWidgetTop = QLabel("---- Top ----")
        self.middleWidgetTop.setStyleSheet("background-color: #239EE1;")
        self.middleWidgetTop.setFixedSize(150, 75)
        layout.addWidget(self.middleWidgetTop)

        self.middleWidgetBottom = QLabel("---- X ----")
        self.middleWidgetBottom.setStyleSheet("background-color: #85623C;")
        self.middleWidgetBottom.setFixedSize(150, 75)
        layout.addWidget(self.middleWidgetBottom)


# Main interface
class AttitudeIndicator(QGroupBox):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setObjectName("PFD_Main")
        gridLayout = QGridLayout()
        self.setLayout(gridLayout)

        self.indicatorGA = ADIButtonIndicator("GA", "green", self)
        gridLayout.addWidget(self.indicatorGA, 0, 0, 1, 1, Qt.AlignRight)

        self.indicatorDH = ADIButtonIndicator("DH", "orange", self)
        gridLayout.addWidget(self.indicatorDH, 0, 2, 1, 1, Qt.AlignLeft)

        self.mainPanel = ADIMainCentral(self)
        gridLayout.addWidget(self.mainPanel, 0, 1, 3, 1, Qt.AlignCenter)

        self.testButton = QPushButton(self)
        self.testButton.setText("Test")
        gridLayout.addWidget(self.testButton, 2, 0, 1, 1, Qt.AlignRight)

        self.knob = QDial(self)
        self.knob.setFixedSize(50, 50)
        gridLayout.addWidget(self.knob, 2, 2, 1, 1, Qt.AlignLeft)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AttitudeIndicator()
    widget.show()
    sys.exit(app.exec_())
