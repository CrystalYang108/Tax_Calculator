# Feel free to code your definitions here in order to separate your concerns.
all_items = []
shopping = True
while shopping == True:
    enter = input("Enter the price of your first item:")
    print("The price of your item is $" + enter)
    enter = float(enter)
    def calculatetax(enter):
        tax = .08875
        return enter * tax
    tax_cost = calculatetax(enter)
    print("The tax of your item is $" + str(tax_cost))
    
    sum = tax_cost + enter
    print("The total price is $" + str(sum))
    enter2 = input("Do you want to enter another item?")
    if enter2 != "Yes":
        shopping = False
