# DailyCoding 47
def bestBuy(stocks):
  bestBuy = candidate = 0
  bestSell = 1

  for i in range(2, len(stocks)):
    if stocks[i] < stocks[bestBuy] and stocks[i] < stocks[candidate]:
      candidate = i
    if stocks[i] - stocks[candidate] > stocks[bestSell] - stocks[bestBuy]:
      bestSell = i
      bestBuy = candidate

  return arr[bestSell] - arr[bestBuy]

stocks = [9, 11, 8, 185, 7, 10, 9]
print(bestBuy(stocks))
