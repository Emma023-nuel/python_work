def get_valid_input(prompt, data_type, validation_function=None):
    """
    Gets user input with validation.

    Args:
        prompt (str): The message to display to the user.
        data_type (type): The expected data type (e.g., float, int, str).
        validation_function (callable, optional): A function to perform additional validation.
            Defaults to None.

    Returns:
        The validated user input.
    """
    while True:
        try:
            user_input = input(prompt)
            value = data_type(user_input)  # Convert to the specified data type
            if validation_function is None or validation_function(value):
                return value
            else:
                print("Invalid input. Please follow the instructions.")
        except ValueError:
            print("Invalid input. Please enter a value of the correct type.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def validate_positive(value):
    """
    Checks if a value is positive.

    Args:
        value: The value to check.

    Returns:
        bool: True if the value is positive, False otherwise.
    """
    return value > 0

def validate_currency_code(code, supported_currencies):
    """
    Validates a currency code against a list of supported currencies.

    Args:
        code (str): The currency code to validate.
        supported_currencies (list): A list of valid currency codes.

    Returns:
        bool: True if the code is valid, False otherwise.
    """
    return code.upper() in supported_currencies

def get_exchange_rate(from_currency, to_currency, exchange_rates):
    """
    Gets the exchange rate between two currencies.

    Args:
        from_currency (str): The source currency code.
        to_currency (str): The target currency code.
        exchange_rates (dict): A dictionary of exchange rates.

    Returns:
        float: The exchange rate, or None if not found.
    """
    if from_currency in exchange_rates and to_currency in exchange_rates:
        if from_currency == "GBP":
            return exchange_rates[to_currency]
        elif to_currency == "GBP":
            return 1 / exchange_rates[from_currency]
        else:
            #calculate rate.
            return exchange_rates[to_currency] / exchange_rates[from_currency]
    else:
        return None

def calculate_conversion(amount, exchange_rate):
    """
    Calculates the converted amount.

    Args:
        amount (float): The amount to convert.
        exchange_rate (float): The exchange rate.

    Returns:
        float: The converted amount.
    """
    return amount * exchange_rate

def display_conversion_result(amount, from_currency, converted_amount, to_currency, exchange_rate):
    """
    Displays the conversion result.

    Args:
        amount (float): The original amount.
        from_currency (str): The source currency code.
        converted_amount (float): The converted amount.
        to_currency (str): The target currency code.
        exchange_rate (float): The exchange rate used.
    """
    print(f"\n{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    print(f"Exchange rate used: {exchange_rate:.4f}")

def main():
    """
    Main function to run the currency converter program.
    """
    # --- Constants ---
    GBP_CODE = "GBP"
    SUPPORTED_CURRENCIES = ["EUR", "USD", "JPY", "CAD", "AUD", "CHF"]  # Add more as needed
    DEFAULT_EXCHANGE_RATES = {"EUR": 1.18, "USD": 1.30, "JPY": 145.00,
                               "CAD": 1.70, "AUD": 1.95, "CHF": 1.20}  # Example rates

    exchange_rates = DEFAULT_EXCHANGE_RATES.copy() #copy

    while True:
        print("\nCurrency Exchange Calculator")
        print("-----------------------------")
        print("1. Convert from GBP to Foreign Currency")
        print("2. Convert from Foreign Currency to GBP")
        print("3. Update Exchange Rates")
        print("4. Exit")

        choice = get_valid_input("Enter your choice (1, 2, 3, or 4): ", int, lambda x: 1 <= x <= 4)

        if choice == 4:
            print("Exiting program.")
            break

        if choice in (1, 2):
            if choice == 1:
                from_currency = GBP_CODE
                to_currency = get_valid_input(f"Enter the target currency ({', '.join(SUPPORTED_CURRENCIES)}): ", str,
                                                lambda x: validate_currency_code(x, SUPPORTED_CURRENCIES))
                to_currency = to_currency.upper()
            else:
                from_currency = get_valid_input(f"Enter the source currency ({', '.join(SUPPORTED_CURRENCIES)}): ", str,
                                                lambda x: validate_currency_code(x, SUPPORTED_CURRENCIES))
                from_currency = from_currency.upper()
                to_currency = GBP_CODE

            amount = get_valid_input("Enter the amount to convert: ", float, validate_positive)

            exchange_rate = get_exchange_rate(from_currency, to_currency, exchange_rates)
            if exchange_rate is None:
                print("Error: Currency not supported or exchange rate not available.")
                continue  #restart the loop.

            converted_amount = calculate_conversion(amount, exchange_rate)
            display_conversion_result(amount, from_currency, converted_amount, to_currency, exchange_rate)

        elif choice == 3:
            print("\nCurrent Exchange Rates:")
            for currency, rate in exchange_rates.items():
                print(f"{GBP_CODE} to {currency}: {rate:.4f}")
            currency_to_update = get_valid_input(f"Enter the currency code to update ({', '.join(SUPPORTED_CURRENCIES)}): ", str,
                                                    lambda x: validate_currency_code(x, SUPPORTED_CURRENCIES))
            currency_to_update = currency_to_update.upper()
            new_rate = get_valid_input(f"Enter the new exchange rate for {GBP_CODE} to {currency_to_update}: ", float, validate_positive)
            exchange_rates[currency_to_update] = new_rate
            print("Exchange rate updated.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


print("i am working")
