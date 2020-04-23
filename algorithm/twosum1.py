
class Solution:
    def twoSum(self, nums, target):
        ret = []
        # length = len(nums)
        for num in nums:
            if target - num in nums:
                if num*2 == target and nums.count(num) == 1:
                    continue
                elif num*2 == target:
                    i = nums.index(num)
                    j = nums.index(num,i+1,len(nums))
                    return [i,j]
                else:
                    return [nums.index(num),nums.index(target - num)]
            else:
                continue
        
        return ret

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    ret = Solution().twoSum(nums,target)
    for r in ret:
        print(r)

