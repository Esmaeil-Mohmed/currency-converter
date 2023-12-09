import requests


while True:
    initial_currency = input("Enter the initial currency: ")
    target_currency = input("Enter the target currency: ")
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("the amount must be a number")
    if amount <= 0:
        print("amount must be greater than 0")
    else:
        url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

        payload = {}
        headers= {
        "apikey": "Ss5bG60b3lJblbrndsp5lDDlSBgn8caZ"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        if status_code != 200:
            print("something went wrong, please try again later.")
            exit()
        result = response.json()
        print(f"result is: {result['result']} and conversion rate is {result['info']['rate']}")
