
def discount(product):
    for i in range(len(product)):
        productDictIter = product[i]
        productExpiryDate = productDictIter.get('expiration_date')
        productPrice = productDictIter.get('price')
        if productExpiryDate == 'today':
            productPrice = round(productPrice - ((productPrice / 100.0) * 30), 2)
        print(productPrice)


productsListDict = [{'milk': '1', 'expiration_date': 'today', 'price': 1.45},
                    {'organic milk': '2', 'expiration_date': 'tomorrow', 'price': 2.15},
                    {'filtered milk - whole': '3', 'expiration_date': 'tomorrow', 'price': 1.95},
                    {'filtered milk - skimmed': '4', 'expiration_date': 'today', 'price': 1.85}, ]


productIteration = productsListDict[0]
keys = productIteration.get('expiration_date')

discount(productsListDict)