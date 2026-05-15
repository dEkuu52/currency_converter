import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
url = "https://v6.exchangerate-api.com/v6/latest/USD"
headers = {"Authorization": f"Bearer {api_key}"}


exchange_rates = None

# -------------- Function for downloading api keys --------------
def pars_currency():
    global exchange_rates

    try:
        response = requests.get(url , headers=headers)
        data = response.json()
        exchange_rates = data['conversion_rates']
        return True
    except requests.exceptions.HTTPError as http_error:
        print(f'HTTP Error {http_error}')
    except requests.exceptions.ConnectionError as conection_error:
        print(f'Conection Error {conection_error}')
    except requests.exceptions.Timeout as timeout_error:
        print(f'Timeout Error{timeout_error}')
    except requests.exceptions.RequestException as requests_error:
        print(f'Requests Error{requests_error}')
    except KeyError:
        print(f'Error: USD not found')
    except Exception as e:
        print(f'An error occurred {e}')
        return False

def time():
    today_date = datetime.date.today()
    formatted_date = today_date.strftime('%d-%m-%Y')
    return formatted_date



# -------------- Function Converter ---------------
def live_currency():
    global exchange_rates

    if not exchange_rates:
        print('courses are not loaded')
        return

    while True:
        from_currency = input('Enter the currency you want to convert: ').upper()
        if from_currency == 'STOP':
            return


        print('If you want to exit and go to the main menu, enter "STOP"')

        to_currency = input('Enter the currency you are converting to: ').upper()

        if to_currency == 'STOP':
            return

        times = time()

        if exchange_rates:
            if to_currency in exchange_rates:
                while True:
                    try:
                        amount = float(input(f'How much {from_currency} do you want to transfer in {to_currency}? '))
                        result = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
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
    global exchange_rates

    if exchange_rates is None:
        print('Error, please try again')
        return

    if 'RUB' in exchange_rates:
        print(f"""
         ------------------------
            1 USD = {exchange_rates['RUB']:.4f} RUB 
         ------------------------
""")
    else:
        print(f"""
    --------------------------------------------------
        Failed to receive course USD in RUB.
    --------------------------------------------------
""")




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
    if not pars_currency():
        print('Internet problems, try restarting the program')
        return


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









