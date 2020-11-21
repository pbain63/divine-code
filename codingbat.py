##Codingbat python 
#https://codingbat.com/python

List-2 > sum13

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

Solutions:

'''
def sum13(nums):
  
	tot = 0
	i = 0
	while i < len(nums):
		if nums[i] == 13:
			i += 1
		else:
			tot += nums[i]
		i += 1
	return tot
	'''
''' Or

def sum13(nums):

    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1

    return total
'''
''' Or

def sum13(nums):
  co=0
  if len(nums)<=0:
    return co
  for a in range(1,len(nums)):
    if nums[a]==13:
      continue
    elif nums[a-1]==13:
      continue
    else:
      co=co+nums[a]      
  if nums[0]!=13:
    co+=nums[0]
  return co
  '''
  
 #Or
def sum13(nums):
  while 13 in nums:
    if nums.index(13) < len(nums)-1:
      nums.pop(nums.index(13)+1)
    nums.pop(nums.index(13))
    
  return sum(nums)