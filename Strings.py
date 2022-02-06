print("Hello World")

message = 'My name is karthik.. and i am 33 years old'
print(message)

print(len(message))

print(message[3:7])

print(message.upper())

print(message.lower())

print(message.count("r"))

print(message.find("and"))     #returns starting index

print(message.find("universe"))  #returns -1

message = message.replace("33","25")
print(message)

greeting = 'Hello'
name = 'Karthik'

message2 = greeting + ", " + name + ". Welcome!"
print(message2)

message3 = '{}, {}. Welcome!'.format(greeting,name)
print(message3)

message4 = f'{greeting}, {name}. Welcome!'
print(message4)

message4 = f'{greeting}, {name.upper()}. Welcome!'
print(message4)

#print(dir(name))   #gives all the method linked with vairable

#print(help(str))

print(help(str.format))  # no () 