def intersects(a, b):
    return (a[0] < b[1] < a[1]) or (b[0] < a[1] < b[1])

def minimumRoomsV1(intervals):
    # O(n^2)
    n = len(intervals)
    rooms = 0

    for i in range(n - 1):
        for j in range(i+1, n):
            if intersects(intervals[i], intervals[j]):
                rooms += 1

    return rooms

def minimumRoomsV2(intervals):
    n = len(intervals)
    rooms = 0
    intervals = sorted(intervals, key=lambda x: x[1])

    for i in range(n-1):
        if intersects(intervals[i], intervals[i+1]):
            rooms += 1
    print(intervals)
    return rooms

intervals = [[30, 75], [0, 70], [60, 150]]
print(minimumRoomsV1(intervals))
print(minimumRoomsV2(intervals))
