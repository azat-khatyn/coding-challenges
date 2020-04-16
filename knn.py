
from math import sqrt

# a = [3, 7]
# b = [2, 8]
def dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def knn(data_x, data_y, K, x):

    # compute distances between the x and all points
    list_of_distances = []
    for i in range(len(data_x)):
        distance = dist(x,data_x[i])
        list_of_distances.append((distance, data_y[i]))
    print(list_of_distances)

    # sort the distances in ascending order
    list_of_distances.sort()

    # taking k nearest points
    top_k = list_of_distances[:K]
    print(top_k)

    # selecting a most frequent label among k nearest points
    frequencies = {}
    for t in top_k:
        if t[1] in frequencies:
            frequencies[t[1]] += 1
        else:
            frequencies[t[1]] = 1
    return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[0][0]

data_x = [[1, 2], [1, 3], [0, 1], [7, 8], [9, 9]]
data_y = [1, 1, 1, 2, 2]
K = 3
x = [-5, -2]

print(knn(data_x, data_y, K, x))

