#converting datatype

weekly_rate = input("weekly pay")

weekly_rate = float(weekly_rate)

print("Your weekly pay is", weekly_rate)

#Display bi-weekly pay
print("Every two weeks you make", "$", weekly_rate * 2)


#see what the datatype is for a variable
print(type(weekly_rate))