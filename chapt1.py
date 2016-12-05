# -*- coding: utf-8 -*-
from collections import Counter
from collections import defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2,"scipy"),
    (2, "Numpy"), (2, "Statmodels"), (2, "Pandas"), (3, "R"), (3, "Python"),
    (3, "Statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "Programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "Theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "Neural Networks"), (8, "Neural Networks"), (8, "deep learning"),
    (8, "Big data"), (8, "artificial intelligence"), (9, "hadoop"),
    (9, "java"), (9, "MapReduce"), (9, "Big Data")
]

# index of user_ids by interest (keys are interests)
user_ids_by_interest = defaultdict(list)
# index of interest by user_id (keys are user_ids)
interest_by_user_ids = defaultdict(list)
for (user_id, interest) in interests:
    user_ids_by_interest[interest].append(user_id)
    interest_by_user_ids[user_id].append(interest)


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (83000, 4.2)]


def nb_of_friends(user):
    return len(user["friends"])


def not_the_same(user1, user2):
    return user1["id"] != user2["id"]


def not_friends(user1, user2):
    return all(not_the_same(friend, user2) for friend in user1["friends"])


def friend_of_friends_ids(user):
    return Counter(friend_of_friend["id"]
                   for friend in user["friends"]
                   for friend_of_friend in friend["friends"]
                   if not_the_same(user, friend_of_friend)
                   and not_friends(user, friend_of_friend))


def data_scientists_who_likes(target_interest):
    return [user_id
            for (user_id, interest) in interests
            if interest == target_interest]


def most_common_interests(user):
    return Counter(user_interested_id
                   for interest in interest_by_user_ids[user["id"]]
                   for user_interested_id in user_ids_by_interest[interest]
                   if user_interested_id != user["id"])


if __name__ == '__main__':
    for user in users:
        user["friends"] = []

    for i, j in friendship:
        users[i]["friends"].append(users[j])
        users[j]["friends"].append(users[i])

    total_connections = sum(nb_of_friends(user) for user in users)
    num_users = len(users)

    avg_connections = total_connections / num_users

    # create a list of users and nb_of_friends :
    num_friend_by_id = [(user["id"], nb_of_friends(user)) for user in users]

    sorted(num_friend_by_id, key=lambda user_id_and_nb_friends: user_id_and_nb_friends[1], )

    print(num_friend_by_id)
    print(friend_of_friends_ids(users[3]))

    print(most_common_interests(users[0]))

    print(NotImplemented)
