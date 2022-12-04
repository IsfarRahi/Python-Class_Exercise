"""

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Input: nums = [3,2,4], target = 6
Output: [1,2]
Input: nums = [3,3], target = 6
Output: [0,1]

"""

no_of_items = int(input("Enter the number of items:"))
lst = [ int(input("Enter the value:")) for i in range(no_of_items)]

print(lst)

x = int(input('Target number:'))
if lst[int(input())] + lst[int(input())] == x:
    print(list(x))
else:
    print("no")