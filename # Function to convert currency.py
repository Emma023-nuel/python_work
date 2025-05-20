def currency_converter():
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the base currency (e.g., GBP): ").upper()
    to_currency = input("Enter the target currency (e.g., USD): ").upper()

    # Ask if user wants to input a custom exchange rate
    custom_rate = input("Do you want to enter a custom exchange rate? (yes/no): ").lower()
    
    if custom_rate == "yes":
        rate = float(input(f"Enter the exchange rate from {from_currency} to {to_currency}: "))
    else:
        exchange_rates = {
            "GBP": {"USD": 1.25, "EUR": 1.15, "JPY": 150.0},
            "USD": {"GBP": 0.8, "EUR": 0.92, "JPY": 120.0},
            "EUR": {"GBP": 0.87, "USD": 1.09, "JPY": 130.0},
            "JPY": {"GBP": 0.0067, "USD": 0.0083, "EUR": 0.0077},
        }
        if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
            return "Invalid currency or conversion not supported."
        rate = exchange_rates[from_currency][to_currency]

    converted_amount = amount * rate
    print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    print(f"Exchange Rate Used: {rate}")
