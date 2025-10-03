from addings import *
import math


def process_trigonometric_function(window, function_type):
	"""Вычисляет тригонометрическую функцию указанного типа."""
	try:
		angle = float(window.trig_input.text())
		radians = math.radians(angle)
		if function_type == 'sin':
			result = math.sin(radians)
		elif function_type == 'cos':
			result = math.cos(radians)
		elif function_type == 'tan':
			result = math.tan(radians)
		else:
			raise ValueError(f"Неверный тип тригонометрической функции: {function_type}")
		final_result = format_number(dynamic_precision(result))
		window.trig_output.setText(f"{final_result}")
		clear_errors()
		add_to_history(f"{function_type}({angle})", final_result)
		update_history()
		
	except ValueError as ve:
		handle_error(f"Ошибка: {ve}", input_data=angle, function_name='process_trigonometric_function')
	except Exception as e:
		handle_error( f"Ошибка: {e}", input_data=angle, function_name='process_trigonometric_function')
