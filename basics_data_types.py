#student_grades = [9.1, 88, 7.5]
# what can the dir() function do for you? 
# open interactive shell and find out

# how do you find out what the attribute/method does for you?
# dir(str)
# help(str.upper)
# myworld = 'hello'
# myworld.title()

student_grades = {"Mary": 9.1, "Sam":88, "John": 7.5}
mysum = sum(student_grades.values())
length = len(student_grades) # len returns the count in the container/list
mean = mysum / length
print(mean)