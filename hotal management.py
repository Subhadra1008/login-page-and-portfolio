menu = {
    'pizza': 150,
    'pasta': 80,
    'burger': 65,
    'coffee': 30,
    'tea': 20,
    'petties': 30,
    'samosa': 15,
    'coco':50
}

print("Welcome to my restaurant:")
print("'pizza': Rs.150\n'pasta': Rs.80\n'burger': Rs.65\n'coffee': Rs.30\n'tea': Rs.20\n'petties': Rs.30\n'samosa': Rs.15\n'coco':50bur")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ").strip().lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Order item '{item_1}' is not available yet!")

another_item = input("Do you want to add another item? (yes/no): ").strip().lower()
if another_item == "yes":
    item_2 = input("Enter the name of the second item: ").strip().lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Order item '{item_2}' is not available yet!")

print(f"The total amount to pay is Rs.{order_total}")