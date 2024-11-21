def unique_triplets(nums):
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left,right =i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
            elif total<0:
                left+=1
            else:
                right-=1
    return result


n=input('Enter the elements: ')
nums=n.split(" ")
nums=[int(num) for num in nums]
unique_triplets(nums)