# 5_data structures_dictionary.py

# ------- dictionary : key-value pair

product1 = {
    "title": "Snow white story book",
    "price": 200,
    "rating": 7.8,
    "languages": ["Eng", "Urdu", "Germen"],
    "isUsed": True 
}

print(product1)
print(product1["title"])
# print(product1["stock"]) # error
print(product1.get("price"))
print(product1.get("stock"))

product1["stock"] = 25
print(product1)

print(len(product1))

print("stock" in product1)
print("discount" in product1)

print(product1["languages"][1])

for key in product1:
    print(f"{key} is {product1[key]}")


