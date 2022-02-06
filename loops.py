num = [1,2,3,4,5]
num2 = [1,2,3,4,5]
char = ["a","b","c"]

print(num is num2)
print(id(num))
print(id(num2))

#use and , or & not operators in loop

for i in num:
    print(i)

for i in num:
    for j in char:
        print(j, end=" ")   # break and continue