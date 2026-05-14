

---

# 💱 Currency Converter CLI

A convenient console-based tool for instant currency conversion. The application fetches real-time data via API, keeping you updated with the latest exchange rate fluctuations.

---

 ## 🚀 Key Features

 ### • Live Conversion — Fetching the most up-to-date exchange rates.
 ### • Smart Input — Automatic case conversion for currency codes (e.g., usd -> USD).
 ### • Secure Storage — Environment variables (.env) to protect your API key.
 ### • Error Handling — Resilience against invalid input and network issues.
 ### • Quick View — Instant access to the current USD/RUB exchange rate.

---

 ## 💿 project deployment


     git clone https://github.com/dEkuu52/currency_converter.git
     cd currency_converter
     python -m venv venv
     source venv/bin/activate or .\venv\Scripts\activate на Windows
     pip install -r requirements.txt
     python main.py


 

---

 ## 📖 How to Use

Run the application using the following command:
python main.py


 ### Available Commands

| Command  | Description |
|:---------|:-------------|
| **1**    | Converter: enter the "From" currency, the "To" currency, and the amount. |
| **2**    | List: view popular currency codes. |
| **3**    | Daily rate: instantly display the value of 1 USD in RUB. |
| **stop** | Exit: safely shut down the program. |


---

 ## 📊 Badges
 ![python](img/python-3.10+-blue.svg)
 

---

 ## 🛡 Security

The project is developed following best security practices:
1. Dependency Inversion: API keys are not hardcoded into the script.
2. Validation: The program verifies currency availability in the database before calculation.
3. Exception Handling: ValueError handling prevents the app from crashing when text is entered instead of numbers.

---

 ## 👨‍💻 Author
> Kirill / dEkuu52 — GitHub Profile (https://github.com/dEkuu52)

---

 