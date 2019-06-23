def sum_pairs(ints, sum):
    left_index = None
    right_index = None
    found_sum = False
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if found_sum and j > right_index:
                break
            if found_sum and i >= right_index:  # don't keep looking, we already got the best solution
                return [ints[left_index], ints[right_index]]
            if ints[i] + ints[j] == sum:
                if not found_sum or j < right_index:
                    left_index = i
                    right_index = j
                    found_sum = True
                    break  # don't keep looking on this line

    if found_sum:
        return [ints[left_index], ints[right_index]]
    else:
        return None
