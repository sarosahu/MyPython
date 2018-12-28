from decimal import Decimal
from fractions import Fraction

total_amount = Decimal('3.163875')

print(float(total_amount))

sugar_cups = Fraction('2.5')
scale_factor = Fraction(5/8)

print(float(sugar_cups * scale_factor))
