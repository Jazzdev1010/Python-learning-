bill_items =[]

item={}
item_name = input("Enter item name: ")
item_price = float(input("Enter price: "))
item_quantity = int(input("Enter quantity: "))

total_cost = item_price * item_quantity

# storing values in dictionary
item["item"] = item_name
item["price"] = item_price
item["quantity"] = item_quantity
item["total"] = total_cost

# appending dictionary to tuple
bill_items.append(item)
print("Bill details:")
print(bill_items)