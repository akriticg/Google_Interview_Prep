nums = [0,1,0,3,12]
zero = 0  # records the position of "0"
for i in range(len(nums)):
    if nums[i] != 0:
        print("i = ", i)
        print(nums)
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1
        print(zero)
        print(nums)
