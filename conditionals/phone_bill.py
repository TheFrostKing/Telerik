
from decimal import Decimal


texts = int(input())
calls = int(input())

text_difference =0
add_text_cost=0
calls_diff =0
add_calls_cost=0
if texts > 20:
    text_difference = texts - 20
    add_text_cost = 0.06 * text_difference

if calls > 60:
    calls_diff = calls - 60
    add_calls_cost = calls_diff * 0.1

add_costs = add_calls_cost + add_text_cost
add_costs_after_taxes= add_costs * 0.2 
total_bill = add_costs_after_taxes+add_costs + 12

print(f"{text_difference} additional messages for {round(Decimal(add_text_cost),2)} levas\n\
{calls_diff} additional minutes for {round(Decimal(add_calls_cost),2)} levas\n\
{round(Decimal(add_costs_after_taxes),2)} additional taxes\n\
{round(Decimal(total_bill),2)} total bill")
