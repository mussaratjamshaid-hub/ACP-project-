
import sys
from PyQt5.QtWidgets import QApplication
from gui.app_gui import AppGUI

if __name__ == "__main__":
    qt_app = QApplication(sys.argv)
    window = AppGUI()
    window.show()
    sys.exit(qt_app.exec_())
