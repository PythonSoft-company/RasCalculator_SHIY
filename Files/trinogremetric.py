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
		
	except ValueError as ve:
		print(ve)
		handle_error(ve, input_data=window.trig_input.text(), function_name="process_trigonometric_function")
	except Exception as e:
		print(e)
		handle_error(e, input_data=window.trig_input.text(), function_name="process_trigonometric_function")