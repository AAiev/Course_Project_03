class Operation:
    def __init__(self, list_operation):
        self.list_operation = list_operation if list_operation else {}

    def __repr__(self):
        return f"Operation(dict_operation={self.list_operation})"


    def date_operation(self, dict_operation):
        """
        date_operation - из полученного словаря получает строку по ключу 'date'
        и возвращает дату в формате: ДД.ММ.ГГГГ
        :param dict_operation: словарь операции
        :return: дата в формате ДД.ММ.ГГГГ
        """
        date_operation_year = dict_operation['date'][0:4]
        date_operation_month = dict_operation['date'][5:7]
        date_operation_day = dict_operation['date'][8:10]
        return f'{date_operation_day}.{date_operation_month}.{date_operation_year}'


