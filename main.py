'''
The text here was given by the test giver:

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
import time
import random

def get_sublist_from(the_list):
  '''
  This was my first effort, crude but it works.

  This method is only faster when there is at-least 1 negative
  value in the list otherwise this method is horribly slow.
  '''
  tic = time.perf_counter()
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
  toc = time.perf_counter()
  print(f"get_sublist_from ran in {toc - tic:0.4f} seconds")
  return __is__

def get_sublist_faster_from(the_list):
  '''
  True if any value is negative otherwise False.
  '''
  tic = time.perf_counter()
  __is__ = any([n<0 for n in the_list])
  toc = time.perf_counter()
  print(f"get_sublist_faster_from ran in {toc - tic:0.4f} seconds")
  return __is__

def get_sublist_fastest_from(the_list):
  '''
  True if any first element is negative otherwise False, after sorted.
  '''
  tic = time.perf_counter()
  the_nums = sorted(the_list)
  __is__ = the_nums[0] < 0
  toc = time.perf_counter()
  print(f"get_sublist_faster_from ran in {toc - tic:0.4f} seconds")
  return __is__

def get_sublist_even_faster_from(the_list):
  '''
  True if any element is negative otherwise False.

  This method is always fastest.
  '''
  tic = time.perf_counter()
  __is__ = len([n for n in the_list if (n < 0)]) > 0
  toc = time.perf_counter()
  print(f"get_sublist_even_faster_from ran in {toc - tic:0.4f} seconds")
  return __is__


nums = [1, -2, 3, 4]
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #1'
print('='*30)

nums = [1, 2, 3, 4]
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #2'
print('='*30)

nums = [1, 2, 3, 4, 10]
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #3'
print('='*30)

nums = []
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #4'
print('='*30)

nums = [-1, 0, 0, 1]
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #5'
print('='*30)

L = [-1] + [1 for i in range(0, 100000-1)]
nums = [random.choice(L) for i in range(0, 100000)]
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #6'
print('='*30)

L = [1 for i in range(0, 10000)]
nums = [random.choice(L) for i in range(0, 10000)]
is1 = get_sublist_from(nums)
is2 = get_sublist_faster_from(nums)
is3 = get_sublist_faster_from(nums)
is4 = get_sublist_even_faster_from(nums)
assert (is1 == is2) and (is1 == is3) and (is1 == is4), 'Failed #7'
print('='*30)
