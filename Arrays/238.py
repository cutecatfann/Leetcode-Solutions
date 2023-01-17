class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two pass solution, two pointers. 
        # O(n) time and O(1) space complexity

        length = len(nums) # to save time
        res = [1] * length # inititalize an array that is as long as nums, with 1 in all positions

        prefix = 1 # first pointer goes from beginning
        for i in range(length):
            res[i]= prefix # update the position in result to the prefix
            prefix *= nums[i] # then multiply together the nums value to what the prefix previously was
            # this will get the product of all the elements of nums aside from nums i

        postfix = 1 # second pointer goes from end
        for i in range(length -1,-1,-1): # go to the back of the array, flip to front, flip to back
            res[i] *= postfix # prefix is already in array, to not overwrite it mutiply the res by postfix
            postfix *= nums[i] # update postix by the numbers in res

        return res
