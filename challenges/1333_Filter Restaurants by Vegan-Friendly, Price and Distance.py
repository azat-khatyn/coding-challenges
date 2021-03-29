"""

Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
veganFriendly = 1, maxPrice = 50, maxDistance = 10
Output: [3,1,5]

"""


def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    # specifying the indices of pieces of information
    id_ind = 0
    rating_ind = 1
    veganFriendly_ind = 2
    price_ind = 3
    distance_ind = 4

    # where
    good_restaurants = [
        rest for rest in restaurants
        if (veganFriendly == 0 or rest[veganFriendly_ind] == 1) and rest[price_ind] <= maxPrice and rest[distance_ind] <= maxDistance
    ]

    # order by
    good_restaurants.sort(key=lambda x: (x[rating_ind], x[id_ind]), reverse=True)

    return [rest[id_ind] for rest in good_restaurants]


restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
# Output: [3,1,5]

print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))


restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10

print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))


restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 30
maxDistance = 3

print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))