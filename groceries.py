
Groceries = ["Milk", "Apples", "Cheese", "Bread"]
Price = [18, 8, 45, 23]

price_of_groceries = {Groceries[i]: Price[i] for i in range(0, len(Groceries))}

Wallet = 300


def shopping():
    shopping = Wallet - sum(Price)
    return shopping


print(price_of_groceries)
print(shopping())
