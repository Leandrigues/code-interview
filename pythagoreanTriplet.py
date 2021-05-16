# GeeksForGeeks
def pythagoreanTriplet(arr):
    squares = list(map(lambda x: x**2,arr))
    # diff = list(map(lambda x: ))
    diff = [x - arr[i] for i,x in enumerate(squares)]
    print(diff)
    dic = dict(zip(squares, diff)

arr = [3,1,4,6,5]
print(pythagoreanTriplet(arr))