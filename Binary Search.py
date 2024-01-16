
import random

def main():

    worklist = []

    for i in range(random.randint(0,13)):
        worklist.append(random.randint(0,13))

    span = len(worklist) - 1
    if span == 0:
        return 0
    random_index = worklist[random.randint(0,span)]

    print(f'looking for {random_index} in worklist')

    low_number = 0
    high_number = span

    while high_number > low_number:
        middle = (low_number + high_number) // 2
        middle_value = worklist[middle]
        print(worklist)
        print(middle_value)


if __name__ == '__main__':
    main()

