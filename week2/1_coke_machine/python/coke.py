COKE_PRICE=50
VALID_COINS=[5, 10, 25]

def coke_machine():
    amount = 0
    while amount < COKE_PRICE:
        print('Amount Due: {}'.format(COKE_PRICE - amount))
        coin = input('Insert Coin: ')
        
        if not coin.isnumeric():
            print('Please, input a number')
            continue
        
        coin = int(coin)
        if not coin in VALID_COINS:
            print('Please, input a valid coin ({})'.format(
                ", ".join(str(i) for i in VALID_COINS)
            ))
            continue
        
        amount = amount + coin
    
    print('Total inserted: {}'.format(amount))
    print('Coke price: {}'.format(COKE_PRICE))
    print('Change Owed: {}'.format(amount - COKE_PRICE))