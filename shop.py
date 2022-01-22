class order():
    total = 0
    price = 35

    def __init__(self, amount=1, spicy=False):
        self.amount=amount
        self.spicy=spicy
        order.total += amount

    