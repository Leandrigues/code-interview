class Solution:
    def __init__(self):
        self.dates = []

    def solution(self, arr):
        self.collect_date(arr)
        self.add_missing_dates(arr)
        stocks_diff = self.stocks_diff(arr)
        print(stocks_diff)
        # print(arr)
        for i in range(len(arr)):
            acc = 0
            for j in range(len(self.dates)):
                acc += arr[j][i][1]
            print(acc)
    def add_missing_dates(self, arr):
        for company_stock in arr:
            for i, date in enumerate(self.dates):
                if i >= len(company_stock) or company_stock[i][0] != date:
                    if i == 0:
                        company_stock.insert(i, [date, 0])
                    else:
                        company_stock.insert(i, [date, company_stock[i-1][1]])
                 
    def collect_date(self, arr):
        for company_stock in arr:
            for (date, _) in company_stock:
                self.dates.append(date) if date not in self.dates else self.dates
        print(self.dates)

    def stocks_diff(self, arr):
        stocks_diff = []

        for company_stock in arr:
            current_diff = []
            previous_price = 0
            for (_, current_price) in company_stock:
                current_diff.append(current_price - previous_price)
                previous_price = current_price
            stocks_diff.append(current_diff)

        return stocks_diff
Solution().solution([
    [["5/1", 100], ["5/5", 200]],
    [["5/5", 100], ["5/8", 50]],
    [["5/1", 250], ["5/8", 400]]
])
