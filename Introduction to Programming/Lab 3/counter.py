import sys
try:
    start = int(input("Start >> "))
    end = int(input("End >> "))
    step = int(input("Step >> "))
except:
    print("Integers only!")
    sys.exit()

for i in range(start, end+1, step):
    print(i)
