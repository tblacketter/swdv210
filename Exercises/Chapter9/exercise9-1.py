#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    shipping_rate = Decimal(".085")
    shipping_cost = subtotal * shipping_rate
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax + shipping_cost

    lc.setlocale(lc.LC_ALL, "en_US")
    order_total = lc.currency(order_total, grouping = True)
    invoice_total = lc.currency(invoice_total, grouping = True)

    # display the results
    s1 = ">10"
    s2 = 20
    s3 = "10,"
    print(f"{'Order total:':{s2}} {order_total:{s1}}")
    print(f"{'Discount amount':{s2}} {discount:{s3}}")
    print(f"{'Subtotal':{s2}} {subtotal:{s3}}")
    print(f"{'Shipping cost':{s2}} {shipping_cost:{s1}}")
    print(f"{'Sales tax':{s2}} {sales_tax:{s3}}")
    print(f"{'Invoice total':{s2}} {invoice_total:{s1}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
