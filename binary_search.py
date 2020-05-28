data = [2,5,6,7,9,14,15,27,30]
target = 15

#binary search in linear time:


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

#binary search iterative:


def bin_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = int((low + high)/2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#binary search recursive:


def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = int((low + high)/2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


print(bin_search([2,5,6,7,9,14,15,27,30], 15))
print(binary_search([2,5,6,7,9,14,15,27,30], 15, 0, len(data)-1))
