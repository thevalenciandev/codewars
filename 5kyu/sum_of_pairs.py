ints = [1, 4, 8, 7, 3, 15]
# l2= [1, -2, 3, 0, -6, 1]
# l3= [20, -13, 40]
# l4= [1, 2, 3, 4, 1, 0]
# ints= [10, 5, 2, 3, 7, 5]
# l6= [4, -2, 3, 3, 4]
# l7= [0, 2, 0]
# l8= [5, 9, 13, -3]
sum = 10


def sum_pairs(ints, sum):
    processed_ints = set()
    processed_ints.add(ints[0])
    for i in range(1, len(ints)):
        int_needed = sum - ints[i]
        if int_needed in processed_ints:
            return [int_needed, ints[i]]
        else:
            processed_ints.add(ints[i])
    return None


print(sum_pairs(ints, sum))
