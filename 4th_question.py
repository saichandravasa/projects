# finding the bigget value from the input data

a = int(input('enter 1st number : '))
b = int(input('enter 2nd number : '))

if a == b:
    print('both numbers are same.... give another number to find which is big ')
elif a>b:
    print(a,'is bigger than',b)
else:
    print(b,'is bigger than',a)
