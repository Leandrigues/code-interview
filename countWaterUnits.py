# DailyCoding 30
def capacity(arr):
    n = len(arr)
    left_maxes = [0 for _ in range(n)]
    right_maxes = [0 for _ in range(n)]

    current_left_max = 0
    for i in range(n):
        current_left_max = max(current_left_max, arr[i])
        left_maxes[i] = current_left_max

    print(left_maxes)

    current_right_max = 0
    for i in range(n - 1, -1, -1):
        current_right_max = max(current_right_max, arr[i])
        right_maxes[i] = current_right_max

    print(right_maxes)

    total = 0
    for i in range(n):
        print(f"At position {i}: {min(left_maxes[i], right_maxes[i]) - arr[i]}")
        total += min(left_maxes[i], right_maxes[i]) - arr[i]
    return total

# arr = [3,0,3,1,5]
arr = [3,0,2]
capacity(arr)