courses = ["Maths", "Chemistry", "Physics", "English"]
courses_2 = ["Commerce", "Accounts", "Business Maths", "English"]

print(len(courses))
print(courses[0])
print(courses[2:])

courses.append("Art") #append
print(courses)

courses.insert(3,"Tamil")  #insert
print(courses)

courses_1 = ["Maths", "Chemistry", "Physics", "English"]
courses_2 = ["Commerce", "Accounts", "Business Maths", "English"]
courses_1.extend(courses_2)  #extend
print(courses_1)

courses.append(courses_2)  # it will add the lists, not the individual elements
print(courses)

courses.remove("Art")  # removes element in the list by str value
print(courses)

courses.pop(5)   # removes element (or list) by index and returns the value
print(courses)

numbers = [3, 1, 5, 2 ,4]  # reverse the indexes
numbers.reverse()
print(numbers)

courses.reverse()
print(courses)

numbers.sort()   # it will modify the original list
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))  # it will return duplicate list 

print(min(courses))

print(max(courses))

print(max(numbers))

print(sum(numbers))

courses_acc = ["Commerce", "Accounts", "Business Maths", "English"]
print(courses_acc.index("Business Maths"))  # returns index position

print("Maths" in courses_acc)  # False
print("English" in courses_acc)  # True

for index, course in enumerate(courses_acc):  # to grab the index and the value
    print(index, course)

for index, course in enumerate(courses_acc, start=1):     # starting index value
    print(index, course)

courses_acc_str = ' - '.join(courses_acc)  # first it will split and then join 
print(courses_acc_str)


new_courses_acc = courses_acc_str.split(" - ")  
print(new_courses_acc)