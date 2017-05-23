from aircraft.cockpit.Basic_T import Basic_T

from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    styleSheetString = open('aircraft/cockpit/style/cockpit.txt').read()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet( styleSheetString )

    widget =  Basic_T()
    widget.show()

    sys.exit(app.exec_())