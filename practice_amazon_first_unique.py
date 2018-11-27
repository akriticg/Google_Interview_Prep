'''
given a string of million characters, find the first unique character
'''


def unique_char(given):
    dict = {}
    ind = {}

    for char in given:
        if char in dict.keys():
            dict[char] += 1
            ind[char] = None
        else:
            dict[char] = 1
            ind[char] = given.index(char)

    smallest = len(given) + 1
    for k in ind.values():
        if k is None:
            pass
        else:
            if(k < smallest):
                print(k)
                smallest = k
    print(ind.values())

    return(given[smallest])

print(unique_char("amazoncandids"))
