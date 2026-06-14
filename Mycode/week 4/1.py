#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[0]:
                if nums[mid] < target or nums[mid] >= nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[0] or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
sol = Solution()
print(sol.search([3, 1], 1))