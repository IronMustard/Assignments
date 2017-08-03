
user_item_rating = {
    'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0,
              'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
    'user2': {'item1': 3.0, 'item2': 3.5, 'item3': 1.5,
              'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
    'user3': {'item1': 2.5, 'item2': 3.0, 'item4': 3.5,
              'item6': 4.0},
    'user4': {'item2': 3.5, 'item3': 3.0, 'item4': 4.0,
              'item5': 2.5, 'item6': 4.5},
    'user5': {'item1': 3.0, 'item2': 4.0, 'item3': 2.0,
              'item4': 3.0, 'item5': 2.0, 'item6': 3.0},
    'user6': {'item1': 3.0, 'item2': 4.0, 'item4': 5.0,
              'item5': 3.5, 'item6': 3.0},
    'user7': {'item2': 4.5, 'item4': 4.0, 'item5': 1.0}
}

def flipdictionary(user_dict):
    item_user_rating = {}
    for user in user_dict.keys():
        item_dict = user_dict[user]
        for item in item_dict.keys():
            if item not in item_user_rating:
                item_user_rating[item] = {}
            item_user_rating[item][user] = user_dict[user][item]
    return item_user_rating

item_user_rating = flipdictionary(user_item_rating)
# print(item_user_rating)

def compare_keys(dct1, dct2):
    keys1 = dct1.keys()
    keys2 =dct2.keys()
    overlap_keys = list(set(keys1).intersection(keys2))
    return overlap_keys

# print (compare_keys(user_item_rating['user1'], user_item_rating['user3']))

def user_similarity(userA, userB, ratings_dict):
    lst_of_diff =[]
    itemdctA = ratings_dict[userA]
    itemdctB = ratings_dict[userB]
    sharedkeys = compare_keys(itemdctA, itemdctB)
    for key in sharedkeys:
        abs_diff = abs(itemdctA[key] - itemdctB[key])
        lst_of_diff.append(abs_diff)
    average_of_abs_diff = sum(lst_of_diff)/len(lst_of_diff)
    return (average_of_abs_diff)

# print(user_similarity('user3', 'user7',user_item_rating))

def make__user_pairs(users):
    lst_of_user_pairs = []
    for user1 in users:
        for user2 in users:
            if user1 != user2:
                pairs = (user1, user2)
                lst_of_user_pairs.append(pairs)
    return lst_of_user_pairs

paired_users = make__user_pairs(user_item_rating.keys())
# print(paired_users)

largest_diff_pair = None
largest_diff_value = None
smallest_diff_pair = None
smallest_diff_value = None

for user_tuple in paired_users:
    computed_user_similarity = user_similarity(user_tuple[0],user_tuple[1], user_item_rating)
    # print(computed_user_similarity, user_tuple)
    if largest_diff_value == None or largest_diff_value < computed_user_similarity:
        largest_diff_value = computed_user_similarity
        largest_diff_pair = user_tuple
    if smallest_diff_value == None or smallest_diff_value > computed_user_similarity:
        smallest_diff_value = computed_user_similarity
        smallest_diff_pair = user_tuple
print('User pair with largest difference:',largest_diff_pair,largest_diff_value)
print('User pair with smallest difference:',smallest_diff_pair,smallest_diff_value)

def item_similarity(itemA, itemB, ratings_dict):
    lst_of_diff =[]
    userdctA = ratings_dict[itemA]
    userdctB = ratings_dict[itemB]
    sharedkeys = compare_keys(userdctA, userdctB)
    for key in sharedkeys:
        abs_diff = abs(userdctA[key] - userdctB[key])
        lst_of_diff.append(abs_diff)
    average_of_abs_diff = sum(lst_of_diff)/len(lst_of_diff)
    return (average_of_abs_diff)

# print(item_similarity('item1', 'item2',item_user_rating))

def make__item_pairs(items):
    lst_of_item_pairs = []
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                pairs = (item1, item2)
                lst_of_item_pairs.append(pairs)
    return lst_of_item_pairs

paired_items = make__item_pairs(item_user_rating.keys())
# print(paired_items)

largest_diff_pair = None
largest_diff_value = None
smallest_diff_pair = None
smallest_diff_value = None

for item_tuple in paired_items:
    computed_item_similarity = item_similarity(item_tuple[0],item_tuple[1], item_user_rating)
    # print(computed_item_similarity, item_tuple)
    if largest_diff_value == None or largest_diff_value < computed_item_similarity:
        largest_diff_value = computed_item_similarity
        largest_diff_pair = item_tuple
    if smallest_diff_value == None or smallest_diff_value > computed_item_similarity:
        smallest_diff_value = computed_item_similarity
        smallest_diff_pair = item_tuple
print('Item pair with largest difference:',largest_diff_pair,largest_diff_value)
print('Item pair with smallest difference:',smallest_diff_pair,smallest_diff_value)
