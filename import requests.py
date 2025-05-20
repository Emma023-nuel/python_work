import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        return rates.get(target_currency, None)
    else:
        print("Error fetching exchange rates.")
        return None

def currency_converter(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Conversion rate not available.")
        return None

if __name__ == "__main__":
    print("Currency Converter")
    amount = float(input("Enter amount: "))
    base_currency = input("Enter base currency (e.g., GBP): ").upper()
    target_currency = input("Enter target currency (e.g., USD): ").upper()

    result = currency_converter(amount, base_currency, target_currency)
    if result:
        print(f"{amount} {base_currency} is equal to {result:.2f} {target_currency}")