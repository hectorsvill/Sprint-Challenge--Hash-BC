#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    difference = 0
    for i in range(length):
        # get difference 
        difference = limit - weights[i]
        # check if difference is in hash map
        retrieved_weight = hash_table_retrieve(ht, weights[i])
        # print(retrieved_weight)
        if retrieved_weight is not None:
            return (i, retrieved_weight)
        else:
            # hash the difference as index and location as value
            hash_table_insert(ht, difference, i)
    # return indeces of itme weight in a tupple 
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""
weights = [ 4, 4] #6, 10, 15, 16 ]
x = get_indices_of_item_weights(weights, len(weights), 8)
print(x)