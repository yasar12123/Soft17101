class Bakery:
    """
    A class to store bakery orders.
    """
    def __init__(self, itemType, quantity, pricePerItem, deliveryDate):
        self.itemType = itemType
        self.quantity = quantity
        self.pricePerItem = pricePerItem
        self.deliveryDate = deliveryDate

    def get_invoice(self):
        return self.pricePerItem*self.quantity

    def __str__(self):
        return ('\n' "Item: " + self.itemType +
                '\n' "Quantity: " + str(self.quantity) +
                '\n' "Unit Price: " + str(self.pricePerItem) +
                '\n' "Delivery Date: " + self.deliveryDate +
                '\n' "Total Amount: " + str(self.get_invoice()) )

    def update_quantity(self, newQuantity:int):
        if newQuantity < 0:
            raise ValueError("The input quantity %d cant be less than 0" %newQuantity)
        self.quantity = newQuantity
        return self.quantity

    def get_item(self):
        return print(self.itemType)

    def get_quantity(self):
        return print(self.quantity)

    def invoice_test(self):
        return print(self)


# orders
order1 = Bakery("baguettes", 50, 1.20, "01/02/2023")
order2 = Bakery("coke", 100, 2.25, "01/02/2023")


#order1.update_quantity(30)
#order1.get_item()
#order1.get_quantity()

#print(order1)
#print(order2)

#order1.invoice_test()

print(order1.__str__())