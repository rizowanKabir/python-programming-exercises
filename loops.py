for i in 1,2,3,4,5:
    print("Round:",i) 

# 2nd example.

scores = [10,20,30,40,55,66]
total = 0

for score in scores:
    total += score
    print("Current total:",total)
print("Final Total:",total)     

# 3rd example.

files = [" Report.csv ", " DATA.csv ", " final.TXT "] 

for file in files:
    file = file.strip().lower().replace(".txt",".csv")
    print("Processing:",file) 

# Challenge time -1

number = 7
for i in range(1,11):
    print(f"{i} X {number} = {i * number}")

# Challenge time -2

pyramid = "*"
for i in range(1,7):
    print(pyramid * i)  

# Break statement

names = ["shakil","shagor","","Sobuj"]

for name in names:
    if name == "":
        print("Empty value detected!.")
        break
    print("Name:",name) 

# Continue statement.

days = ['Mon','Tue','Wed','Sat','Sun']

for day in days:
    if day in ['Sun','Sat']:
        continue
    print(f"Work Days: {day}") 

# Nested loops

for x in range(3):
    for y in range(2):
        print(f"({x},{y})") 

colors = ["red","green","Blue"]
sizes = ["S","M",'L']

for color in colors:
    for size in sizes:
        print(f"{color} - size {size}") 

years = [2026,2027]
months = ["Jan","Feb"]
days = range(1,29)

for year in years:
    for month in months:
        for day in days:
            print(f"report_{year}_{month}_{day}.csv") 

# While loops

count = 1

while count <= 5:
    print(count)
    count += 1 

answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ").lower()
print("Thank You!")     

attempts = 0

while attempts < 3:
    answer = input("Do You Agree?(yes/no): ").lower()
    if answer == "yes":
        print("Glad we are on the same page.")
        break
    attempts += 1
else:
    print(f"{attempts} Strikes you.You will be out.")    


