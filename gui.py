import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import skilltree_gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = skilltree_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
