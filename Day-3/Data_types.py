#Data types
#Numeric type
#int
product_quantity = 3
order_id = 10987432
print("order_id",order_id)

#float
product_price = 749.99
discount_percentage = 15.5
average_rating = 4.3
print(average_rating)

#Complex
z = 5 + 2j # Not commonly used in typical e-commerce workflows
print(z)

#sequence type
#str
customer_name = "Rohit Sharma"
delivery_address = "Bangalore, Karnataka"
product_category = "Electronics"
print(customer_name)

#list
L=["Shoes","T-shirt"]
print(L)

#tuple
warehouse_location = (12.9716, 77.5946) # Latitude and Longitude
product_dimensions = (12.5, 9.8, 2.2) # Length, Width,Height in inches
print(product_dimensions)

#Set Types
#set
available_sizes = {"S", "M", "L", "XL"}
popular_brands = {"Nike", "Adidas", "Puma", "Nike"} # 'Nike'only once
print(popular_brands)

#frozenset-Immuntable set
frozen_tags = frozenset(["Sale", "Limited Edition",
"Trending"])
print(frozen_tags)

#Mapping
#dict
product_details = {
"name": "Wireless Mouse",
"brand": "Logitech",
"price": 899.99,
"rating": 4.5
}
customer_profile = {
"name": "Anjali Verma",
"email": "anjali@example.com",
"prime_member": True
}
print(product_details,customer_profile)

#Boolean
#bool
is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(is_logged_in)

#None Type
tracking_number = None
delivery_partner = None
print(tracking_number)
