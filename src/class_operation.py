from operator import itemgetter
from datetime import datetime

class Operation:
    def __init__(self, list_operation):
        self.list_operation = list_operation if list_operation else {}

    def __repr__(self):
        return f"Operation(dict_operation={self.list_operation})"


    def five_last_successful_operations(self):
        """
        five_last_successful_operations - Берет исходный список словарей,
        сортирует его по убыванию даты и выводит первые 5 операций успешно выполненных
        :return: list_last_five_operation - список из 5 последних операций
        """
        list_correct = [i for i in self.list_operation if 'date' in list(i.keys())]
        list_operation_sort_date = sorted(list_correct, key=itemgetter('date'), reverse=True)
        list_last_five_operation = []
        for operation in list_operation_sort_date:
            if len(list_last_five_operation) < 5:
                if operation['state'] == 'EXECUTED':
                    list_last_five_operation.append(operation)
            else:
                break
        return list_last_five_operation

    def date_operation(self, dict_operation):
        """
        date_operation - из полученного словаря получает строку по ключу 'date'
        и возвращает дату в формате: ДД.ММ.ГГГГ
        :param dict_operation: словарь операции
        :return: дата в формате ДД.ММ.ГГГГ
        """
        date_operation = datetime.datetime.strptime(dict_operation['date'], "%Y-%b-%dT%H:%M:%S.%f")
        return f'{date_operation.day}.{date_operation.month}.{date_operation.year}'
