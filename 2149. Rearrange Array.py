def rearrangeArray(nums):
    result = []
    n = len(nums)
    if n == 2:
        result.append(nums[1])
        result.append(nums[0])
        return result

    pos = []
    neg = []
    for i in range(n):
        if nums[i] >= 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    pos_idx = 0
    neg_idx = 0

    while pos_idx < len(pos):
        result.append(pos[pos_idx])
        result.append(neg[neg_idx])

        pos_idx += 1
        neg_idx += 1

    return result



nums = []
print(rearrangeArray(nums))