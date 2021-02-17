"""
{
    "business_of_interest_id": 10,
    "positive_reviews": [
        {
            "user_id": 13,
            "business_id": 10
        },
        {
            "user_id": 21,
            "business_id": 10
        },
        {
            "user_id": 3,
            "business_id": 12
        },
        {
            "user_id": 13,
            "business_id": 11
        },
        {
            "user_id": 21,
            "business_id": 11
        },
        {
            "user_id": 13,
            "business_id": 12
        },
        {
            "user_id": 21,
            "business_id": 12
        }
    ]
}
"""

import sys
import json


def compute_set_of_unique_users(business_id, reviews):
    return {pr['user_id'] for pr in reviews if business_id == pr['business_id']}


def compute_similarity(unique_users_of_a_business_x, unique_users_of_a_business_y):
    intersection = len(unique_users_of_a_business_x.intersection(unique_users_of_a_business_y))
    union = len(unique_users_of_a_business_x.union(unique_users_of_a_business_y))
    return intersection / union


data = json.load(sys.stdin)
business_of_interest_id = data['business_of_interest_id']
positive_reviews = data['positive_reviews']

unique_users_of_business_of_interest = compute_set_of_unique_users(business_of_interest_id, positive_reviews)
all_business_ids = {pr['business_id'] for pr in positive_reviews}

max_similarity = 0
max_similarity_business_id = None
for a_business_id in all_business_ids:
    if a_business_id != business_of_interest_id:
        unique_users_of_a_business = compute_set_of_unique_users(a_business_id, positive_reviews)
        similarity = compute_similarity(unique_users_of_a_business, unique_users_of_business_of_interest)
        if similarity > max_similarity:
            max_similarity = similarity
            max_similarity_business_id = a_business_id

print(max_similarity_business_id)
