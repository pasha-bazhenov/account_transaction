from utils.main import recent_operations, sort_operations, mask_card_number, mask_account_number, \
    output_operation



def test_mask_card_number():
    assert mask_card_number("Visa Classic 2842878893689012") == "Visa Class 8428**** 78 9012"


def test_mask_account_number():
    assert mask_account_number("Счет 90424923579946435907") == "**5907"


def test_sort_operations():
    data = [
        {'date': '2021-01-05', 'description': 'Operation 1'},
        {'date': '2021-02-10', 'description': 'Operation 2'},
        {'date': '2021-01-15', 'description': 'Operation 3'}
    ]
    expected_result = [
        {'date': '2021-02-10', 'description': 'Operation 2'},
        {'date': '2021-01-15', 'description': 'Operation 3'},
        {'date': '2021-01-05', 'description': 'Operation 1'}
    ]
    result = sort_operations(data)
    assert result == expected_result


def test_output_operation(capsys):
    operation = {
        'date': '2021-01-15T13:30:00',
        'description': 'Payment',
        'from': '1234567890123456',
        'to': '1234567890',
        'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}}
    }
    expected_output = "15.01.2021 Payment\n1234567890 56****  3456 -> счет **7890\n100 USD\n\n"
    output_operation(operation)
    captured = capsys.readouterr()

    assert captured.out == expected_output
