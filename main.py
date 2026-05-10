import requests
import datetime

def text_application():
    with open('rool.txt', 'r', encoding='utf-8') as file:
        content = file.read()  # Читает весь файл
        print(content)



def pars_currency(base_currency):
    url = f'api_token{base_currency}'
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates']
    except Exception as e:
        print('An error occurred')
        return e

def time():
    today_date = datetime.date.today()
    formatted_date = today_date.strftime('%d-%m-%Y')
    return formatted_date


def live_currency():
    from_currency = input('Enter the currency you want to convert: ').upper()
    to_currency = input('Enter the currency you are converting to: ').upper()
    rates = pars_currency(from_currency)
    times = time()

    if rates and to_currency in rates:
            try:
                amount = float(input(f'How much {from_currency} do you want to transfer in {to_currency}? '))
                result = amount * rates[to_currency]
                print(f'at the moment {times} the rate is {result} {to_currency}')
            except ValueError:
                print('Input error, please try again')

def list_currency():
    curr = [
        'usd' ,
        'eur' ,
        'rub' ,
        'cyn' ,
        'cny' ,
        'byn' ,
        'gbp'
    ]
    result = " ".join(curr)
    return result




