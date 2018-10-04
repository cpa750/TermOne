from math import ceil

total = float(input("Enter the total bill amount: "))

print("15% tip:", total*0.15, sep=" ")
print("20% tip:", total*0.2, sep=" ")

print("15% tip, bill rouded up:", round(ceil(total)*0.15, 2), sep=" ")
print("20% tip, bill rouded up:", round(ceil(total)*0.2, 2), sep=" ")
