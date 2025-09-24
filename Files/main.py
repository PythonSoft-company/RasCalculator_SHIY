from UI import MyApp
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtGui import QIcon
from calculate import *
from addings import *
from equations import *
import logging
history = []
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs.log')

app = QApplication(sys.argv)

app.setWindowIcon(QIcon("calculator.ico"))
window = MyApp()
window.button_calc.clicked.connect(lambda: calculate(window))
window.button_system_of_equations.clicked.connect(lambda: solve_system_of_equations(window))
window.show()
sys.exit(app.exec())

