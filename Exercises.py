## Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
           
def number(num1, num2):
    
    for num in range (1500, 2701):
        list_values = []
        if (num % 7 == 0) and (num % 5 == 0):
            #values.append(num)
            #print(num, end=" ")
            list_values.append(num)

    print(list_values)        
          
            
func = number(1500,2701)
# print(func)
#----------------------------------------------------------------------------------#

# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

def temp(value, scale):
    
    if scale == "F" or "f":
        C = 5*((value-32)/9)
        return round(C, 2)
    elif scale == "C" or "c":
        F = (9*(value/5)) + 32
        return  round(F, 2)
    else:
        return "Please enter valid scale"    

temp1 = temp(60, "C")
temp2 = temp(45, "F")
print(temp1) 
print(temp2)   





