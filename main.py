# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().intputNumber("Please enter unit price : ")
    qnt = Invoice().intputNumber("Please enter quantity of product : ")
    discount = Invoice().intputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products)

print("Your total pure price is : ", total_amount)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
