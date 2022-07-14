#Prajwal Gurung 
#Chapter 2 Quiz Solutions

#Q0201 Solutions
#1
x = 55
print(x)
#2
x = 60
#3
print(x+10)

#Q0202 Solutions
#1
x = 20
#2
y = 5.8
#3
print(type(x))
print(type(y))

#Q0203 Solutions
first_name = "Prajwal " 
last_name = "Gurung"
#1
print("My name is " + first_name + last_name)

#2
print("My name is {}{}".format(first_name, last_name))

#3
print(f"My name is {first_name}{last_name}")

#4
print("My name is %s%s" % (first_name, last_name))

#Q0204 Solutions
#1
pi = 3.14159265
print(f"{pi:.3f}")

#2
print(f"{pi:_>10.2f}")

#3
print(f"The value of PIE is {pi:.2f}")

#Q0205 Solutions
#1
#name = input("What is your name? ")
#2
#age = input("What is your age? ")
#3
#print(f"Hello! My name is {name} and I am {age} years old.")

#Q0206 Solutions
#1
x = 5
y = 5
print(x+y)

#2
x = 5
y = 5.5
print(x+y)

#3
x = 5.5
y = 6.5
print(x+y)

#4
x = "Hello "
y = "world"
print(x+y)

#5
# x = 5
# y = "hello"   
# print(x+y)        #prints out an error as + opperand does not support 'int' and 'str'

#Q0207 Solutions
import math
#1
print(math.sqrt(10))

#2
print(pow(10,20))

#3
print(100//30)

#4
print(1289%25)

#Q0208 Solutions
x = 10
y = 12
#1
print(x > y)

#2
print(x < y)

#3
print(x >= y)

#4
print(x <= y)

#5
print(x+2 == y)

#6
print(x+2 != y)

#Q0209 Solutions
weather_cloudy_today = True
rain_yesterday = True
rain_today = weather_cloudy_today and rain_yesterday

print("Is it going to rain today?", rain_today)

#Q0210 Solutions
#1
print(type(12) is int)

#2
print(type(100/12) is float)

#3
