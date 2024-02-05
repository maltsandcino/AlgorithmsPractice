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

print(average / 7)

###print highest temperature in first 10 days
temps = []
for i in range(10):
    temps.append(temperatures[i][1])
print(max(temps[0:10]))

##Better way to calculate average than above method, allowing for user input if made into a method
print(sum(temps[0:7])/len(temps[0:7]))

'''-----------------'''

temperatures = {}

with open("nyc_weather.csv", "r") as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = float(tokens[1])
        temperatures[day] = temperature

print(temperatures)
print(temperatures['Jan 9'])
print(temperatures['Jan 4'])

'''--------'''

###Count how many times each word appears in the text

all_words = []
with open("poem.txt", "r") as f:
    for line in f:
        line_string = line.strip()
        individual_words = line_string.split(' ')
        all_words = all_words + individual_words
        
all_words.remove("")

word_count = {}

for word in all_words:
    print(word)
    try:
        if word_count[word]:
            word_count[word] = word_count[word] + 1
    except:
        word_count[word] = 1

print(word_count)

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
