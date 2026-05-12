import requests
import datetime
import os
from dotenv import load_dotenv

# -------------- Start menu text function --------------
def text_application():
    with open('rool.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)



# -------------- Function for downloading api keys --------------
def pars_currency(base_currency):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = f'{api_key}{base_currency}'
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


# -------------- Function Converter --------------
def live_currency():
    from_currency = input('Enter the currency you want to convert: ').upper()
    to_currency = input('Enter the currency you are converting to: ').upper()
    rates = pars_currency(from_currency)
    times = time()

    if rates and to_currency in rates:
        while True:
            try:
                amount = float(input(f'How much {from_currency} do you want to transfer in {to_currency}? '))
                result = amount * rates[to_currency]
                print(f'at the moment {times} the rate is {result} {to_currency}')
                print('Would you like to transfer any other currencies?')
                user_response = input('yes or no: ').lower()
                if user_response == 'yes':
                    live_currency()
                elif user_response == 'no':
                    print(text_application())
                    break
                else:
                    exit()
            except ValueError:
                print('Input error, please try again')


# -------------- Available currencies function --------------
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
    print(result)




# -------------- A function for displaying the exchange rate to the dollar for today. --------------
def curs_today():
    pass



# -------------- Main Function --------------
def main():
    while True:  # Добавляем бесконечный цикл
        text_application()
        user_selection = input('Enter the function you need (or type "stop" to exit): ')

        if user_selection.lower() == 'stop':
            print("Program stopped.")
            break

        if user_selection == '1':
            live_currency()
        elif user_selection == '2':
            list_currency()
        elif user_selection == '3':
            curs_today()

# -------------- Run Programm --------------
if __name__ == '__main__':
        main()








