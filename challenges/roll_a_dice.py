# import random
#
# def roll(A):
#     one = 0
#     two = 0
#     three = 0
#     four = 0
#     five = 0
#     six = 0
#     for i in range(1000):
#         toss = random.choice(A)
#         if toss == 1:
#             one += 1
#         if toss == 2:
#             two += 1
#         if toss == 3:
#             three += 1
#         if toss == 4:
#             four += 1
#         if toss == 5:
#             five += 1
#         if toss == 6:
#             six += 1
#     return print('Ones ' + str(one), 'Twos ' + str(two), 'Threes ' + str(three), 'Fours ' + str(four), 'Fives ' + str(five), 'Sixes ' + str(six))
#
#
# A = [1, 2, 3, 4, 5, 6]
#
# print(roll(A))



from random import randrange
def roll(n):
    tosses = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        toss = randrange(6)
        tosses[toss] += 1
    return tosses


print(roll(10))
