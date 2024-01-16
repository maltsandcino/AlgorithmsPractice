
import random

def main():

    worklist = []

    for i in range(random.randint(0,13)):
        worklist.append(random.randint(0,13))

    span = len(worklist)
    if span == 0:
        return 0
    random_index = worklist[random.randint(0,span)]

    print(f'looking for {random_index} in worklist')


if __name__ == '__main__':
    main()

