ind = -1


def linear_search(list, k):
    i = 0
    for x in list:
        if x == k:
            globals()['ind'] = i
            return True
        i += 1


list = [20, 4, 50, 38, 49, 19, 8]
k = 83
if linear_search(list, k):
    print("Found at ", ind)
else:
    print("Not Found")

