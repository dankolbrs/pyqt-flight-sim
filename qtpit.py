from aircraft.cockpit.Basic_T import BasicT

from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    styleSheetString = open('aircraft/cockpit/style/cockpit.txt').read()
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheetString)
    widget = BasicT()
    widget.show()
    sys.exit(app.exec_())
