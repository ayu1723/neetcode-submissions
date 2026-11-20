class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        HashMap = [-1] * n  
        
        for num in nums:
            d = num % n  
            
            while HashMap[d] != -1:
                if HashMap[d] == num:
                    return True  
                d = (d + 1) % n  
            
            HashMap[d] = num  
        
        return False 













         
