"""

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Example 3:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 4:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 5:

Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]


Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the stings of list1 are unique.
All the stings of list2 are unique.

"""


def findRestaurant(list1, list2):
    candidate_restaurants = None
    current_min = len(list1) + len(list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if i+j < current_min:
                    candidate_restaurants = list()
                    candidate_restaurants.append(list1[i])
                    current_min = i+j
                elif i+j == current_min:
                    candidate_restaurants.append(list1[i])
    return candidate_restaurants


def findRestaurant_dict(list1, list2):
    candidates_map = {}

    for i in range(len(list1)):
        if list1[i] not in candidates_map:
            candidates_map[list1[i]] = [i]
        else:
            candidates_map[list1[i]].append(i)

    for i in range(len(list2)):
        if list2[i] not in candidates_map:
            candidates_map[list2[i]] = [i]
        else:
            candidates_map[list2[i]].append(i)

    candidate_restaurants = None
    current_min = len(list1)+len(list2)
    for k, v in candidates_map.items():
        if len(v) == 2:
            if sum(v) < current_min:
                candidate_restaurants = list()
                candidate_restaurants.append(k)
                current_min = sum(v)
            elif sum(v) == current_min:
                candidate_restaurants.append(k)
    return candidate_restaurants



rest1 = ["Shogun","Tapioca Express","Burger King","KFC"]
rest2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]


print(findRestaurant_dict(rest1, rest2))