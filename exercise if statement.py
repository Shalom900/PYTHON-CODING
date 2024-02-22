Price = 1000000
Price_3 = 2000000
has_good_credit = True

if Price:
    down_payment = 0.1 * Price
    Upper_payment = 0.1 * Price * Price_3

elif Price_3:
    Upper_payment = 0.1 * Price * Price_3
    
else:
    down_payment = 0.2 * price

print(f"Down payment and Upper_Payment: {down_payment} {Upper_payment}]")

