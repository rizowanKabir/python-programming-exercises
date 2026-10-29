print("Wake up")
print("Coffee machine")
print("Make coffee")
print("Enjoy it")
print("Working for a while")
print("Make coffee")
print("Enjoy it for a long.")
print("I am enjoying a lots")


def clean_name(name):
    print(name.strip().lower())
clean_name("Hello    ")    

# Building full name & clean function 

def full_name(first_name,last_name,country):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_names = first + " " + last
    print(full_names," " + "From" +" ",country)

#Positional Arguments
full_name("Kabir","Rizowan","Norawy")  

#Keyword Arguments
full_name(first_name="Rizowan",last_name="Kabir",country="Norway") 




