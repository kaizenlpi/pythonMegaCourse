# Create a mean/average function 

#def name(parameter, parameter, etc). Parameters are inputs for your function to produce some output. 

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5])) # This line executes your code. Print the mean of the list.
print(type(mean), type(sum)) 