import csv

temperatures = []

with open("nyc_weather.csv", "r") as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = float(tokens[1])
        temperatures.append([day, temperature])

###Print average temperature in first week
average = 0
for i in range(7):
    average = average + temperatures[i][1]

# print(average / 7)

###print highest temperature in first 10 days
temps = []
for i in range(10):
    temps.append(temperatures[i][1])
# print(max(temps[0:10]))

##Better way to calculate average than above method, allowing for user input if made into a method
# print(sum(temps[0:7])/len(temps[0:7]))

'''-----------------'''

temperatures = {}

with open("nyc_weather.csv", "r") as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = float(tokens[1])
        temperatures[day] = temperature

# print(temperatures)
# print(temperatures['Jan 9'])
# print(temperatures['Jan 4'])

'''--------'''

###Count how many times each word appears in the text

all_words = []
word_count = {}

with open("poem.txt", "r") as f:
    for line in f:
        all_words = all_words + line.strip().split(' ')
        
all_words.remove("")

for word in all_words:
    try:
        if word_count[word]:
            word_count[word] = word_count[word] + 1
    except:
        word_count[word] = 1

# print(word_count)

# Better Implementation:
# word_count = {}
# with open("poem.txt","r") as f:
#     for line in f:
#         tokens = line.split(' ')
#         for token in tokens:
#             token=token.replace('\n','')
#             if token in word_count:
#                 word_count[token]+=1
#             else:
#                 word_count[token]=1

# print(word_count)
'''------------'''
# Exercise 4 TODO

# Implement a hashtable which handles collisions with linear probing

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

 ##Hash function   
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        
        found = 0
       
        if self.arr[h] is not None and key in self.arr[h].keys():   
            self.arr[h] = {key: val}
            found = 1
        elif self.arr[h] is not None and key not in self.arr[h].keys():
            found = 2            
            for slot in range(h + 1, self.MAX - 1):
                print(slot)
                if self.arr[slot] == None:
                    self.arr[slot] = {key: val}
                    found = 3
                    break
            if found == 2:
                for slot in range(0, h - 1):
                    if self.arr[slot] == None:
                        self.arr[slot] = {key: val}
                        slot_found = 3
                        break
        else:
            self.arr[h] = {key: val}      
        
    def __getitem__(self, key):
        h = self.get_hash(key)

        if key in self.arr[h].keys():
            return self.arr[h][key]
        else:
            for slot in self.arr:
                if slot is not None and key in slot.keys():
                    return slot[key]
       
                
t = HashTable()
# print(t.arr)
t.__setitem__('march 15', 130)
# print(t.arr)
t.__setitem__('march 06', 160)
print(t.arr)
print(t['march 15'])
print(t['march 06'])

    
