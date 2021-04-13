function solution(arr) {
  arr = arr.filter((i) => i >= 0)
  let candidate = arr[0]

  for (let number of arr) {
    if (number == candidate) {
      candidate -= 1
    }

  }


}

const arr = [3, 4, -1, 1]
// const arr = [1, 2, 3]
solution(arr)