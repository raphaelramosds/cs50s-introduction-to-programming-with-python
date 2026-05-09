COKE_PRICE = 50
VALID_COINS = [5, 10, 25]

# NOTE: Because `invoice` is a mutable object, the changes inside `process` will be reflected in the caller's scope. 
#       This is basically how modifying by reference works in Python.
def process(coin: str, invoice: dict) -> bool:
    if not coin.isnumeric():
        print("Please, input a number")
        return False

    coin = int(coin)
    if not coin in VALID_COINS:
        print(
            "Please, input a valid coin ({})".format(
                ", ".join(str(i) for i in VALID_COINS)
            )
        )
        return False

    invoice["total_inserted"] = invoice["total_inserted"] + coin
    if invoice["total_inserted"] >= COKE_PRICE:
        invoice["change"] = invoice["total_inserted"] - COKE_PRICE

    return True


def coke_machine_static(inputs: list) -> dict:
    """
    Testable version of coke_machine which does not depend upon stdin
    """
    invoice = {"total_inserted": 0, "coke_price": COKE_PRICE, "change": 0}
    
    for coin in inputs:
        if not process(str(coin), invoice):
            continue

    return invoice


def coke_machine() -> None:
    invoice = {"total_inserted": 0, "coke_price": COKE_PRICE, "change": 0}

    while invoice["total_inserted"] < COKE_PRICE:
        print("Amount Due: {}".format(COKE_PRICE - invoice["total_inserted"]))
        coin = input("Insert Coin: ")
        if not process(coin, invoice):
            continue

    print("-" * 10)
    print("Total inserted: {}".format(invoice["total_inserted"]))
    print("Coke price: {}".format(COKE_PRICE))
    print("Change Owed: {}".format(invoice["change"]))
