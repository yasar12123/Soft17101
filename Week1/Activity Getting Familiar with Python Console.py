#0 vat calc
item_location = input("is the item located outside of the UK?")
item_type = input("is the item a book or document?")
purchase_price = float(input("what is the purchase price?"))
if item_location == "yes" and item_type == "no": print("VAT required, The total cost of the item is: " + str(purchase_price*1.2))
else: print("No VAT required, The total cost of the item is: " + str(purchase_price))



#1. convert hours into minutes#
hours = float(input("what is the number of hours you want to convert to minutes"))
print("There are " + str(hours*60) + " minutes in " + str(hours) + " hours")


#2. cost of expenses
loop = int(input("Number of Expenses: "))
expenses_name = []
expenses_list = []
count = -1
for expen_name_list in range(loop):
    count+=1
    expenses_name.append(input("Name of Expenditure: "))
    expenses_list.append(input("Cost of " + str(expenses_name[count]) + ": " ))

print(sum([float(x) for x in expenses_list]))


