from UI import MyApp
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtGui import QIcon
from calculate import *
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
window = MyApp()
check_first_run_and_show_tutorial()
window.button_calc.clicked.connect(lambda: calculate(window))
window.entry.returnPressed.connect(lambda: calculate(window))
window.button_system_of_equations.clicked.connect(lambda: solve_system_of_equations(window))
window.entry_system_of_equations.returnPressed.connect(lambda: solve_system_of_equations(window))
window.button_mean.clicked.connect(lambda: calculate_statistics(window, 'mean'))
window.button_median.clicked.connect(lambda: calculate_statistics(window, 'median'))
window.button_max.clicked.connect(lambda: calculate_statistics(window, 'max'))
window.button_min.clicked.connect(lambda: calculate_statistics(window, 'min'))
window.button_range.clicked.connect(lambda: calculate_statistics(window, 'range'))
window.button_variance.clicked.connect(lambda: calculate_statistics(window, 'variance'))
window.sin_button.clicked.connect(lambda: process_trigonometric_function(window, 'sin'))
window.cos_button.clicked.connect(lambda: process_trigonometric_function(window, 'cos'))
window.tan_button.clicked.connect(lambda: process_trigonometric_function(window, 'tan'))
window.button_fractions_calculate.clicked.connect(lambda: arithmetic_operation_fractions(window,
                                                                                         window.entry_first_fraction.text(),
                                                                                         window.entry_second_fraction.text(),
                                                                                         window.operator_variable.currentText()))
window.cl_b.clicked.connect(lambda: window.history_text.clear())
window.tgb.clicked.connect(lambda: webbrowser.open_new_tab("https://t.me/Ras_Kakulator_official"))
window.button_cor.clicked.connect(lambda: get_root_degree(window))
window.button_exit.clicked.connect(lambda: window.close())
window.form_btn.clicked.connect(lambda: webbrowser.open_new_tab("https://forms.yandex.ru/u/6861698d84227cbab5e787ba"))

window.show()
sys.exit(app.exec())

