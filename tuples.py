fruits=("apple", "banana", "cherry")
vegetables=("carrot", "broccoli", "spinach")
products=("spaghetti", "rice", "beans")
food=fruits+vegetables+products
food=list(food)

middle_index=len(food)//2
middle=food[middle_index:middle_index+1]
print(middle)
first_three=food[:3]
last_three=food[3:]
del food
check='carrot' in vegetables
print(check)





