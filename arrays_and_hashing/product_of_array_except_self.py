class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        prod = 1

        for i in range(len(nums)):
            for k in range(len(nums)):
                if i == k:
                    continue
                else:
                    prod *= nums[k]

            output.append(prod)
            prod = 1

        return output
    
    #Brute force solution