nums=[12, 45, 7, 89, 23]
#lets make the first element as maximum cuz we dont know the maximum element yet
maximum=nums[0]
for i in range(len(nums)):
    if nums[i]>maximum:
        maximum=nums[i]
print(maximum)