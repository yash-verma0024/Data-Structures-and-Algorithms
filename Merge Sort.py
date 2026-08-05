def merge_array(left , right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n :
        while i < n :
            result.append(left[i])
            i += 1
    if j < m :
        result.append(right[j])
        j += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left, right)

nums = [4,5,8,6,3,5,2,1,4,4]
print(merge_sort(nums))


# TC : O(n log n)
# SC : O(n)