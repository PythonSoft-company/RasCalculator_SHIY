from UI import MyApp
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtGui import QIcon
from calculate import *
from addings import *

import logging
history = []
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs.log')

app = QApplication(sys.argv)

app.setWindowIcon(QIcon("calculator.ico"))
window = MyApp()
window.button_calc.clicked.connect(lambda: calculate(window))

window.show()
sys.exit(app.exec())

