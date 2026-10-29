# Transformation, Concatenation,

phone = "017731-55-468"
print(phone.replace("-","/"))

price = "$12,200030.00"
print(price.replace("$","").replace(",",""))

number = "+49 (176) 123-4567"
print(number.replace("+","0 0").replace(" ","").replace("(","").replace(")","").replace("-","").replace(""," "))

print(f"{{This is me}}") 

stamp= "2026-10-06,1:00"
print(stamp.split("-")) 

# Whitespace cleaning

text = " Engineering"

print(text.lstrip())

variable = "968-Maria, ( Data Engineer ) ;; 27y  "

clean = (variable.replace("968","name:").replace(","," |").replace("(","role: ").replace("-"," ").replace(" "," ").replace(")","").replace(";;","| age:"))
final = clean.lower()
print(final.strip()) 

