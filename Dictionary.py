person = {"Name":"Karthik", "Age":26, "Gender":"Male", "Status":"Single"}

print(person["Name"])  #get individual values   # returns key error person["Nationality"]

print(person.get("Age")) # if you are trying to access the key which is not present will return
                         # an key error in indexing. but in get it will return "None"

print(person.get("Nationality"))    # returns "None"

print(person.get("Nationality", "NotFound")) 

person["Number"] = "9600-XXX-XXX"
print(person)

person["Name"] = "Cathrine"   # update the existing value
print(person)

person.update({"Age":23, "Gender":"Female", "Status":"Divorced"})
print(person)

del person["Number"]
print(person)

age = person.pop("Age")   # dict pop = key ; list pop = index
print(age)

print(person.keys())
print(person.values())
print((person.items()))

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
