'''
Given a list of integers nums, return whether there is a sublist such that its sum is strictly larger than the total sum of the list.

Constraints

n ≤ 100000 where n is the length of nums
Example 1
Input
nums = [1, -2, 3, 4]

Output
True

Explanation
The sum of the list is 6 and the sum of the sublist [3, 4] is 7 which is strictly larger.

Example 2
Input
nums = [-2]

Output
True

Explanation
The sum of the list is -2 and we can choose the empty sublist ([]) for a sum of 0.
'''

def get_sublist_from(the_list):
    sub_list = []
    the_nums = sorted(the_list)

    __is__ = False
    total = sum(the_nums)
    print('total {}'.format(total))
    for i, n in enumerate(the_nums):
        if (n >= 0):
            sub_list = the_nums[i:]
            if (sum(sub_list) > total):
                __is__ = True
                break
    return __is__


nums = [1, -2, 3, 4]
s_list = get_sublist_from(nums)
print('sub-list is {}'.format(s_list))
print('='*30)

nums = [1, 2, 3, 4]
s_list = get_sublist_from(nums)
print('sub-list is {}'.format(s_list))
print('='*30)

nums = [1, 2, 3, 4, 10]
s_list = get_sublist_from(nums)
print('sub-list is {}'.format(s_list))
print('='*30)

nums = []
s_list = get_sublist_from(nums)
print('sub-list is {}'.format(s_list))
print('='*30)

nums = [-1, 0, 0, 1]
s_list = get_sublist_from(nums)
print('sub-list is {}'.format(s_list))
print('='*30)
