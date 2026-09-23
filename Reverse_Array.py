array = [1,2,3,4,5]

def reverse(array, left, right):
    if left >= right :
        return

    array[left], array[right] = array[right], array[left]

    reverse(array, left + 1 , right - 1)

    return array

print(reverse(array, 0, len(array)-1))


# TC = O(n/2) --> O(n)
# SC = O(n/2) --> O(n)    ---> Stack Space