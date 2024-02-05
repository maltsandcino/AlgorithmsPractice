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