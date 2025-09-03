class Solution:
    def search(self, nums: list[int], target:int) -> int:
        l, r = 0, len(nums) - 1             #initiate your pointers.

        while l <= r:
            mid = (l + r) // 2              #initiate middle pointer
            if target == nums[mid]:         #if found on first try, return
                return mid
            
            
            if nums[l] <= nums[mid]:        #we know that the left is 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 #eliminates left
                else:
                    r = mid - 1 #eliminates right
         
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 #eliminates right
                else:
                    l = mid + 1 #eliminates left
        return -1

myarr = [9,1,2,3,4,5,6,7,8,0]


myprob = Solution()

print(myprob.search(myarr, 7))