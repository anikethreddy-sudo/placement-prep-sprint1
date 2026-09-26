nums=[12, -2, 7, 15, -7, 9, 2]
target=0
hash_table = {}
for i in range(len(nums)):
    need=target-nums[i]
    if need in hash_table:
        print([hash_table[need], i])

        break
    hash_table[need] = i