import json


with open("../operations.json", "r", encoding='utf-8') as file:
    data_json = file.read()
data = json.loads(data_json)
data = [trans for trans in data if trans]


def sort_operations(data):
    """сортируем операции по дате в порядке убывания"""
    return sorted(data, key=lambda x: x['date'], reverse=True)


def mask_card_number(operation_from):
    """маскируем номер карты"""
    return ' '.join([operation_from[:10], operation_from[14:18] + '****', operation_from[18:20], operation_from[-4:]])


def mask_account_number(operation_to):
    """маскируем номер счета"""
    return '**' + operation_to[-4:]


def output_operation(operation):
    """выводим операцию в заданном формате"""
    operation_date = operation['date'][:10].split("-")
    operation_description = operation['description']
    operation_from = operation.get('from', '')
    operation_to = operation['to']
    operation_amount = operation['operationAmount']['amount']
    operation_currency = operation['operationAmount']['currency']['name']

    masked_card_number = mask_card_number(operation_from)
    masked_account_number = mask_account_number(operation_to)

    print(f"{operation_date[2]}.{operation_date[1]}.{operation_date[0]} {operation_description}")
    print(f"{masked_card_number} -> счет {masked_account_number}")
    print(f"{operation_amount} {operation_currency}")
    print()


def recent_operations(data):
    sorted_data = sort_operations(data)
    for operation in sorted_data[:5]:
        output_operation(operation)


recent_operations(data)

