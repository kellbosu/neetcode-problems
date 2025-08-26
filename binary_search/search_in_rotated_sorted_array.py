class Solution:
    def search(self, nums: list[int], target:int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]: #if found on first try
                return mid
            
            
            if nums[l] <= nums[mid]: 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 #eliminates left
                else:
                    r = mid - 1 #eliminates right
         
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

myarr = [0,1,2,3,4,5,6,7,8,9]


myprob = Solution()

print(myprob.search(myarr, 7))