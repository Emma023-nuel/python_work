def currency_converter(amount, from_currency, to_currency):
    # Predefined exchange rates (example rates, update as needed)
    exchange_rates = {
        "GBP": {"USD": 1.25, "EUR": 1.15, "JPY": 150.0},
        "USD": {"GBP": 0.8, "EUR": 0.92, "JPY": 120.0},
        "EUR": {"GBP": 0.87, "USD": 1.09, "JPY": 130.0},
        "JPY": {"GBP": 0.0067, "USD": 0.0083, "EUR": 0.0077},
    }

    # Check if the currencies are valid
    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return "Invalid currency or conversion not supported."

    # Perform the conversion
    rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * rate
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"

def show_menu():
    print("\nCurrency Converter Menu")
    print("1. GBP to USD")
    print("2. GBP to EUR")
    print("3. GBP to JPY")
    print("4. USD to GBP")
    print("5. USD to EUR")
    print("6. USD to JPY")
    print("7. EUR to GBP")
    print("8. EUR to USD")
    print("9. EUR to JPY")
    print("10. JPY to GBP")
    print("11. JPY to USD")
    print("12. JPY to EUR")
    print("13. Exit")

def get_conversion_choice(choice):
    options = {
        1: ("GBP", "USD"),
        2: ("GBP", "EUR"),
        3: ("GBP", "JPY"),
        4: ("USD", "GBP"),
        5: ("USD", "EUR"),
        6: ("USD", "JPY"),
        7: ("EUR", "GBP"),
        8: ("EUR", "USD"),
        9: ("EUR", "JPY"),
        10: ("JPY", "GBP"),
        11: ("JPY", "USD"),
        12: ("JPY", "EUR"),
    }
    return options.get(choice, (None, None))

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Select a conversion option (1-13): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 13:
            print("Thank you for using the currency converter!")
            break

        from_curr, to_curr = get_conversion_choice(choice)
        if not from_curr or not to_curr:
            print("Invalid choice. Please select a valid option.")
            continue

        try:
            amount = float(input(f"Enter the amount in {from_curr}: "))
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue

        result = currency_converter(amount, from_curr, to_curr)
        print(result)

if __name__ == "__main__":
    main()