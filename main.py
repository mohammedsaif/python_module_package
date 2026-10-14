import calculator
from shop.billing import calculate_discount
from shop.product import get_products

#from calculator import add

#import calculator as cal
#cal.add
import math

product = get_products()

price = product["price"]

final_price = calculate_discount(price,10)


products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Phone", "price": 20000},
    {"name": "Headphones", "price": 3000}
]

for product in products:
    price = product["price"]
    final_price = calculate_discount(price,10)
    print("product",price)
    print("final_price",final_price)
print(product)
print(price)
print(final_price)


print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(calculator.add(10,5))
print(calculator.sub(10,5))
print(calculator.mul(10,5))