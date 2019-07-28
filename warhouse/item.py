class Item:
    id = 0
    title = ''
    category = ''
    price = 0
    stock = 0
    Iid = 0

    def __init__(self, id, title, category, price, stock, Iid):
        self.id = id
        self.title = title
        self.category = category
        self.price = price
        self.stock = stock
        self.Iid = Iid
