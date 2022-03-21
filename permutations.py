class Solution:
    
    def permute(self, nums):
            
        def backtracking(seen, available):
            # base case
            print("Calling backtracking with ", seen, available)
            if not available:
                print("Returning true  with", seen, available)
                return True
            
            # recursive 
            for index, num in enumerate(available):
                
                # make a choice and update the conf 
                new_seen = seen + [num]
                
                status = backtracking(new_seen, 
                                      available[:index]+available[index+1:])
                
                if status is True:
                    res.append(new_seen)

                # seen is not modified so there is no undo operations
            print("Returning false with", seen, available)
                
            return False
                   
        res = []
        backtracking([], nums)
        
        return res
res = Solution().permute([1,2,3])
print(res)