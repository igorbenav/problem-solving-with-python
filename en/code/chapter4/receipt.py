print("=== Receipt Printer ===", end="\n\n")

store_name = input("Store name: ").strip().title()
customer_name = input("Customer name: ").strip().title()

print()
item1_name = input("Item 1 name: ").strip()
item1_qty = int(input("Item 1 quantity: "))
item1_price = float(input("Item 1 price: "))
item1_valid = True

if item1_qty < 0 or item1_price < 0:
    print("  Invalid: quantity and price must not be negative.")
    item1_valid = False
elif item1_qty == 0:
    print(f"  Skipping {item1_name} (quantity is 0).")
    item1_valid = False

print()
item2_name = input("Item 2 name: ").strip()
item2_qty = int(input("Item 2 quantity: "))
item2_price = float(input("Item 2 price: "))
item2_valid = True

if item2_qty < 0 or item2_price < 0:
    print("  Invalid: quantity and price must not be negative.")
    item2_valid = False
elif item2_qty == 0:
    print(f"  Skipping {item2_name} (quantity is 0).")
    item2_valid = False

print()
item3_name = input("Item 3 name: ").strip()
item3_qty = int(input("Item 3 quantity: "))
item3_price = float(input("Item 3 price: "))
item3_valid = True

if item3_qty < 0 or item3_price < 0:
    print("  Invalid: quantity and price must not be negative.")
    item3_valid = False
elif item3_qty == 0:
    print(f"  Skipping {item3_name} (quantity is 0).")
    item3_valid = False

item1_total = item1_qty * item1_price if item1_valid else 0
item2_total = item2_qty * item2_price if item2_valid else 0
item3_total = item3_qty * item3_price if item3_valid else 0

subtotal = item1_total + item2_total + item3_total

if subtotal >= 100:
    discount_rate = 0.10
    discount_label = "10%"
elif subtotal >= 50:
    discount_rate = 0.05
    discount_label = "5%"
else:
    discount_rate = 0.0
    discount_label = ""

discount = subtotal * discount_rate
after_discount = subtotal - discount

tax_rate = 0.08
tax = after_discount * tax_rate
total = after_discount + tax

width = 35

print()
print("=" * width)
print(f"{store_name:^{width}}")
print("=" * width)
print(f"Customer: {customer_name}")
print("-" * width)
print(f"{'Item':<15} {'Qty':>3} {'Price':>7} {'Total':>7}")
print("-" * width)

if item1_valid:
    p1 = f"${item1_price:.2f}"
    t1 = f"${item1_total:.2f}"
    print(f"{item1_name:<15} {item1_qty:>3} {p1:>7} {t1:>7}")

if item2_valid:
    p2 = f"${item2_price:.2f}"
    t2 = f"${item2_total:.2f}"
    print(f"{item2_name:<15} {item2_qty:>3} {p2:>7} {t2:>7}")

if item3_valid:
    p3 = f"${item3_price:.2f}"
    t3 = f"${item3_total:.2f}"
    print(f"{item3_name:<15} {item3_qty:>3} {p3:>7} {t3:>7}")

print("-" * width)
sub_str = f"${subtotal:.2f}"
print(f"{'Subtotal:':>27} {sub_str:>7}")

if discount_rate > 0:
    disc_str = f"-${discount:.2f}"
    print(f"{'Discount (' + discount_label + '):':>27} {disc_str:>7}")
    after_str = f"${after_discount:.2f}"
    print(f"{'After discount:':>27} {after_str:>7}")

tax_str = f"${tax:.2f}"
total_str = f"${total:.2f}"
print(f"{'Tax (8%):':>27} {tax_str:>7}")
print("=" * width)
print(f"{'TOTAL:':>27} {total_str:>7}")
print("=" * width)
print(f"{'Thank you for your purchase!':^{width}}")
