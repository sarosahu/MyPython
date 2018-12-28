
from decimal import Decimal

#Doing currency calculations

tax_rate = Decimal('7.25')/Decimal(100)
purchase_amount = Decimal('2.95')
print(tax_rate*purchase_amount)

#To round to the nearest penny, create a penny object:
penny = Decimal('0.01')

total_amount = purchase_amount + tax_rate*purchase_amount

print("Total amount : ",total_amount)
print("total_amount.quantize(penny) : ",total_amount.quantize(penny))
