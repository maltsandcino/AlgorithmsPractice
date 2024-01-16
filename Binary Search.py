
import random

def main():

    worklist = []

    for i in range(random.randint(0,13)):
        worklist.append(random.randint(0,13))
    
    if not worklist:
        quit()

    worklist.sort()

    span = len(worklist) - 1
    if span == 0:
        exit()

    lowest_value = worklist[0]

    print(f"Randomly Generated List: {worklist}")
    print("-----")
  
    for i in range(random.randint(0,span)):
        value = worklist.pop(0)
        worklist.append(value)    
    print(f"List is rotated, moving one spot each time, randomly: {worklist}")
    print("------")
   
    print(f'looking for {lowest_value} in worklist:')
    print("------")

    ###Find the first instance of the lowest number in sorted list

    low_number = 0
    high_number = span
    found = False

    while found == False:
        middle = (low_number + high_number) // 2
        middle_value = worklist[middle]
        low_value = worklist[0]
        high_value = worklist[span]

        if low_value < high_value:
            print("Array has not been rotated, position 0 is answer.")
            found = True
        
        elif low_value == high_value and len(worklist) == 2:
            print("Array has not been rotated, position 0 is answer.")
        
        elif low_value == high_value and worklist[span] < worklist[span - 1]:
            print(f"The answer is at position {span - 1}")

        elif span == 1:
            print("Array contains one number, cannot be rotated.")

        elif middle > 0 and middle_value < worklist[middle - 1]:
            print(f"The answer is {middle_value} at position {middle}")
            found = True

        elif middle_value > worklist[high_number]:
            low_number = middle + 1

        else:
            high_number = middle - 1


if __name__ == '__main__':
    main()

