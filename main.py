import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


# -------------- Function for downloading api keys --------------
def pars_currency(base_currency = 'USD'):
    url = f"https://v6.exchangerate-api.com/v6/latest/{base_currency}"
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url , headers=headers)
        data = response.json()
        return data['conversion_rates']
    except requests.exceptions.HTTPError as http_error:
        print(f'HTTP Error {http_error}')
    except requests.exceptions.ConnectionError as conection_error:
        print(f'Conection Error {conection_error}')
    except requests.exceptions.Timeout as timeout_error:
        print(f'Timeout Error{timeout_error}')
    except requests.exceptions.RequestException as requests_error:
        print(f'Requests Error{requests_error}')
    except KeyError:
        print(f'Error: {base_currency} not found')
    except Exception as e:
        print(f'An error occurred {e}')
        return None

def time():
    today_date = datetime.date.today()
    formatted_date = today_date.strftime('%d-%m-%Y')
    return formatted_date



# -------------- Function Converter ---------------
def live_currency():
    while True:
        from_currency = input('Enter the currency you want to convert: ').upper()
        if from_currency == 'STOP':
            return main()


        print('If you want to exit and go to the main menu, enter "STOP"')

        to_currency = input('Enter the currency you are converting to: ').upper()

        if to_currency == 'STOP':
            return main()


        rates = pars_currency(from_currency)

        times = time()

        if rates:
            if to_currency in rates:
                while True:
                    try:
                        amount = float(input(f'How much {from_currency} do you want to transfer in {to_currency}? '))
                        result = amount * rates[to_currency]
                        print(f'''
                ---------------------------------------------------
                 at the moment {times} the rate is {result} {to_currency}
                ---------------------------------------------------
''')
                        break

                    except ValueError:
                        print('Input error, please try again')
                    except Exception as e:
                        print(f'An error occurred {e}')
            else:
                print(f'Error: {to_currency} not found')
        else:
            print(f'Error: {from_currency} not found')



# -------------- Available currencies function --------------
def list_currency():
    curr = [
        'USD' ,
        'EUR' ,
        'RUB' ,
        'KZT' ,
        'CNY' ,
        'BYN' ,
        'GBP'
    ]
    result = " ".join(curr)

    print(f'''
           Available currencies
    ----------------------------------
        {result}
    ----------------------------------
            ''')




# -------------- A function for displaying the exchange rate to the dollar for today. --------------
def curs_today():
    from_curr = 'USD'
    to_curr = 'RUB'
    rates = pars_currency(from_curr)
    if rates and to_curr in rates:

        print(f'''
        -----------------------------------------------
        1 {from_curr} = {rates[to_curr]:.4f} {to_curr}
        -----------------------------------------------
                ''')
    else:

        print(f'''
        --------------------------------------------------
        Failed to receive course {from_curr} in {to_curr}.
        --------------------------------------------------
               ''')



# -------------- Start menu text function --------------
def text_application():
    try:
        with open('rool.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('File not found')



# -------------- Main Function --------------
def main():
    text_application()
    while True:
        user_selection = input('Enter the function you need (or type "stop" to exit): ')

        if user_selection.lower() == 'stop':
            print("Program stopped.")
            exit()


        if user_selection == '1':
            live_currency()
        elif user_selection == '2':
            list_currency()
        elif user_selection == '3':
            curs_today()
        else:
            print('Invalid input, please try again')

# -------------- Run Programm --------------
if __name__ == '__main__':
    main()









