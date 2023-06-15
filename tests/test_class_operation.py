from src.class_operation import Operation
test_dict_operation = {'date': '2019-12-08T22:46:21.935582',
  'description': 'Открытие вклада',
  'id': 863064926,
  'operationAmount': {'amount': '41096.24',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 90424923579946435907'}
test_operation = Operation(test_dict_operation)


def test_date_operation():
    assert test_operation.date_operation() == '08.12.2019'

def test_title_operation():
    assert test_operation.title_operation() == 'Открытие вклада'





