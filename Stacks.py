from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

#### Reverse a string using a stack (exercise)
def reverse_string(string):

    string_stack = Stack()
    reversed_string = ""

    for char in string:
        string_stack.push(char)
    
    for i in range(len(string)):
        reversed_string = reversed_string + string_stack.pop()
    
    return print(reversed_string)

string = "hello"

reverse_string(string)

### Check to see if brackets are balanced using stack (exercise)

LEFT_BRACKETS = ["{", "[", "<", "("]
RIGHT_BRACKETS = ["}", "]", ">", ")"]

left = Stack()

###The below helper function can be more easily used to check if a character matches than how i have it implemented in the main function below
##def is_match(ch1, ch2):
    # match_dict = {
    #     ')': '(',
    #     ']': '[',
    #     '}': '{'
    # }
    # return match_dict[ch1] == ch2

def balance_check(string):
    
    for char in string:
        if char in LEFT_BRACKETS:
            left.push(char)
        elif char in RIGHT_BRACKETS:
            compare_char = left.pop()
            if compare_char == "{" and char == "}":
                continue
            elif compare_char == "[" and char == "]":
                continue
            elif compare_char == "<" and char == ">":
                continue
            elif compare_char == "(" and char == ")":
                continue
            else:
                return False
        else:
            continue

    if left.is_empty():
        return True
    else:
        return False
    
bchecktest = "This is a test"

print(balance_check(bchecktest))
