# -*- coding: utf-8 -*-

"""Attitude Indicator"""

import sys
from PyQt5 import QtCore, QtWidgets


## widget that appears top left and right
class ADI_Button_Indicator(QtWidgets.QFrame):

    def __init__(self, label, color, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        #self.setStyleSheet("border: 1px outset #efefef")
        self.setProperty("class", QtCore.QVariant("ADI_Button_Indicator") )
        self.setFixedSize(100, 120)

        vBox = QtWidgets.QVBoxLayout(self)
        self.setLayout( vBox)

        self.label = QtWidgets.QLabel(label)
        self.label.setAlignment(QtCore.Qt.AlignCenter )
        self.label.setProperty("class", QtCore.QVariant("PFD_IndButton") )
        vBox.addWidget( self.label )

        self.light = QtWidgets.QLabel(" ")
        self.light.setStyleSheet("background-color: %s" % color )
        vBox.addWidget( self.light )


## Main panel in the middle
class ADI_Main_Central(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setProperty("class", QtCore.QVariant("panel") )

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setColumnStretch(1, 2)
        gridLayout.setColumnStretch(2, 2)
        gridLayout.setColumnStretch(3, 2)
        gridLayout.setColumnStretch(4, 2)
        self.setLayout( gridLayout )

        #self.setStyleSheet("background-color: black; QSplitter::groove { color: red;}")

        self.headingSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.headingSlider.setMinimum(0)
        self.headingSlider.setMaximum(100)
        self.headingSlider.setValue(40)
        self.headingSlider.setTickInterval( 20 )
        self.headingSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        #self.headingSlider.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.headingSlider, 0, 1, 1, 4)

        self.leftSlider = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.leftSlider.setMinimum(0)
        self.leftSlider.setMaximum(5)
        self.leftSlider.setValue(2)
        self.leftSlider.setTickInterval( 1 )
        self.leftSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        #self.leftSlider.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.leftSlider, 1, 0, 2, 1)


        self.rightSlider = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
        self.rightSlider.setMinimum(0)
        self.rightSlider.setMaximum(5)
        self.rightSlider.setValue(3)
        self.rightSlider.setTickInterval( 1 )
        self.rightSlider.setTickPosition(QtWidgets.QSlider.TicksLeft)
        #self.rightSlider.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.rightSlider, 1, 5, 2, 1)


        self.bottomSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.bottomSlider.setMinimum(0)
        self.bottomSlider.setMaximum(2)
        self.bottomSlider.setValue(1)
        self.bottomSlider.setTickInterval( 1 )
        self.bottomSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        #self.bottomSlider.setStyleSheet("background-color: #bbbbbb")
        gridLayout.addWidget(self.bottomSlider, 3, 2, 1, 2)

        #self.middleWidgetTop = QtWidgets.QLabel("---- X ----")
        #self.middleWidgetTop.setStyleSheet("background-color: #239EE1;")
        #gridLayout.addWidget(self.middleWidgetTop, 1, 1, 1, 4, QtCore.Qt.AlignCenter)

        #self.middleWidgetBottom = QtWidgets.QLabel("---- X ----")
        #self.middleWidgetBottom.setStyleSheet("background-color: #85623C; margin: 0px;")
        #gridLayout.addWidget(self.middleWidgetBottom, 2, 1, 1, 4, QtCore.Qt.AlignCenter)

        self.middleWidget = Attitude_MiddleBlock()
        gridLayout.addWidget( self.middleWidget, 1, 1, 2, 4, QtCore.Qt.AlignCenter)

class Attitude_MiddleBlock(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout( layout )

        self.middleWidgetTop = QtWidgets.QLabel("---- Top ----")
        self.middleWidgetTop.setStyleSheet("background-color: #239EE1;")
        self.middleWidgetTop.setFixedSize( 150, 75 )
        #gridLayout.addWidget(self.middleWidgetTop, 1, 1, 1, 4, QtCore.Qt.AlignCenter)
        layout.addWidget( self.middleWidgetTop)

        self.middleWidgetBottom = QtWidgets.QLabel("---- X ----")
        self.middleWidgetBottom.setStyleSheet("background-color: #85623C;")
        self.middleWidgetBottom.setFixedSize( 150, 75 )
        #gridLayout.addWidget(self.middleWidgetBottom, 2, 1, 1, 4, QtCore.Qt.AlignCenter)
        layout.addWidget( self.middleWidgetBottom)


## Main interface
class Attitude_Indicator(QtWidgets.QGroupBox):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setObjectName("PFD_Main")
        gridLayout = QtWidgets.QGridLayout()
        self.setLayout( gridLayout )

        self.indicatorGA = ADI_Button_Indicator("GA", "green", self)
        gridLayout.addWidget(self.indicatorGA, 0, 0, 1, 1, QtCore.Qt.AlignRight)

        self.indicatorDH= ADI_Button_Indicator("DH", "orange", self)
        gridLayout.addWidget(self.indicatorDH, 0, 2, 1, 1, QtCore.Qt.AlignLeft)

        self.mainPanel = ADI_Main_Central(self)
        gridLayout.addWidget(self.mainPanel, 0, 1, 3, 1, QtCore.Qt.AlignCenter)

        self.testButton = QtWidgets.QPushButton(self)
        self.testButton.setText("Test")
        gridLayout.addWidget(self.testButton, 2, 0, 1, 1, QtCore.Qt.AlignRight)

        self.knob = QtWidgets.QDial(self)
        self.knob.setFixedSize( 50, 50)
        gridLayout.addWidget(self.knob, 2, 2, 1, 1, QtCore.Qt.AlignLeft)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widget =  Attitude_Indicator()
    widget.show()

    sys.exit(app.exec_())