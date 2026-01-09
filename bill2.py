bill_items = []
grand_total = 0

num_items = int(input("How many items do you want to enter? "))

for i in range(num_items):
    print(f"Item {i + 1}")

    item = {}

    item_name = input("Enter item name: ")
    item_price = float(input("Enter price: "))
    item_quantity = int(input("Enter quantity: "))

    total_cost = item_price * item_quantity
    grand_total += total_cost

    item["item"] = item_name
    item["price"] = item_price
    item["quantity"] = item_quantity
    item["total"] = total_cost

    bill_items.append(item)

print("Grocery Bill Details:")
for item in bill_items:
    print(item)

print("Grand Total:", grand_total)
