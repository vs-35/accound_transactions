import json
from datetime import datetime

filename = "../data/operations.json"


def load_operations(filename):
    """Функция загружает список операций из файла"""
    with open(filename, "r", encoding="utf-8") as file:
        json_dict = json.load(file)
        valid_dict = [op for op in json_dict if op != {}]
        return valid_dict


def date_format(date_string):
    """Функция преобразует универсальный формат даты операции в заданный формат"""
    dt_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
    date_operation = datetime.strftime(dt_object, '%d.%m.%Y')
    return date_operation


def get_five_last_operations(list_sorted):
    """Функция возращает пять последних операций"""
    successful_operations =[operation for operation in list_sorted if operation["state"] == "EXECUTED"]
    five_last_operations = successful_operations[:5]
    return five_last_operations


def sorted_by_date(json_dict):
    """Функция сортирует операции по дате.
    Более поздние операции находятся вверху списка."""
    list_sorted = sorted(json_dict, key=lambda x: x.get("date"), reverse=True)
    return list_sorted


def bank_account_hide(operation_expenditure):
    """Функция маскирует номер счета/карты"""
    if operation_expenditure:
        name_bank_account = " ".join(operation_expenditure.split(" ")[:-1])
        number_bank_account = operation_expenditure.split(" ")[-1]

        if len(number_bank_account) == 16:
            number_hide = number_bank_account[:6] + "*" * 6 + number_bank_account[-4:]
            number_separated = [number_hide[i:i + 4] for i in range (0,len(number_bank_account), 4)]
            return f'{name_bank_account} {" ".join(number_separated)}'

        elif len(number_bank_account) == 20:
            return f'{name_bank_account} {number_bank_account.replace(number_bank_account[:-4],"**")}'

    return "not defined"


def information_output(operations):
    """Функция выводит информацию о пяти последних операциях пользователю"""
    for operation in operations:
        print(f"{date_format(operation['date'])} {operation['description']}\n"
              f"{bank_account_hide(operation.get('from'))} -> {bank_account_hide(operation.get('to'))}\n"
              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency'] ['name']}\n")
