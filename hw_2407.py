

######################################### Question 10 + 11
# input formula from user
formula = input("Enter formula:") # 3 + 4 = 7

l1 = formula.split()
# ['3', '+', '4', '=',' '7']

# l1[0] = '3' -- x
# l1[1] = '+' -- oper
# l1[2] = '4' -- y
# l1[3] = '='
# l1[4] = '7' -- sum
# check if formula syntax is correct
if len(l1) != 5:
    print('bad formula. should be like: 3 + 4 = 7')
elif not l1[1] in ['+','*','-','/']:
    print('bad formula sign. should be + - * /')
elif not l1[3] == '=':
    print('bad formula. mising =')
else:
    # check if formula is true or false
    x = float(l1[0])
    oper = l1[1]
    y = float(l1[2])
    sum = float(l1[4])
    if oper == '+':
        if sum == x + y:
            print(f'formula: {formula} -- is correct')
        else:
            print(f'formula: {formula} -- is INCORRECT')
    elif oper == '-':
        if sum == x - y:
            print(f'formula: {formula} -- is correct')
        else:
            print(f'formula: {formula} -- is INCORRECT')
    elif oper == '*':
        if sum == x * y:
            print(f'formula: {formula} -- is correct')
        else:
            print(f'formula: {formula} -- is INCORRECT')
    elif oper == '/':
        if sum == x / y:
            print(f'formula: {formula} -- is correct')
        else:
            print(f'formula: {formula} -- is INCORRECT')


######################################### Question 9
# input 3 numbers from user
x = int(float(input("enter 1 number:")))
y = int(float(input("enter 2 number:")))
z = int(float(input("enter 3 number:")))

# compare numbers and print biggest
# check if x is biggest
# else check if y is biggest
# else -- z is biggest
#         +        *
if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)


######################################### Question 8
# input 2 numbers from user
x = int(float(input("enter 1 number:")))
y = int(float(input("enter 2 number:")))

# compare numbers and print biggest
if x > y:
    print(f'{x} is bigger than {y}')
elif y > x:
    print(f'{y} is bigger than {y}')
else:
    print(f'{x} == {y}')

# compare numbers and print biggest -- more accurate
if x > y:
    print(x)
elif y > x:
    print(y)

big = x
if y > x:
    big = y
print(big)

print('finish')

