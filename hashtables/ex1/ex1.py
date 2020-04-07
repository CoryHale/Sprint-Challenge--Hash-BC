#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    index = 0
    for weight in weights:
        hash_table_insert(ht, weight, index)
        index += 1

    for i in range(ht.capacity):
        if ht.storage[i]:
            pointer = ht.storage[i]

            compliment = limit - pointer.key
            comp = hash_table_retrieve(ht, compliment)

            if comp is not None and comp <= ht.capacity:
                if comp:
                    if comp == pointer.value:
                       print(pointer.value)
                       pointer = pointer.next
                       print(pointer.value)

                    index_1 = pointer.value
                    index_2 = comp

                    print(f"{index_1}, {index_2}")

                    if index_1 >= index_2:
                        answer = [index_1, index_2]
                    else:
                        answer = [index_2, index_1]

                    return answer

    return None




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
