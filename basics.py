# x = 10
# y = "10" # using quotes with a number tells python interpreter this is a string/text. 
# z = 10.1

# sum1 = x + x
# sum2 = y + y

# print(sum1, sum2)
# print(type(x), type(y), type(z)) #using the type() function tells you what the type of each value is. 

# you can list integers, strings, and a list in a list. 
#student_grades = [9.1, "hello", [1,2,4.33]]

# list is a class. converts the range into a class datatype to make the range more readable. 
student_grades = list(range(0, 11))
print(student_grades)

# autogenerate list of integers in certain order
# example of printing out a bracketed list aka array, which is a list too. 
temperatures = [3.2,2, "Texas"]
print(temperatures)

rainfall = [2.1,5,"Texas",[1,2,33]]
print(rainfall)