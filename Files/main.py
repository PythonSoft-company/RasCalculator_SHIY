from UI import MyApp
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtGui import QIcon
from calculate import *
from addings import *
from equations import *
from statistic import *
import logging
history = []
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs.log')
with open("logs.log", "w") as f:
	f.write("")
app = QApplication(sys.argv)

app.setWindowIcon(QIcon("calculator.ico"))
window = MyApp()
window.button_calc.clicked.connect(lambda: calculate(window))
window.button_system_of_equations.clicked.connect(lambda: solve_system_of_equations(window))
window.button_mean.clicked.connect(lambda: calculate_statistics(window, 'mean'))
window.button_median.clicked.connect(lambda: calculate_statistics(window, 'median'))
window.button_max.clicked.connect(lambda: calculate_statistics(window, 'max'))
window.button_min.clicked.connect(lambda: calculate_statistics(window, 'min'))
window.button_range.clicked.connect(lambda: calculate_statistics(window, 'range'))
window.button_variance.clicked.connect(lambda: calculate_statistics(window, 'variance'))
window.show()
sys.exit(app.exec())

