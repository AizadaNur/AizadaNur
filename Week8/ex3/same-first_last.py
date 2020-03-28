def same_first_last(nums):
    for i in range(len(nums)):
        if len(nums)>=1 and (nums[0]==nums[len(nums)-1]):
            return True
    return False