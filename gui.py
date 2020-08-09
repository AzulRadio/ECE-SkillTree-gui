import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(450,300)
w.move(500,300)
w.setWindowTitle('Skilltree')
w.show()

sys.exit(app.exec_())
