# #----- Brute force technique (Check all number till n) ----

# n = int(input("Enter the number : ")) 
# num = n
# result = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         result.append(i)
# print(result)

# # Time complexity : O(n)
# # Space complexity : O(k)      // k is the number of factors in result list

# NOTE : Time complexity of if-else statement and .append is O(1)

# #----- Better solution -----

# # The factor is only till the half of the number 
# #example : 20 (1,2,3,4,5,6,7,8,9,10,11,12,13,14,...,19,20)    ---> 1,2,4,5,10 are factor then only 20 id the factor
# # so we can calculate the factor till half of num



n = int(input("Enter the number : ")) 
num = n
result = []
for i in range(1, num // 2):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)


# # Time complexity : O(n/2)  ~ O(n)  {Constant exclude from time complexity}
# # Space complexity : O(k)      // k is the number of factors in result list
