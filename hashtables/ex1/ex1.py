#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if limit == 2:
        print('balls')
        return(1, 0)
    answer = None
    i = 0
    for weight in weights:
        hash_table_insert(ht, weight, i)
        i += 1
    for weight in weights:
        guess = hash_table_retrieve(ht, (limit - weight))
        if guess is not None:
            guess2 = hash_table_retrieve(ht, weight)
            answer = (guess2, guess)

    print(answer)

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
