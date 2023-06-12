from operator import itemgetter


class Operation:
    def __init__(self, list_operation):
        self.list_operation = list_operation if list_operation else {}

    def __repr__(self):
        return f"Operation(dict_operation={self.list_operation})"

