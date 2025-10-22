from string import printable
import addings

def to_10(n, ss):
    print(n, ss)
    ss = int(ss)
    print(type(n), type(ss))
    try:
        return int(str(n), ss)
    except Exception as e:
        print(type(e), e)
        raise ValueError(f"Для {ss} системы счисления можно использовать только символы {printable[:ss]}")


from string import ascii_uppercase


def to_2_36(n,ss):
    # Функция принимает число n
    # Переводит в систему счисления равной ss
    # И возвращает число в виде строки
    ss = int(ss)
    alph = "0123456789" + ascii_uppercase
    res = ''
    while n > 0:
        res = alph[n % ss] + res
        n //= ss
    return res

def calculate_sch(window, type, ss):
    try:
        a = to_10(window.entry_first_num.text(), ss)
        print(a)
        b = to_10(window.entry_second_num.text(), ss)
        print(b)
        if type == "+":
            result = a+b
        elif type == "-":
            result = a-b
        elif type == "*":
            result = a*b
        elif type == "/":
            result = a/b
            result = int(result)
        else:
            raise ValueError("Такого нет")
        print(result)
        result = to_2_36(result, ss)
        print(result)
        window.label_sch_result.setText(f"{result}")
        addings.add_to_history(f"{a}{type}{b} в {ss} сс", str(result))
        print(window.label_sch_result.text())
        # update_history()

    except ValueError as ve:
        addings.handle_error(str(ve), function_name="calculate_sch")
    except Exception as e:
        addings.handle_error(str(e), function_name="calculate_sch")

def perevod_to(window, ss1, ss2):
    try:
        a = to_10(window.entry_first_num.text(), ss1)
        
        result = to_2_36(a, ss2)
        print(result)
        window.label_sch_result.setText(f"{result}")
        
        print(window.label_sch_result.text())
        # update_history()

    except ValueError as ve:
        addings.handle_error(str(ve), function_name="calculate_sch")
    except Exception as e:
        addings.handle_error(str(e), function_name="calculate_sch")