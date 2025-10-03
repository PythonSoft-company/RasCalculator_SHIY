from UI import *
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

check_first_run_and_show_tutorial()

print(sys.argv)
app.setWindowIcon(QIcon("calculator.ico"))
window = Main()
window.show()
calculator = Calculator()
equation_ui = EqualationUI()
window.call_calculator.clicked.connect(lambda: calculator.show())
window.call_equalation.clicked.connect(lambda: equation_ui.show())
statistic = StatisticUI()
window.call_statistic.clicked.connect(lambda: statistic.show())
trigonometry = TrigonometryUI()

window.call_trigonometry.clicked.connect(lambda: trigonometry.show())
fractions = FractionUI()
window.call_fractions.clicked.connect(lambda: fractions.show())
history_ui = HistoryandError()
window.call_history.clicked.connect(lambda: history_ui.show())

calculator.button_calc.clicked.connect(lambda: calculate(calculator))
calculator.entry.returnPressed.connect(lambda: calculate(calculator))
equation_ui.button_system_of_equations.clicked.connect(lambda: solve_system_of_equations(equation_ui))
equation_ui.entry_system_of_equations.returnPressed.connect(lambda: solve_system_of_equations(equation_ui))
statistic.button_mean.clicked.connect(lambda: calculate_statistics(statistic, 'mean'))
statistic.button_median.clicked.connect(lambda: calculate_statistics(statistic, 'median'))
statistic.button_max.clicked.connect(lambda: calculate_statistics(statistic, 'max'))
statistic.button_min.clicked.connect(lambda: calculate_statistics(statistic, 'min'))
statistic.button_range.clicked.connect(lambda: calculate_statistics(statistic, 'range'))
statistic.button_variance.clicked.connect(lambda: calculate_statistics(statistic, 'variance'))
trigonometry.sin_button.clicked.connect(lambda: process_trigonometric_function(trigonometry, 'sin'))
trigonometry.cos_button.clicked.connect(lambda: process_trigonometric_function(trigonometry, 'cos'))
trigonometry.tan_button.clicked.connect(lambda: process_trigonometric_function(trigonometry, 'tan'))
fractions.button_fractions_calculate.clicked.connect(lambda: arithmetic_operation_fractions(fractions,
                                                                                         fractions.entry_first_fraction.text(),
                                                                                         fractions.entry_second_fraction.text(),
                                                                                         fractions.operator_variable.currentText()))
history_ui.cl_b.clicked.connect(lambda: history_ui.history_text.clear())
window.tgb.clicked.connect(lambda: webbrowser.open_new_tab("https://t.me/Ras_Kakulator_official"))
calculator.button_cor.clicked.connect(lambda: get_root_degree(calculator))
window.button_exit.clicked.connect(lambda: window.close())
window.form_btn.clicked.connect(lambda: webbrowser.open_new_tab("https://forms.yandex.ru/u/6861698d84227cbab5e787ba"))

sys.exit(app.exec())


