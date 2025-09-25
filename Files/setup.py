from cx_Freeze import setup, Executable
import os
import sys



app_version = input("Версия: ")
base_executable = 'Win32Gui'
# Базовые настройки сборки
app_name = "Рас. Калькулятор"       # Название вашего приложения
     # Тип приложения (GUI или консольное); None - консольный режим
icon_path = "calculator.ico"      # Путь к иконке приложения (если есть)

# Скрипт главного модуля
# Ярлык в меню "Пуск"
start_menu_shortcut = Executable(
    script="main.py",
    base=base_executable,
    icon=icon_path,
    target_name="calculator.exe",
    shortcut_name='Рас.Калькулятор',
    shortcut_dir='ProgramMenuFolder'
)

# Ярлык на рабочем столе
desktop_shortcut = Executable(
    script="main.py",
    base=base_executable,
    icon=icon_path,
    target_name="calculator.exe",
    shortcut_name='Рас.Калькулятор',
    shortcut_dir='DesktopFolder'
)

# Параметры сборки
options = {
    "build_exe": {
        
        "includes": [],                      # Дополнительные модули, если нужны
        "include_files": ["addings.py", "calculate.py", "calculator.ico", "equations.py", "logs.log", "settings_icon.png", "statistic.py", "trinogremetric.py", "UI.py"],# Добавляем файл version.txt
        "optimize": 2,
        
        "zip_include_packages": ['*'],
        "zip_exclude_packages": ['tkinter']
         # Попробуйте добавить этот параметр# Уровень оптимизации байт-кода (может уменьшить размер)
    },
    "bdist_msi": {
        "upgrade_code": "{66666666-6667-6666-6666-666666666666}",  # Уникальный идентификатор обновления
        "add_to_path": False,  # Не добавлять в PATH
        'initial_target_dir': 'C:\\Antonrasrab',


    }
}

# Настройка сборки
setup(
    name=app_name,
    version=app_version,
    description="Рас. Калькулятор",
    executables=[start_menu_shortcut, desktop_shortcut],  # Два разных ярлыка,
    options=options,
    author='PythonSoft'
)
