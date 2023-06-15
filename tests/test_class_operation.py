import unittest
from src.class_operation import Operation
test_dict_operation = {'date': '2019-12-08T22:46:21.935582',
  'description': 'Открытие вклада',
  'id': 863064926,
  'operationAmount': {'amount': '41096.24',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 90424923579946435907'}


class TestOperation(unittest.TestCase):
    def setUp(self):
        self.operation = Operation()

    def test_date_operation(self):
        self.assertEqual(self.operation.date_operation(test_dict_operation), "08.12.2019")





