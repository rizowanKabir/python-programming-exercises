print("=" * 30)
print("Python Build in Data Structure.")
print("=" * 30) 

empty = []
print(empty)

letters = "Python"
print(list(letters))
print(type(letters))

number = list(range(5))
print(number)

# Empty list
empty_more_list = []
empty_list = list()
print(type(empty_list))

# Access & Read List 

lst = ['a','b','c','d']
print(lst)
print(lst[0])
print(lst[3]) 

matrix = [['a','b','c'],['d','e','f'],['g','h','i']]
print(matrix)
print(matrix[0][0]) 

# Unpacking the list.

personal_information = ["Kabir",26,"Python Developer","Bangladesh"]

name,age,role,country = personal_information
print("Name:",name)
print("Age:",age)
print("Role:",role)
print("Country:",country) 

# Explore & Analyze.

numbers = [1,5,3,2,4]

print("Max:",max(numbers))
print("Min:",min(numbers))
print("Sum:",sum(numbers))
print("Len:",len(numbers))
print("count:",numbers.count(2)) 

letters = ["a","b","c","d"]
letters.append("f")
letters.insert(0,"A")
print(letters)

# Copying List 

numbers = [10,20,30]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator)) 

price = lambda x: x * 2
print(price(2)) 

prices = [100,120,101,130,99]

print(list(filter(lambda p: p >= 100,prices))) 

domains = [
    'www.google.com',
    'openai.com',
    'localhost',
    'WWW.DATAWITHBARA.COM'
]

cleaned = [d.lower().replace('www.','') for d in domains if '.'in d] # List comprehension
print(cleaned) 

# Tuple 

my_tuple = (10,30,20,40)
print(type(sorted(my_tuple))) 

# Sets 

a = {10,30,20,10,40}
b = {40,50,60,50,70}

print(a.union(b)) # Union
print(a | b) 

# Dictionary all the things

my_dict = {
    'a':10,
    'b':20,
    'c':30
}

print(my_dict) # dictionary is ordered  

user = {'id':1,'age':25,'country':'Dhaka'}

print('age' in user)
print('name' not in user) 

print(user.keys())
print(user.values())
print(user.items())

for key,value in user.items():
    print(key,value)

for u in user:
    print(u,user[u])    

# Add, Update, Remove

user["name"] = "Kabir" # Add
user['age'] = 35 # Update single data
user.update({"age":35,"name":"sohag"}) # Update multiple data
age = user.pop("age")
print(user) 
print("Remove item is:",age) 







