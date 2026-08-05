def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i < high:
            i += 1

        while nums[j] > pivot and j > low:
            j -= 1
        
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
        
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        p_idx = partition(nums, low , high)
        quick_sort(nums, low, p_idx - 1)
        quick_sort(nums, p_idx + 1, high)  
        return nums


nums = [4,5,8,6,3,5,2,1,4,4]
quick_sort(nums, 0, len(nums) - 1)
print(nums)