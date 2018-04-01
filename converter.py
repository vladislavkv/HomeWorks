value = input("Введите (крипто)валюту для перевода из KZT (USD/RUB/EUR/BTC/ETH): ")

if value == "USD" :
    amount = int(input("Введите сумму для перевода в USD: "))
    tamount = amount / 320,55
    print("=", tamount, " USD")
    print("При: 1 USD = 320,55 KZT")
    
if value == "RUB" :
    amount = int(input("Введите сумму для перевода в RUB: "))
    tamount = amount / 5,66
    print("=", tamount, " RUB")
    print("При: 1 RUB = 5,66 KZT")

if value == "EUR" :
    amount = int(input("Введите сумму для перевода в EUR: "))
    tamount = amount / 394,34
    print("=", tamount, " EUR")
    print("При: 1 EUR = 394,34 KZT")

if value == "BTC" :
    amount = int(input("Введите сумму для перевода в BTC: "))
    tamount = amount / 2914345,43
    print("=", tamount, " BTC")
    print("При: 1 BTC = 2914345,43 KZT")
    print("По данным с сайта pokur.su, на 13.03.2018")

if value == "ETH" :
    amount = int(input("Введите сумму для перевода в ETH: "))
    tamount = amount / 220803,42
    print("=", tamount, " ETH")
    print("При: 1 ETH = 220803,42 KZT")
    print("По данным с сайта pokur.su, на 13.03.2018")
