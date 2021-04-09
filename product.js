// DailyCoding
const product = (arr) => {
  let entireProduct = 1
  let answer = []
  let answerObject = {}

  // Calculate first element
  arr.forEach((item) => {
      entireProduct *= item
  })

  // Build object
  arr.forEach((item, index) => {
    answerObject[index] = entireProduct / item
  })

  return Object.values(answerObject)
}

console.log(product([1,2,3,4,5]))
