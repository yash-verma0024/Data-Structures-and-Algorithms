# Method 1 : Using for loop

def largest(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i]> largest:
            largest = arr[i]

        # OR max()          --->  NOTE : Since max takes 2 input therfore the TC of max fubction in this case is O(1)

        # largest = max(largest, arr[i])

    return largest

print(largest([-7,-88,-99,-2,-1]))

# TC : O(n)
# SC : O(1)


# Method 2 : Using infinity

def largest(arr):
    largest = float('-inf')         # For - infinity we can use float('-inf') and for + infinity we can use float('inf')
    for i in range(len(arr)):
        if arr[i]> largest:
            largest = arr[i]
            
    return largest

print(largest([-7,-88,-99,-2,-1]))

# TC : O(n)
# SC : O(1)