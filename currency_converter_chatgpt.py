import requests

def currency_converter(api_key, amount, from_currency, to_currency):
    # Set up the API endpoint
    endpoint = f"http://data.fixer.io/api/latest"
    
    # Set up the parameters
    params = {
        "access_key": api_key,
        "base": from_currency,
        "symbols": to_currency
    }

    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200 and not data.get("error"):
            rate = data["rates"][to_currency]
            converted_amount = amount * rate
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print(f"Error: {data.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    api_key = "Ss5bG60b3lJblbrndsp5lDDlSBgn8caZ"
    
    # User input for conversion
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    currency_converter(api_key, amount, from_currency, to_currency)
