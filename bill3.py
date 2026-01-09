bill_items = []
grand_total = 0
item_count = 0

while True:
    item_count += 1
    print(f"item {item_count}")

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

    if item_count >= 2:
        choice = input("Want to keep going? \n Press 'c' to continue or 'q' to quit: ").lower()
        if choice == 'q':
            break

print("\nGrocery Bill Details:")
for item in bill_items:
    print(item)

print("\nGrand Total:", grand_total)
