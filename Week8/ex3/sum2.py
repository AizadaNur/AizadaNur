def sum2(nums):
    sum=0
    for i in range(len(nums)):
        if len(nums)<3:
            sum+=nums[i]
        else:
            sum=nums[0]+nums[1]
    return sum