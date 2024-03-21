#DevonPoole
#3/21/24
#P3HW2
#Calculating employee pay for hours worked


reg_hrs = <40
name = input("Enter employee's name: ")
totalhrs = (int(input("Enter number of hours worked: ")
payrate = (float(input("Enter employee's pay rate: ")
                 
print("------------" * 7)

print("Employee name: ", name)

print("Hours Worked     Pay Rate        OverTime Hours      OverTime Pay        RegHour Pay         Gross Pay")

print(f'{totalhrs} {payrate} {totalhrs - reg})