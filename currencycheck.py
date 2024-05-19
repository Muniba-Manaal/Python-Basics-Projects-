from forex_python.converter import CurrencyRates, CurrencyCodes
import sys


# Mapping of currency codes to country names
currency_to_country = {
    'PHP': 'Philippines',
    'USD': 'United States',
    'EUR': 'European Union',
    'JPY': 'Japan',
    'GBP': 'United Kingdom',
    'AUD': 'Australia',
    'CAD': 'Canada',
    'CHF': 'Switzerland',
    'CNY': 'China',
    'SEK': 'Sweden',
    'NZD': 'New Zealand',
    'MXN': 'Mexico',
    'SGD': 'Singapore',
    'HKD': 'Hong Kong',
    'NOK': 'Norway',
    'KRW': 'South Korea',
    'TRY': 'Turkey',
    'RUB': 'Russia',
    'INR': 'India',
    'BRL': 'Brazil',
    'ZAR': 'South Africa',
    # ... add additional known currencies and their countries
}


def list_currencies():
    c = CurrencyRates()
    try:
        # Get all available currency codes from the library
        available_currencies = c.get_rates('PHP').keys()
        # Filter out only the known currencies we have information for
        known_currencies = {code: currency_to_country.get(code, 'Unknown')
                            for code in available_currencies
                            if code in currency_to_country}
        return known_currencies
    except Exception as e:
        print(f"Error fetching currency list: {e}")
        sys.exit(1)


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        from_currency_name = currency_to_country.get(from_currency, 'Unknown Currency')
        to_currency_name = currency_to_country.get(to_currency, 'Unknown Currency')
        from_symbol = CurrencyCodes().get_symbol(from_currency)
        to_symbol = CurrencyCodes().get_symbol(to_currency)

        print(f"{from_symbol}{amount} {from_currency} ({from_currency_name}) is equal to "
              f"{to_symbol}{converted_amount:.2f} {to_currency} ({to_currency_name})")
    except Exception as e:
        print(f"Error in currency conversion: {e}")
        sys.exit(1)


def get_validated_input(prompt, type_func, condition=lambda x: True):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            sys.exit(0)
        try:
            value = type_func(user_input)
            if condition(value):
                return value
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    print("Welcome to the Currency Converter!")
    print("Type 'exit' at any point to leave the program.\n")

    known_currencies = list_currencies()
    print("Available currencies and their countries:")
    for code, country in known_currencies.items():
        print(f"{code} - {country}")
    print("\n")

    from_currency = get_validated_input(
        "Enter the currency you are converting from (e.g., USD): ",
        str.upper,
        lambda x: x in known_currencies
    )

    to_currency = get_validated_input(
        "Enter the currency you are converting to (e.g., EUR): ",
        str.upper,
        lambda x: x in known_currencies
    )

    amount = get_validated_input(
        "Enter the amount to convert: ",
        float,
        lambda x: x > 0
    )

    convert_currency(amount, from_currency, to_currency)


if __name__ == "__main__":
    main()
