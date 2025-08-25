furniture = ['sofa', 'table', 'chair', 'bed', 'desk']
cost = [500, 200, 100, 800, 150]

furniture_required = 'sofa'
quantity_purchased = 2

bill_amount = 0

if furniture_required in furniture and quantity_purchased > 0:
    index = furniture.index(furniture_required)
    price = cost[index]
    bill_amount = price * quantity_purchased
    print(f"The bill amount for {quantity_purchased} {furniture_required}(s) is: ${bill_amount}")
else:
    print("Invalid furniture or quantity. Bill amount is $0.")

furniture_required = 'lamp'
quantity_purchased = 1

bill_amount = 0

if furniture_required in furniture and quantity_purchased > 0:
    index = furniture.index(furniture_required)
    price = cost[index]
    bill_amount = price * quantity_purchased
    print(f"The bill amount for {quantity_purchased} {furniture_required}(s) is: ${bill_amount}")
else:
    print("Invalid furniture or quantity. Bill amount is $0.")

furniture_required = 'chair'
quantity_purchased = 0

bill_amount = 0

if furniture_required in furniture and quantity_purchased > 0:
    index = furniture.index(furniture_required)
    price = cost[index]
    bill_amount = price * quantity_purchased
    print(f"The bill amount for {quantity_purchased} {furniture_required}(s) is: ${bill_amount}")
else:
    print("Invalid furniture or quantity. Bill amount is $0.")