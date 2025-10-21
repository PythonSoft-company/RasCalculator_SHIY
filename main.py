from UI import *
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtGui import QIcon

from addings import *
from equations import *
from statistic import *
from trinogremetric import *
from start import *
import logging
import webbrowser

history = []
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs.log')
with open("logs.log", "w") as f:
	f.write("")
app = QApplication(sys.argv)

app.setWindowIcon(QIcon("calculator.ico"))

check_first_run_and_show_tutorial()

print(sys.argv)
app.setWindowIcon(QIcon("calculator.ico"))
window = NewApp()
window.show()
calculator = Calculator()
equation_ui = EqualationUI()

statistic = StatisticUI()

trigonometry = TrigonometryUI()


fractions = FractionUI()

history_ui = HistoryandError()


sys.exit(app.exec())


