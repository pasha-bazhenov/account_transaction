import json


with open("../operations.json", "r", encoding='utf-8') as file:
    data_json = file.read()
data = json.loads(data_json)


def recent_operations(data):
    """ Сортируем операции по дате в порядке убывания"""
    data = [trans for trans in data if trans]
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)

    # Выводим последние 5 операций
    for operation in sorted_data[:5]:
        operation_date = operation['date'][:10].split("-")
        operation_description = operation['description']
        operation_from = operation.get('from', '')
        operation_to = operation['to']
        operation_amount = operation['operationAmount']['amount']
        operation_currency = operation['operationAmount']['currency']['name']

        # Маскируем номер карты и номер счета
        masked_card_number = ' '.join(
            [operation_from[:10], operation_from[14:18] + '****', operation_from[18:20], operation_from[-4:]])
        masked_account_number = '**' + operation_to[-4:]

        # Выводим операцию в заданном формате
        print(f"{operation_date[2]}.{operation_date[1]}.{operation_date[0]} {operation_description}")
        print(f"{masked_card_number} -> счет {masked_account_number}")
        print(f"{operation_amount} {operation_currency}")
        print()


recent_operations(data)


