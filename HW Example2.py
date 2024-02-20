#name
#date
#program detail - input/output


#Street is a string datatype
street = input("What street do you live on? ")

#convert to int() in the same line
house_num = int(input("What is your house number? "))

#calculate neighbor number
neigh_num = house_num + 2

#print our address & neighbors
print("Your address is", house_num, street)
print("Your neighbor's address is", neigh_num, street)