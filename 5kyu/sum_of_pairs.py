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
    left_index = len(ints)
    right_index = len(ints)
    found_sum = False
    i = 0
    j = 1
    while i < right_index:
        while j < right_index:
            if ints[i] + ints[j] == sum:
                if j < right_index:
                    left_index = i
                    right_index = j
                    found_sum = True
            j += 1
        i += 1
        j = i + 1

    if found_sum:
        return [ints[left_index], ints[right_index]]
    else:
        return None


print(sum_pairs(ints, sum))
