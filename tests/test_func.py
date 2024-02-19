from utils.func import recent_operations


def test_recent_operations():
    assert recent_operations([
        {
            "id": 863064926,
            "state": "executed",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "usd",
                    "code": "usd"
                }
            },
            "description": "Открытие вклада",
            "to": "счет 90424923579946435907"
        },
        {
            "id": 114832369,
            "state": "executed",
            "date": "2019-12-07t06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "usd",
                    "code": "usd"
                }
            },
            "description": "перевод организации",
            "from": "visa classic 2842878893689012",
            "to": "счет 35158586384610753655"
        },
        {
            "id": 560813069,
            "state": "canceled",
            "date": "2019-12-03t04:27:03.427014",
            "operationAmount": {
                "amount": "17628.50",
                "currency": {
                    "name": "usd",
                    "code": "usd"
                }
            },
            "description": "перевод с карты на карту",
            "from": "mastercard 1796816785869527",
            "to": "visa classic 7699855375169288"
        },
        {
            "id": 154927927,
            "state": "executed",
            "date": "2019-11-19t09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {
                    "name": "руб.",
                    "code": "rub"
                }
            },
            "description": "перевод организации",
            "from": "maestro 7810846596785568",
            "to": "счет 43241152692663622869"
        },
        {
            "id": 482520625,
            "state": "executed",
            "date": "2019-11-13t17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "rub"
                }
            },
            "description": "перевод со счета на счет",
            "from": "счет 38611439522855669794",
            "to": "счет 46765464282437878125"
        }
    ]) == ("08.12.2019 открытие вклада\nnone -> счет **5907\n41096.24 usd\n"
           "\n07.12.2019 перевод организации\nvisa classic 8428**** 78 9012 -> счет **3655\n48150.39 usd\n"
           "\n03.12.2019 перевод с карты на карту\nmastercard 6816**** 78 9527 -> счет **9288\n17628.50 usd\n"
           "\n19.11.2019 перевод организации\nmaestro 78 6596**** 78 5568 -> счет **2869\n30153.72 руб.\n"
           "\n13.11.2019 перевод со счета на счет\nсчет 38611 2285**** 56 9794 -> счет **8125\n62814.53 руб.\n"
           "\n16.04.2018 перевод организации\nvisa platinum 1813166339376336 -> счет **5907\n65169.27 usd")