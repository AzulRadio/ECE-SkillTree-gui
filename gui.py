import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont

import skilltree_gui
import skilltree
from functools import partial



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = skilltree_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.c.clicked.connect(partial(skilltree.learn, skilltree.c))
    ui.labelc.setText(skilltree.status(skilltree.c))
    ui.labelc.setFont(QFont("Agency FB", 9))
    sys.exit(app.exec_())
