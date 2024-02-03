'''Part One'''
Expenses = []

Expenses.append(2200)
Expenses.append(2350)
Expenses.append(2600)
Expenses.append(2130)
Expenses.append(2190)

print(Expenses)

print("The difference between February and January is:", Expenses[1] - Expenses[0])

First_Quarter = 0
for i in range(3):
    First_Quarter = First_Quarter + Expenses[i]

print("The total Expenditures for the first quarter are:", First_Quarter)

for index, month in enumerate(Expenses):
    if month == 2000:
        print(f"2000 dollars spent in {index}th month")
if 2000 not in Expenses:
    print("In no month did you spend exactly 2000 dollars.")

Expenses.append(1980)

print("After June's expenses, we have updated our array to the following:", Expenses)

Expenses[3] = Expenses[3] - 200

print("After April's return, the expense list is the following:", Expenses)

print("--------------")

'''Part Two'''

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print("The list has this many elements:", len(heros))

heros.append('black panther')
print(heros)
heros.pop()
print(heros)
heros.insert(3, 'black panther')
print(heros)
heros = heros[:1:] + ['doctor strange'] + heros[3::]
print(heros)
heros = sorted(heros)
print(heros)
print("-------")

''' part 3 '''
###Compile list of odd numbers in a user defined range

length_of_list = int(input('Please give an integer input above 0: '))
odds_list = []
if length_of_list > 0:
    for i in range(length_of_list + 1):
        if not i % 2 == 0:
            odds_list.append(i)

    print(odds_list)
else:
    print('List cannot have zero values')