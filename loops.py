
names = ['dani','ran','suzi','moshe']
#print(names[0].upper())
#print(names[1])

# for loop
# foreach loop
# while
# do
name = 'dani'
name = names[0]
name = 'ran'
name = names[1]
name = 'suzi'
name = names[2]
# name <- put inside the next in line ...
    # 1 print(name)
    # 2 print(name.upper())
    # 3
    # 4
    # ...
for name in names:
    print(name.upper())

numbers = [5, 80.2, -5, 22, 123.2]
sum_list = 0
for number in numbers:
    print(int(number))
    sum_list = sum_list + number
print(f'sum of {numbers} = {sum_list}. python say :', sum(numbers))
print('after foreach loop')

# ['h','e','l','l','o']
for c in "hello":
    print(c.upper())

for x in [4,-10,100,200]:
    print(f'{x} * 2 = {x * 2}')

grades = [80.1, 100 , 'aaa', 70, -1000, 40, 33]
sum_grades  = 0
counter = 0
for grade in grades:
    if str(grade).isalpha():
        continue # jump to next iteration. to next item
    if grade == -1000:
        break # will not continue in the loop. break free!!
    sum_grades = sum_grades + grade
    counter = counter + 1

#avg = sum_grades / len(grades)
avg = sum_grades / counter
print(f' average of {grades} for {counter} students == {avg}')






