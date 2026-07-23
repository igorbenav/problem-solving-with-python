print("=== Receipt Printer ===", end="\n\n")

store_name = input("Store name: ").strip().title()
customer_name = input("Customer name: ").strip().title()
print()

item1_name = input("Item 1 name: ").strip()
item1_qty = int(input("Item 1 quantity: "))
item1_price = float(input("Item 1 price: "))

item2_name = input("Item 2 name: ").strip()
item2_qty = int(input("Item 2 quantity: "))
item2_price = float(input("Item 2 price: "))

item3_name = input("Item 3 name: ").strip()
item3_qty = int(input("Item 3 quantity: "))
item3_price = float(input("Item 3 price: "))

item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
item3_total = item3_qty * item3_price

subtotal = item1_total + item2_total + item3_total
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax

width = 35

print()
print("=" * width)
print(f"{store_name:^{width}}")
print("=" * width)
print(f"Customer: {customer_name}")
print("-" * width)

print(f"{'Item':<15} {'Qty':>3} {'Price':>7} {'Total':>7}")
print("-" * width)

p1 = f"${item1_price:.2f}"
t1 = f"${item1_total:.2f}"
print(f"{item1_name:<15} {item1_qty:>3} {p1:>7} {t1:>7}")

p2 = f"${item2_price:.2f}"
t2 = f"${item2_total:.2f}"
print(f"{item2_name:<15} {item2_qty:>3} {p2:>7} {t2:>7}")

p3 = f"${item3_price:.2f}"
t3 = f"${item3_total:.2f}"
print(f"{item3_name:<15} {item3_qty:>3} {p3:>7} {t3:>7}")

print("-" * width)
sub_str = f"${subtotal:.2f}"
tax_str = f"${tax:.2f}"
total_str = f"${total:.2f}"
print(f"{'Subtotal:':>27} {sub_str:>7}")
print(f"{'Tax (8%):':>27} {tax_str:>7}")
print("=" * width)
print(f"{'TOTAL:':>27} {total_str:>7}")
print("=" * width)
print(f"{'Thank you for your purchase!':^{width}}")
