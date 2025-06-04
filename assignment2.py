# assignment 2

# problem 1

b = []
for i in range(1,10,2):
    b.append(i)
    print (b)
a = int(input("Insert digit between 0 to 10:- "))

if (a in b):
    print('given number is odd')

else :
    print('given number is even')

# problem 2

a = 0

for i in range(1,51):
    a=a+i

print('The sum of numbers from 1 to 50 is: ' + str(a))
