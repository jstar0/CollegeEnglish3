import random

people = ['于景一 34', '亓悦 5', '张超 1', '张佳鹏 48']
numbers = ['A', 'B', 'C', 'D']

random.shuffle(people)

for i in range(len(people)):
    print(numbers[i], people[i])
