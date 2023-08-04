pos = -1


def binary_search(list, k):
    lb = 0
    ub = len(list) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if list[mid] == k:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < k:
                lb = lb + 1
            else:
                ub = ub - 1
    return False


list = [20, 30, 10, 44, 59, 27]
list.sort()
k = 44

if binary_search(list, k):
    print("Found At ", pos)
else:
    print("Not Found")
