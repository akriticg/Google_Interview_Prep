from collections import Counter


def dp(arr, sum):

    sum_dict = Counter()

    for k in arr:

        sum_dict_keys = sum_dict.keys()
        new_sum = []
        print(sum_dict)

        for each_key in sum_dict_keys:

            if each_key + k <= sum:
                new_sum.append(each_key + k)

        for num in new_sum:
            sum_dict[num] += 1

        sum_dict[k] += 1

    print(sum_dict[16])


dp([2, 4, 10, 6], 16)
